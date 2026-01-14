import os
from dotenv import load_dotenv

load_dotenv("sus.env")
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    if api_key==None:
        raise RuntimeError ("no key")
    
    from google import genai
    client = genai.Client(api_key=api_key)

    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    output = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    print(output.text)

if __name__ == "__main__":
    main()
