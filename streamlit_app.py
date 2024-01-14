import streamlit as st
from PIL import Image
from streamlit_timeline import timeline

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

def display_social_media_links():
    cols = st.columns(len(SOCIAL_MEDIA) + 1)
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        with cols[index]:
            st.markdown(f"[{platform}]({link})")
    with cols[-1]:
        st.markdown(f"[Email](mailto:{EMAIL})")

def display_navigation():
    with st.sidebar:
        st.markdown("## Navigation")
        nav_items = ["Career Snapshots", "Education", "Skills", "Work Experience", "Projects"]
        for item in nav_items:
            st.markdown(f"[{item}](#{item.lower().replace(' ', '-')})")

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
    
    for category, skills in skills_categories.items():
        st.subheader(category)
        st.markdown(", ".join(skills))

def display_work_experience():
    st.subheader('Work Experience')
    with st.expander("View Work Experience"):
        st.markdown("""
        ### Lead Data Scientist at Urja.io, India (2021-2022)
        - Spearheaded the development of an analytics dashboard, enhancing client engagement by 25%.
        - Implemented a machinery failure prediction model, reducing operational costs by 23%.
        ### Software Engineer at Société Générale, India (2017-2020)
        - Streamlined REST API development, resulting in 20% cost reduction and 30% faster module implementation.
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
    with st.expander("View Projects"):
        # Project 1 - Imbalanced Meteorological Data Analysis for Rainfall Prediction
        st.markdown("""
        ### [Imbalanced Meteorological Data Analysis for Rainfall Prediction](https://github.com/rishabhindoria25/Imbalanced_Meteorological_Data_Analysis) - December 2023
        - Enhanced prediction accuracy in an imbalanced dataset using SMOTE, class weight adjustments, and optimizer tuning.
        - Developed and trained ConvLSTM Model for Rainfall Forecasting, achieving 77% Class-1 Accuracy.
        """)

        # Project 2 - Biomedical Text Tagging Using BioBert
        st.markdown("""
        ### [Biomedical Text Tagging Using BioBert](https://github.com/rishabhindoria25/Biomedical_Text_Tagging) - December 2023
        - Automated the use case of NER by tagging genes and proteins in biomedical text data using transformer-based BioBert model.
        """)

        # Project 3 - Image Segmentation with Contextual Captioning
        st.markdown("""
        ### [Image Segmentation with Contextual Captioning](https://github.com/rishabhindoria25/Image_Segmentation) - October 2023
        - Implemented CNN with PyTorch and OpenCV for efficient image segmentation with F1-Score of 0.92.
        - Developed RNN in TensorFlow and NLTK for generating context-aware captions from segmented data with 70 Perplexity score.
        """)

        # Project 4 - Enhanced Audio Journaling with LLM
        st.markdown("""
        ### [Enhanced Audio Journaling with LLM](https://github.com/rishabhindoria25/Enhanced_Audio_Journaling) - August 2023
        - Implemented containerized audio processing algorithms, focusing on emotion detection for accurate sentiment analysis.
        - Leveraged Snowflake for efficient and scalable data storage.
        - Utilized GPT-3.5 prompt engineering for generating personalized feedback.
        """)

        # Project 5 - Finance Search Optimization
        st.markdown("""
        ### [Finance Search Optimization](https://github.com/rishabhindoria25/Finance_Search_Optimization) - May 2023
        - Engineered a Q&A and text summarization platform, ingesting financial transcripts from Kafka pub-sub.
        - Used Langchain traditional filters, RAG, and Pinecone for vector similarity.
        - Dockerized Airflow data pipelines and Spark processing strategies.
        """)

        # Project 6 - Sentiment Analysis: Deciphering Restaurant Reviews
        st.markdown("""
        ### [Sentiment Analysis: Deciphering Restaurant Reviews](https://github.com/rishabhindoria25/Sentiment_Analysis_Restaurant_Reviews) - April 2023
        - Developed a dataset of restaurant reviews through prompt engineering using OpenAI's Davinci model.
        - Applied text preprocessing techniques followed by TF-IDF Vectorization and Naive Bayes algorithm for sentiment analysis.
        """)

        # Project 7 - Glycoprotein Sequence Prediction
        st.markdown("""
        ### [Glycoprotein Sequence Prediction](https://github.com/rishabhindoria25/Glycoprotein_Sequence_Prediction) - March 2023
        - Designed and implemented a system for predicting Glycoprotein sequences by combining PSI-BLAST search with a GAT model.
        """)

        # Project 8 - H&M Product Recommendation System
        st.markdown("""
        ### [H&M Product Recommendation System](https://github.com/rishabhindoria25/HM_Product_Recommendation_System) - November 2023
        - Conducted customer segmentation analysis using clustering techniques on customer embeddings.
        - Built product recommendations using item-item embeddings with sentence transformer & TF-IDF vectorization.
        - Improved recommendation results by incorporating pre-trained Glove embeddings and clustering pipelines.
        """)

        # Project 9 - AndroXmeda
        st.markdown("""
        ### [AndroXmeda](https://github.com/AndroXmeda) - January 2023 to April 2023
        - Modeled a REST API with NodeJS, Express, Postgres, Bcrypt, and Sequelize ORM for a full-stack ReactJS application.
        - Deployed the REST API on AWS CloudFormation using S3, RDS, and EC2.
        - Set up CI/CD pipelines with custom GitHub Actions for API delivery and AWS SES notifications.
        """)

        # Project 10 - Economics of Happiness
        st.markdown("""
        ### [Economics of Happiness](https://github.com/rishabhindoria25/Economics_of_Happiness) - November 2022
        - Utilized logistic regression and decision trees for exploratory analysis of the relationship between economic indicators and happiness.
        """)

        # Project 11 - QueryVision
        st.markdown("""
        ### [QueryVision](https://github.com/rishabhindoria25/QueryVision), under Dr. Ajitha Shenoy - January 2017 to June 2017
        - Developed a Python script for image similarity search using a pre-trained VGG16 model, achieving 95% top-10 matching accuracy.
        - Implemented feature extraction and cosine similarity calculation for a dataset of 10,000 images.
        """)


# Page Configuration
st.set_page_config(
    page_title="Rishabh Indoria",
    page_icon=PROFILE_PIC_PATH,
    layout="wide",
    initial_sidebar_state="expanded"
)

if __name__ == "__main__":
    display_header()
    display_social_media_links()
    st.markdown("---")
    display_navigation()
    display_summary()
    display_career_snapshot()
    display_skills()
    display_education()
    display_work_experience()
    display_projects()

    # Footer
    st.markdown("---")
    st.markdown("© 2024 Rishabh Indoria")
