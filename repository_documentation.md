# LangGraph ReAct Agent & Fundamentals

This repository contains a step-by-step implementation of **LangGraph** concepts, progressing from basic state graphs and custom routing logic to building a **ReAct (Reasoning + Acting) Agent** powered by Google Gemini and custom tools.

---

## Technical Features

* **State Management**: Using primitives (`str`), `TypedDict`, and `MessagesState` with the `add_messages` reducer function.
* **Routing**: Implementation of static edges and dynamic control flow using `add_conditional_edges`.
* **LLM & Tool Integration**: Binding tools to Google Gemini (`gemini-2.5-flash`) via `langchain-google-genai`.
* **Agent Loops**: Utilizing `ToolNode` and `tools_condition` from `langgraph.prebuilt` to execute cyclical tool calls (ReAct loop).

---

## File Overview

| File Name | Description |
| :--- | :--- |
| `0_graph_state_str.py` | Basic graph using a primitive string (`str`) as state. |
| `1_graph_state_dict.py` | State definition using `TypedDict` for structured state management. |
| `2_graph_conditional_edge.py` | Implementing conditional routing based on state evaluation using custom functions. |
| `3_graph_introduction_model.py` | Integrating `ChatGoogleGenerativeAI` inside nodes to make dynamic routing decisions. |
| `4_graph_messages_states.py` | Using standard `MessagesState` with `Annotated` reducers (`add_messages`) to manage message history. |
| `5_graph_model_tool.py` | Binding custom tools (`@tool`) to the Gemini model using `.bind_tools()`. |
| `6_graph_toolcall.py` | Adding a prebuilt `ToolNode` and dynamic conditional routing via `tools_condition`. |
| `8_graph_agent.py` | Complete **ReAct Math Agent** with system prompts, multiple math tools (`multiply`, `addition`, `substraction`), and a full agent loop. |
| `test.py` | Environment variable validation check for Gemini API keys. |

---

## Architecture: ReAct Agent Loop (`8_graph_agent.py`)

The final agent follows a standard ReAct execution loop:

```
       +------------+
       |   START    |
       +-----+------+
             |
             v
   +------------------+
---| chat_with_tools  |<---+
|  +------------------+    |
|            |             |
|   (tools_condition)      |
|     /          \         |
|  [Tool Called] [No Tool] |
|   /              \       |
v  v                v      |
+-------+        +-----+   |
| tools |        | END |   |
+---+---+        +-----+   |
    |                      |
    +----------------------+
```

1. **User Query**: Input is passed to the `chat_with_tools` node.
2. **LLM Evaluation**: Model determines whether it can answer directly or needs to invoke a tool (`addition`, `substraction`, `multiply`).
3. **Conditional Branching (`tools_condition`)**:
   * If a tool call is generated, routing shifts to the `tools` node.
   * If no tool is needed, execution routes directly to `END`.
4. **Execution & Feedback**: The `ToolNode` executes the function and passes the result back to `chat_with_tools` to generate the final response.

---

## Prerequisites & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install langgraph langchain-google-genai python-dotenv
```

### 3. Environment Variables
Create a `.env` file in the root directory and configure your Google Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## How to Run

### Execute Individual Scripts
Run any phase of the implementation directly using Python:
```bash
python 8_graph_agent.py
```

### Development with LangGraph CLI
If you have `langgraph-cli` installed, you can visualize and interact with the agent using LangGraph Studio:
```bash
langgraph dev
```