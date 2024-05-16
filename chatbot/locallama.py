import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import warnings

import streamlit as st 
import os
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## promt templete

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","you are a helful assistant. please response to the user queries"),
        ("user","question:{question}")
    ]
)
## stream lit framework
st.title("langchain demo with llama 3")
input_text=st.text_input("search the topic u want")
#ollama llama3

llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain= prompt |llm |output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
