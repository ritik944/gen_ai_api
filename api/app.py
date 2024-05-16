from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app= FastAPI(
    title="langchain server",
    version="1.0",
    description="a simple api server"
    
)
add_routes(
    app,
    ChatOpenAI(),
    path="/opneai"
)
model=ChatOpenAI()
llm=Ollama(model="llama3")

prompt1=ChatPromptTemplate.from_template("write me a essay about {topic} a 100 words")
prompt2=ChatPromptTemplate.from_template("write me a poem about {topic} for a 5 year old child  in 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)
add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
    








