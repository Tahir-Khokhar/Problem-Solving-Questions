# 21. Parse log file for errors.

# Problem: Read a log file and return a list of lines that contain the word "ERROR".

def extract_errors(filepath):
    errors = []
    with open(filepath, 'r') as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line.strip())
    return errors


with open("app.log", "w") as f:
    f.write("INFO: Started\nERROR: Connection failed\nERROR: Timeout\nINFO: Done\n")
print(extract_errors("app.log"))
# Output: ['ERROR: Connection failed', 'ERROR: Timeout']