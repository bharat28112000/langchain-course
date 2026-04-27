# from dotenv import load_dotenv
# import os 
# from langchain_anthropic import ChatAnthropic

# load_dotenv()

# anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

# def main():
#     print(os.getenv("ANTHROPIC_API_KEY"))
#     print("Hello from langchain-course!")

from dotenv import load_dotenv, find_dotenv
import os

def main():
    dotenv_path = find_dotenv()
    print(f"Found .env at: {dotenv_path}")
    load_dotenv(dotenv_path)
    print(os.getenv("ANTHROPIC_API_KEY"))


if __name__ == "__main__":
    main()
