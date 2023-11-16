import streamlit
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kayle, Spinach and Rocket Smoothie')
streamlit.text('🐔 Half- boiled cage free egg 2')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list= my_fruit_list.set_index('Fruit')
# let us put list here so they can pick the fruits of their choice
#streamlit.multiselect("pick some fruits:", list(my_fruit_list.index))

# pick the list here so they can pick the fruit they want 
fruits_selected= streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show= my_fruit_list.loc[fruits_selected]
# display the table on the page 
streamlit.dataframe(fruits_to_show)
# create the repeatable code block(called function)
def get_fruityvice_data (this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
 
#new section to display
streamlit.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
     streamlit.error('Please select a fruit to get information.')
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)

except URLError as e:
      streamlit.error()

#streamlit.text(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

#streamlit.stop()

streamlit.header("the fruit load list contains:")
#snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()

# add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx= snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)

#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchall()
#streamlit.header("the fruit load list contains:")
#streamlit.dataframe(my_data_row)

#"jackfruit" , "papaya" , "gauva" ,"kiwi"
# allow the user to add a fruit 
def insert_row_snowflake(new_fruit):
     with my_cnx.cursor() as my_cur:
         my_cur.execute("INSERT INTO fruit_load_list (fruit_name) VALUES (%s)", (new_fruit,))
         return "Thanks for adding " + new_fruit 
         #my_cur.execute("insert into fruit_load_list(FRUIT_NAME) values ('"+ jackfruit + "')")
          #return 'Thanks for adding' + new_fruit
      
add_my_fruit= streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
   my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function=insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
#streamlit.write('Thanks for adding', add_my_fruit)
# this will not work correctly
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")


