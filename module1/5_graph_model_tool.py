from langgraph.graph import StateGraph,START,END,MessagesState 
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv,find_dotenv 
from langchain.tools import tool #annotation that when used on a function becomes a tool that can be used by our llm 
#We load our env variables:
_=load_dotenv(find_dotenv())
"""
Btw for messages state under the hood we have this defined as our class:
class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
"""
model_llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
@tool 
def multiply(nb1:int,nb2:int)->int:
    """
    This tool is used for multiplying 2 numbers and returning the product 
    """
    return nb1*nb2 
#We bind our llm with the tools we created:
model_llm_with_tool=model_llm.bind_tools([multiply])
#nodes:
def chat_with_tool(state:MessagesState)->MessagesState:
    return {"messages":[model_llm_with_tool.invoke(state["messages"])]}
builder=StateGraph(MessagesState)
builder.add_node("chat_with_tool",chat_with_tool)
builder.add_edge(START,"chat_with_tool")
builder.add_edge("chat_with_tool",END)
graph=builder.compile()
