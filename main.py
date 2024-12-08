import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def generate_linkedin_post(topic, tone, length):
    """Generate a LinkedIn post using OpenAI."""
    try:
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        prompt = f"Write a professional LinkedIn post about {topic}. "
        prompt += f"The tone should be {tone} and the length should be {length}."
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional LinkedIn content creator."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating post: {str(e)}"

def main():
    st.title("LinkedIn Post Generator")
    st.write("Generate engaging LinkedIn posts with AI")
    
    # Input fields
    topic = st.text_input("What would you like to post about?")
    tone = st.selectbox("Select the tone of your post:", 
                       ["Professional", "Casual", "Inspirational", "Educational"])
    length = st.selectbox("Select the length of your post:",
                         ["Short (1-2 paragraphs)", "Medium (2-3 paragraphs)", "Long (3-4 paragraphs)"])
    
    if st.button("Generate Post"):
        if not topic:
            st.warning("Please enter a topic for your post.")
            return
            
        with st.spinner("Generating your LinkedIn post..."):
            generated_post = generate_linkedin_post(topic, tone, length)
            st.text_area("Generated Post", generated_post, height=300)
            
            st.success("Post generated successfully!")
            
if __name__ == "__main__":
    main()
