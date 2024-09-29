from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
import os 
import json
import pandas as pd 
import traceback 
from dotenv import load_dotenv
import PyPDF2

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=key,model_name="gpt-3.5-turbo",temperature=0.7)