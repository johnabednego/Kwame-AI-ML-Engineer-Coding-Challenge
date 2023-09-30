import streamlit as st
import requests

# Streamlit UI code
st.title("Question Answering System")

# User input for question
question = st.text_input("Enter your question:")

# Button to retrieve relevant passages and generate answers
if st.button("Get Answer"):
    # Send a POST request to the Flask API endpoint
    api_url = "http://localhost:4000/api/question"  # Corrected API endpoint URL
    data = {'question': question}
    response = requests.post(api_url, json=data)
    print("API RESPONSE:", end=" => ")
    print(response.text)
    result = response.json()
    
    # Display relevant passages and direct answer
    st.subheader("Relevant Passages:")
    for passage in result['answers']:
        st.write(passage['passage'])
    
    st.subheader("Direct Answer:")
    st.write(result['direct_answer'])
