
import time
import yaml

import openai

with open("config.yaml", 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

openai.api_base = config['api_base']
openai.api_key = config['api_key']

default_parameters = {
    "model": "gpt-3.5-turbo-0613",
    "temperature": 0.5,
    "top_p": 1,
    # "max_tokens": 100,
}

def get_response(messages, parameters=None):
    if parameters is None:
        parameters = default_parameters
    parameters["messages"] = messages
    
    while True:
        try:
            completion = openai.ChatCompletion.create(**parameters)
            total_tokens = completion.usage['total_tokens']
        except Exception as e:
            print(e)
            time.sleep(3)
            continue
        break
    return completion.choices[0].message.content.strip(), total_tokens