import requests
import json
from PIL import Image, ImageDraw, ImageFont

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
                        'Authorization': 'Bearer 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'}).json()


print(apology["choices"][0]["text"])

newApology = """ 
Dear World,

I would like to offer a sincere and heartfelt apology for my recent actions. I know that what I did was wrong, and I deeply regret the pain and inconvenience that I caused.

I was driving through town when I saw a hotdog stand. I was feeling hungry, so I decided to stop and get something to eat. But when I went to pay, I realized that I had left my wallet at home. I didn't have any money to pay for the hotdog, so I did the only thing I could think of - I drove my hotdog through the store and stole all the clothes.

I know that this was wrong, and I am truly sorry for my actions. I can understand why you are upset, and I fully accept responsibility for my actions. I promise to do better in the future.

Sincerely,

[Your Name]
"""

# DRAW ON TO AN IMAGE

img = Image.open("notes.jpg")
drawImg = ImageDraw.Draw(img)
myFont = ImageFont.truetype('SF.otf', 75)
drawImg.text((100, 260), text=newApology, font=myFont, fill=(14, 14, 14))
img.show()
