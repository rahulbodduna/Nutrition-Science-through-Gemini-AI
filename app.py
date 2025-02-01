import os
import streamlit as st
import google.generativeai as genai

# Configure your API key (replace with your actual API key)
genai.configure(api_key="AIzaSyAlpI-C9RfSJH9kD7Rwm1V8KLU_-jnOkp0")

# Function to generate the diet plan
def generate_diet_plan(age, health_condition):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )

    # Crafting a prompt based on user input (age and health condition)
    user_input = f"Write a nutritious diet plan for a person aged {age}, suffering from {health_condition}. The diet should focus on health improvements and well-being."

    # Start the chat session with the model
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [user_input],
            },
        ]
    )

    # Generate the response
    response = chat_session.send_message(user_input)
    return response.text

# Streamlit interface
def main():
    st.title("Nutritious Diet Plan Generator")

    # Getting user inputs
    age = st.number_input("Enter Age", min_value=1, max_value=120, value=45)
    health_condition = st.selectbox("Select Health Condition", ["Low Blood Pressure", "Diabetes", "Cholesterol", "Obesity", "Heart Disease"])

    # Button to generate diet plan
    if st.button("Generate Diet Plan"):
        with st.spinner("Generating your diet plan..."):
            diet_plan = generate_diet_plan(age, health_condition)
            st.subheader(f"Diet Plan for Age {age} with {health_condition}")
            st.write(diet_plan)

if __name__ == "__main__":
    main()
