import openai
import json
import time
import os

openai.api_key="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"

timestamp = time.strftime("%Y_%m_%d-%H_%M_%S", time.gmtime())
filename = timestamp + ".txt"

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("User: Welcome to OpenAI chat!\n")

discussions=[{"role": "system", 
              "content": "You are a helpful assistant."}]

while (True):
    p=input("Enter quit to quit, or enter your prompt: ")
    if (p=="quit"):
        break
    
    discussions.append({"role": "user", "content":p})
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=discussions
        )

    x=json.loads(str(completion))
    response = x["choices"][0]["message"]["content"]
    
    discussions.append({"role": "assistant", "content": response})
    
    with open(filename, 'a') as f:
        f.write("User: " + p + "\n")
        f.write("AI: " + response + "\n")
    
    print("\nAI says: ", response, "\n")

print("Have a nice day!")