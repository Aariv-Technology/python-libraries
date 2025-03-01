import os
from pydub import AudioSegment

# Define input and output folders
input_folder = "input"
output_folder = "output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get list of audio files in input folder
audio_files = [f for f in os.listdir(input_folder) if f.lower().endswith((".mp3", ".wav", ".ogg", ".flac"))]

# Check if there are any files
if not audio_files:
    print("No audio files found in the 'input' folder.")
    exit()

# Ask for desired output format
formats = ["mp3", "wav", "ogg", "flac"]
print("\nAvailable formats: mp3, wav, ogg, flac")
output_format = input("Enter the format you want to convert to: ").strip().lower()

# Validate format
if output_format not in formats:
    print("Invalid format. Exiting.")
    exit()

# Process all files in the input folder
for input_file in audio_files:
    input_path = os.path.join(input_folder, input_file)

    # Load the audio file
    try:
        audio = AudioSegment.from_file(input_path)
    except Exception as e:
        print(f"❌ Error processing {input_file}: {e}")
        continue

    # Save the converted file
    output_filename = os.path.splitext(input_file)[0] + "." + output_format
    output_path = os.path.join(output_folder, output_filename)
    audio.export(output_path, format=output_format)

    print(f"✅ Converted: {input_file} → {output_filename}")

print("\n🎉 All files converted successfully!")
