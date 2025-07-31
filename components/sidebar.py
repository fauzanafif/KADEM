# components/sidebar.py
import streamlit as st

def show_main_sidebar():
    st.image("https://raw.githubusercontent.com/fauzanafif/KADEM/main/assets/logo-dema.png", width=140)

    st.markdown("#### 📌 Ketentuan Penilaian")
    st.info("🔒 Demi kelancaran dan ketetapan kriteria, **formulir penilaian hanya dapat diisi sekali**.")

    st.page_link("pages/dashboard.py", label="🏠 Dashboard", icon="🏠")
    st.page_link("app.py", label="🔙 Kembali", icon="↩️")

    st.markdown("---")
    st.markdown("📄 **Unduh Soal Pertanyaan Penilaian**")

    with open("assets/soal_penilaian_kandidat.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Unduh PDF",
            data=pdf_file,
            file_name="soal_penilaian_kandidat.pdf",
            mime="application/pdf"
        )

    with open("assets/soal_penilaian_kandidat.docx", "rb") as docx_file:
        st.download_button(
            label="📥 Unduh DOCX",
            data=docx_file,
            file_name="soal_penilaian_kandidat.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    st.markdown("---")
    st.markdown("🧑‍💼 **Dikembangkan oleh:** Tim KADEM UNIDA Gontor")
