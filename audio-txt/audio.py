import speech_recognition as sr
import os

# Define input/output folders
input_folder = "audio_input"
output_folder = "audio_output"
os.makedirs(output_folder, exist_ok=True)

# Initialize recognizer
recognizer = sr.Recognizer()

# Process each audio file
for audio_name in os.listdir(input_folder):
    audio_path = os.path.join(input_folder, audio_name)

    if not audio_name.lower().endswith((".mp3", ".wav", ".ogg", ".m4a")):
        print(f"Skipping {audio_name}: Unsupported format")
        continue

    print(f"Processing: {audio_name}...")

    # Load the audio file
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        text_filename = os.path.splitext(audio_name)[0] + ".txt"
        output_path = os.path.join(output_folder, text_filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"✅ Transcription saved: {text_filename}")

    except sr.UnknownValueError:
        print(f"❌ Could not understand {audio_name}")
    except sr.RequestError:
        print("❌ Google Speech API error")
