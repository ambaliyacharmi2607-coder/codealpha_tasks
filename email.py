import re

# Input and output file names
input_file = "input.txt"
output_file = "emails.txt"

# Read the text file
with open(input_file, "r") as file:
    text = file.read()

# Find all email addresses
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)

# Remove duplicate emails
emails = list(set(emails))

# Save emails into another file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")
print("Total emails found:", len(emails))