import requests
import json
from PIL import Image, ImageDraw, ImageFont
import time
from dotenv import load_dotenv
import os

load_dotenv()

print()


# GENERATE APOLOGY

extra_flavor = ("Explain why you're still a good person.",
                "Remind readers to like and subscribe.")
users_sin = "I drove a hotdog through a clothing store, stole all the clothes, and then ranted about porn"
temp = .99
max_tokens = 4000
url = 'https://api.openai.com/v1/completions'
requestObj = {"model": "text-davinci-002",
              "prompt": "Write a long-winded and disingenuous apology addressed to the world. This is what they are guilty of: " + users_sin + " Go in to extreme detail about what happened. Mention how other people have done the same thing and gotten away with it.", "temperature": temp, "max_tokens": max_tokens}

apology = requests.post('https://api.openai.com/v1/completions', json=requestObj, headers={
                        'Authorization': 'Bearer ' + os.environ.get("api-key")}).json()


print(apology["choices"][0]["text"])

# print(type(apology))

# DRAW ON TO AN IMAGE

# img = Image.open("notes.jpg")
# drawImg = ImageDraw.Draw(img)
# myFont = ImageFont.truetype('SF.otf', 75)
# drawImg.text((100, 260), text=apology, font=myFont, fill=(14, 14, 14))
# img.show()
