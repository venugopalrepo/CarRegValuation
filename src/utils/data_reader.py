import re
import os

def read_registration_numbers(file_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
    full_path = os.path.join(base_dir, "..", "..","tests", "data", file_path)  # Correct path to data folder

    with open(full_path, "r") as file:
        content = file.read()
    return re.findall(r"\b[A-Z]{2}[0-9]{2} [A-Z]{3}\b|\b[A-Z]{2}[0-9]{2}[A-Z]{3}\b", content)

def read_expected_output(file_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
    full_path = os.path.join(base_dir, "..", "..","tests", "data", file_path)  # Correct path to data folder

    expected_data = {}
    with open(full_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) >= 3:
                expected_data[parts[0]] = {"make_model": parts[1], "year": parts[2]}
    return expected_data