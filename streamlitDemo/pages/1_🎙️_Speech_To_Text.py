import streamlit as st
from utility import APP_NAME, DEMO_AUDIO_3_PATH, NO_API_SET_FLAG, get_stt_api, realtime_audio_file_STT, realtime_audio_recording_STT, autoplay_audio

st.set_page_config(page_title="Speech To Text Demo", page_icon="🎙️", layout="wide")

st.markdown("# Speech To Text Demo🎙️")
st.write(
    f"""
    This demo illustrates a real time transcription of the Speech To Text Model of {APP_NAME}. 
    Try out an audio sample or test with a live recording of your own voice!
    """
)

if get_stt_api() == NO_API_SET_FLAG:
    st.warning('Please setup the STT API endpoint on the API Setup page', icon="⚠️")

sampleAudioTab, liveRecordingTab = st.tabs(["AUDIO SAMPLE", "TEST LIVE RECORDING"])

with sampleAudioTab:
    if st.button('Start Transcribing Sample'):
        autoplay_audio(DEMO_AUDIO_3_PATH)
        realtime_audio_file_STT(DEMO_AUDIO_3_PATH)


with liveRecordingTab:
    realtime_audio_recording_STT()

