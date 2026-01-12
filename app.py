import streamlit as st
from agent import ask  # Imports your ask function from agent.py
import os
import pandas as pd
from sqlalchemy import create_engine

# Auto-create DB from CSV if not exists (for cloud)
if not os.path.exists("superstore.db"):
    df = pd.read_csv("superstore.csv", encoding='latin1')
    engine = create_engine("sqlite:///superstore.db")
    df.to_sql("orders", engine, if_exists="replace", index=False)


# Page config
st.set_page_config(
    page_title="Superstore GenBI Agent",
    page_icon="📊",
    layout="wide"
)


st.title("Superstore Natural Language BI Agent ⚡")
# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Example questions (clickable chips)
st.markdown("**Quick examples:**")
cols = st.columns(3)
if cols[0].button("Top 5 profitable products"):
    st.session_state.messages.append({"role": "user", "content": "Top 5 profitable products"})
    st.rerun()
if cols[1].button("Profit by category"):
    st.session_state.messages.append({"role": "user", "content": "Profit by category"})
    st.rerun()
if cols[2].button("Sales trend by month"):
    st.session_state.messages.append({"role": "user", "content": "Sales trend by month"})
    st.rerun()
st.markdown("Ask anything about sales, profit, categories, regions, etc. in plain English!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about Superstore (e.g. 'What are my top 5 profitable products?' or 'Show sales trend by month')"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking and querying the database..."):
            try:
                response = ask(prompt)
                st.markdown(response)
            except Exception as e:
                st.error(f"Oops — something went wrong: {str(e)}")
                st.info("Try rephrasing the question or check if the database is connected.")

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar extras
st.sidebar.header("About This Demo")
st.sidebar.markdown("""
This is a **Generative BI Agent** built with:
- LangChain + Groq (Llama 3.3 70B)
- SQLite (Superstore dataset)
- Streamlit for the chat UI

Ask questions like:
- Top categories by profit?
- Sales by region in 2018?
- Customers with highest lifetime value?
""")

st.sidebar.info("Refresh the page to clear chat history.")
