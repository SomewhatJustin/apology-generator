import requests
import json

url = 'https://api.openai.com/v1/completions'
auth = ('Authorization', 'Bearer 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')
requestObj = {"model": "text-davinci-002",
              "prompt": "Say this is a test", "temperature": 0, "max_tokens": 6}

apology = requests.post('https://api.openai.com/v1/completions', json=requestObj, headers={
                        'Authorization': 'Bearer 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'})

apology_json = apology.json()
#new_apology = json.loads(apology_json)

print(apology_json["choices"][0]["text"])

# print(json.loads(apology.json()))
