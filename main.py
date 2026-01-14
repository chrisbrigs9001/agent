import os
from dotenv import load_dotenv
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    if api_key==None:
        raise RuntimeError ("no key")
    
    #establish parser for CLI args
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`
    
    from google import genai
    client = genai.Client(api_key=api_key)

    #create new list of types.Content, set the users prompt as the message
    from google.genai import types
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    #prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)
    
    if(response.usage_metadata==None):
        raise RuntimeError("Metadata is none, failed API request")
    
    if(args.verbose):
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print(response.text)

if __name__ == "__main__":
    main()
