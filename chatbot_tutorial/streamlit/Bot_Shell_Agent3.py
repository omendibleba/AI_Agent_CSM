## Simple bot to only respond to an input
import os 
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.tools import BaseTool, StructuredTool, tool
from langchain_community.tools import ShellTool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor,create_react_agent # To load simple ReAct agent. Reason an act
from langchain import hub
import warnings
warnings. filterwarnings('ignore') 



# Define API key for OPenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

## Load default OpenAI chatbot
llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.0)

# Define function to get bot  response
@tool
def bot_response(input: str) -> str:
    """Use Chatbot to answer questions that do not require any tools. Do ont perform any action if this tool is used."""
    output = llm.invoke(
        [
            HumanMessage(
                content=str(input)
            )
        ])
    return output.content

# Define tool 
shell_tool = ShellTool()

# Define list of tools the LLM is going to use 
tools_list = [bot_response,shell_tool]

# Get the template prompt to use - you can modify this!
prompt = hub.pull("hwchase17/react")


## Construct the ReAct agent by defining the llm, tools and prompt template
shell_Agent = create_react_agent(llm=llm,tools=tools_list,prompt=prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=shell_Agent, tools=tools_list, verbose=True)

# Define function to get response
def Shell_Agent(input):

    # Run executor to get response 
    response = agent_executor.invoke({"input":str(input)})
    
    return response['output']