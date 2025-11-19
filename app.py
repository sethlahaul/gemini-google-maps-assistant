import streamlit as st
import os
from google import genai
from google.genai import types

# Page configuration
st.set_page_config(
    page_title="Google Maps Assistant (GenAI)",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
    }
    .source-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        margin-top: 10px;
        font-size: 0.9em;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for API Key
with st.sidebar:
    st.header("Configuration")
    api_key_input = st.text_input("Google API Key", type="password", help="Enter your Gemini API Key")
    if api_key_input:
        os.environ["GOOGLE_API_KEY"] = api_key_input
    
    st.markdown("---")
    st.markdown("### About")
    st.info("This app uses **Gemini 2.0 Flash** with **Google Maps Grounding** to provide real-world routing and travel information.")

# Main App
st.title("🗺️ AI Travel Assistant")
st.markdown("Plan your journey with real-time insights from Google Maps.")

col1, col2 = st.columns(2)
with col1:
    source = st.text_input("From", placeholder="e.g., Bangalore, India")
with col2:
    destination = st.text_input("To", placeholder="e.g., Mysore, India")

if st.button("Find Best Routes"):
    if not source or not destination:
        st.warning("Please enter both source and destination.")
        st.stop()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("Please enter your Google API Key in the sidebar.")
        st.stop()

    try:
        with st.spinner("Consulting Google Maps..."):
            client = genai.Client(api_key=api_key)
            
            prompt = f"""
            I want to travel from {source} to {destination}.
            Please find the best routes by:
            1. Road (Driving)
            2. Train (Transit)
            3. Flight (if applicable)
            
            For each mode, provide:
            - Estimated travel time and cost
            - Distance
            - Key route details or transit lines
            - Also, add details of weather conditions and traffic conditions, give details based on current weather conditions
            - For road and rail travel, give additional details about maintenance and construction work
            
            Finally, give a recommendation on the best option based on time and convenience.
            """
            
            response = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=[types.Tool(google_maps=types.GoogleMaps())]
                )
            )
            
            # Display Response
            st.markdown("### 📍 Route Analysis")
            st.markdown(response.text)
            
           
                            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
