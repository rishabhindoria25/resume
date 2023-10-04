import streamlit as st
from streamlit_timeline import timeline
from PIL import Image
image = Image.open("icon.jpg")
profile_pic = Image.open('dp.png')
resume_file = "RishabhIndoria_Resume.pdf"
Email = "indoria.r@northeastern.edu",
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/rishabhindoria/",
    "GitHub": "https://github.com/rishabhindoria25",
    "Kaggle": "https://www.kaggle.com/rishabhindoria",
}

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.set_page_config(page_title="Rishabh Indoria", page_icon=image, layout="centered", initial_sidebar_state="auto")
st.write("# **<span style='color:#000000'>Rishabh Indoria</span>** ~~THE IT CROWD~~", unsafe_allow_html=True)
# Load the image
profile_pic = Image.open('dp.png')
st.image(profile_pic, width=230)
st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream",
    )

st.write("Email", Email)


# st.markdown("""---""")
st.markdown('## Summary', unsafe_allow_html=True)
st.markdown("""---""")
st.info('''
<div style="text-align: center;">
    <strong>HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?</strong>
</div>
<div style="text-align: center;">
    I am a highly accomplished data scientist with a strong focus on achieving measurable results. I possess extensive experience working within cross-functional teams to achieve organizational objectives. Being highly motivated to innovate existing business processes, I achieve optimal results in an efficient and cost-effective manner, utilizing my in-depth domain expertise. I have consistently demonstrated exceptional diligence and commitment to excellence in both my coursework and various work. I am eager to continue this level of performance in future projects, utilizing diverse models, frameworks, and data.
</div>
''', unsafe_allow_html=True)
# st.info('''
# &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?**
# \nI am a highly accomplished data scientist with a strong focus on achieving measurable results. I possess extensive experience working within cross-functional teams to achieve organizational objectives. Being highly motivated to innovate existing business processes, I achieve optimal results in an efficient and cost-effective manner, utilizing my in-depth domain expertise. I have consistently demonstrated exceptional diligence and commitment to excellence in both my coursework and various work. I am eager to continue this level of performance in future projects, utilizing diverse models, frameworks, and data.
# ''')

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
st.markdown('''
## Career-snapshot
''')
st.markdown("""---""")    
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

#####################
st.markdown('''
## Education
''')
st.markdown("""---""")
txt("**<span style='color:#000000'>Masters of Science</span>** (Information Systems), *<span style='color:#000000'>Northeastern University</span>*, Boston, Massachusetts",
'2022-2024')
st.markdown('''
- GPA: **<span style='color:#000000'>3.75</span>**
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>Bachelors of Technology</span>** (Information Technology), *<span style='color:#000000'>Manipal Institute of Technology</span>*, Manipal, India",
'2013-2017')

#####################
st.markdown('''
## Skills
''')
st.markdown("""---""")
txt3("**<span style='color:#000000'>Software Programming and Scripting</span>**", "<span style='color:#000000'>Python,&ensp; Spark,&ensp; Java,&ensp; SQL,&ensp; Kafka,&ensp; Linux,&ensp; Numpy,&ensp; Pandas,&ensp; MATLAB,&ensp; Algorithms</span>")
txt3("**<span style='color:#000000'>Machine Learning</span>**", "<span style='color:#000000'>Scikit-Learn,&ensp; Multivariate Statistics,&ensp; Supervised/Unsupervised learning,&ensp; Bayesian Models,&ensp; Statistical learning</span>")
txt3("**<span style='color:#000000'>Deep Learning</span>**", "<span style='color:#000000'>TensorFlow,&ensp; Keras,&ensp; PyCaret,&ensp; PyTorch,&ensp; Natural Language Processing (NLP),&ensp; Large Language Models (LLM),&ensp; Azure Computer vision,&ensp; CNN</span>")
txt3("**<span style='color:#000000'>Web Development</span>**", "<span style='color:#000000'>Flask,&ensp; Streamlit,&ensp; FastAPI,&ensp; Node.js,&ensp; Express.js,&ensp; React.js,&ensp; Nginx,&ensp; Gunicorn,&ensp; HTTP chunked protocol</span>")
txt3("**<span style='color:#000000'>Cloud</span>**", "<span style='color:#000000'>AWS (Ec2,&ensp; IoT,&ensp; S3,&ensp; CloudFront,&ensp; Lambda,&ensp; Cloudwatch,&ensp; Redshift),&ensp; GCP,&ensp; Git,&ensp; Airflow,&ensp; Terraform,&ensp; SageMaker</span>")
txt3("**<span style='color:#000000'>Data Warehouse</span>**", "<span style='color:#000000'>Snowflake,&ensp; Redis,&ensp; Pinecone,&ensp; InfluxDB,&ensp; Telegraf,&ensp; Hadoop,&ensp; Hive,&ensp; Databricks</span>")
txt3("**<span style='color:#000000'>Data Visualization and Analysis Tools</span>**", "<span style='color:#000000'>PowerBI,&ensp; Tableau,&ensp; ChartJS,&ensp; Grafana Labs,&ensp; MS Excel</span>")
txt3("**<span style='color:#000000'>Business Skills</span>**", "<span style='color:#000000'>Agile standup,&ensp; Decision-making,&ensp; Attention-to-detail,&ensp; Fintech</span>")

# st.markdown("""---""")
# txt3("**<span style='color:#000000'>Software Programming and Scripting</span>**", "<span style='color:#000000'>Python,&ensp;Javascript,&ensp;Node.js,&ensp;SQL,&ensp;HTML,&ensp;CSS,&ensp;React.js</span>")
# txt3("**<span style='color:#000000'>Database</span>**", "<span style='color:#000000'>InfluxDB, &ensp; MongoDB ,&ensp;  MSSQL , &ensp; Redshift ,&ensp;  DynamoDB</span>")
# txt3("**<span style='color:#000000'>Frameworks</span>**", "<span style='color:#000000'>Pycaret , &ensp; PyTorch , &ensp; Scikit-learn ,&ensp;  Telegraf , &ensp; Flask ,&ensp; streamlit, &ensp;  keras ,  &ensp; Tensorflow</span>")
# txt3("**<span style='color:#000000'>Cloud Tools</span>**", "<span style='color:#000000'>AWS (EC2, S3, RDS, SES, SNS, Route 53, CloudFormation, CloudWatch, Lambda, IoT Core)</span>")
# txt3("**<span style='color:#000000'>Tools</span>**", "<span style='color:#000000'>Postman , &ensp; Docker ,&ensp;  Kubernetes ,&ensp;  VS code</span>")
# txt3("**<span style='color:#000000'>CI/CD</span>**", "<span style='color:#000000'>Git , &ensp; Jenkins , &ensp; Jira , &ensp; XL-Deploy</span>")
# txt3("**<span style='color:#000000'>Data Visualization</span>**", "<span style='color:#000000'> Grafana ,&ensp;  Chart.js , &ensp; Tableau , &ensp; PowerBI</span>")

#####################

st.markdown('''
## Work Experience
''')
st.markdown("""---""")
txt("**<span style='color:#000000'>Lead Data Scientist</span>**, *<span style='color:#000000'>Urja.io</span>*, India",
'2021-2022')
st.markdown('''
- Spearheaded the development team in creating an analytics dashboard platform, resulting in a 25% increase in client engagement
- Achieved a 23% cost reduction by delivering a 94% accurate machinery failure prediction using fbprophet time series forecasting
- Built a customer churn model with a 70% recall and prescriptive reports on Tableau to retain IoT business
- Implemented a scalable distributed ETL/ELT pipeline infrastructure, enabling real-time time-series data collection and anomaly detection from structured or unstructured data generated by 2,000 IoT devices with minimal data loss
- Saved 10 person-hours biweekly by efficiently communicating A/B test results to stakeholders via concise, automated reports
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>Software Engineer</span>**, *<span style='color:#000000'>Société Générale</span>*, India",
'2017-2020')
st.markdown('''
- Realized a 20% cost reduction and accelerated module implementation by 30% through streamlined REST API development and global Infrastructure as Code deployment using Terraform, Packer AMI, and Gitlab CI/CD
- Enhanced fraud detection by 17% by applying predictive modeling techniques to detect irregular transaction volume changes
- Improved risk management by 21% via identification of high-value transactions exceeding model forecasts
''', unsafe_allow_html=True)

#####################
st.markdown('''
## Projects
''')
st.markdown("""---""")
txt("**<span style='color:#000000'>[ImagiGEN](https://github.com/orgs/ImagiGEN/repositories)</span>**, *<span style='color:#000000'>Northeastern University</span>*, Boston, MA",
'May 2023 - Aug 2023')
st.markdown('''
- Developed an emotion-aware audio journaling app with voice tone analysis for precise emotional detection. Integrated mood chart visualization and prompt engineering to achieve a 20% increase in user retention
- Led cross-functional teams in creating a contextual search tool for financial researchers, introducing vector similarity, traditional filters, and hybrid search approaches to enhance information retrieval speed by 50% with greater context for improved insights
- Created Azure computer vision 4.0 diffusion model-based Model-as-a-Service for automatic image analysis, precise product search, and efficient clustering of images, leading to a 35% search precision boost and 40% faster processing
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>[Economics of Happiness](https://github.com/rishabhindoria25/Economics_of_Happiness)</span>**, <span style='color:#000000'>Northeastern University</span>, Boston, MA",
'Dec 2022')
st.markdown('''
- Conducted exploratory analysis using regression, classification, and AutoML to understand relationships between economic indicators and happiness index across 150 countries
- Performed hyperparameter tuning and SHAP analysis of economic factors’ impact on happiness, gaining 15% more insights
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>[QueryVision](https://github.com/rishabhindoria25/QueryVision), under Dr. Ajitha Shenoy</span>**, <span style='color:#000000'>Manipal Institute of Technology</span>, India",
'Jan 2017- Jun 2017')
st.markdown('''
- Developed a Python script for image similarity search using a pre-trained VGG16 deep learning model, facilitating the retrieval of visually similar images from a dataset. Achieved a top-10 matching accuracy rate of 95% on a diverse collection of 10,000 book cover images.
- Implemented feature extraction and cosine similarity calculation techniques, processing and analyzing a dataset of over 10,000 images with an average query time of under 1 second per image. Demonstrated strong analytical and machine learning skills in the context of computer vision, resulting in improved search efficiency and user experience. 
''', unsafe_allow_html=True)

txt("**<span style='color:#000000'>[AndroXmeda](https://github.com/AndroXmeda)</span>**, *<span style='color:#000000'>Northeastern University</span>*, Boston, MA",
'Jan 2023 - Apr 2023')
st.markdown('''
- Modeled a REST API with <span style='color:#000000;font-weight:bold'>NodeJS, Express, Postgres, Bcrypt and Sequelize ORM</span> for a Full-Stack application in ReactJS
- Deployed the REST API on AWS CloudFormation using <span style='color:#000000;font-weight:bold'>S3, RDS and EC2</span> using a custom AMI built using Packer
- Modeled custom <span style='color:#000000;font-weight:bold'>GitHub Actions</span> to setup CI/CD pipelines for streamlining API delivery with <span style='color:#000000;font-weight:bold'>AWS SES</span> notifications
''', unsafe_allow_html=True)

#####################
# Add social media links

st.markdown("## Find me on")
st.markdown("""---""")
# st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    with cols[index].container():
        st.markdown(f"<p style='text-align:center'><a href='{link}'>{platform}</a></p>", unsafe_allow_html=True)
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#         cols[index].write(f"[{platform}]({link})")
st.footer()
    # cols[index].write(f"[{platform}]({link})")
# with st.footer("Copyright © 2023 Example"):

#         # Create columns for each social media platform
#         cols = st.columns(len(SOCIAL_MEDIA))

#         # Iterate over the social media platforms and add links to the footer
#         for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#             cols[index].write(f"[{platform}]({link})")
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
# st.markdown('![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://share.streamlit.io/https://rishabhindoria25-resume-streamlit-app-rxhkpg.streamlit.app&label=VisitorsCount&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
