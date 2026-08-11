import requests
import re

# Fixed webpage URL
url = "https://www.example.com"

# Send request to webpage
response = requests.get(url)

# Check if webpage was successfully loaded
if response.status_code == 200:

    # Get webpage HTML
    html = response.text

    # Extract title from HTML
    title = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)

    if title:
        page_title = title.group(1)

        # Save title into a file
        with open("page_title.txt", "w") as file:
            file.write(page_title)

        print("Webpage title:", page_title)
        print("Title saved successfully in page_title.txt")

    else:
        print("Title not found.")

else:
    print("Failed to load webpage.")