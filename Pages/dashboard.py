import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io

st.set_page_config(page_title="Dashboard KADEM", layout="wide")

# Fungsi metode SAW
def hitung_saw(df, bobot):
    kriteria = ["IPK", "Organisasi", "Kepemimpinan", "Akhlak"]
    df_norm = df.copy()

    for k in kriteria:
        max_val = df[k].max()
        df_norm[k] = df[k] / max_val if max_val != 0 else 0

    df["Skor SAW"] = (df_norm["IPK"] * bobot["IPK"] +
                      df_norm["Organisasi"] * bobot["Organisasi"] +
                      df_norm["Kepemimpinan"] * bobot["Kepemimpinan"] +
                      df_norm["Akhlak"] * bobot["Akhlak"]).round(4)
    return df

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
    st.image("https://raw.githubusercontent.com/fauzanafif/KADEM/main/assets/logo-dema.png", width=140)
    st.markdown("#### \U0001F4CC Ketentuan Penilaian")
    st.info("\U0001F512 Demi kelancaran dan ketetapan kriteria, **formulir penilaian hanya dapat diisi sekali**. Tidak ada proses *update* setelah disimpan.")

    st.markdown("---")
    st.markdown("\U0001F4C4 **Unduh Soal Pertanyaan Penilaian**")
    with open("assets/soal_penilaian_kandidat.docx", "rb") as docx_file:
        st.download_button(
            label="\U0001F4E5 Unduh DOCX",
            data=docx_file,
            file_name="soal_penilaian_kandidat.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    st.markdown("---")
    st.markdown("\U0001F9D1‍\U0001F4BC **Dikembangkan oleh:** Tim KADEM UNIDA Gontor")

st.title("\U0001F393 Dashboard Penilaian Kandidat DEMA")

if 'kandidat_list' not in st.session_state:
    st.session_state.kandidat_list = []

st.subheader("\U0001F4DD Form Penilaian Kandidat")
st.markdown("\U0001F9D1‍\U0001F4BC Unduh soal yang disediakan sistem di bagian sidebar.")

fakultas_unida = ["Tarbiyah", "Syariah", "Ushuluddin", "Ekonomi dan Manajemen", "Sains dan Teknologi", "Humaniora", "ILKES"]
prodi_unida = [
    "Pendidikan Agama Islam", "Pendidikan Bahasa Arab", "Pendidikan Bahasa Inggris",
    "Hukum Ekonomi Syariah", "Ilmu Al-Qur'an dan Tafsir", "Perbandingan Mazhab dan Hukum",
    "Ekonomi Islam", "Manajemen", "Teknik Informatika", "Ilmu Komunikasi", "Kedokteran",
    "Agroteknologi", "Teknik Industri Pertanian"
]

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

    submitted = st.form_submit_button("\u2705 Simpan Data")

    if submitted:
        if not nim or not nama:
            st.warning("⚠️ NIM dan Nama wajib diisi.")
        elif any(k["NIM"] == nim for k in st.session_state.kandidat_list):
            st.error(f"❌ NIM {nim} sudah pernah diinput. Data tidak dapat ditambahkan ulang.")
        else:
            bobot = {"IPK": 0.25, "Organisasi": 0.25, "Kepemimpinan": 0.25, "Akhlak": 0.25}
            skor_total = round((ipk / 5) * bobot["IPK"] + (organisasi / 5) * bobot["Organisasi"] +
                               (kepemimpinan / 5) * bobot["Kepemimpinan"] + (akhlak / 5) * bobot["Akhlak"], 4)

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
st.subheader("\U0001F4CA Ranking Kandidat (Metode SAW)")

if st.session_state.kandidat_list:
    df = pd.DataFrame(st.session_state.kandidat_list)
    bobot = {"IPK": 0.25, "Organisasi": 0.25, "Kepemimpinan": 0.25, "Akhlak": 0.25}
    df = hitung_saw(df, bobot)
    df_sorted = df.sort_values(by="Skor SAW", ascending=False).reset_index(drop=True)

    emojis = ['\U0001F947', '\U0001F948', '\U0001F949'] + ['\u2B50'] * (len(df_sorted) - 3)
    df_sorted.insert(0, "Ranking", emojis[:len(df_sorted)])

    st.dataframe(df_sorted.style.set_properties(**{'text-align': 'center'}), use_container_width=True)

    excel_buffer = io.BytesIO()
    df_sorted.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)
    st.download_button(
        label="\U0001F4E5 Unduh Tabel Ranking (Excel)",
        data=excel_buffer,
        file_name="ranking_kandidat_saw.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("\U0001F4C8 Grafik Skor SAW per Kandidat")
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        ax2.bar(df_sorted["Nama"], df_sorted["Skor SAW"], color="#3399ff")
        ax2.set_ylabel("Skor SAW")
        ax2.set_title("Skor SAW per Kandidat")
        plt.xticks(rotation=45)
        st.pyplot(fig2)

    with col2:
        st.subheader("\U0001F4CA Rata-Rata Kontribusi Kriteria")
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
else:
    st.info("Belum ada data kandidat yang dimasukkan.")