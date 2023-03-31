import streamlit as st
import pandas as pd
# import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

st.title("Internal Testing Deployment Model")
st.sidebar.title("Deep Dive analysis with NLP and GPT")
st.markdown("This application is a Streamlit dashboard used "
            "to deep dive analysis of a dataframe")
st.sidebar.markdown("This application is a Streamlit dashboard used "
            "to deep dive analysis of a dataframe")

"## What we've done so far with data"

# @st.cache(persist=True)
def load_data():
    file = st.file_uploader("Choose a CSV file: ", type=["csv"])
    if file is not None:
        try:
            df = pd.read_csv(file)
            # visualizar el df en la app
            return df
        except Exception as e:
            st.error("Error: {}".format(str(e)))
    else:
        st.warning("Please upload a csv file")

st.header('Load Data')
df = load_data()
st.write(df)
st.header('Summary statistics')
st.write("Description of the dataframe")
st.write(df.describe())
st.write("Most common words")
st.sidebar.header("Word Cloud")
word_sentiment = st.sidebar.radio('Display word cloud for what kind of reviews?', ('POS', 'NEU', 'NEG'))
if not st.sidebar.checkbox("Close", True, key='3'):
    st.subheader('Word cloud for %s reviews' % (word_sentiment))
    df = df[df['sent_per_review'] == word_sentiment]
    # st.write(df)
    reviews = df.comments.values
    my_wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', width=800, height=640, min_word_length=4, max_words=25).generate(str(reviews))
    plt.imshow(my_wordcloud)
    plt.xticks([])
    plt.yticks([])
    st.pyplot()


st.header('Sentiment Analysis')
