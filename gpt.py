import os

import openai

openai.api_type = "azure"

openai.api_version = "2023-03-15-preview"

openai.api_base = os.getenv ("OPENAI_API_BASE") # 你的Azure OpenAI资源的端点值。

openai.api_key = os.getenv ("OPENAI_API_KEY")

conversation= [

  {"role": "system", "content": "You are a helpful assistant."}

]

while(True):

  user_input = input ()

  conversation.append ({"role": "user", "content": user_input})

  response = openai.ChatCompletion.create (

    engine="gpt-3.5-turbo", # 你部署ChatGPT或GPT-4模型时选择的部署名称。

    messages = conversation

  )

  conversation.append ({"role": "assistant", "content": response ['choices'] ['message'] ['content']})

  print ("\n" + response ['choices'] ['message'] ['content'] + "\n")

