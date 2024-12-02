import json
import urllib2

url = 'https://api-inference.huggingface.co/models/{model_lab}/{model_name}/v1/chat/completions'
api_key = 'hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
basisprompt = u'''Generate a basic JSON containing only the following information on the person mentioned: dateofbirth, placeofbirth, dateofdeath, placeofdeath. Do not provide further information.'''

headers = {
    'Authorization': 'Bearer ' + api_key,
    'Content-Type': 'application/json',
}

data = {
  'messages': [ 
      {
         'role': 'user',
         'content': basisprompt + value
      }
  ],
  'max_tokens': 2048,
  'stream': False,
  'temperature': 0,
}

data_string = json.dumps(data)
data_bytes = data_string.encode('utf-8')

req = urllib2.Request(url, data=data_bytes, headers=headers)

response = urllib2.urlopen(req)
response_bytes = response.read()
response_json = json.loads(response_bytes.decode('utf-8'))
content = response_json["choices"][0]["message"]["content"] 
content = content.replace("<|end_of_turn|>", "") 
return content
