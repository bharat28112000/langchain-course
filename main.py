from dotenv import load_dotenv, find_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from langchain_anthropic import ChatAnthropic
from typing import List
from pydantic import BaseModel, Field
from tavily import TavilyClient
import os

load_dotenv(find_dotenv())
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

class Source(BaseModel):
    """Schema for the source used by the agent."""
    url: str = Field(description="The url of the source")

class AgentResponse(BaseModel):
    """Schema for the response used by the agent with the sources used to generate the response."""
    response: str = Field(description="The response from the agent")
    sources: List[Source] = Field(default_factory=list, description="The sources used to generate the response")


@tool
def get_weather(city: str) -> str:
    """
    Tool that searches the web for the weather in a given city.

    Args:
        city: The city to search for the weather.
    Returns:
        The weather in the city.
    """
    response = tavily_client.search(query=f"weather in {city}")
    return f"The weather in {city} is {response}."

# @tool
# def get_weather(city: str) -> str:
#     """
#     Tool that searches the web for the weather in a given city.

#     Args:
#         city: The city to search for the weather.
#     Returns:
#         The weather in the city.
#     """

#     return f"The weather in {city} is sunny."

llm = ChatAnthropic(model="claude-sonnet-4-6", anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"))
tools = [get_weather]
agent = create_agent(model = llm, tools = tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    print(result)

if __name__ == "__main__":
    main()
