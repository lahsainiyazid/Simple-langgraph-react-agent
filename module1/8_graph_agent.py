from langgraph.graph import StateGraph,START,END,MessagesState 
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv,find_dotenv 
from langchain.tools import tool#annotation that when used on a function becomes a tool that can be used by our llm 
from langgraph.prebuilt import ToolNode,tools_condition
from langchain.messages import SystemMessage #To create a system message that will guide the llm. 
from typing import Literal 
load_dotenv(find_dotenv())
model_llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)
@tool
def multiply(nb1:int,nb2:int)->int:
    """
    This tool returns the multiplication of 2 numbers 
    """
    return nb1*nb2 
@tool 
def addition(nb1:int,nb2:int)->int:
    """
    Return the sum of 2 numbers!
    """
    return nb1+nb2 
@tool 
def substraction(nb1:int,nb2:int)->int:
    """
    Return the substraction of 2 numebrs!
    """
    return nb1-nb2
model_llm_with_tools=model_llm.bind_tools([multiply,addition,substraction])
system_message=SystemMessage(content="You are a helpful Math teacher")
def chat_with_tools(state:MessagesState)->MessagesState:
    return {
        "messages":[model_llm_with_tools.invoke(state["messages"]+[system_message])]}#We have to concatentate a list with a list!
builder=StateGraph(MessagesState)
builder.add_node("chat_with_tools",chat_with_tools)
builder.add_node("tools",ToolNode([multiply,addition,substraction]))
builder.add_edge(START,"chat_with_tools")
builder.add_conditional_edges("chat_with_tools",tools_condition)
builder.add_edge("tools","chat_with_tools")
"""
Here the tools_condition has end if llm judges we do not need any tool->end tool_condition returns in this state end__.
"""
graph=builder.compile()
