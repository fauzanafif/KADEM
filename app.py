import streamlit as st
from streamlit_extras.switch_page_button import switch_page


# Konfigurasi halaman utama
st.set_page_config(
    page_title="KADEM | Beranda",
    page_icon="📘",
    layout="wide"
)

# CSS styling
st.markdown("""
    <style>
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    .title {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #1e40af, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.3rem;
        animation: fadeIn 1s ease-in-out;
    }
    .subtitle {
        font-size: 1.5rem;
        font-weight: 500;
        color: #2563eb;
        text-align: center;
        margin-bottom: 2rem;
    }
    .logo-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        animation: bounce 2s infinite;
        margin-bottom: 1.5rem;
    }
    .start-button {
        background-color: #2563eb;
        color: white;
        border: none;
        padding: 0.4rem 1.2rem;
        font-size: 0.85rem;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        margin-top: 0.7rem;
    }
    .start-button:hover {
        background-color: #1e40af;
    }
    .dalil {
        font-style: italic;
        text-align: center;
        color: #374151;
        font-size: 1.1rem;
        background-color: #f0f4ff;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #2563eb;
        width: 60%;
        margin: 1.5rem auto;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #6b7280;
        margin-top: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("assets/logo-dema.png", width=140)
    st.markdown("## 📘 KADEM")
    st.markdown("Aplikasi Pemilihan Kandidat DEMA")
    st.markdown("---")
    st.markdown("👤 Dibuat oleh: Tim KADEM UNIDA Gontor")

# Judul
st.markdown('<div class="title">Selamat Datang di Aplikasi KADEM</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">(Pemilihan Kandidat DEMA)</div>', unsafe_allow_html=True)

# Logo + Tombol Mulai di tengah
st.markdown("""
<div class="logo-container">
    <img src="https://raw.githubusercontent.com/fauzanafif/KADEM/main/assets/logo-dema.png" width="280"/>
</div>
""", unsafe_allow_html=True)

# Tombol kecil di tengah bawah logo
col1, col2, col3 = st.columns([4, 1, 4])
with col2:
    if st.button("🚀 Mulai", key="start_btn"):
        switch_page("Dashboard")

# Konten pendukung
st.markdown('<div class="section-title">🧠 Pemilihan Bijak Sesuai Data</div>', unsafe_allow_html=True)
st.write("""
Pemimpin yang baik lahir dari proses yang baik. KADEM memastikan proses ini berbasis pada **nilai-nilai Islami** dan **data yang terukur**, agar keputusan yang diambil benar-benar mencerminkan _maslahat_ untuk semua.
""")

st.markdown("""
<div class="dalil">
💬 <b>“Apabila suatu urusan diserahkan kepada yang bukan ahlinya, maka tunggulah kehancurannya.”</b><br/>
<i>(HR. Bukhari)</i>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer">© 2025 KADEM - UNIDA Gontor</div>', unsafe_allow_html=True)
