## Simple bot to only respond to an input
import os 
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Define API key for OPenAI
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

os.environ["OPENAI_API_KEY"] =  "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"
## Load default OpenAI chatbot
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.0)

# Define function to get bot  response
def bot_response(input):
    # Invoke the chatbot using a hummanMessage to reecive an AIMessage
    output = chat.invoke(
        [
            HumanMessage(
                content=str(input)
            )
        ])
    return output.content

# ## Test inputs @ T=0:
# Tell me a joke about the clouds
# Tell me the same joke again
# Create new folder named test_1