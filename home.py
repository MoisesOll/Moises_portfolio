import streamlit as st
import base64


def home():
    
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Moises Ollero's Portfolio",
        page_icon="💻",
    )

    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/Foto_retrato.png", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/CV_English_2025.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Top title
    st.write(f"""<div class="title"><strong>Hi! My name is</strong> Moises Ollero👋</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div style="display: flex; justify-content: center;">
       <img src="{img}" alt="Moises Ollero" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    </div>
    """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Data Scientist specialized in Generative AI</div>""", unsafe_allow_html=True)
    st.write(f"""<div class="subtitle" style="text-align: center;">AI Engineer</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        # "Kaggle": ["https://www.kaggle.com/", "https://www.kaggle.com/static/images/site-logo.svg"],
        "LinkedIn": ["https://www.linkedin.com/in/moises-ollero/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/MoisesOll", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"]
        #"Twitter": ["https://twitter.com/", "https://cdn-icons-png.flaticon.com/512/733/733579.png"],
        #"YouTube": ["https://www.youtube.com/", "https://cdn-icons-png.flaticon.com/512/1384/1384060.png"],
        #"Medium": ["https://medium.com/", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Medium_logo_Monogram.svg/1200px-Medium_logo_Monogram.svg.png"]
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 I am an **AI Engineer** at @[Avanade](https://www.avanade.com/es-es)

    - ❤️ Passionate about Generative AI, Data, Optimization, Automation and more!
    
    - 🤖 I enjoy developing projects such as... it will soon come to life 😜
    
    - 🏂 Also enjoy practicing sports such as skiing, snowboarding and CrossFit! Lately, I've been trying to take up running, but...
    
    - 📫 How to reach me: moises.ollero@gmail.com
    
    - 🏠 Madrid, Spain
    """)

    st.write("##")

    # Download CV button
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="CV_English_2025.pdf",
        mime="application/pdf",
    )

    st.write("##")
    
    # st.write(f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects in the navigation menu! (Coming soon...)</div>""", unsafe_allow_html=True)


if __name__ == "__main__":

    home()
