# import streamlit as st
# from streamlit_timeline import timeline
# from PIL import Image
# image = Image.open("icon.jpg")
# profile_pic = Image.open('dp.png')
# resume_file = "RishabhIndoria_Resume.pdf"
# with open(resume_file, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
# st.set_page_config(page_title="Rishabh Indoria", page_icon=image,layout="centered", initial_sidebar_state="auto")
# # PAGE_CONFIG = {"page_title":, 
# #                "page_icon":, 
# #                "layout":"centered", 
# #                "initial_sidebar_state":"auto"}

# #####################
# # Header
# # # --- HERO SECTION ---
# # col1, col2 = st.columns(2, gap="small")
# # with col1:
    
# #     st.image(profile_pic, width=230)
# #     # st.image(profile_pic, width=230)

# # with col2:
# #     # st.title(NAME)
# #     # st.write(DESCRIPTION)
# #     st.write("# **<span style='color:#000000'>Rishabh Indoria</span>** ~~THE IT CROWD~~", unsafe_allow_html=True)
# #     st.download_button(
# #         label=" 📄 Download Resume",
# #         data=PDFbyte,
# #         file_name=resume_file.name,
# #         mime="application/octet-stream",
# #     )
# #     # st.write("📫", EMAIL)


# st.write("# **<span style='color:#000000'>Rishabh Indoria</span>** ~~THE IT CROWD~~", unsafe_allow_html=True)

# image = Image.open('dp.png')
# st.image(image, width=150)

# st.markdown('## Summary', unsafe_allow_html=True)
# st.info('''
# &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?**
# \nI am a highly accomplished data scientist with a strong focus on achieving measurable results. I possess extensive experience working within cross-functional teams to achieve organizational objectives. Being highly motivated to innovate existing business processes, I achieve optimal results in an efficient and cost-effective manner, utilizing my in-depth domain expertise. I have consistently demonstrated exceptional diligence and commitment to excellence in both my coursework and various work. I am eager to continue this level of performance in future projects, utilizing diverse models, frameworks, and data.
# ''')

# #####################
# # Navigation

# st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# st.markdown("""
# <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #021014;">
#   <a style="color: #16A2CB" class="navbar-brand" target="_blank">Rishabh Indoria</a>
#   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#     <span class="navbar-toggler-icon"></span>
#   </button>
#   <div class="collapse navbar-collapse" id="navbarNav">
#     <ul class="navbar-nav">
#       <li class="nav-item active">
#         <a style="color: #FFFFFF" class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
#       </li>
#       <li class="nav-item">
#         <a style="color: #FFFFFF" class="nav-link" href="#career-snapshot">Career snapshots</a>
#       </li>
#       <li class="nav-item">
#         <a style="color: #FFFFFF" class="nav-link" href="#education">Education</a>
#       </li>
#       <li class="nav-item">
#         <a style="color: #FFFFFF" class="nav-link" href="#work-experience">Work Experience</a>
#       </li>
#       <li class="nav-item">
#         <a style="color: #FFFFFF" class="nav-link" href="#projects">Projects</a>
#       </li>
#       <li class="nav-item">
#         <a style="color: #FFFFFF" class="nav-link" href="#social-media">Social Media</a>
#       </li>
#     </ul>
#   </div>
# </nav>
# """, unsafe_allow_html=True)

# #####################
# # Custom function for printing text
# def txt(a, b):
#   col1, col2 = st.columns([4,1])
#   with col1:
#     st.markdown(a, unsafe_allow_html=True)
#   with col2:
#     st.markdown(b, unsafe_allow_html=True)

# def txt2(a, b):
#   col1, col2 = st.columns([1,4])
#   with col1:
#     st.markdown(f'{a}', unsafe_allow_html=True)
#   with col2:
#     st.markdown(b, unsafe_allow_html=True)

# def txt3(a, b):
#   col1, col2 = st.columns([1,2])
#   with col1:
#     st.markdown(a, unsafe_allow_html=True)
#   with col2:
#     st.markdown(b, unsafe_allow_html=True)
  
# def txt4(a, b, c):
#   col1, col2, col3 = st.columns([1.5,2,2])
#   with col1:
#     st.markdown(f'`{a}`', unsafe_allow_html=True)
#   with col2:
#     st.markdown(b, unsafe_allow_html=True)
#   with col3:
#     st.markdown(c, unsafe_allow_html=True)

# #####################
# st.markdown("""---""")
# st.markdown('''
# ## Career-snapshot
# ''')
    
# with st.spinner(text="Building line"):
#     with open('timeline.json', "r") as f:
#         data = f.read()
#         timeline(data, height=500)

# #####################
# st.markdown("""---""")
# st.markdown('''
# ## Education
# ''')
# txt("**<span style='color:#000000'>Masters of Science</span>** (Information Systems), *<span style='color:#000000'>Northeastern University</span>*, Boston, Massachusetts",
# '2022-2024')
# st.markdown('''
# - GPA: **<span style='color:#000000'>3.76</span>**
# ''', unsafe_allow_html=True)

# txt("**<span style='color:#000000'>Bachelors of Technology</span>** (Information Technology), *<span style='color:#000000'>Manipal Institute of Technology</span>*, Manipal, India",
# '2013-2017')

# #####################
# st.markdown("""---""")
# st.markdown('''
# ## Skills
# ''')

# txt3("**<span style='color:#000000'>Language</span>**", "<span style='color:#000000'>Python,&ensp;Javascript,&ensp;Node.js,&ensp;SQL,&ensp;HTML,&ensp;CSS,&ensp;React.js</span>")
# txt3("**<span style='color:#000000'>Database</span>**", "<span style='color:#000000'>InfluxDB, &ensp; MongoDB ,&ensp;  MSSQL , &ensp; Redshift ,&ensp;  DynamoDB</span>")
# txt3("**<span style='color:#000000'>Frameworks</span>**", "<span style='color:#000000'>Pycaret , &ensp; PyTorch , &ensp; Scikit-learn ,&ensp;  Telegraf , &ensp; Flask ,&ensp; streamlit, &ensp;  keras ,  &ensp; Tensorflow</span>")
# txt3("**<span style='color:#000000'>Cloud Tools</span>**", "<span style='color:#000000'>AWS (EC2, S3, RDS, SES, SNS, Route 53, CloudFormation, CloudWatch, Lambda, IoT Core)</span>")
# txt3("**<span style='color:#000000'>Tools</span>**", "<span style='color:#000000'>Postman , &ensp; Docker ,&ensp;  Kubernetes ,&ensp;  VS code</span>")
# txt3("**<span style='color:#000000'>CI/CD</span>**", "<span style='color:#000000'>Git , &ensp; Jenkins , &ensp; Jira , &ensp; XL-Deploy</span>")
# txt3("**<span style='color:#000000'>Data Visualization</span>**", "<span style='color:#000000'> Grafana ,&ensp;  Chart.js , &ensp; Tableau , &ensp; PowerBI</span>")

# #####################
# st.markdown("""---""")
# st.markdown('''
# ## Work Experience
# ''')

# txt("**<span style='color:#000000'>Lead Data Scientist</span>**, *<span style='color:#000000'>Urja.io</span>*, India",
# '2021-2022')
# st.markdown('''
# - Developed model using <span style='color:#000000;font-weight:bold'>unsupervised K-means clustering</span> and <span style='color:#000000;font-weight:bold'>fbprophet</span> to forecast machine maintenance using peak detection and <span style='color:#000000;font-weight:bold'>Time-series Data</span>. Achieved <span style='color:#000000;font-weight:bold'>97%</span> accuracy
# - Engineered a data ingestion pipeline that utilized <span style='color:#000000;font-weight:bold'>AWS IoT Core, InfluxDB, and Telegraf</span> to ingest real-time time-series data sent by 2,000 IoT devices. Thus, reducing data loss to <span style='color:#000000;font-weight:bold'>1%</span>
# - Designed a parallel channel for data ingestion via HTTP chunked protocol and Telegraf directory monitoring plugin, leading to <span style='color:#000000;font-weight:bold'>zero</span> service charge for IoT data management
# - Supervised the development team and coordinated with clients to build an in-house one-stop interaction dashboard to remove dependency on Grafana Labs for energy data visualization, leading to <span style='color:#000000;font-weight:bold'>25%</span> increase in insights
# ''', unsafe_allow_html=True)

# txt("**<span style='color:#000000'>Software Engineer</span>**, *<span style='color:#000000'>Société Générale</span>*, India",
# '2017-2020')
# st.markdown('''
# - Automated the daily reporting system, reducing report generation efforts by <span style='color:#000000;font-weight:bold'>6</span> person-days each month
# - Developed and deployed <span style='color:#000000;font-weight:bold'>REST APIs</span> for global teams to get trade data saving <span style='color:#000000;font-weight:bold'>2.5</span> person-hours daily in ad-hoc ticket requests
# - Migrated existing applications running on on-prem machines to <span style='color:#000000;font-weight:bold'>AWS EC2</span>, by creating <span style='color:#000000;font-weight:bold'>CI/CD</span> pipeline using <span style='color:#000000;font-weight:bold'>Docker</span>. Thereby, reducing the TCO by <span style='color:#000000;font-weight:bold'>20%</span> to maintain machines and databases
# - Coordinated with teams on effective strategies to migrate monolithic architecture to microservices, saving <span style='color:#000000;font-weight:bold'>30%</span> time on new modules
# ''', unsafe_allow_html=True)

# #####################
# st.markdown("""---""")
# st.markdown('''
# ## Projects
# ''')

# txt("**<span style='color:#000000'>AndroXmeda</span>**, *<span style='color:#000000'>Northeastern University</span>*, Boston, MA",
# 'Jan 2023 - Apr 2023')
# st.markdown('''
# - Modeled a REST API with <span style='color:#000000;font-weight:bold'>NodeJS, Express, Postgres, Bcrypt and Sequelize ORM</span> for a Full-Stack application in ReactJS
# - Deployed the REST API on AWS CloudFormation using <span style='color:#000000;font-weight:bold'>S3, RDS and EC2</span> using a custom AMI built using Packer
# - Modeled custom <span style='color:#000000;font-weight:bold'>GitHub Actions</span> to setup CI/CD pipelines for streamlining API delivery with <span style='color:#000000;font-weight:bold'>AWS SES</span> notifications
# ''', unsafe_allow_html=True)

# txt("**<span style='color:#000000'>Economics of Happiness</span>**, <span style='color:#000000'>Northeastern University</span>, Boston, MA",
# 'Dec 2022')
# st.markdown('''
# - Determined the optimal border value for the <span style='color:#000000;font-weight:bold'>classification</span> of Happy Score (Ordinal Values) into "Happy" or "Sad", utilizing various mathematical measures, such as the mean, median, harmonic mean, and geometric mean 
# - Examined the impact of utilizing different border values on the performance of models and the relative importance of predictors
# ''', unsafe_allow_html=True)

# txt("**<span style='color:#000000'>Wine Quality Prediction</span>**, <span style='color:#000000'>Northeastern University</span>, Boston, MA",
# 'Oct 2022')
# st.markdown('''
# - Tuned hyperparameters using <span style='color:#000000;font-weight:bold'>Regression, Classification and AutoML</span> to gain insights on why predicting a wine's quality in ordinal values are less accurate than classifying it.
# ''', unsafe_allow_html=True)

# txt("**<span style='color:#000000'>Image Feature Comparison and Ranking, under Dr. Ajitha Shenoy</span>**, <span style='color:#000000'>Manipal Institute of Technology</span>, India",
# 'Jan 2017- Jun 2017')
# st.markdown('''
# - Extracted features from query image stored in <span style='color:#000000;font-weight:bold'>AWS s3</span>. Compared and matched the <span style='color:#000000;font-weight:bold'>SURF</span> features and returned top 10 matching images with an accuracy of <span style='color:#000000;font-weight:bold'>92.7%</span>. The developed model was immune to image rotation
# - This tool is used by Manipal Institute of Technology for library catalogue management, saving <span style='color:#000000;font-weight:bold'>1.5</span> hours of librarian work everyday
# ''', unsafe_allow_html=True)

# txt("**<span style='color:#000000'>Do My Chores: Microsoft Code.Fun.Do Hackathon</span>**, <span style='color:#000000'>Manipal Institute of Technology</span>, India",
# 'Aug 2016')
# st.markdown('''
# - Developed a windows application to help students do or get chores done with an associated payout, cutting down late submissions by <span style='color:#000000;font-weight:bold'>20%</span>. Chores were displayed as markers on google maps
# ''', unsafe_allow_html=True)


# #####################
# st.markdown("""---""")
# st.markdown('''
# ## Social Media
# ''')
# txt2("**<span style='color:#000000'>LinkedIn</span>**", "<span style='color:#000000'>https://www.linkedin.com/in/rishabhindoria/</span>")
# txt2("**<span style='color:#000000'>GitHub</span>**", "<span style='color:#000000'>https://github.com/rishabhindoria25/</span>")
# txt2("**<span style='color:#000000'>Kaggle</span>**", "<span style='color:#000000'>https://www.kaggle.com/rishabhindoria</span>")

# #####################
# st.markdown("""---""")
# st.header("Contact Me")


# contact_form = """
# <form action="https://formsubmit.co/indoriarishabh25@gmail.com" method="POST">
#      <input type="hidden" name="_captcha" value="false">
#      <input type="text" name="name" placeholder="Your name" required>
#      <input type="email" name="email" placeholder="Your email" required>
#      <textarea name="message" placeholder="Your message here"></textarea>
#      <button type="submit">Send</button>
# </form>
# """

# st.markdown(contact_form, unsafe_allow_html=True)

# st.markdown("""---""")

# with open("style.css") as f:
#     st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
# st.markdown('![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://share.streamlit.io/https://rishabhindoria25-resume-streamlit-app-rxhkpg.streamlit.app&label=VisitorsCount&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')

# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

import streamlit as st
from streamlit_timeline import timeline
from PIL import Image

# Define your variables
PAGE_TITLE = "Rishabh Indoria"
PAGE_ICON = ":wave:"
NAME = "Rishabh Indoria"
DESCRIPTION = """
Highly accomplished data scientist with a strong focus on achieving measurable results.
"""
EMAIL = "indoriarishabh25@gmail.com"

# Load your images and resume file here
profile_pic = Image.open('dp.png')
resume_file = "RishabhIndoria_Resume.pdf"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Hero Section
st.write("# **<span style='color:#000000'>Rishabh Indoria</span>** ~~THE IT CROWD~~", unsafe_allow_html=True)
st.image(profile_pic, width=150)
st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?**
\nI am a highly accomplished data scientist with a strong focus on achieving measurable results. I possess extensive experience working within cross-functional teams to achieve organizational objectives. Being highly motivated to innovate existing business processes, I achieve optimal results in an efficient and cost-effective manner, utilizing my in-depth domain expertise. I have consistently demonstrated exceptional diligence and commitment to excellence in both my coursework and various work. I am eager to continue this level of performance in future projects, utilizing diverse models, frameworks, and data.
''')

# Navigation
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #021014;">
  <a style="color: #16A2CB" class="navbar-brand" target="_blank">Rishabh Indoria</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a style="color: #FFFFFF" class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a style="color: #FFFFFF" class="nav-link" href="#career-snapshot">Career snapshots</a>
      </li>
      <li class="nav-item">
        <a style="color: #FFFFFF" class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a style="color: #FFFFFF" class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a style="color: #FFFFFF" class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a style="color: #FFFFFF" class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a, unsafe_allow_html=True)
    with col2:
        st.markdown(b, unsafe_allow_html=True)

def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'{a}', unsafe_allow_html=True)
    with col2:
        st.markdown(b, unsafe_allow_html=True)

def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a, unsafe_allow_html=True)
    with col2:
        st.markdown(b, unsafe_allow_html=True)

def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`', unsafe_allow_html=True)
    with col2:
        st.markdown(b, unsafe_allow_html=True)
    with col3:
        st.markdown(c, unsafe_allow_html=True)

# Define your text content using the custom functions
# Header
txt("# **<span style='color:#000000'>Rishabh Indoria</span>** ~~THE IT CROWD~~", unsafe_allow_html=True)

# Career Snapshot
st.write("# **<span style='color:#000000'>Rishabh Indoria</span>** ~~THE IT CROWD~~", unsafe_allow_html=True)
st.image(profile_pic, width=150)
st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?**
\nI am a highly accomplished data scientist with a strong focus on achieving measurable results. I possess extensive experience working within cross-functional teams to achieve organizational objectives. Being highly motivated to innovate existing business processes, I achieve optimal results in an efficient and cost-effective manner, utilizing my in-depth domain expertise. I have consistently demonstrated exceptional diligence and commitment to excellence in both my coursework and various work. I am eager to continue this level of performance in future projects, utilizing diverse models, frameworks, and data.
''')

# Career Snapshot
st.markdown("---")
st.markdown('''
## Career-snapshot
'')

with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

# Education
st.markdown("---")
st.markdown('''
## Education
''')

txt("**<span style='color:#000000'>Masters of Science</span>** (Information Systems), *<span style='color:#000000'>Northeastern University</span>*, Boston, Massachusetts",
'2022-2024')
st.markdown('''
- GPA: **<span style='color:#000000'>3.76</span>**
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>Bachelors of Technology</span>** (Information Technology), *<span style='color:#000000'>Manipal Institute of Technology</span>*, Manipal, India",
'2013-2017')

# Skills
st.markdown("---")
st.markdown('''
## Skills
''')

txt3("**<span style='color:#000000'>Language</span>**", "<span style='color:#000000'>Python,&ensp;Javascript,&ensp;Node.js,&ensp;SQL,&ensp;HTML,&ensp;CSS,&ensp;React.js</span>")
txt3("**<span style='color:#000000'>Database</span>**", "<span style='color:#000000'>InfluxDB, &ensp; MongoDB ,&ensp;  MSSQL , &ensp; Redshift ,&ensp;  DynamoDB</span>")
txt3("**<span style='color:#000000'>Frameworks</span>**", "<span style='color:#000000'>Pycaret , &ensp; PyTorch , &ensp; Scikit-learn ,&ensp;  Telegraf , &ensp; Flask ,&ensp; streamlit, &ensp;  keras ,  &ensp; Tensorflow</span>")
txt3("**<span style='color:#000000'>Cloud Tools</span>**", "<span style='color:#000000'>AWS (EC2, S3, RDS, SES, SNS, Route 53, CloudFormation, CloudWatch, Lambda, IoT Core)</span>")
txt3("**<span style='color:#000000'>Tools</span>**", "<span style='color:#000000'>Postman , &ensp; Docker ,&ensp;  Kubernetes ,&ensp;  VS code</span>")
txt3("**<span style='color:#000000'>CI/CD</span>**", "<span style='color:#000000'>Git , &ensp; Jenkins , &ensp; Jira , &ensp; XL-Deploy</span>")
txt3("**<span style='color:#000000'>Data Visualization</span>**", "<span style='color:#000000'> Grafana ,&ensp;  Chart.js , &ensp; Tableau , &ensp; PowerBI</span>")

# Work Experience
st.markdown("---")
st.markdown('''
## Work Experience
''')

txt("**<span style='color:#000000'>Lead Data Scientist</span>**, *<span style='color:#000000'>Urja.io</span>*, India",
'2021-2022')
st.markdown('''
- Developed model using <span style='color:#000000;font-weight:bold'>unsupervised K-means clustering</span> and <span style='color:#000000;font-weight:bold'>fbprophet</span> to forecast machine maintenance using peak detection and <span style='color:#000000;font-weight:bold'>Time-series Data</span>. Achieved <span style='color:#000000;font-weight:bold'>97%</span> accuracy
- Engineered a data ingestion pipeline that utilized <span style='color:#000000;font-weight:bold'>AWS IoT Core, InfluxDB, and Telegraf</span> to ingest real-time time-series data sent by 2,000 IoT devices. Thus, reducing data loss to <span style='color:#000000;font-weight:bold'>1%</span>
- Designed a parallel channel for data ingestion via HTTP chunked protocol and Telegraf directory monitoring plugin, leading to <span style='color:#000000;font-weight:bold'>zero</span> service charge for IoT data management
- Supervised the development team and coordinated with clients to build an in-house one-stop interaction dashboard to remove dependency on Grafana Labs for energy data visualization, leading to <span style='color:#000000;font-weight:bold'>25%</span> increase in insights
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>Software Engineer</span>**, *<span style='color:#000000'>Société Générale</span>*, India",
'2017-2020')
st.markdown('''
- Automated the daily reporting system, reducing report generation efforts by <span style='color:#000000;font-weight:bold'>6</span> person-days each month
- Developed and deployed <span style='color:#000000;font-weight:bold'>REST APIs</span> for global teams to get trade data saving <span style='color:#000000;font-weight:bold'>2.5</span> person-hours daily in ad-hoc ticket requests
- Migrated existing applications running on on-prem machines to <span style='color:#000000;font-weight:bold'>AWS EC2</span>, by creating <span style='color:#000000;font-weight:bold'>CI/CD</span> pipeline using <span style='color:#000000;font-weight:bold'>Docker</span>. Thereby, reducing the TCO by <span style='color:#000000;font-weight:bold'>20%</span> to maintain machines and databases
- Coordinated with teams on effective strategies to migrate monolithic architecture to microservices, saving <span style='color:#000000;font-weight:bold'>30%</span> time on new modules
''', unsafe_allow_html=True)

# Projects
st.markdown("---")
st.markdown('''
## Projects
''')

txt("**<span style='color:#000000'>AndroXmeda</span>**, *<span style='color:#000000'>Northeastern University</span>*, Boston, MA",
'Jan 2023 - Apr 2023')
st.markdown('''
- Modeled a REST API with <span style='color:#000000;font-weight:bold'>NodeJS, Express, Postgres, Bcrypt and Sequelize ORM</span> for a Full-Stack application in a team of 5
- Optimized the performance of the server and the codebase with <span style='color:#000000;font-weight:bold'>Async-Await, NPM scripts</span> and <span style='color:#000000;font-weight:bold'>Advanced JS/ES6</span>
- Designed an Android application to interact with the server using <span style='color:#000000;font-weight:bold'>Android Studio</span>
- Implemented user-authentication using <span style='color:#000000;font-weight:bold'>JWT Tokens</span> to enhance security of data
- Enhanced overall efficiency by building complex SQL queries using <span style='color:#000000;font-weight:bold'>SQL View</span> and optimizing it further using <span style='color:#000000;font-weight:bold'>Indexes</span>
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>StockX-Dataset-Analysis</span>**, *<span style='color:#000000'>Northeastern University</span>*, Boston, MA",
'Jan 2023 - Apr 2023')
st.markdown('''
- Conducted data analysis on a dataset containing information about products listed on StockX
- Created various visualizations using <span style='color:#000000;font-weight:bold'>Matplotlib and Seaborn</span> to gain insights into market trends
- Utilized <span style='color:#000000;font-weight:bold'>Pandas</span> for data manipulation and cleaning
- Developed a <span style='color:#000000;font-weight:bold'>Machine Learning model using Scikit-Learn</span> to predict the price of sneakers based on various features
- Presented findings and insights to the class in an organized and visually appealing manner using <span style='color:#000000;font-weight:bold'>Jupyter Notebook</span>
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>IoT-Based Energy Management System</span>**, *<span style='color:#000000'>Urja.io</span>*, India",
'Jan 2021 - Apr 2021')
st.markdown('''
- Designed and developed a scalable IoT-based energy management system to help industries monitor, analyze, and optimize energy consumption
- Set up the entire backend infrastructure on AWS, including IoT Core for device connectivity, InfluxDB for time-series data storage, and Lambda functions for data processing
- Developed a real-time dashboard using Grafana for data visualization and anomaly detection
- Implemented machine learning models for predictive maintenance of industrial machines
- Successfully reduced energy consumption by 20% in pilot projects for clients in the manufacturing sector
''', unsafe_allow_html=True)

# Contact Information
st.markdown("---")
st.markdown('''
## Contact Information
''')

txt2("Email", EMAIL)
txt2("LinkedIn", "[Connect with me](https://www.linkedin.com/in/rishabh-indoria/)")
txt2("GitHub", "[Check out my GitHub](https://github.com/RishabhIndoria)")
st.markdown(f"[Download my Resume](data:application/pdf;base64,{PDFbyte.decode('latin1')})", unsafe_allow_html=True)

# Social Media Links
st.markdown("---")
st.markdown('''
## Social Media
''')

st.image("https://img.icons8.com/cute-clipart/64/000000/linkedin.png", use_column_width=True)
st.image("https://img.icons8.com/cute-clipart/64/000000/github.png", use_column_width=True)

# Footer
st.markdown("---")
st.markdown('''
### Connect with me!
''')

st.markdown('<p><span style="color: #16A2CB; font-weight: 500;">Disclaimer:</span> This website is under construction</p>', unsafe_allow_html=True)

# Add timeline
timeline('''
{
    "dateTimeFormat": "iso",
    "events": [
        {
            "start": "2022-05-01T00:00:00.000Z",
            "title": "Job at Urja.io",
            "subtitle": "Lead Data Scientist",
            "content": "Joined Urja.io as a Lead Data Scientist, where I worked on developing machine learning models for predictive maintenance and energy management in industrial IoT."
        },
        {
            "start": "2021-08-01T00:00:00.000Z",
            "end": "2022-05-01T00:00:00.000Z",
            "title": "Master's Degree",
            "subtitle": "Northeastern University",
            "content": "Pursued a Master's degree in Information Systems from Northeastern University, specializing in data science and machine learning."
        },
        {
            "start": "2017-07-01T00:00:00.000Z",
            "end": "2020-07-01T00:00:00.000Z",
            "title": "Job at Société Générale",
            "subtitle": "Software Engineer",
            "content": "Worked as a Software Engineer at Société Générale, where I developed and maintained software applications for financial data analysis and reporting."
        },
        {
            "start": "2013-08-01T00:00:00.000Z",
            "end": "2017-07-01T00:00:00.000Z",
            "title": "Bachelor's Degree",
            "subtitle": "Manipal Institute of Technology",
            "content": "Completed my Bachelor's degree in Information Technology from Manipal Institute of Technology."
        }
    ]
}
''', height=300)

