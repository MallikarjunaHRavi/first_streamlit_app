import streamlit
streamlit.title('My Parents New Healthy Dinner')
 
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kayle, Spinach and Rocket Smoothie')
streamlit.text('🐔 Half- boiled cage free egg 2')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas 
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list= my_fruit_list.set_index('Fruit')

# let us put list here so they can pick the fruits of their choice
streamlit.multiselect('pick some fruits:', list(my_fruit_list.index))

# display the table on the page 
streamlit.dataframe(my_fruit_list)
