from dotenv import load_dotenv,find_dotenv
import os 
load_dotenv(find_dotenv())
key=os.environ.get("GEMINI_API_KEY")
print(key)
