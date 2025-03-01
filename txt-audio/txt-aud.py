from gtts import gTTS
import os

# Define input and output folders
input_folder = "text_input"
output_folder = "audio_output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each text file in the input folder
for text_name in os.listdir(input_folder):
    text_path = os.path.join(input_folder, text_name)

    # Only process .txt files
    if not text_name.lower().endswith(".txt"):
        print(f"Skipping {text_name}: Unsupported format")
        continue

    print(f"Processing: {text_name}...")

    # Read text content
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print(f"Skipping {text_name}: Empty file")
        continue

    # Convert text to speech
    tts = gTTS(text=text, lang="en")  # Change 'en' to another language if needed

    # Save output as an audio file
    audio_filename = os.path.splitext(text_name)[0] + ".mp3"
    output_path = os.path.join(output_folder, audio_filename)
    tts.save(output_path)

    print(f"✅ Audio saved: {audio_filename}")
