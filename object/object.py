from ultralytics import YOLO
import cv2
import os

# Load YOLOv8 model (downloads if not available)
model = YOLO("yolov8n.pt")

# Define input and output folders
input_folder = "input"  # Ensure this folder exists
output_folder = "output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Check if input folder exists
if not os.path.exists(input_folder):
    print(f"Error: Input folder '{input_folder}' does not exist! Create it and add images.")
    exit()

# Process each image in the input folder
for image_name in os.listdir(input_folder):
    image_path = os.path.join(input_folder, image_name)  # ✅ Corrected variable

    # Read image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Skipping {image_name}: Unable to read image")
        continue

    # Run YOLOv8 inference
    results = model(image)

    # Extract detected object names
    detected_objects = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])  # Get class ID
            class_name = model.names[class_id]  # Convert to class name
            detected_objects.append(class_name)

    # Print detected objects
    print(f"Image: {image_name}")
    if detected_objects:
        object_names = "_".join(set(detected_objects))  # Merge detected names with underscores
        print(f"Detected objects: {', '.join(set(detected_objects))}")
    else:
        object_names = "no_object"
        print("No objects detected.")

    # Save annotated image with only the object name
    new_filename = f"{object_names}.jpeg"  # Save only with object name
    output_path = os.path.join(output_folder, new_filename)

    annotated_image = results[0].plot()
    cv2.imwrite(output_path, annotated_image)  # Save image with detections
    print(f"Processed image saved as: {new_filename}")
