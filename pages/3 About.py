import streamlit as st

# create a title for your app
st.title('Scraping Reddit Data')
st.subheader('About this App')

st.markdown("""
This app performs scaping of the data from reddit.
The app likely utilizes web scraping techniques to navigate Reddit's pages, extract relevant information, and organize it in a structured format. It might employ API calls or use libraries like Beautiful Soup or PRAW (Python Reddit API Wrapper) to interact with Reddit's API and retrieve data such as post titles, content, author information, and comments.

One of the key benefits of your app is the ability to gather large amounts of data quickly and easily. This can be particularly useful for researchers, data analysts, journalists, or anyone interested in studying the Reddit community. The app allows you to aggregate information from multiple threads, subreddits, or even across the entire Reddit platform, providing a comprehensive view of discussions and opinions on various topics.

The extracted data can be further processed and analyzed to identify patterns, trends, or sentiments within the Reddit community. This analysis can help in generating insights, developing strategies, or even predicting user behavior. By understanding the pulse of Reddit, you can make informed decisions, create engaging content, or tailor your marketing efforts to reach a wider audience.
""")
            
st.image("reddit app logo.png")