import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="KADEM | Kandidat DEMA",
    page_icon="📘",
    layout="centered"
)

# CSS kustom dengan animasi bounce dan styling menarik
st.markdown("""
    <style>
    @keyframes bounce {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-10px);
        }
    }

    .title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #1e40af, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.3rem;
        animation: fadeIn 1s ease-in-out;
    }

    .subtitle {
        font-size: 1.3rem;
        font-weight: 500;
        color: #2563eb;
        text-align: center;
        margin-bottom: 2.5rem;
        animation: fadeIn 2s ease-in-out;
    }

    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        animation: bounce 2s infinite;
        margin-bottom: 1rem;
    }

    .footer {
        text-align:center;
        font-size:0.9rem;
        color:#6b7280;
        margin-top: 3rem;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# Judul dan Subjudul
st.markdown('<div class="title">Selamat Datang di Aplikasi KADEM</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">(Pemilihan Kandidat DEMA)</div>', unsafe_allow_html=True)

# Logo dengan animasi
st.markdown('<div class="logo-container"><img src="https://raw.githubusercontent.com/your-repo/assets/logo-dema.png" width="300"/></div>', unsafe_allow_html=True)

# Penjelasan
st.markdown("---")
st.write("""
**KADEM** (Kandidat DEMA) adalah aplikasi digital yang digunakan untuk proses seleksi dan pemilihan kandidat Ketua dan Wakil Ketua DEMA secara **transparan**, **efisien**, dan **inovatif**.

➡️ Gunakan menu di samping (sidebar) untuk melihat profil kandidat atau melakukan pemilihan.
""")

# Footer
st.markdown('<div class="footer">© 2025 KADEM - UNIDA Gontor</div>', unsafe_allow_html=True)
