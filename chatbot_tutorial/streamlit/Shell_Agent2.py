import os 
from langchain_community.tools import ShellTool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor,create_react_agent # To load simple ReAct agent. Reason an act
from langchain import hub
import warnings
warnings. filterwarnings('ignore') 

# Define API key for OPenAI
# os.environ["OPENAI_API_KEY"] =  
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Define tool 
shell_tool = ShellTool()

## Define LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

# Define list of tools the LLM is going to use 
tools = [shell_tool]

# Get the template prompt to use - you can modify this!
prompt = hub.pull("hwchase17/react")

## Construct the ReAct agent by defining the llm, tools and prompt template
shell_Agent = create_react_agent(llm=llm,tools=tools,prompt=prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=shell_Agent, tools=tools, verbose=True)


# Define function to get response
def Shell_Agent(input):

    # Run executor to get response 
    response = agent_executor.invoke({"input":str(input)})
    
    return response['output']