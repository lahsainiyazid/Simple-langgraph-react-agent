#importing our libs:
from langgraph.graph import StateGraph,START,END
from typing_extensions import TypedDict #So our state is of type typed dict 
#State 
class State(TypedDict):
    graph_str:str 
def greeting(state:State)->State:
    """
    Function takes a dict and returns a dict with greetings:
    """
    return {"graph_str":state["graph_str"]+"welcome to AI carrer lab"}

#Node 
#Edges
#putting our graph together:
builder=StateGraph(State)
builder.add_node("greeting",greeting)
builder.add_edge(START,"greeting")
builder.add_edge("greeting",END)
graph=builder.compile()
