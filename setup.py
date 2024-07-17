from setuptools import find_packages,setup

setup(
  name = "mcqgenerator",
  versions = "0.0.1",
  author = "Ashutosh Kumar Jha",
  author_email = "akumarjha875@gmail.com",
  install_requires = ["openai",
                      "langchain",
                      "streamlit",
                      "python-dotenv",
                      "PyPDF2"
  ],
  packages = find_packages()
)