import streamlit as st
import requests
import os

# Set up Streamlit interface
st.title("Text to Speech with ElevenLabs API")
text_input = st.text_area("Enter text to convert to speech:")

# Your ElevenLabs API key
api_key = st.secrets["api_key"]  # Use Streamlit secrets to securely store your API key

if st.button("Convert to Speech"):
    if text_input:
        try:
            # API request payload
            payload = {
                "text": text_input,
                "voice": "en_us_male",  # Example voice setting, modify as needed
                "model_id": "eleven_monolingual_v1"  # Ensure you are using the correct model ID
            }

            # API request headers
            headers = {
                "Content-Type": "application/json",
                "xi-api-key": api_key
            }

            # API endpoint (verify the correct endpoint in the API documentation)
            api_url = "https://api.elevenlabs.io/v1/text-to-speech"

            # Make the API request
            response = requests.post(api_url, json=payload, headers=headers)

            # Log the entire response for debugging
            st.text(f"Response Status Code: {response.status_code}")
            st.text(f"Response Content: {response.text}")

            # Check the response
            if response.status_code == 200:
                audio_data = response.content  # Assume the API returns the audio data directly

                # Save the audio data to a file
                audio_filename = "output.wav"
                with open(audio_filename, "wb") as audio_file:
                    audio_file.write(audio_data)

                st.audio(audio_data, format="audio/wav")
                st.success(f"Audio saved as {audio_filename}")

                # Add, commit, and push the audio file to the GitHub repository
                os.system(f"git add {audio_filename}")
                os.system(f"git commit -m 'Add generated audio file'")
                os.system("git push")

            else:
                st.error(f"Error: {response.status_code} - {response.json().get('detail', 'No detail available')}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.text(f"Traceback: {e.__traceback__}")

    else:
        st.warning("Please enter some text to convert.")
