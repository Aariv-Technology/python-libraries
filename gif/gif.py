import cv2
import imageio
import os

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Paths
video_path = "input/abc.mp4"  # Your input video
output_gif_path = "output/clip.gif"

# Time settings (in seconds)
start_time = 5  # Start time for the GIF
end_time = 10   # End time for the GIF

# Open video
cap = cv2.VideoCapture(video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))  # Get the FPS of the video
start_frame = int(start_time * fps)
end_frame = int(end_time * fps)

frames = []
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Capture frames within the desired range
    if start_frame <= frame_count <= end_frame:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
        frames.append(frame_rgb)

    if frame_count > end_frame:
        break

    frame_count += 1

cap.release()

# Save as an animated GIF
if frames:
    imageio.mimsave(output_gif_path, frames, duration=0.1)  # 0.1s per frame (adjustable)
    print(f"✅ GIF clip saved at {output_gif_path}")
else:
    print("❌ No frames extracted. Check your video path and time range.")
