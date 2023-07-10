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

def get_hot_topics(limit=10):
    # try:
        data = []
        posts = reddit.subreddit('all').hot(limit=limit)
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
