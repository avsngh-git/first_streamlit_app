import streamlit
import pandas
streamlit.title("☕☕Daddy's Breakfast Diner🍞🥐")
streamlit.header('Breakfast Menu')
streamlit.text('Oatmeal')
streamlit.text('Banana smoothie')


# Read CSV from S3 bucket and display the dataframe on the app
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.header('🍋🍇List of Fruits Available🍉🥭')

# Allow customers to pick a list of fruits 
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index))

# Display the dataframe
streamlit.dataframe(my_fruit_list)
