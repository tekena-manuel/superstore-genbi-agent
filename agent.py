import streamlit as st

from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq
from langchain_community.agent_toolkits import create_sql_agent
# from langchain.agents import AgentType

# Connect to the Superstore database
db = SQLDatabase.from_uri("sqlite:///superstore.db")

# Groq LLM setup - PASTE YOUR REAL KEY HERE
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=st.secrets["GROQ_API_KEY"],  # Load from Streamlit secrets
    max_tokens=1024,
)


# Schema prefix to force correct column names
schema_prefix = """
You are a SQL expert querying the Superstore sales dataset.
Table name: orders

IMPORTANT: Use EXACT column names (case-sensitive, with spaces where they exist):
- "Customer Name"    ← This is the column with actual customer names (e.g. 'Sean Miller', 'Tamara Chand')
- "Customer ID"
- "State"
- "Region"
- "Category"
- "Sales"
- "Profit"
- "Order Date"
- "Quantity"
- "Discount"

ALWAYS enclose column names that contain spaces in double quotes: "Customer Name"
NEVER use underscores in column names unless they really exist in the table.
When asked about customers, ALWAYS select and display the actual value from "Customer Name".
"""

# Create the SQL agent
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True,
    agent_type="tool-calling",           # better reliability with Groq models
    prefix=schema_prefix,
    max_iterations=30,
)

# Simple function to ask questions
def ask(question):
    response = agent_executor.invoke({"input": question})
    return response["output"]
