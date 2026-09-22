from langgraph.graph import START,END,StateGraph
from typing_extensions import TypedDict 
from typing import Literal ,NotRequired
from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv,find_dotenv #Searches for env also in parent files.
load_dotenv(find_dotenv())
key=os.environ.get("GEMINI_KEY")
#State:
class State(TypedDict):
    graph_int:NotRequired[int]
    graph_str:str 
model_llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0,api_key=key)
#nodes:
def node1(state:State)->State:
    """
    Take a state and ask our 
    model to take a number between 1 or 2 
    """
    model_response=model_llm.invoke("choose between 1 or 2 or 3 .reply only with number")
    if isinstance(int(model_response.content),int):
        return   {"graph_int":int(model_response.content),
                "graph_str":state["graph_str"]+"passed by node 1"}
    else:
        return  {"graph_int":0,
                "graph_str":state["graph_str"]+"passed by node 1"}

def node2(state:State)->State:


    model_response=model_llm.invoke("choose between 1 or 2 or 3.reply only with number")
    if isinstance(int(model_response.content),int):
        return   {"graph_int":int(model_response.content),
                "graph_str":state["graph_str"]+"passed by node 1"}
    else:
        return  {"graph_int":0,
                "graph_str":state["graph_str"]+"passed by node 1"}
def node3(state:State)->State:

    model_response=model_llm.invoke("choose between 1 or 2 or 3.reply only with number")
    if isinstance(int(model_response.content),int):
        return   {"graph_int":int(model_response.content),
                "graph_str":state["graph_str"]+"passed by node 1"}
    else:
        return  {"graph_int":0,
                "graph_str":state["graph_str"]+"passed by node 1"}

#CReate edges:
def next_step(state:State)->Literal["node2","node3",END]:
    #Check state and return which node to go.
    number_state=state.get("graph_int")
    if number_state==2:
        return "node2"
    elif number_state==3:
        return "node3"
    else :
        return END

#Building graph:
builder=StateGraph(State)
builder.add_node("node1",node1)
builder.add_node("node2",node2)
builder.add_node("node3",node3)
builder.add_edge(START,"node1")
builder.add_conditional_edges("node1",next_step)
builder.add_edge("node2",END)
builder.add_edge("node3",END)
#Create the graph:
graph=builder.compile()
