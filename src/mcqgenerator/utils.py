import os 
import PyPDF2
import json
import traceback

def read_file(file):
  if file.name.endswith(".pdf"):
    try:
      pdf_reader = PyPDF2.PdfFileReader(file)
      text = ""
      for page in pdf_reader.pages:
        text = text + page.extract_text()
      return text
    except Exception as error:
      raise Exception("Error handling the pdf:",error)
  
  elif file.name.endswith(".txt"):
    return file.read().decode("utf-8")
  
  else:
    raise Exception("Unsupported file format. Only pdf and text file formats can be used")
  

def get_table_data(quiz_str):
  try:
    quiz_dict = json.loads(quiz_str)
    quiz_table_data =[]
    
    for key,value in quiz_dict.items():
      mcq = value["mcq"]
      options = "||".join(
        [
          f"{option}->{option_value}" for option,option_value in value["options"]
        ]
      )
      correct = value["correct"]
      quiz_table_data.append({"MCQ":mcq,"Choices":options,"Correct":correct})
    return quiz_table_data
  except Exception as error:
    raise Exception("Invalid quiz string is entered:",error)
  