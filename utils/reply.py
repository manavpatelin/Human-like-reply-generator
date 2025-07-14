from openai import OpenAI
import os
from dotenv import load_dotenv
from utils.db import client

load_dotenv()
client=OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def generate_reply(platform,post_text):
    
    # tone generator
    tone_promt = f"What is the tune of this post? {post_text}"
    tone_response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [{'role':'user','content':tone_promt}],
        temperature = 0.5
    )
    tone = tone_response.choices[0].message.content.strip()

    #intenet generator
    intent_promt = f"What is the intent of this post? {post_text}"
    intent_response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [{'role':'user','content':intent_promt}],
        temperature = 0.5
    )
    intent = intent_response.choices[0].message.content.strip()

    #reply generator
    reply_promt = f"Reply to this post on {platform}. Tone: {tone}. Intent: {intent}." f"Make it human-like, platform-friendly, and avoid generic AI patterns.\n\nPost: \"{post_text}\"\n\nReply:"
    reply_response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [{'role':'user','content':reply_promt}],
        temperature = 0.5
    )
    reply = reply_response.choices[0].message.content.strip()
    return reply


