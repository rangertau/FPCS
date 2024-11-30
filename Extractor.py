import re
import csv

# File paths
input_file = "output.txt"  # Path to the text file containing the input
output_csv = "detections_with_time.csv"  # Path to the output CSV file

# Initialize lists to store extracted data
detection_details = []
timestamps = []

# Read the input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Process each line in the file
for line in lines:
    # Extract detection details
    detection_match = re.search(r"0:\s\d+x\d+\s(.*?),\s[\d.]+ms", line)
    if detection_match:
        detection_details.append(detection_match.group(1))
    
    # Extract timestamps
    time_match = re.search(r"Time:\s([\d-]+\s[\d:.]+)", line)
    if time_match:
        timestamps.append(time_match.group(1))

# Ensure the lists are aligned
if len(detection_details) != len(timestamps):
    print("Error: Mismatch between detections and timestamps")
else:
    # Write the extracted data to a CSV file without quotes
    with open(output_csv, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)  # No quotes for normal fields
        writer.writerow(["Detection ID", "Details", "Timestamp"])  # CSV header

        for i, (details, timestamp) in enumerate(zip(detection_details, timestamps), start=1):
            writer.writerow([i, details, timestamp])

    print(f"Detections and timestamps saved to {output_csv}")


'''
#This will stream the input instead of loading the entire file if it is too large

with open(input_file, "r") as file:
    for line in file:
        detection_match = re.search(r"0:\s\d+x\d+\s(.*?),\s[\d.]+ms", line)
        if detection_match:
            detection_details.append(detection_match.group(1))

        time_match = re.search(r"Time:\s([\d-]+\s[\d:.]+)", line)
        if time_match:
            timestamps.append(time_match.group(1))

'''

#import csv
from collections import Counter
#import re



# File paths
input_csv = "detections_with_time.csv"  # Path to the CSV file
output_class_counts = "class_counts.csv"  # Path to save the class counts

# Initialize a Counter to store class counts
class_counter = Counter()

# Read the CSV file
with open(input_csv, "r") as csv_file:
    reader = csv.DictReader(csv_file)  # Read CSV with default comma delimiter
    for row in reader:
        details = row["Details"]
        
        # Find all class names in the details using regex
        # This will match the class names like 'Sedan2Dr', 'SUV-Hatchback'
        classes = re.findall(r'\d+\s([A-Za-z\-]+)', details)
        
        # Update the counter with the found classes
        class_counter.update(classes)

# Write the class counts to a new CSV file
with open(output_class_counts, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Class", "Count"])  # Header row
    for class_name, count in class_counter.items():
        writer.writerow([class_name, count])

print(f"Class counts saved to {output_class_counts}")


