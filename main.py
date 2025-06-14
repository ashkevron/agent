import sys
import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )
    
    if verbose:
        print("User prompt:", user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    function_responses = []
    if response.function_calls:
        for function_call_part in response.function_calls:
            result = call_function(function_call_part, verbose)
            if not result.parts[0].function_response.response or not result.parts:
                raise Exception("call_function did not return a valid result")
            if verbose:
                print(f"-> {result.parts[0].function_response.response}")
            function_responses.append(result.parts[0])
    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    
    else:
        print("Response:")
        print(response.text)

if __name__ == "__main__":
    main()
