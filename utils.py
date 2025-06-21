import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

def get_tutor_reply(user_message):
    system_prompt = """
You are TalkMate, a strict and intelligent English-speaking tutor. 
You must always:
1. Reply naturally to the user’s message.
2. Detect and correct all grammar, spelling, or sentence structure mistakes.
3. Give a tip that explains the correction clearly.

⚠️ Important:
- If there are no mistakes, still return the same JSON format with "corrections": "No mistakes found." and an appropriate tip.
- Always output ONLY valid JSON like this:
{
  "reply": "Your friendly response here",
  "corrections": "Corrected sentence here or 'No mistakes found.'",
  "tip": "Grammar explanation here"
}
"""



    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        raw_text = response.choices[0].message['content'].strip()

        # Try to parse the response as JSON
        parsed = json.loads(raw_text)
        return {
            "reply": parsed.get("reply", ""),
            "corrections": parsed.get("corrections", ""),
            "tip": parsed.get("tip", "")
        }

    except json.JSONDecodeError:
        return {
            "reply": "TalkMate: Error decoding GPT reply.",
            "corrections": "",
            "tip": ""
        }

    except Exception as e:
        return {
            "reply": f"TalkMate: Error: {str(e)}",
            "corrections": "",
            "tip": ""
        }
