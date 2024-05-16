import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import warnings

import streamlit as st
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## promt templete

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","you are a helful assistant. please response to the user queries"),
        ("user","question:{question}")
    ]
)

## stream lit framework
st.title("langchain demo with opnen ai")
input_text=st.text_input("search the topic u want")

llm=ChatOpenAI()
output_parser=StrOutputParser()
chain= prompt |llm |output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))