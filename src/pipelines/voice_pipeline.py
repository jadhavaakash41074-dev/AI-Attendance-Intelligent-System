from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np 
import io
import librosa
import streamlit as st 

@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()

def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder() 

        # if librasa can return the two things 1) audio 2)sample rate
        # sr (sample rate ): in one second how much audio can goes to measurement 
        #in 1 second  audios 16,000 small measurements to divide that .
        audio,sr  = librosa.load(io.BytesIO(audio_bytes),sr=16000) 
        wav = preprocess_wav(audio)
        embedding = encoder.embed_utterance(wav)
        return embedding.tolist()
    except Exception as e:
        st.error("voice recog error")
        return None

def identify_speaker(new_embedding , candidates_dict , threshold =0.65):
    if new_embedding is None or not candidates_dict:
        return None ,0.0
    best_sid = None
    best_score = -1.0

    for sid , store_embedding in candidates_dict.items():
        if store_embedding is not None:
            # check the direction of both vector in same direct similar like cosine similarity 
            similarity =np.dot(new_embedding,store_embedding) 
            if similarity>best_score:
                best_score  = similarity
                best_sid = sid

    # best_score can we get then to check threshold compare
    if best_score >= threshold:
        return best_sid , best_score

    return None , best_score

# if audio is come in bulk amount
def process_bulk_audio(audio_bytes , candidates_dict, threshold =0.65):

    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr =16000)
        segments = librosa.effects.split(audio, top_db =30)

        identified_results ={}

        for start , end in segments:

            if (end-start)< sr*0.5:
                continue
            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            embedding = encoder.embed_utterance(wav)

            sid , score = identified_results(embedding, candidates_dict, threshold)

            if sid is not None:
                if sid not in identified_results or score > identified_results[sid]:
                    identified_results[sid] = score 
        return identified_results
    
    except Exception as e:
        st.error("Bulk Process error")
        return {}
