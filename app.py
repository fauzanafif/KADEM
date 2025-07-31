import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="KADEM | Kandidat DEMA",
    page_icon="📘",
    layout="wide"
)

# CSS kustom untuk tampilan halaman dan sidebar
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
        animation: fadeIn 2s ease-in-out;
    }

    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        animation: bounce 2s infinite;
        margin-bottom: 1rem;
    }

    .section-title {
        font-size: 1.7rem;
        font-weight: 600;
        color: #1e3a8a;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
        text-align: center;
    }

    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #6b7280;
        margin-top: 3rem;
    }

    .dalil {
        font-style: italic;
        text-align: center;
        margin-top: 1.5rem;
        color: #374151;
        font-size: 1.1rem;
        background-color: #f0f4ff;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #2563eb;
        width: 60%;
        margin-left: auto;
        margin-right: auto;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Styling sidebar */
    section[data-testid="stSidebar"] {
        background-color: #e0ecff;
        padding: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/fauzanafif/KADEM/main/assets/logo-dema.png", width=150)
    st.markdown("## 📘 KADEM")
    st.markdown("**Aplikasi Pemilihan Kandidat DEMA**")
    st.markdown("Berbasis data dan nilai Islami.")
    st.markdown("---")
    st.markdown("👤 Dibuat oleh: Tim KADEM UNIDA Gontor")

# Judul dan subjudul
st.markdown('<div class="title">Selamat Datang di Aplikasi KADEM</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">(Pemilihan Kandidat DEMA)</div>', unsafe_allow_html=True)

# Logo tengah
st.markdown(
    '<div class="logo-container">'
    '<img src="https://raw.githubusercontent.com/fauzanafif/KADEM/main/assets/logo-dema.png" width="280"/>'
    '</div>',
    unsafe_allow_html=True
)

# Penjelasan
st.markdown('<div class="section-title">🧠 Pemilihan Bijak Sesuai Data</div>', unsafe_allow_html=True)
st.write("""
Pemimpin yang baik lahir dari proses yang baik. KADEM memastikan proses ini berbasis pada **nilai-nilai Islami** dan **data yang terukur**, agar keputusan yang diambil benar-benar mencerminkan _maslahat_ untuk semua.
""")

# Dalil
st.markdown("""
<div class="dalil">
💬 <b>“Apabila suatu urusan diserahkan kepada yang bukan ahlinya, maka tunggulah kehancurannya.”</b><br/>
<i>(HR. Bukhari)</i>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2025 KADEM - UNIDA Gontor</div>', unsafe_allow_html=True)
