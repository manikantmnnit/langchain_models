from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model=ChatAnthropic(model='claude-3-5-sonnet-20241022',temperature=0.2,max_tokens_to_sample=)
result=model.invoke("capital of USA is ........")
print(result.content)
