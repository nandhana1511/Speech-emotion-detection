import sounddevice as sd
import soundfile as sf
import tkinter as tk
from tkinter import filedialog, messagebox
from joblib import load
import librosa
import numpy as np

# Loading trained models
gender_model = load('gender_model.joblib')
emotion_model = load('emotion_model.joblib')

emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'pleasant_surprised', 'sad']

def extract_features(file_path):
    y, sr = librosa.load(file_path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    mfccs = np.mean(mfccs.T, axis=0)
    chroma = np.mean(chroma.T, axis=0)
    spectral_contrast = np.mean(spectral_contrast.T, axis=0)
    return np.hstack([mfccs, chroma, spectral_contrast])

def classify_audio(file_path):
    try:
        features = extract_features(file_path)
        features = np.expand_dims(features, axis=0)
        
        # Predict gender
        gender_prediction = gender_model.predict(features)[0]
        
        if gender_prediction == 1:
            return "Male audio detected. Please upload a female audio"
        
        # Predict emotion if female
        emotion_prediction = emotion_model.predict(features)[0]
        
        # Get the emotion label
        emotion = emotions[emotion_prediction]
        
        return f"Detected emotion: {emotion}"
    
    except Exception as e:
        print(f"Error classifying audio: {e}")
        return f"Error: {e}"

class AudioClassifierGUI:
    def __init__(self, master):
        self.master = master
        master.title("Audio Emotion Classifier")
        master.configure(bg="#808080")

        self.label = tk.Label(master, text="Select an audio file or record your own:", bg="#808080", fg="#000000", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.select_button = tk.Button(master, text="Select File", command=self.select_file, bg="#36454F", fg="#ffffff", font=("Helvetica", 10), width=20)
        self.select_button.pack(pady=10)

        self.record_button = tk.Button(master, text="Record Audio", command=self.record_audio, bg="#36454F", fg="#ffffff", font=("Helvetica", 10), width=20)
        self.record_button.pack(pady=10)
        
        self.detect_button = tk.Button(master, text="Detect Emotion", command=self.detect_emotion, bg="#928E85", fg="#ffffff", font=("Helvetica", 10), width=20)
        self.detect_button.pack(pady=10)
        
        self.result_label = tk.Label(master, text="", bg="#808080", fg="#000000", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.selected_file = None

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
        if file_path:
            self.selected_file = file_path
            self.result_label.config(text="File selected: " + file_path)
        else:
            messagebox.showerror("Error", "No file selected.")

    def record_audio(self):
        fs = 44100 
        seconds = 5

        try:
            print("Recording...")
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='float64')
            sd.wait()

            temp_file = "recorded_audio.wav"
            sf.write(temp_file, myrecording, fs)

            self.selected_file = temp_file
            self.result_label.config(text="Audio recorded successfully!")

        except Exception as e:
            print(f"Error recording audio: {e}")
            messagebox.showerror("Error", f"Error recording audio: {e}")

    def detect_emotion(self):
        if self.selected_file:
            try:
                result = classify_audio(self.selected_file)
                self.result_label.config(text=result)
            except Exception as e:
                print(f"Error classifying audio: {e}")
                messagebox.showerror("Error", f"Error classifying audio: {e}")
        else:
            messagebox.showerror("Error", "No audio file selected or recorded.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioClassifierGUI(root)
    root.mainloop()
