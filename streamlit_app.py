import streamlit as st
import requests
import json

# Set up Streamlit interface
st.title("Text to Speech with ElevenLabs API")
text_input = st.text_area("Enter text to convert to speech:")

# Your ElevenLabs API key
api_key = "sk_fae3356ea114cdfa623777bfe0504f2fd2f24619d7a66f28"

if st.button("Convert to Speech"):
    if text_input:
        try:
            # API request payload
            payload = {
                "text": text_input,
                "voice_settings": {
                    "voice": "Adam",  # Example voice setting, modify as needed
                    "model": "eleven_multilingual_v2"
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

            # Log the entire response for debugging
            st.text(f"Response Status Code: {response.status_code}")
            st.text(f"Response Content: {response.text}")

            # Check the response
            if response.status_code == 200:
                audio_data = response.content  # Assume the API returns the audio data directly
                st.audio(audio_data, format="audio/wav")
            else:
                st.error(f"Error: {response.status_code} - {response.json().get('detail', 'No detail available')}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.text(f"Traceback: {e.__traceback__}")

    else:
        st.warning("Please enter some text to convert.")

