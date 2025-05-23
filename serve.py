from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv

# Loading the environment variables
load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
model=ChatGroq(model="gemma2-9b-it",api_key=GROQ_API_KEY)

# 1. Create Prompt Template
system_template="Translate the following into {language}"
prompt_template=ChatPromptTemplate.from_messages([("system",system_template),("user","{text}")])

# Output parser
parser=StrOutputParser()

# Create chain
chain=prompt_template|model|parser

# App definition
app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces",
)

# Adding chain routes
add_routes(app,
           chain,
           path="/chain",
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)