import streamlit as st
from PIL import Image
from streamlit_timeline import timeline
import pandas as pd
# Constants
PROFILE_PIC_PATH = Image.open('dp.png')
RESUME_FILE = "RishabhIndoria_Resume.pdf"
EMAIL = "indoria.r@northeastern.edu"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/rishabhindoria/",
    "GitHub": "https://github.com/rishabhindoria25"
}

# Functions
@st.cache(allow_output_mutation=True)
def load_image(image_path):
    return Image.open(image_path)

@st.cache(allow_output_mutation=True)
def read_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()

def display_header():
    profile_pic = PROFILE_PIC_PATH
    st.image(profile_pic, width=150)
    st.title("Rishabh Indoria")
    st.download_button(
        label="Download Resume",
        data=read_file(RESUME_FILE),
        file_name=RESUME_FILE,
        mime="application/pdf",
    )

def create_navbar():
    # HTML for the navbar
    navbar_html = """
    <style>
    #navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background-color: #4CAF50;
        color: red;
        text-align: center;
        z-index: 999;
    }
    #navbar a {
        padding: 14px 20px;
        text-decoration: none;
        color: blue;
    }
    </style>
    <div id="navbar">
        <a href="#home">Home</a>
        <a href="#career-snapshot">Career Snapshot</a>
        <a href="#education">Education</a>
        <a href="#skills">Skills</a>
        <a href="#work-experience">Work Experience</a>
        <a href="#projects">Projects</a>
    </div>
    """
    st.markdown(navbar_html, unsafe_allow_html=True)

def display_social_media_links():
    cols = st.columns(len(SOCIAL_MEDIA) + 1)
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        with cols[index]:
            st.markdown(f"[{platform}]({link})")
    with cols[-1]:
        st.markdown(f"[Email](mailto:{EMAIL})")

def display_career_snapshot():
    st.subheader('Career Snapshot')
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=400)

def display_education():
    st.subheader('Education')
    st.markdown("""
    ### Masters of Science (Information Systems), Northeastern University, Boston, Massachusetts (2022-2024)
    - GPA: 3.75
    ### Bachelors of Technology (Information Technology), Manipal Institute of Technology, Manipal, India (2013-2017)
    """)

def display_skills():
    st.subheader('Skills')
    skills_categories = {
        "Programming and Development": ["Python", "Java", "SQL", "Spark", "Kafka", "Linux", "Numpy", "Pandas", "MATLAB"],
        "Machine Learning": ["Scikit-Learn", "Multivariate Statistics", "Supervised/Unsupervised Learning", "Bayesian Models"],
        "Deep Learning and AI": ["TensorFlow", "Keras", "PyTorch", "NLP", "CNN", "GPT-3"],
        "Web Development": ["Flask", "Streamlit", "FastAPI", "Node.js", "React.js", "Nginx", "Gunicorn"],
        "Cloud and Data Technologies": ["AWS", "GCP", "Azure", "Snowflake", "Hadoop", "Databricks"],
        "Data Visualization and Analysis": ["PowerBI", "Tableau", "ChartJS", "Grafana Labs", "MS Excel"]
    }
    
    # Transforming the dictionary into a DataFrame
    data = [{"Category": category, "Skills": ", ".join(skills)} for category, skills in skills_categories.items()]
    df = pd.DataFrame(data)

    # Displaying the DataFrame as a table
    st.table(df)

def display_work_experience():
    st.subheader('Work Experience')

    # Experience 1 - Lead Data Scientist at Urja.io
    with st.expander("URJA.IO | Lead Data Scientist (February 2021 - August 2022)"):
        st.markdown("""
        - Spearheaded development team in creating an end-to-end analytical dashboard tool, resulting in a 25% increase in user retention.
        - Reduced costs by 23% with a 94% accurate machinery-failure prediction system using Facebook Prophet for forecasting.
        - Streamlined stakeholder communication by 10 hours weekly through efficient Tableau reporting of A/B test progress.
        """)

    # Experience 2 - Data Scientist at Societe Generale Global Solution Centre
    with st.expander("SOCIETE GENERALE GLOBAL SOLUTION CENTRE | Data Scientist (July 2017 - March 2020)"):
        st.markdown("""
        - Enhanced deployment speed by 30% with Infrastructure as Code (IaC) through Terraform and GitHub CI/CD optimizations.
        - Increased fraud detection in investment banking by 17% using XGBoost models for identifying irregular transaction volumes.
        - Boosted risk management efficiency by 21% using Isolation Forest to spot high-value transactions exceeding forecasted pricing.
        - Employed NER and POS tagging techniques to redact financial transcripts, achieving a low error rate of 3.5%.
        """)


def display_summary():
    st.subheader('Summary')
    st.info('''
    **HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?**
    I am a highly accomplished data scientist with a strong focus on achieving measurable results. 
    I possess extensive experience working within cross-functional teams to achieve organizational objectives. 
    Being highly motivated to innovate existing business processes, I achieve optimal results in an efficient and 
    cost-effective manner utilizing my in-depth domain expertise. I have consistently demonstrated exceptional 
    diligence and commitment to excellence in both my coursework and professional work. I am eager to continue 
    this level of performance in future projects, utilizing diverse models, frameworks, and data.
    ''')

def display_projects():
    st.subheader('Projects')

    # Project 1 - Imbalanced Meteorological Data Analysis for Rainfall Prediction
    with st.expander("Imbalanced Meteorological Data Analysis for Rainfall Prediction - December 2023"):
        st.markdown("""
        - Enhanced prediction accuracy in an imbalanced dataset using SMOTE, class weight adjustments, and optimizer tuning.
        - Developed and trained ConvLSTM Model for Rainfall Forecasting, achieving 77% Class-1 Accuracy.
        [Project Link](https://github.com/rishabhindoria25/Imbalanced_Meteorological_Data_Analysis)
        """)

    # Project 2 - Biomedical Text Tagging Using BioBert
    with st.expander("Biomedical Text Tagging Using BioBert - December 2023"):
        st.markdown("""
        - Automated the use case of NER by tagging genes and proteins in biomedical text data using transformer-based BioBert model.
        [Project Link](https://github.com/rishabhindoria25/Biomedical_Text_Tagging)
        """)

    # Project 3 - Image Segmentation with Contextual Captioning
    with st.expander("Image Segmentation with Contextual Captioning - October 2023"):
        st.markdown("""
        - Implemented CNN with PyTorch and OpenCV for efficient image segmentation with F1-Score of 0.92.
        - Developed RNN in TensorFlow and NLTK for generating context-aware captions from segmented data with 70 Perplexity score.
        [Project Link](https://github.com/rishabhindoria25/Image_Segmentation)
        """)

    # Project 4 - Enhanced Audio Journaling with LLM
    with st.expander("Enhanced Audio Journaling with LLM - August 2023"):
        st.markdown("""
        - Implemented containerized audio processing algorithms, focusing on emotion detection for accurate sentiment analysis.
        - Leveraged Snowflake for efficient and scalable data storage.
        - Utilized GPT-3.5 prompt engineering for generating personalized feedback.
        [Project Link](https://github.com/rishabhindoria25/Enhanced_Audio_Journaling)
        """)

    # Project 5 - Finance Search Optimization
    with st.expander("Finance Search Optimization - May 2023"):
        st.markdown("""
        - Engineered a Q&A and text summarization platform, ingesting financial transcripts from Kafka pub-sub.
        - Used Langchain traditional filters, RAG, and Pinecone for vector similarity.
        - Dockerized Airflow data pipelines and Spark processing strategies.
        [Project Link](https://github.com/rishabhindoria25/Finance_Search_Optimization)
        """)

    # Project 6 - Sentiment Analysis: Deciphering Restaurant Reviews
    with st.expander("Sentiment Analysis: Deciphering Restaurant Reviews - April 2023"):
        st.markdown("""
        - Developed a dataset of restaurant reviews through prompt engineering using OpenAI's Davinci model.
        - Applied text preprocessing techniques followed by TF-IDF Vectorization and Naive Bayes algorithm for sentiment analysis.
        [Project Link](https://github.com/rishabhindoria25/Sentiment_Analysis_Restaurant_Reviews)
        """)

    # Project 7 - Glycoprotein Sequence Prediction
    with st.expander("Glycoprotein Sequence Prediction - March 2023"):
        st.markdown("""
        - Designed and implemented a system for predicting Glycoprotein sequences by combining PSI-BLAST search with a GAT model.
        [Project Link](https://github.com/rishabhindoria25/Glycoprotein_Sequence_Prediction)
        """)

    # Project 8 - H&M Product Recommendation System
    with st.expander("H&M Product Recommendation System - November 2023"):
        st.markdown("""
        - Conducted customer segmentation analysis using clustering techniques on customer embeddings.
        - Built product recommendations using item-item embeddings with sentence transformer & TF-ID -IDF vectorization.
        - Improved recommendation results by incorporating pre-trained Glove embeddings and clustering pipelines.
        [Project Link](https://github.com/rishabhindoria25/HM_Product_Recommendation_System)
        """)
    # Project 9 - AndroXmeda
    with st.expander("AndroXmeda - January 2023 to April 2023"):
        st.markdown("""
        - Modeled a REST API with NodeJS, Express, Postgres, Bcrypt, and Sequelize ORM for a full-stack ReactJS application.
        - Deployed the REST API on AWS CloudFormation using S3, RDS, and EC2.
        - Set up CI/CD pipelines with custom GitHub Actions for API delivery and AWS SES notifications.
        [Project Link](https://github.com/AndroXmeda)
        """)

    # Project 10 - Economics of Happiness
    with st.expander("Economics of Happiness - November 2022"):
        st.markdown("""
        - Utilized logistic regression and decision trees for exploratory analysis of the relationship between economic indicators and happiness.
        [Project Link](https://github.com/rishabhindoria25/Economics_of_Happiness)
        """)

    # Project 11 - QueryVision
    with st.expander("QueryVision, under Dr. Ajitha Shenoy - January 2017 to June 2017"):
        st.markdown("""
        - Developed a Python script for image similarity search using a pre-trained VGG16 model, achieving 95% top-10 matching accuracy.
        - Implemented feature extraction and cosine similarity calculation for a dataset of 10,000 images.
        [Project Link](https://github.com/rishabhindoria25/QueryVision)
        """)


# Page Configuration
st.set_page_config(
    page_title="Rishabh Indoria",
    page_icon=PROFILE_PIC_PATH,
    layout="wide",
    initial_sidebar_state="expanded"
)

if __name__ == "__main__":
    create_navbar()
    display_header()
    display_social_media_links()
    st.markdown("---")
    display_summary()
    display_career_snapshot()
    display_skills()
    display_education()
    display_work_experience()
    display_projects()

    # Footer
    st.markdown("---")
    st.markdown("© 2024 Rishabh Indoria")
