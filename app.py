import os
import requests

# This is a tool to group download PDF files with the are.na API
# More information about the are.na api can be found here: https://dev.are.na/documentation/channels

def fetch_api(channel_slug):
    url = f"https://api.are.na/v2/channels/{channel_slug}/contents?per=500"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        api_response = response.json()
        get_attachment(api_response)
    else:
        print("Failed to fetch channel contents. Status code:", response.status_code)

def get_attachment(api_response):
    folder_name = "downloaded_files"
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for item in api_response['contents']:
        if item.get('attachment'):
            attachment = item.get('attachment')
            attachment_url = attachment.get('url')
            if attachment_url:
                title = item.get('title', 'Untitled')  # Get the title or use 'Untitled' if it's missing
                download_attachment(attachment_url, folder_name, title)

def download_attachment(attachment_url, folder, title):
    # Remove invalid characters from the title to use as filename
    filename = "".join(x for x in title if x.isalnum() or x in "_- ")
    filename = f"{filename}.pdf"
    filepath = os.path.join(folder, filename)

    # Download the file
    with open(filepath, 'wb') as f:
        response = requests.get(attachment_url)
        if response.status_code == 200:
            f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download {filename}. Status code: {response.status_code}")

if __name__ == "__main__":
    # Example usage:
    # Example channel with a lot of PDF's https://www.are.na/mo-mcknight/texts-seb9ve3j0ta
    # channel_slug = texts-seb9ve3j0ta
    channel_slug = "PASTE_CHANNEL_NAME_HERE"
    fetch_api(channel_slug)
