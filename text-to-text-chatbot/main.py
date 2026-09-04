import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def txt_2_txt_model(prompt):

    model = init_chat_model("google_genai:gemini-3-flash-preview")

    # response = model.invoke("What is Ai in brief?")

    # print(response.content[0]['text'])

    from langchain.messages import HumanMessage, SystemMessage


    messages = [
        SystemMessage(content="You are Helping Expert Agent who help the user to solve his query. Give response as better as you can and generate only which user want instead of giving long and unnessary response. And one more thing understand user context what he want and give answer as per queastion."),
        HumanMessage(prompt)
    ]

    for chunk in model.stream(messages):
        print(chunk.text, end="")


txt_2_txt_model("Explain Ai in two lines")