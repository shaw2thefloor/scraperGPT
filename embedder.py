from openai import OpenAI
import os
import requests

key = os.getenv("GPT_KEY")
client = OpenAI(api_key=key)

#models = requests.get("https://api.openai.com/v1/engines", headers={"Authorization": "Bearer " + key}).json()
#print(models)

with open("embeddings.txt", "w+") as emb:
    print(client.embeddings.create(input=["france", "germany", "frances", "grapefruit", "banana"], model="text-embedding-ada-002"), file=emb)
    print("\n---\n---\n---\n---\n", file=emb)


'''
x = {'object': 'list', 'data': [
    {'object': 'engine', 'id': 'whisper-1', 'ready': True, 'owner': 'openai-internal', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'tts-1', 'ready': True, 'owner': 'openai-internal', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'dall-e-2', 'ready': True, 'owner': 'system', 'permissions': None, 'created': None},
    {'object': 'engine', 'id': 'tts-1-hd-1106', 'ready': True, 'owner': 'system', 'permissions': None, 'created': None},
    {'object': 'engine', 'id': 'tts-1-hd', 'ready': True, 'owner': 'system', 'permissions': None, 'created': None},
    {'object': 'engine', 'id': 'gpt-3.5-turbo-1106', 'ready': True, 'owner': 'system', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'gpt-4-0125-preview', 'ready': True, 'owner': 'system', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'gpt-4-turbo-preview', 'ready': True, 'owner': 'system', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'text-embedding-3-small', 'ready': True, 'owner': 'system', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'text-embedding-3-large', 'ready': True, 'owner': 'system', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'gpt-3.5-turbo-16k', 'ready': True, 'owner': 'openai-internal', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'gpt-4-1106-preview', 'ready': True, 'owner': 'system', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'gpt-4-turbo-2024-04-09', 'ready': True, 'owner': 'system', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'babbage-002', 'ready': True, 'owner': 'system', 'permissions': None, 'created': None},
    {'object': 'engine', 'id': 'gpt-4o-2024-05-13', 'ready': True, 'owner': 'system', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'gpt-4-turbo', 'ready': True, 'owner': 'system', 'permissions': None, 'created': None},
    {'object': 'engine', 'id': 'gpt-4', 'ready': True, 'owner': 'openai', 'permissions': None, 'created': None},
    {'object': 'engine', 'id': 'gpt-4-0613', 'ready': True, 'owner': 'openai', 'permissions': None, 'created': None},
    {'object': 'engine', 'id': 'dall-e-3', 'ready': True, 'owner': 'system', 'permissions': None, 'created': None},
    {'object': 'engine', 'id': 'gpt-3.5-turbo-0125', 'ready': True, 'owner': 'system', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'tts-1-1106', 'ready': True, 'owner': 'system', 'permissions': None, 'created': None},
    {'object': 'engine', 'id': 'gpt-3.5-turbo', 'ready': True, 'owner': 'openai', 'permissions': None, 'created': None},
    {'object': 'engine', 'id': 'gpt-3.5-turbo-instruct', 'ready': True, 'owner': 'system', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'gpt-3.5-turbo-instruct-0914', 'ready': True, 'owner': 'system', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'text-embedding-ada-002', 'ready': True, 'owner': 'openai-internal', 'permissions': None,
     'created': None},
    {'object': 'engine', 'id': 'davinci-002', 'ready': True, 'owner': 'system', 'permissions': None, 'created': None},
    {'object': 'engine', 'id': 'gpt-4o', 'ready': True, 'owner': 'system', 'permissions': None, 'created': None}]}
'''