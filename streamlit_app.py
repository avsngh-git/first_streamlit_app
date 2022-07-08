import streamlit
import pandas
streamlit.title('hello this is my first app')
streamlit.header('Breakfast Menu')
streamlit.text('Oatmeal')
streamlit.text('Banana smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
