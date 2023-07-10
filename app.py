import streamlit as st 
# from mining import get_hot_topics, get_post_comments_by_id, get_post_comments_by_url, get_subreddit


import praw
import pandas as pd
from praw.models import MoreComments

reddit = praw.Reddit(
    client_id='6fya8IjqaVcDMGcBnYBJsg', 
    client_secret='45M4BcpP6r7oV2_9GQw4-i5l_GlQ3g', 
    user_agent='Scaping App')



def get_subreddit(keyword = 'Valorant', limit = 10):
    # get 10 hot posts from the MachineLearning subreddit
    try:
        data = []
        posts = reddit.subreddit(keyword).hot(limit=None)
        for post in posts:
            data.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
        return pd.DataFrame(data,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
    except Exception as e:
        print(f"Could not fetch {keyword}", e)
        return e

def get_hot_topics():
    # try:
        data = []
        posts = reddit.subreddit('all').hot(limit=None)
        for post in posts:
            data.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
        return pd.DataFrame(data,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
    # except Exception as e:
    #     print(f"Could not fetch data", e)

def get_post_comments_by_id(id='14oqeq7'):
    try:
        submission = reddit.submission(id=id)
        data = []
        for comment in submission.comments:
            if isinstance(comment, MoreComments):
               continue
            data.append({
                'comment': comment.body,
                'id': comment.id,
                'author_is_blocked':comment.author_is_blocked,
                'comment_type': comment.comment_type,
                'banned_by':comment.banned_by,
                'total_awards_received': comment.total_awards_received,
                'subreddit':comment.subreddit,
                'likes':comment.likes,
                'author':comment.author,
                'created_utc':comment.created_utc,
                'score': comment.score,
                'ups': comment.ups,
                'downs': comment.downs,
            })
        
        return pd.DataFrame(data)
    except Exception as e:
        print(e)

def get_post_comments_by_url(url='https://www.reddit.com/r/Cosmere/comments/14ni8vl/secret_project_3_full_book_discussion/'):
    try:
        submission = reddit.submission(url=url)
        data = []
        for comment in submission.comments:
            if isinstance(comment, MoreComments):
               continue
            data.append({
                'id': comment.id,
                'comment': comment.body,
                'author':comment.author,
                'score': comment.score,
                'author_is_blocked':comment.author_is_blocked,
                'banned_by':comment.banned_by,
                'total_awards_received': comment.total_awards_received,
                'subreddit':comment.subreddit,
                'likes':comment.likes,
                'created_utc':comment.created_utc,
                'comment_type': comment.comment_type,
                'ups': comment.ups,
                'downs': comment.downs,
            })
        
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
        return e


st.title("ENTER YOUR TOPIC")

#with st.form(key = "form1"):
my_form = st.form(key = "form1")
name = my_form.text_input(label = "Enter your topic here")
submit = my_form.form_submit_button(label = "Submit your topic")
result = None
savebtn = None
if submit and name:
    result = get_subreddit(name)
    if isinstance(result, pd.DataFrame):
        st.dataframe(result)
if isinstance(result, pd.DataFrame):
    with st.form(key='save'):
        name = st.text_input('file name')
        filetype = st.selectbox('filetype', ['csv', 'xlsx','json'])
        savebtn = st.form_submit_button('save')
if savebtn and name and filetype == 'csv':
    result.to_csv(f'{name}.{filetype}', index=False)
elif savebtn and name and filetype == 'xlsx':
    result.to_excel(f'{name}.{filetype}', index=False)

#st.title('Select what to scrap')
#cols=  ['Comments', 'Time of posting','Upvote', 'Shares']
#selected_cols= st.multiselect('Select your action', cols)
#st.write(f'You selected: {len(selected_cols)} actions')


# st.title("Choose URL or ID ")
# #Radio button to select URL or ID
# form_selection = st.radio("Choose your action:", ("URL", "ID"))
# #Now display the form according t
# if form_selection == "URL":
#     url = st.text_input("Enter URL")
# elif form_selection == "ID":
#     id = st.text_input("Enter ID")
# # Submit button
# if st.button("Submit"):
#     st.write("Form submitted!")

st.title("Choose URL or ID")
# Radio button to select URL or ID
form_selection = st.radio("Choose your action:", ("URL", "ID"))
#Now display the form according to the user's selection
if form_selection == "URL":
    url = st.text_input("Enter URL")
elif form_selection == "ID":
    id = st.text_input("Enter ID")
# Submit button
if st.button("Submit"):
    if form_selection == "URL":
        df = get_post_comments_by_url(url)
        st.write(df)
    elif form_selection == "ID":
        df = get_post_comments_by_id(id)
        st.write(df)


