from langgraph.graph import StateGraph, START, END

def greeting(state: str) -> str:
    return state + " Welcome to AI career Lab"

builder = StateGraph(str)
builder.add_node("greeting", greeting)

builder.add_edge(START, "greeting")
builder.add_edge("greeting", END)

graph = builder.compile()
