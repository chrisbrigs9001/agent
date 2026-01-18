import os
import argparse

from call_function import available_functions
from prompts import system_prompt

from google import genai
from google.genai import types
from dotenv import load_dotenv

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
    

    client = genai.Client(api_key=api_key)

    #create new list of types.Content, set the users prompt as the message
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    #prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )
    
    if(not response.usage_metadata):
        raise RuntimeError("Metadata is none, failed API request")
    
    if(args.verbose):
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    
    if (not response.function_calls):
        print("Response:")
        print(response.text)
        return
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
    

if __name__ == "__main__":
    main()
