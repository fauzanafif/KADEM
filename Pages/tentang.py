import streamlit as st

st.markdown('<div class="title">Tentang Aplikasi</div>', unsafe_allow_html=True)
st.write("---")

st.markdown("""
Aplikasi ini dibuat untuk membantu proses pemilihan Ketua DEMA (Dewan Mahasiswa) secara objektif 
menggunakan pendekatan **Sistem Pendukung Keputusan (SPK)** dengan metode **Weighted Sum Model (WSM)**.

### 👨‍💻 Fitur Utama:
- Upload dan analisis data kandidat
- Perhitungan otomatis berdasarkan bobot kriteria
- Rekomendasi ketua terbaik secara transparan

### 🛠 Teknologi:
- Python
- Streamlit
- Pandas
""")
