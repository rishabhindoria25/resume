import streamlit as st
from streamlit_timeline import timeline
from PIL import Image
image = Image.open("icon.jpg")
st.set_page_config(page_title="Rishabh Indoria", page_icon=image,layout="centered", initial_sidebar_state="auto")
# PAGE_CONFIG = {"page_title":, 
#                "page_icon":, 
#                "layout":"centered", 
#                "initial_sidebar_state":"auto"}

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
st.markdown('![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://share.streamlit.io/https://rishabhindoria25-resume-streamlit-app-rxhkpg.streamlit.app&label=VisitorsCount&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')
#####################
# Header 
st.write("# **<span style='color:#000000'>Rishabh Indoria</span>**, ~~THE IT CROWD~~", unsafe_allow_html=True)

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?**
\nI am a highly accomplished scientist with a strong focus on achieving measurable results. I possess extensive experience working within cross-functional teams to achieve organizational objectives. I am highly motivated to innovate existing business processes and to achieve optimal results in an efficient and cost-effective manner, utilizing my in-depth domain expertise. I have consistently demonstrated exceptional diligence and a commitment to excellence in both my coursework and various tasks. I am eager to continue this level of performance in the future, utilizing diverse models, frameworks, and data.
''')

#####################
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
        <a style="color: #FFFFFF" class="nav-link" href="#career-snapshot">Career snapshot</a>
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

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a, unsafe_allow_html=True)
  with col2:
    st.markdown(b, unsafe_allow_html=True)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'{a}', unsafe_allow_html=True)
  with col2:
    st.markdown(b, unsafe_allow_html=True)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a, unsafe_allow_html=True)
  with col2:
    st.markdown(b, unsafe_allow_html=True)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`', unsafe_allow_html=True)
  with col2:
    st.markdown(b, unsafe_allow_html=True)
  with col3:
    st.markdown(c, unsafe_allow_html=True)

#####################
st.markdown("""---""")
st.markdown('''
## Career-snapshot
''')
    
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

#####################
st.markdown("""---""")
st.markdown('''
## Education
''')
txt("**<span style='color:#000000'>Masters of Science</span>** (Information Systems), *<span style='color:#000000'>Northeastern University</span>*, Boston, Massachusetts",
'2022-2024')
st.markdown('''
- GPA: **<span style='color:#000000'>3.67</span>**
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>Bachelors of Technology</span>** (Information Technology), *<span style='color:#000000'>Manipal Institute of Technology</span>*, Manipal, India",
'2013-2017')

#####################
st.markdown("""---""")
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

#####################
st.markdown("""---""")
st.markdown('''
## Work Experience
''')

txt("**<span style='color:#000000'>Lead Data Scientist</span>**, *<span style='color:#000000'>Urja.io</span>*, India",
'2021-2022')
st.markdown('''
- Developed model using <span style='color:#000000'>unsupervised K-means clustering</span> and <span style='color:#000000'>fbprophet</span> to forecast machine maintenance using peak detection and <span style='color:#000000'>Time-series Data</span>. Achieved <span style='color:#000000'>97%</span> accuracy
- Engineered a data ingestion pipeline that utilized <span style='color:#000000'>AWS IoT Core, InfluxDB, and Telegraf</span> to ingest real-time time-series data sent by 2000 IoT devices. Thus, reducing data loss to <span style='color:#000000'>1%</span>
- Designed a parallel channel for data ingestion via HTTP chunked protocol and Telegraf directory monitoring plugin, leading to <span style='color:#000000'>zero</span> service charge for IoT data management
- Supervised the dev team and coordinated with clients to build an in-house one-stop interaction dashboard to remove dependency on Grafana Labs for energy data visualization, leading to 25% more insights
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>Software Engineer</span>**, *<span style='color:#000000'>Société Générale</span>*, India",
'2017-2020')
st.markdown('''
- Automated the daily reporting system, reducing report generation efforts by <span style='color:#000000'>6</span> person-days over a period of month
- Developed and deployed <span style='color:#000000'>REST APIs</span> for global teams to get trade data saving <span style='color:#000000'>2.5</span> person-hours daily in ad-hoc ticket requests
- Migrated existing applications running on on-prem machines to <span style='color:#000000'>AWS EC2</span>, by creating <span style='color:#000000'>CI/CD</span> pipeline using <span style='color:#000000'>Docker</span>. Thereby, reducing the TCO by <span style='color:#000000'>20%</span> to maintain machines and databases
- Coordinated with teams on effective strategies to migrate monolithic architecture to microservices, saving 30% time on new modules
''', unsafe_allow_html=True)

#####################
st.markdown("""---""")
st.markdown('''
## Projects
''')

txt("**<span style='color:#000000'>AndroXmeda</span>**, *<span style='color:#000000'>Northeastern University</span>*, Boston, MA",
'Jan 2023 - Apr 2023')
st.markdown('''
- Modeled a REST API with <span style='color:#000000'>NodeJS, Express, Postgres, Bcrypt and Sequelize ORM</span> for a Full-Stack application in ReactJS
- Deployed the REST API on AWS CloudFormation using <span style='color:#000000'>S3, RDS and EC2</span> using a custom AMI built using Packer
- Modeled custom <span style='color:#000000'>GitHub Actions</span> to setup CI/CD pipelines for streamlining API delivery with <span style='color:#000000'>AWS SES</span> notifications
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>Economics of Happiness</span>**, <span style='color:#000000'>Northeastern University</span>, Boston, MA",
'Dec 2022')
st.markdown('''
- Determined the optimal border value for the <span style='color:#000000'>classification</span> of Happy Score (Ordinal Values) into "Happy" or "Sad", utilizing various mathematical measures, such as the mean, median, harmonic mean, and geometric mean 
- Examined the impact of utilizing different border values on the performance of models and the relative importance of predictors
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>Wine Quality Prediction</span>**, <span style='color:#000000'>Northeastern University</span>, Boston, MA",
'Oct 2022')
st.markdown('''
- Gained insights on why predicting a wine's quality in ordinal values are less accurate than classifying, employing <span style='color:#000000'>Regression, Classification and AutoML</span> with tuned hyperparameters
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>Image Feature Comparison and Ranking, under Dr. Ajitha Shenoy</span>**, <span style='color:#000000'>Manipal Institute of Technology</span>, India",
'Jan 2017- Jun 2017')
st.markdown('''
- Extracted features from query image stored in <span style='color:#000000'>AWS s3</span>. Compared and matched the <span style='color:#000000'>SURF</span> features and returned top 10 matching images with an accuracy of <span style='color:#000000'>92.7%</span>. The developed model was immune to image rotation
- This tool is used by Manipal Institute of Technology for library catalogue management, saving <span style='color:#000000'>1.5</span> hours of librarian everyday
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>Do My Chores: Microsoft Code.Fun.Do Hackathon</span>**, <span style='color:#000000'>Manipal Institute of Technology</span>, India",
'Aug 2016')
st.markdown('''
- Developed a windows application to help students do or get chores done with an associated payout, cutting down late submissions by <span style='color:#000000'>20%</span>. Chores were displayed as markers on google maps
''', unsafe_allow_html=True)


#####################
st.markdown("""---""")
st.markdown('''
## Social Media
''')
txt2("**<span style='color:#000000'>LinkedIn</span>**", "<span style='color:#000000'>https://www.linkedin.com/in/rishabhindoria/</span>")
txt2("**<span style='color:#000000'>GitHub</span>**", "<span style='color:#000000'>https://github.com/rishabhindoria25/</span>")
txt2("**<span style='color:#000000'>Kaggle</span>**", "<span style='color:#000000'>https://www.kaggle.com/rishabhindoria</span>")

#####################
st.markdown("""---""")
st.header("Contact Me")


contact_form = """
<form action="https://formsubmit.co/indoriarishabh25@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
