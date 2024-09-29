import os 
import json
import traceback
import pandas as pd 
from dotenv import load_dotenv
import streamlit as st
from langchain.callbacks import get_openai_callback
from mcqgenerator.utils import read_file,get_table_data
from mcqgenerator.mcqgenerator import 