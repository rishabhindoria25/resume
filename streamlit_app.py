import streamlit as st
from streamlit_timeline import timeline
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Rishabh Indoria, THE IT CROWD
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?
- Experienced Educator, Researcher and Administrator with almost twenty years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Strong verbal and written communication skills as demonstrated by extensive participation as invited speaker at `10` conferences as well as publishing 149 research articles.
- Strong track record in scholarly research with H-index of `32` and total citation of 3200+.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" target="_blank">Rishabh Indoria</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#career-snapshot">Career snapshot</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
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
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################

st.markdown('''
## Career-snapshot
''')
    
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

#####################
st.markdown('''
## Education
''')

txt('**Masters of Science** (Information Technology), *Northeastern University*, Boston, Massachusetts',
'2022-2024')
st.markdown('''
- GPA: `3.67`
''')

txt('**Bachelors of Technology** (Information Technology), *Manipal Institute of Technology*, India',
'2013-2017')

#####################
st.markdown('''
## Skills
''')
txt3('Language', '`Python`, `JavaScript`, `Java`, `Node.js`, `SQL`, `HTML`, `CSS`, `React.js`')
txt3('Database', '`InfluxDB`, `MongoDB`, `MSSQL`, `Redshift`, `DynamoDB`')
txt3('Frameworks', '`Pycaret`, `PyTorch`, `Scikit-learn`, `Telegraf`, `Flask`, `keras`, `Tensorflow`')
txt3('Cloud Tools', '`AWS (EC2, S3, RDS, SES, SNS, Route 53, CloudFormation, CloudWatch, Lambda, IoT Core)`')
txt3('Tools', '`Postman`, `Docker`, `Kubernetes`, `VS code`')
txt3('CI/CD', '`Git`, `Jenkins`, `Jira`, `XL-Deploy`')
txt3('Data Visualization', '`Grafana`, `Chart.js`, `Tableau`, `PowerBI`')

#####################
st.markdown('''
## Work Experience
''')

txt('**Lead Data Scientist, Urja.io**, India',
'2021-2022')
st.markdown('''
- Developed model using unsupervised K-means clustering and fbprophet to forecast machine maintenance using peak detection and Time-series Data. Achieved 97% accuracy
- Engineered a data ingestion pipeline that utilized AWS IoT Core, InfluxDB, and Telegraf to ingest real-time time-series data sent by 2000 IoT devices. Thus, reducing data loss to 1%
- Designed a parallel channel for data ingestion via HTTP chunked protocol and Telegraf directory monitoring plugin, leading to zero service charge for IoT data management
- Supervised the dev team and coordinated with clients to build an in-house one-stop interaction dashboard to remove dependency on Grafana Labs for energy data visualization
''')

txt('**Software Engineer**, Société Générale, India',
'2017-2020')
st.markdown('''
- Automated the daily reporting system, reducing report generation efforts by six person-days over a period of month
- Developed and deployed REST APIs for global teams to get trade data saving 2.5 person-hours daily in ad-hoc ticket requests
- Migrated existing applications running on on-prem machines to AWS ECS, by creating CI/CD pipeline using Docker. Thereby, reducing the TCO by 20% to maintain machines and databases
- Coordinated with teams on effective strategies to migrate monolithic architecture to microservices
''')

#####################
st.markdown('''
## Projects
''')

txt('**USS-Enterprise**, Northeastern University, Boston, MA',
'Jan 2023 - Apr 2023')
st.markdown('''
- Created a system service file to automatically start the web application when the VM starts.
- Utilized Packer to construct custom application AMIs and recorded application and metrics information in CloudWatch.
- Established the network architecture using VPC, subnets, Internet Gateway, NAT, Route Table, and security groups.
''')

txt('**Economics of Happiness**, Northeastern University, Boston, MA',
'Dec 2022')
st.markdown('''
- Determined the optimal border value for the classification of Happy Score (Ordinal Values) into "Happy" or "Sad", utilizing various mathematical measures, such as the mean, median, harmonic mean, and geometric mean 
- Examined the impact of utilizing different border values on the performance of models and the relative importance of predictors
''')

txt('**Wine Quality Prediction**, Northeastern University, Boston, MA',
'Oct 2022')
st.markdown('''
- Gained insights on why predicting a wine's quality in ordinal values are less accurate than classifying, employing Regression, Classification and AutoML with tuned hyperparameters
''')

txt('**Image Feature Comparison and Ranking, under Dr. Ajitha Shenoy**, Manipal Institute of Technology, India',
'Jan 2017- Jun 2017')
st.markdown('''
- Extracted features from query image stored in AWS s3. Compared and matched the SURF features and returned top 10 matching images with an accuracy of 95.7%. The developed model was immune to image rotation
- This tool is used by Manipal Institute of Technology for library catalogue management
''')

txt('**Do My Chores: Microsoft Code.Fun.Do Hackathon**, Manipal Institute of Technology, India',
'Aug 2016')
st.markdown('''
- Developed a windows application to help students do or get chores done with an associated payout, cutting down late submissions by 20%. Chores were displayed as markers on google maps
''')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/rishabhindoria/')
txt2('GitHub', 'https://github.com/rishabhindoria25/')
txt2('Kaggle', 'https://www.kaggle.com/rishabhindoria')
