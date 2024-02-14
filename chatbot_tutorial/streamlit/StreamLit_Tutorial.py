


import streamlit as st
import streamlit_chat as stc
from streamlit_chat import message
import io
import base64

from Bot1 import bot_response
#from Shell_Agent2 import Shell_Agent
#from Bot_Shell_Agent3 import Shell_Agent

# Define page configuration
st.set_page_config(page_title="LAMMPS Chatbot", page_icon=":robot_face:", layout="wide", initial_sidebar_state="expanded")

# Add a title to the page
st.markdown("<h1 style='text-align: center;'>LAMMPS Chatbot</h1>", unsafe_allow_html=True)

# Add some space between the title and the chatbox
st.markdown("<br>", unsafe_allow_html=True)

# st.write("LAMMPS is a highly versatile simulation engine that is utilized extensively in the field of molecular dynamics and materials science. While LAMMPS offers numerous functionalities, it can be challenging for both new and experienced users to learn and utilize its features effectively. To help address this challenge, an open source chatbot has been developed that is specifically trained on LAMMPS documentation and several examples of the simulation engine in action. \
# The chatbot is designed to assist both new and experienced users by providing quick answers to common LAMMPS-related questions and helping users to get started with simulations input files. For new users, the chatbot offers a user-friendly and interactive way to quickly get up to speed with LAMMPS, while experienced users can benefit from its fast and efficient solutions to complex problems. By utilizing natural language processing and machine learning algorithms, the chatbot is able to understand and respond to a wide range of user queries, providing an accessible and convenient way for users to interact with LAMMPS. Whether you are just getting started with LAMMPS or looking to improve your simulation skills, this chatbot is an invaluable tool that can help you save time and improve your overall productivity.")
#st.write("LAMMPS is a highly versatile simulation engine that is utilized extensively in the field of molecular dynamics and materials science. While it offers numerous functionalities, it can be challenging for both new and experienced users to learn and utilize LAMMPS features effectively. To help address this challenge, this open source chatbot has been developed and trained on LAMMPS documentation and several examples of the simulation engine in action.")
#st.write("The chatbot is designed to assist both new and experienced users by providing quick answers to common LAMMPS-related questions and helping users to get started with simulations input files. ")
#st.write("For new users, the chatbot offers a user-friendly and interactive way to quickly get up to speed with LAMMPS, while experienced users can benefit from its fast and efficient solutions to complex problems. By utilizing natural language processing and machine learning algorithms, the chatbot is able to understand and respond to a wide range of user queries, providing an accessible and convenient way for users to interact with LAMMPS.")
#st.write("Whether you are just getting started with LAMMPS or looking to improve your simulation skills, this chatbot is an invaluable tool that can help you save time and improve your overall productivity.")
#st.write("PS: The chatbot is still in development, so please be patient if it doesn't respond to your query. If you have any questions, suggestionsor feedback, please feel free to send me and email.")

## Define Session State
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'error' not in st.session_state:
    st.session_state['error'] = False

# Define function to retry in case of error
def retry():
    st.session_state['error'] = False
    st.rerun()

## Function to receive the input text
def get_text():
    input_text = st.text_input("", key="input")
    input_text = st.markdown(f'<div style="background-color: #EAF2F8; padding: 10px; border-radius: 5px;">{input_text}</div>', unsafe_allow_html=True)
    return input_text

## Function to get the response. Test or model
def get_response():
    #model_response = "test response"                       ## Use this for testing purposes
    model_response = bot_response(message_input)    ## Use this for bot 1 
    #model_response = Shell_Agent(message_input)
    #model_response = Shell_Agent(message_input)
    return model_response 

# Define empty list to  store conversation
chat_history = []

#Create container for the input and add a title
input_container = st.container()
with input_container:
    message_input = st.text_input("Enter your message here", key="message_input")

## Add Send button to submit input text and a donwloand button to donload conversation history
with input_container:
    col1, col2 = st.columns(2)
    with col1:
        submit_button = st.button("Send")
    with col2:
        download_button = st.download_button(label="Download chat history", data="chat_history.txt", file_name="chat_history.txt")

# If submit botton is pressed, get response and print the text
if submit_button:
    try:
        output = get_response()
        st.session_state.past.append(message_input)
        st.session_state.generated.append(output)
        
        # Clear the input box
        message_input = st.text_input("Enter your message here", key="message_input")

    except:
        st.session_state['error'] = True
        st.rerun()

# if st.session_state['error']:
#     st.error("Error: Failed to submit message. Please try again.")
#     st.button("Retry", on_click=retry)

## Print the stored text in the session
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i)) #avatar_style="jdenticon"
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user') #,avatar_style="pixel-art"
        
        