import streamlit as st
from app.main import MusicLLM
from app.utils import *
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Music Composer",layout="centered")
st.title("AI MUSIC COMPOSER")
st.markdown("Generate AI Music by describing the style and content")


music_input = st.text_input("Describe the music you want to compose")
style = st.selectbox("Choose a style" , ["Sad" , "Happy" , "Jazz" , "Romantic" , "Extreme"])

if st.button("Generate Music") and music_input:
    generator = MusicLLM()

    with st.spinner("Generating music"):
        melody = generator.generate_melody(music_input)
        harmony = generator.generate_harmony(melody)
        rhythm = generator.generate_rythm(melody)
        composition = generator.adapt_style(style,melody,harmony,rhythm)


        melody_notes = melody.split()
        melody_freqs = note_to_frequencies(melody_notes)


        harmony_chords = harmony.split()
        harmony_notes=[]
        for chord in harmony_chords:
            harmony_notes.extend(chord.split('-'))

        harmony_freqs = note_to_frequencies(harmony_notes)


        all_freqs = melody_freqs+harmony_freqs


        wav_bytes = generate_wav_bytes_from_notes_freq(all_freqs)
    

    st.audio(BytesIO(wav_bytes), format='audio/wav')

    st.success("Music generated sucesfully....")

    with st.expander("Composition Summary"):
        st.text(composition)
    


