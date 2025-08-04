import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io

st.set_page_config(page_title="Dashboard KADEM", layout="wide")

# CSS styling sidebar
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f6ff;
    }
    section[data-testid="stSidebar"] {
        background-color: #e0ecff;
        padding: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    # Logo KADEM
    st.image("https://raw.githubusercontent.com/fauzanafif/KADEM/main/assets/logo-dema.png", width=140)

    # Informasi penting
    st.markdown("#### 📌 Ketentuan Penilaian")
    st.info("🔒 Formulir penilaian hanya dapat diisi sekali. Tidak dapat diubah setelah disimpan.")

    st.markdown("---")
    st.markdown("📄 **Unduh Soal Pertanyaan Penilaian**")

    with open("assets/soal_penilaian_kandidat.docx", "rb") as docx_file:
        st.download_button(
            label="📥 Unduh DOCX",
            data=docx_file,
            file_name="soal_penilaian_kandidat.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    st.markdown("---")
    st.markdown("🧑‍💼 **Dikembangkan oleh:** Tim KADEM UNIDA Gontor")

st.title("🎓 Dashboard Penilaian Kandidat DEMA")

# Inisialisasi penyimpanan kandidat
if 'kandidat_list' not in st.session_state:
    st.session_state.kandidat_list = []

st.subheader("📝 Form Penilaian Kandidat")
st.markdown("🧑‍💼 Unduh soal yang disediakan sistem di bagian sidebar.")

# List Fakultas dan Prodi UNIDA Gontor
fakultas_unida = ["Tarbiyah", "Syariah", "Ushuluddin", "Ekonomi dan Manajemen", "Sains dan Teknologi", "Humaniora", "ILKES"]
prodi_unida = [
    "Pendidikan Agama Islam", "Pendidikan Bahasa Arab", "Pendidikan Bahasa Inggris",
    "Hukum Ekonomi Syariah", "Ilmu Al-Qur'an dan Tafsir", "Perbandingan Mazhab dan Hukum",
    "Ekonomi Islam", "Manajemen", "Teknik Informatika", "Ilmu Komunikasi", "Kedokteran",
    "Agroteknologi", "Teknik Industri Pertanian"
]

# Form Input Kandidat Baru
with st.form("form_penilaian"):
    col1, col2, col3 = st.columns(3)

    with col1:
        nama = st.text_input("Nama Kandidat")
        nim = st.text_input("NIM")
        prodi = st.selectbox("Program Studi", prodi_unida)

    with col2:
        jurusan = st.selectbox("Fakultas", fakultas_unida)
        asrama = st.text_input("Asrama")

    with col3:
        ipk = st.number_input("Skor IPK (1-5)", 1, 5, 1)
        organisasi = st.number_input("Skor Pengalaman Organisasi (1-5)", 1, 5, 1)
        kepemimpinan = st.number_input("Skor Kepemimpinan (1-5)", 1, 5, 1)
        akhlak = st.number_input("Skor Akhlak (1-5)", 1, 5, 1)

    submitted = st.form_submit_button("✅ Simpan Data")

    if submitted:
        bobot = {"IPK": 0.25, "Organisasi": 0.25, "Kepemimpinan": 0.25, "Akhlak": 0.25}
        skor_total = round(ipk * bobot["IPK"] + organisasi * bobot["Organisasi"] +
                           kepemimpinan * bobot["Kepemimpinan"] + akhlak * bobot["Akhlak"], 2)

        kandidat_baru = {
            "Nama": nama,
            "NIM": nim,
            "Prodi": prodi,
            "Fakultas": jurusan,
            "Asrama": asrama,
            "IPK": ipk,
            "Organisasi": organisasi,
            "Kepemimpinan": kepemimpinan,
            "Akhlak": akhlak,
            "Skor Total": skor_total
        }

        st.session_state.kandidat_list.append(kandidat_baru)
        st.success(f"✅ Data kandidat '{nama}' berhasil ditambahkan.")

# Ranking Tabel
st.markdown("---")
st.subheader("📊 Ranking Kandidat")

if st.session_state.kandidat_list:
    df = pd.DataFrame(st.session_state.kandidat_list)
    df_sorted = df.sort_values(by="Skor Total", ascending=False).reset_index(drop=True)

    emojis = ['🥇', '🥈', '🥉'] + ['⭐'] * (len(df_sorted) - 3)
    df_sorted.insert(0, "Ranking", emojis[:len(df_sorted)])

    st.dataframe(df_sorted.style.set_properties(**{'text-align': 'center'}), use_container_width=True)

    # Download tabel
    excel_buffer = io.BytesIO()
    df_sorted.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)
    st.download_button(
        label="📥 Unduh Tabel Ranking (Excel)",
        data=excel_buffer,
        file_name="ranking_kandidat.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # Grafik Skor Total
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Grafik Skor per Kandidat")
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        ax2.bar(df_sorted["Nama"], df_sorted["Skor Total"], color="#3399ff")
        ax2.set_ylabel("Skor Total")
        ax2.set_title("Skor Total per Kandidat")
        plt.xticks(rotation=45)
        st.pyplot(fig2)

        bar_img = io.BytesIO()
        fig2.savefig(bar_img, format="png", bbox_inches="tight")
        bar_img.seek(0)
        st.download_button(
            label="📸 Unduh Grafik Skor (PNG)",
            data=bar_img,
            file_name="grafik_skor_total.png",
            mime="image/png"
        )

    with col2:
        st.subheader("📊 Rata-Rata Kontribusi Kriteria")
        categories = ["IPK", "Organisasi", "Kepemimpinan", "Akhlak"]
        mean_scores = df[categories].mean().values.tolist()
        mean_scores += mean_scores[:1]

        angles = np.linspace(0, 2 * np.pi, len(categories) + 1, endpoint=True)
        fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
        ax.plot(angles, mean_scores, 'o-', linewidth=2, color='blue')
        ax.fill(angles, mean_scores, alpha=0.25, color='blue')
        ax.set_thetagrids(angles[:-1] * 180 / np.pi, categories)
        ax.set_title("Kontribusi Kriteria")
        ax.grid(True)
        st.pyplot(fig)

        radar_img = io.BytesIO()
        fig.savefig(radar_img, format="png", bbox_inches="tight")
        radar_img.seek(0)
        st.download_button(
            label="📸 Unduh Radar Chart (PNG)",
            data=radar_img,
            file_name="kontribusi_kriteria.png",
            mime="image/png"
        )
else:
    st.info("Belum ada data kandidat yang dimasukkan.")
