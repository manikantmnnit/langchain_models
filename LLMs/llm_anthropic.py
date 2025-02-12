from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

# Load API Key from .env file
load_dotenv()
# anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

# Initialize the Anthropic model
llm = ChatAnthropic(model_name="claude-3-5-sonnet-20241022", temperature=0.7)

# Define translation function
def translate_text(text, target_language):
    prompt = f"Translate the following text into {target_language}:\n\n{text}"
    result = llm.invoke(prompt)
    return result.content  # Clean up the response

# Get user input
text = input("Enter the text: ")
target_language = input("Enter the target language: ")

# Call translation function
translated_text = translate_text(text, target_language)

# Print the translated text
print(f"\nTranslated Text ({target_language}): {translated_text}")
