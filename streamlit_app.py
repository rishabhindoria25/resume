import streamlit as st
from PIL import Image
from streamlit_timeline import timeline
import pandas as pd
import time


# Constants
PROFILE_PIC_PATH = Image.open('dp.png')
RESUME_FILE = "RishabhIndoria_Resume.pdf"
EMAIL = "indoria.r@northeastern.edu"


# Functions
@st.cache(allow_output_mutation=True)
def load_image(image_path):
    return Image.open(image_path)


def read_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()

def display_header_and_education():
    col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 2, 1])

    with col2:
        profile_pic = PROFILE_PIC_PATH
        st.image(profile_pic, width=150, use_column_width='always')
        
    with col4:
        st.title("Rishabh Indoria")
        st.markdown("""
        <style>
        .education-info {
            font-size: 16px;
        }
        .institution {
            font-weight: bold;
        }
        .degree {
            font-style: italic;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="education-info">
            <ul>
                <li>
                    <span class="institution">Northeastern University, Boston, Massachusetts</span><br>
                    <span class="degree">Masters of Science (Information Systems)</span><br>
                    Graduate TA - INFO 7390 Advance Data Sciences<br>
                    <a href="https://learn.microsoft.com/en-us/users/rishabhindoria-5834/credentials/e9c3d93e5b13053f">Microsoft Certified: Azure Data Scientist Associate</a><br>
                    <a href="https://portal.bloombergforeducation.com/certificates/Ge3MctSLAcGvYc4aPnR7r92j">Bloomberg Market Concepts Certification</a><br>
                    <a href="https://www.youtube.com/watch?v=Cf98HE5PRPk">I did a cool presentation at AI Skunkworks!</a>
                </li>
                <li>
                    <span class="institution">Manipal Institute of Technology, Manipal, India</span><br>
                    <span class="degree">Bachelors of Technology (Information Technology)</span><br>
                    <a href="https://github.com/rishabhindoria25/QueryVision">Research Project under Dr. Ajitha Shenoy</a>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.download_button(
            label="Download Resume",
            data=read_file(RESUME_FILE),
            file_name=RESUME_FILE,
            mime="application/pdf",
        )

def display_social_media_links():
    st.subheader('Social Media')
    total_cols = len(SOCIAL_MEDIA) + 1
    cols = st.columns([1] * total_cols)
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        with cols[index + (total_cols - len(SOCIAL_MEDIA)) // 2]:  # Center alignment
            st.markdown(f"[{platform}]({link})")
    with cols[-1 + (total_cols - len(SOCIAL_MEDIA)) // 2]:  # Adjust for email link
        st.markdown(f"[Email](mailto:{EMAIL})")


def display_career_snapshot():
    st.subheader('Career Snapshot')
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=400)

def display_education():
    st.subheader('Education')

    st.markdown("""
    <style>
    .education-info {
        font-size: 16px;
    }
    .institution {
        font-weight: bold;
    }
    .degree {
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="education-info">
        <ul>
            <li>
                <span class="institution">Northeastern University, Boston, Massachusetts</span><br>
                <span class="degree">Masters of Science (Information Systems)</span><br>
                2022 - 2024<br>
                GPA: 3.75
            </li>
            <li>
                <span class="institution">Manipal Institute of Technology, Manipal, India</span><br>
                <span class="degree">Bachelors of Technology (Information Technology)</span><br>
                2013 - 2017
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


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

    # Displaying the DataFrame as a table without index and header
    html = df.to_html(index=False, header=False)
    st.write(html, unsafe_allow_html=True)

def display_work_experience():
    st.subheader('Work Experience')

    # Experience 1 - Lead Data Scientist at Urja.io
    with st.expander("URJA.IO"):
        st.markdown("""
        Lead Data Scientist (April 2020 - August 2022)
        """)
        st.markdown("""
        - Spearheaded development team in creating an end-to-end analytical dashboard tool, resulting in a 25% increase in user retention.
        - Reduced costs by 23% with a 94% accurate machinery-failure prediction system using Facebook Prophet for forecasting.
        - Streamlined stakeholder communication by 10 hours weekly through efficient Tableau reporting of A/B test progress.
        """)

    # Experience 2 - Data Scientist at Societe Generale Global Solution Centre
    with st.expander("SOCIETE GENERALE GLOBAL SOLUTION CENTRE"):
        st.markdown("""
        Data Scientist (July 2017 - March 2020)
        """)
        st.markdown("""
        - Enhanced deployment speed by 30% with Infrastructure as Code (IaC) through Terraform and GitHub CI/CD optimizations.
        - Increased fraud detection in investment banking by 17% using XGBoost models for identifying irregular transaction volumes.
        - Boosted risk management efficiency by 21% using Isolation Forest to spot high-value transactions exceeding forecasted pricing.
        - Employed NER and POS tagging techniques to redact financial transcripts, achieving a low error rate of 3.5%.
        """)


def display_summary():
    st.subheader('Summary')
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.markdown("""
        **HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?**
        """)
    st.markdown('</div>', unsafe_allow_html=True)
    st.info('''
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
    with st.expander("Imbalanced Meteorological Data Analysis for Rainfall Prediction"):
        st.markdown("""
        December 2023
        """)
        st.markdown("""
        - Enhanced prediction accuracy in an imbalanced dataset using SMOTE, class weight adjustments, and optimizer tuning.
        - Developed and trained ConvLSTM Model for Rainfall Forecasting, achieving 77% Class-1 Accuracy.
        [Project Link](https://github.com/NeuraNoir/Imbalanced-Meteorological-Data-Analysis-For-Rainfall-Prediction)
        """)

    # Project 2 - Biomedical Text Tagging Using BioBert
    with st.expander("Biomedical Text Tagging Using BioBert"):
        st.markdown("""
        December 2023
        """)
        st.markdown("""
        - Automated the use case of NER by tagging genes and proteins in biomedical text data using transformer-based BioBert model.
        [Project Link](https://github.com/rishabhindoria25/Biomedical_Text_Tagging)
        """)

    # Project 8 - H&M Product Recommendation System
    with st.expander("H&M Product Recommendation System"):
        st.markdown("""
        November 2023
        """)
        st.markdown("""
        - Conducted customer segmentation analysis using clustering techniques on customer embeddings.
        - Built product recommendations using item-item embeddings with sentence transformer & TF-ID -IDF vectorization.
        - Improved recommendation results by incorporating pre-trained Glove embeddings and clustering pipelines.
        [Project Link](https://github.com/rishabhindoria25/HM_Product_Recommendation_System)
        """)

    # Project 3 - Image Segmentation with Contextual Captioning
    with st.expander("Image Segmentation with Contextual Captioning"):
        st.markdown("""
        October 2023
        """)
        st.markdown("""
        - Implemented CNN with PyTorch and OpenCV for efficient image segmentation with F1-Score of 0.92.
        - Developed RNN in TensorFlow and NLTK for generating context-aware captions from segmented data with 70 Perplexity score.
        [Project Link](https://github.com/NeuraNoir/Image-segmentation-with-contextual-captioning)
        """)

    # Project 4 - Enhanced Audio Journaling with LLM
    with st.expander("Enhanced Audio Journaling with LLM"):
        st.markdown("""
        August 2023
        """)
        st.markdown("""
        - Implemented containerized audio processing algorithms, focusing on emotion detection for accurate sentiment analysis.
        - Leveraged Snowflake for efficient and scalable data storage.
        - Utilized GPT-3.5 prompt engineering for generating personalized feedback.
        [Project Link](https://github.com/ImagiGEN/AudioJournaling)
        """)

    # Project 5 - Finance Search Optimization
    with st.expander("Finance Search Optimization"):
        st.markdown("""
        May 2023
        """)
        st.markdown("""
        - Engineered a Q&A and text summarization platform, ingesting financial transcripts from Kafka pub-sub.
        - Used Langchain traditional filters, RAG, and Pinecone for vector similarity.
        - Dockerized Airflow data pipelines and Spark processing strategies.
        [Project Link](https://github.com/ImagiGEN/contextualQ-A)
        """)

    # Project 6 - Sentiment Analysis: Deciphering Restaurant Reviews
    with st.expander("Sentiment Analysis: Deciphering Restaurant Reviews"):
        st.markdown("""
        April 2023
        """)
        st.markdown("""
        - Developed a dataset of restaurant reviews through prompt engineering using OpenAI's Davinci model.
        - Applied text preprocessing techniques followed by TF-IDF Vectorization and Naive Bayes algorithm for sentiment analysis.
        [Project Link](https://github.com/rishabhindoria25/Sentiment_Analysis_Restaurant_Reviews)
        """)

    # Project 7 - Glycoprotein Sequence Prediction
    with st.expander("Glycoprotein Sequence Prediction"):
        st.markdown("""
        March 2023
        """)
        st.markdown("""
        - Designed and implemented a system for predicting Glycoprotein sequences by combining PSI-BLAST search with a GAT model.
        [Project Link](https://github.com/rishabhindoria25/Glycoprotein_Sequence_Prediction)
        """)
    
    # Project 9 - AndroXmeda
    with st.expander("AndroXmeda"):
        st.markdown("""
        March 2023
        """)
        st.markdown("""
        - Modeled a REST API with NodeJS, Express, Postgres, Bcrypt, and Sequelize ORM for a full-stack ReactJS application.
        - Deployed the REST API on AWS CloudFormation using S3, RDS, and EC2.
        - Set up CI/CD pipelines with custom GitHub Actions for API delivery and AWS SES notifications.
        [Project Link](https://github.com/AndroXmeda)
        """)

    # Project 10 - Economics of Happiness
    with st.expander("Economics of Happiness"):
        st.markdown("""
        November 2022
        """)
        st.markdown("""
        - Utilized logistic regression and decision trees for exploratory analysis of the relationship between economic indicators and happiness.
        [Project Link](https://github.com/rishabhindoria25/Economics_of_Happiness)
        """)

    # Project 11 - QueryVision
    with st.expander("QueryVision"):
        st.markdown("""
        <a name='ResearchProject'></a>
        June 2017
        """)
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

# Define social media links, copyright text, and styling with Streamlit's info blue hue
SOCIAL_MEDIA_FOOTER = {
    "LinkedIn": "https://linkedin.com/in/rishabhindoria/",
    "GitHub": "https://github.com/rishabhindoria25",
    "Email": "mailto:indoria.r@northeastern.edu"
}

FOOTER_STYLE = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #E8F4FF;  # Streamlit's info blue color
    color: #ffffff;  # White text color for better visibility
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
}
.footer a {
    color: inherit;
    padding: 0 10px;
    text-decoration: none;
}
</style>
"""

def display_footer():
    st.markdown(FOOTER_STYLE, unsafe_allow_html=True)
    footer_html = "<div class='footer' style='display: flex; justify-content: space-between; align-items: center;'>"
    footer_html += "<div>"
    for platform, link in SOCIAL_MEDIA_FOOTER.items():
        footer_html += f"<a href='{link}'>{platform}</a> "
    footer_html += "</div>"
    footer_html += "<div>© 2024 Rishabh Indoria</div>"
    footer_html += "</div>"
    st.markdown(footer_html, unsafe_allow_html=True)
    
if __name__ == "__main__":
    display_header_and_education()
    st.markdown("---")
    display_summary()
    st.markdown("---")
    display_career_snapshot()
    st.markdown("---")
    display_skills()
    st.markdown("---")
    display_work_experience()
    st.markdown("---")
    display_projects()
    display_footer()
