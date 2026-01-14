import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    if api_key==None:
        raise RuntimeError ("no key")
    
    from google import genai
    client = genai.Client(api_key=api_key)

    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    output = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    
    if(output.usage_metadata==None):
        raise RuntimeError("Metadata is none, failed API request")
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {output.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {output.usage_metadata.candidates_token_count}")
    
    print(output.text)

if __name__ == "__main__":
    main()
