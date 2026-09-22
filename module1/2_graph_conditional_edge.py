from langgraph.graph import StateGraph,START,END
from typing_extensions import TypedDict
from typing import Literal
#state 
class State(TypedDict):
    graph_str:str 
#nodes 
def node1(state:State)->State:
    """
    This node will Greet our user!
    """
    return {"graph_str":state["graph_str"]+"welcome to AI career lab"}
def node2(state:State)->State:
    """
    This node will greet our user 
    """
    return {"graph_str":state["graph_str"]+"I am in node 2"}
def node3(state:State)->State :
    """
    This node will greet our user 
    """
    return {"graph_str":state["graph_str"]+"I am in node 3"}

#edges 
#The edges do not touch the logic of the node we return if we want to do node2 or node3 
#It guides the graph and cannot call the logic 
def next_step(state:State)->Literal["node2","node3"]:
    """
    guide the state/graph to next node 
    """
    state_str=state["graph_str"]
    array_state_str=state_str.split(" ")
    if array_state_str[0]=="hello":
        return "node2"
    else:
        return "node3"

#putting graph together
builder=StateGraph(State)
builder.add_node("node1",node1)
builder.add_node("node2",node2)
builder.add_node("node3",node3)
builder.add_edge(START,"node1")
builder.add_conditional_edges("node1",next_step)#We choose node 1 and do conditional function next_step 
builder.add_edge("node2",END) #If condition is node2->we go to end 
builder.add_edge("node3",END) #If condition is node3->we go to end 
graph=builder.compile()
