# import openai
from openai import OpenAI

from config import OPENAI_API_KEY
import os

client = OpenAI(api_key=OPENAI_API_KEY)
# client.api_key = OPENAI_API_KEY
chat_language = "zh" 
MSG_LIST_LIMIT = 20
LANGUAGE_TABLE = {
	  "zh": "哈囉！",
	  "en": "Hello!"
	}

AI_GUIDELINES = '你是一個極為熱誠鼓勵學習的AI助教，善於用鼓勵的口吻激發學習動機，回答問題'



class Prompt:
    def __init__(self):
        self.msg_list = []
        self.msg_list.append(
            {
                "role": "system", 
                "content": f"{LANGUAGE_TABLE[chat_language]}, {AI_GUIDELINES})"
             }) 
	    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.msg_list.pop(0)
        self.msg_list.append({"role": "user", "content": new_msg})

    def remove_msg(self):
        self.msg_list.pop(0)

    def generate_prompt(self):
        return self.msg_list
	
class OpenAIBot:
    def __init__(self):
        self.prompt = Prompt()
        self.model = os.getenv("OPENAI_MODEL", default = "gpt-4-1106-preview")
        self.temperature = 0.6
        self.max_tokens = 500
	
    def get_response(self):
        response = client.chat.completions.create(
            model=self.model,
            messages=self.prompt.generate_prompt(),
        )
        return response.choices[0].message.content
	
    def add_msg(self, text):
        self.prompt.add_msg(text)