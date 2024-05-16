from urllib import response
import requests
import streamlit as st

def get_openai_resopse(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})
    
    return response.json()['output']['content']

def get_ollama_resopse(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})
    
    return response.json()['output']

#streamlit framework
st.title('langchain demo')
input_text=st.text_input("write an essay on")
input_text1=st.text_input("write an poem on")

if input_text:
    st.write(get_openai_resopse(input_text))
if input_text1:
    st.write(get_ollama_resopse(input_text1))



