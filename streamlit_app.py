
import streamlit as st
import requests

# Set up Streamlit interface
st.title("Text to Speech with ElevenLabs API")
text_input = st.text_area("Enter text to convert to speech:")

# Your ElevenLabs API key
api_key = "sk_fae3356ea114cdfa623777bfe0504f2fd2f24619d7a66f28"

if st.button("Convert to Speech"):
    if text_input:
        # API request payload
        payload = {
            "text": text_input,
            "voice_settings": {
                "voice": "en_us_male"  # Example voice setting, modify as needed
            }
        }

        # API request headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        # API endpoint
        api_url = "https://api.elevenlabs.io/v1/text-to-speech"

        # Make the API request
        response = requests.post(api_url, json=payload, headers=headers)

        # Check the response
        if response.status_code == 200:
            audio_url = response.json().get("audio_url")
            if audio_url:
                st.audio(audio_url, format="audio/wav")
            else:
                st.error("Audio URL not found in the response.")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter some text to convert.")
