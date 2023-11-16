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
#streamlit.multiselect("pick some fruits:", list(my_fruit_list.index))

# pick the list here so they can pick the fruit they want 
fruits_selected= streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show= my_fruit_list.loc[fruits_selected]
# display the table on the page 
streamlit.dataframe(fruits_to_show)

#new section to display
streamlit.header('Fruityvice Fruit Advice!')

#importing the request from api 
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)

#streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("the fruit load list contains:")
streamlit.dataframe(my_data_row)

streamlit.write('Thanks for adding', add_my_fruit)

# this will not work correctly
my_cur.execute("insert into fruit_load_list values('from streamlit')")


