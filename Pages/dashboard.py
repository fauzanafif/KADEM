import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io

st.set_page_config(page_title="Dashboard KADEM", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f6ff;
    }
    .stTitle {
        color: #003366;
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("🎓 Dashboard Penilaian Kandidat DEMA")

# Inisialisasi penyimpanan kandidat
if 'kandidat_list' not in st.session_state:
    st.session_state.kandidat_list = []

st.subheader("📝 Form Penilaian Kandidat")

# Pilih untuk update
selected_nim = None
if st.session_state.kandidat_list:
    nims = [k["NIM"] for k in st.session_state.kandidat_list]
    selected_nim = st.selectbox("Pilih NIM untuk Update (kosongkan jika tambah baru)", [""] + nims)

# Ambil data jika update
kandidat_terpilih = next((k for k in st.session_state.kandidat_list if k["NIM"] == selected_nim), None)

with st.form("form_penilaian"):
    col1, col2, col3 = st.columns(3)

    with col1:
        nama = st.text_input("Nama Kandidat", kandidat_terpilih["Nama"] if kandidat_terpilih else "")
        nim = st.text_input("NIM", kandidat_terpilih["NIM"] if kandidat_terpilih else "")
        prodi = st.text_input("Program Studi", kandidat_terpilih["Prodi"] if kandidat_terpilih else "")

    with col2:
        jurusan = st.selectbox("Fakultas/Jurusan", ["SAINTEK", "SYARIAH", "TARBIYAH", "ADAB", "EKONOMI"],
                               index=["SAINTEK", "SYARIAH", "TARBIYAH", "ADAB", "EKONOMI"].index(kandidat_terpilih["Fakultas"]) if kandidat_terpilih else 0)
        asrama = st.text_input("Asrama", kandidat_terpilih["Asrama"] if kandidat_terpilih else "")

    with col3:
        ipk = st.number_input("Skor IPK (1-5)", 1, 5, int(kandidat_terpilih["IPK"]) if kandidat_terpilih else 1)
        organisasi = st.number_input("Skor Pengalaman Organisasi (1-5)", 1, 5, int(kandidat_terpilih["Organisasi"]) if kandidat_terpilih else 1)
        kepemimpinan = st.number_input("Skor Kepemimpinan (1-5)", 1, 5, int(kandidat_terpilih["Kepemimpinan"]) if kandidat_terpilih else 1)
        akhlak = st.number_input("Skor Akhlak (1-5)", 1, 5, int(kandidat_terpilih["Akhlak"]) if kandidat_terpilih else 1)

    tombol_label = "🔄 Update Data" if kandidat_terpilih else "✅ Simpan Data"
    submitted = st.form_submit_button(tombol_label)

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

        if kandidat_terpilih:
            index = next(i for i, k in enumerate(st.session_state.kandidat_list) if k["NIM"] == selected_nim)
            st.session_state.kandidat_list[index] = kandidat_baru
            st.success(f"🔄 Data kandidat '{nama}' berhasil di-*update*.")
        else:
            st.session_state.kandidat_list.append(kandidat_baru)
            st.success(f"✅ Data kandidat '{nama}' berhasil ditambahkan.")

# Tampilkan Ranking
st.markdown("---")
st.subheader("📊 Ranking Kandidat")

if st.session_state.kandidat_list:
    df = pd.DataFrame(st.session_state.kandidat_list)
    df_sorted = df.sort_values(by="Skor Total", ascending=False).reset_index(drop=True)

    emojis = ['🥇', '🥈', '🥉'] + ['⭐'] * (len(df_sorted) - 3)
    df_sorted.insert(0, "Ranking", emojis[:len(df_sorted)])

    st.dataframe(df_sorted.style.set_properties(**{'text-align': 'center'}), use_container_width=True)

    # Download Excel
    excel_buffer = io.BytesIO()
    df_sorted.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)
    st.download_button(
        label="📥 Unduh Tabel Ranking (Excel)",
        data=excel_buffer,
        file_name="ranking_kandidat.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # Visualisasi
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
