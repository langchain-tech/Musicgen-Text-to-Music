import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import streamlit as st 
import scipy
import pdb

print("LOaded")


@st.cache_resource
def load_model():
    model = MusicGen.get_pretrained('facebook/musicgen-small')
    return model

def generate_music_tensors(description, duration: int):
    print("Description: ", description)
    print("Duration: ", duration)
    model = load_model()
    model.set_generation_params(duration=duration) 
    wav = model.generate([description])

    return  wav, model.sample_rate

def main():

    st.title("Text to Music Generator🎵")

    with st.expander("See explanation"):
        st.write("Music Generator app built using Meta's Audiocraft library. We are using Music Gen Small model.")

    text_area = st.text_area("Enter your description.......")
    time_slider = st.slider("Select time duration (In Seconds)", 0, 20, 10)

    if text_area and time_slider:
        if st.button("Genrate Music:"):
        	st.write("Genrating music .....")
	        wav, sample_rate = generate_music_tensors(text_area, time_slider)
	        st.write("Saving genrated music .....")
	        file_path = "audios/audio_file"
	        for idx, one_wav in enumerate(wav):
	            audio_write(f"{file_path}", one_wav.cpu(), sample_rate, strategy="loudness", loudness_compressor=True)
	        st.audio("audios/audio_file.wav", format='audio/wav')
if __name__ == "__main__":
    main()
