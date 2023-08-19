from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "image.png"

PAGE_TITLE = "Ali ÖZCAN"
PAGE_ICON = ":rand:"
NAME = "Ali ÖZCAN"
DESCRIPTION = """
Software Developer | Data Scientist | Network Systems
"""
EMAIL = "aliozcan.93@hotmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/ali-özcann",
    "GitHub": "https://github.com/alizcn"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')

st.subheader("Summary")
st.write(
    """
A results-oriented and versatile developer with a strong foundation in web development and data science. Experience in a wide range of programming languages ​​and technologies, including HTML, CSS, Bootstrap, PHP, C#, R and Azure. It can analyze data and create interactive visualizations using Matplotlib, Plot, Folium, Seaborn, and Streamlight. I can use libraries like BeautifulSoup, Selenium in Python, PyQt, Flask, Numpy, Pandas and more. I continue to develop on machine learning and predictive modeling with Scikit-Learn, XGBoost and PySpark.\n

Extensive database knowledge including MySQL, MSSQL, SQLite and MongoDB. I can offer different perspectives and solutions with my familiarity with tools such as POSTMAN, GIT and JIRA, AGILE methodologies and my experience in different fields.\n

With a proactive mindset and a commitment to continuous learning, I want to contribute to, develop and develop innovative solutions and dynamic projects.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
"""
- 👩‍💻 Programming: PHP, C#, R, PYTHON (BeautifulSoup, Selenium, PyQT, Flask, Numpy, Pandas, Scikit-Learn, XGBoost, PySpark)
- 📊 Data Visulization: Matplotlib, Plotly, Folium, Seaborn, Streamlit
- 🗄️ Databases: MSSQL, MongoDB, MySQL, SQLİTE
- 📶 Network: Network Devices, IP Switchboard Systems And Devices, Cisco Products Installation, Configuration And System Support On 
- 📚 Tools: Postman,GIT,JIRA,AGILE
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**INFORMATION TECHNOLOGY TECHNICIAN | TURKISH AIR FORCE**")
st.write("NOVEMBER 2015 – DECEMBER 2017")
st.write(
"""
To provide technical support to end users,

✨ Hardware and software installation and configuration\n
✨ Maintenance and updating of computer systems\n
✨To help with network setup and troubleshooting.\n
✨ Implementation of data backup and recovery solutions\n
✨ Monitor IT security and protect against threats.\n
✨ To educate users about software applications and tools.\n
✨ Managing IT inventory and documents\n
✨ To implement IT policies and security protocols\n
✨ To cooperate with other IT specialists\n
✨ To make hardware repairs and replacements\n
✨ Staying up to date with technology trends\n
✨ Regular network assessments and troubleshooting operations were performed
to ensure a high level of network availability and stability
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**CALL CENTER VOİP SYSTEMS SUPPORT | NETGSM COMMUNICATION AND INFORMATION TECHNOLOGIES INC.**")
st.write("OCTOBER 2014 – OCTOBER 2015")
st.write(
"""
✨ To provide technical support to end users\n
✨ Hardware and software installation, configuration\n
✨To help with network setup and troubleshooting\n
✨ To educate users about software applications and tools\n
✨ Managing IT inventory and documents\n
✨ To cooperate with other IT specialists\n
✨ Staying up to date with technology trends\n
✨ On-site/remote installation and support of power plant systems and
devices
"""
)
st.write('\n')
st.write("🚧", "**CERTIFICATES**")
st.write("JULY 2023")
st.write(
"""
📄 IBM Data Science Professional Certificate
"""
)
