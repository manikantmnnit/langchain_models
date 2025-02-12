from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
from langchain.schema import HumanMessage # 

load_dotenv()



# Default temperature 0.7

# Define a prompt
prompt = "Write the definition of  Machine learning in simple way."

# Low temperature (0.2) 
low_temp_model = ChatOpenAI(
    model_name="gpt-4", 
    temperature=0.2, # low randomness
    max_completion_tokens=10 # short response 
    top_p=0.9, # diverse sampling
    )
low_temp_response = low_temp_model.invoke(prompt)
print("Low Temperature Response (0.2):")
print(low_temp_response.content)
print("\n")

# Medium temperature (0.7)
medium_temp_model = ChatOpenAI(model_name="gpt-4",
                                temperature=0.7,
                                max_completion_tokens=20, # moderate response length
                                top_p=0.95 # diverse sampling 
                                )
medium_temp_response = medium_temp_model.invoke(prompt)
print("Medium Temperature Response (0.7):")
print(medium_temp_response.content)
print("\n")

# High temperature (1.5)
high_temp_model = ChatOpenAI(model_name="gpt-4", 
                             temperature=1.5, # high randomness 
                             max_completion_tokens=40, #  longer response
                             top_p=0.8 # more focused sampling 
                             )
high_temp_response = high_temp_model.invoke(prompt)
print("High Temperature Response (1.5):")
print(high_temp_response.content)