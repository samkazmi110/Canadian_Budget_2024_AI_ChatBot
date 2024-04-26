import streamlit as st
from langchain_helper import Initialize_llm_and_vector_db,get_answer_from_budget


st.title("Canadian Budget 2024 AI Powered: Interact with the Canadian Budget Document: Ask Any Question, Get Immediate Answers")
st.write("Enter your question below:")
question = st.text_input("Question", "")

openapi_key = st.sidebar.text_input("Enter OPEN API KEY", key="openapi_key")

if st.button("ask"):
        Initialize_llm_and_vector_db(openapi_key)
        if question:
            if question.lower() == "exit" or question.lower() == "quit":
                st.stop()

            answer = get_answer_from_budget(question).replace("$","\$")
            st.write("Question: '%s'"% question)
            st.write(f"Answer: '{answer}'")
        else:
            st.warning("Please enter a question.")

