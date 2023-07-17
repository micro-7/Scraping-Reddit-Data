import streamlit as st

# create a title for your app
st.title('Scraping Reddit Data')
st.subheader('Working of this App')


st.markdown("""
Certainly! Let's explore the theory behind scraping Reddit data using PRAW (Python Reddit API Wrapper), pandas, Plotly Express, and Streamlit for building a web app for visualization:

1. PRAW (Python Reddit API Wrapper):
   PRAW is a Python library that provides a convenient way to interact with the Reddit API. It simplifies tasks like authentication, making requests to Reddit's API endpoints, and retrieving data such as posts, comments, user information, and more. PRAW abstracts away the complexity of working directly with the API and allows you to focus on retrieving the data you need.

2. pandas:
   pandas is a powerful data manipulation and analysis library in Python. It introduces two primary data structures: Series and DataFrame. A Series is a one-dimensional labeled array that can hold different types of data, while a DataFrame is a two-dimensional labeled data structure similar to a table. pandas provides efficient data handling capabilities, allowing you to clean, transform, and analyze data easily.

3. Plotly Express:
   Plotly Express is a high-level data visualization library built on top of Plotly. It provides a concise and expressive syntax for creating interactive visualizations with minimal code. Plotly Express offers a wide range of chart types, including bar plots, line plots, scatter plots, and more. It allows customization of plots, adding labels, titles, legends, and other visual elements.

4. Streamlit:
   Streamlit is a Python library used for building interactive web applications for data exploration and visualization. It simplifies the process of creating and sharing data-centric apps by providing a simple and intuitive API. Streamlit enables real-time updates and facilitates interactive data exploration within the web app. It eliminates the need for writing HTML, CSS, or JavaScript code and allows users to interact with the app through their web browser.

Now, let's understand the steps involved in scraping Reddit data and building a web app for visualization:

- Steps 1 to 4: Installation and Importing:
  Install the necessary libraries and import them into your Python environment.

- Step 5: Authentication:
  Authenticate your application using your Reddit API credentials, including the client ID, client secret, and user agent. These credentials are obtained by creating a Reddit developer account and registering an application. The user agent is a unique identifier that helps Reddit identify your application.

- Step 6: Choosing a subreddit:
  Select the specific subreddit from which you want to scrape data. Subreddits are communities within Reddit focused on specific topics.

- Step 7: Scraping data:
  Use PRAW to interact with the Reddit API and retrieve data such as post titles, scores, comments, timestamps, etc. Iterate over the desired posts and extract the relevant information into a suitable data structure, such as a list or a pandas DataFrame.

- Step 8: Creating a pandas DataFrame:
  Convert the scraped data into a pandas DataFrame. A DataFrame provides a tabular structure to organize and manipulate the data efficiently. Each column of the DataFrame represents a specific attribute of the Reddit posts, such as titles, scores, etc.

- Step 9: Visualization using Plotly Express:
  Use Plotly Express to create interactive visualizations based on the pandas DataFrame. Select the appropriate chart type (e.g., bar plot, line plot, scatter plot) and customize the plot's appearance with labels, titles, legends, and other visual elements.

- Step 10: Building a Streamlit app:
  Use Streamlit to build a web application that incorporates the scraped data and the Plotly Express visualization. Define the structure of the web app, including the title, description, and layout. Utilize Streamlit's features to display the visualization within the app.

- Step 11: Running the Streamlit app:
  Execute the Streamlit app, which launches a web server locally. Users can access the app through their web browser, interact with the Reddit data and visualization, and explore the results dynamically.

By combining these libraries and following the outlined steps, you can scrape Reddit data, store it in a pandas DataFrame, create interactive visualizations using Plotly Express, and build a web app using Streamlit. The resulting web app allows users to explore and visualize the scraped Reddit data in an interactive and user-friendly manner.
""")



