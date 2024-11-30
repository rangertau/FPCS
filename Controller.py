import subprocess

'''

this is just to print out the results to stdout
# Arguments to pass
args = ["arg1", "arg2", "arg3"]

# Call the target Python program
result = subprocess.run(["python", "StreamLog.py", *args], capture_output=True, text=True)

# Print the output from the called program
print("Output from target program:")
print(result.stdout)
print("Error output (if any):")
print(result.stderr)
'''



# Arguments to pass
args = ["arg1", "arg2", "arg3"]

# Specify the file to write the output
output_file = "output.txt"

# Call the target Python program and redirect output to the file
with open(output_file, "w") as file:
    result = subprocess.run(
        ["python", "StreamLog.py", *args],
        stdout=file,  # Redirect stdout to the file
        stderr=subprocess.PIPE,  # Capture stderr in case of errors
        text=True  # Handle outputs as strings
    )

# Check for errors and print if any occurred
if result.returncode != 0:
    print("An error occurred:")
    print(result.stderr)
else:
    print(f"Output written to {output_file}")

