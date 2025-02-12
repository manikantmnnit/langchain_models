from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')
result=model.invoke(['What is capital of USA?','What is capital of India?'])  # provoke is designed for single query interactions
results=model.batch(['What is capital of USA?','What is capital of India?'])
print(result)  # answer the last question

for result in results:
    print(result.content)