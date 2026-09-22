from langgraph.graph import START,END,StateGraph,MessagesState
from typing_extensions import TypedDict 
from langchain_core.messages import AnyMessage #union type hint contains:Humanmessage,AIMessage,SystemMessage,ToolMessage 
from typing import List,Annotated 
from langgraph.graph.message import add_messages #Allows us to add messages instead of just appending to the state 
from langchain_google_genai import ChatGoogleGenerativeAI 
#State:

class MessagesState(TypedDict):
    #Annotated is a tool to add our add_messages plugin to our state:
    #in annotated:1->type hint,2->metadata
    messages:Annotated[list[AnyMessage],add_messages]

model_llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)
#nodes :
def chat(state:MessagesState)->MessagesState:
    #Because we use langgraph's reducer we are actually 
    #appending here !
    return {"messages":[model_llm.invoke(state["messages"])]}
#Create edges:
#create graph:
builder=StateGraph(MessagesState)
builder.add_node(chat,"chat")
builder.add_edge(START,"chat")
builder.add_edge("chat",END)
graph=builder.compile()
