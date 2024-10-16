import streamlit as st
from elevenlabs import play,stream,save
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="sk_adb10e3031ae8a259e0b34e859fb799bd1863f39a7effb76", # Defaults to ELEVEN_API_KEY
)

# Título do aplicativo
st.title("Balcão de pedidos")

# Campos de entrada para o nome e a mensagem
name = st.text_input("Nome", "Ricardo!")
message = st.text_input("Mensagem", "Seu pedido está pronto.")
narrador = st.text_input("Narrador", "Adam")

# Botão para gerar e reproduzir o áudio
if st.button("Gerar e Reproduzir Áudio"):
  # Gerando o áudio
    audio = client.generate(

    text=name+message,
    voice=narrador,
    model="eleven_multilingual_v2"
    )

    # Reproduzindo o áudio
    play(audio, notebook=False)
st.success("Áudio gerado e reproduzido com sucesso!")
