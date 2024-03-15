# are.na book downloader

## Introduction
This is a Python tool that allows you to group download PDF files from an are.na channel using the are.na API. More information about the are.na API can be found [here](https://dev.are.na/documentation/channels).

## Requirements
To use this tool, you need to have Python installed on your system. Additionally, the following Python packages are required:
- requests

You can install these dependencies using the following command:

```pip install -r requirements.txt```


## Usage
1. Clone or download this repository to your local machine.
2. Install the required dependencies by running the command mentioned above.
3. Open the Python script `app.py`.
4. Replace the `channel_slug` variable with the slug of the are.na channel you want to download PDFs from.
5. Run the Python script.

## How it Works
The script fetches content from the specified are.na channel using the are.na API. It then iterates through the channel contents, identifies PDF attachments, and downloads them to a local folder named `downloaded_files`. The filenames are generated based on the title of the content block on are.na.

## Example
```python
if __name__ == "__main__":
    # Example usage:
    # Example channel with a lot of PDF's https://www.are.na/mo-mcknight/texts-seb9ve3j0ta
    # channel_slug = texts-seb9ve3j0ta
    channel_slug = "texts-seb9ve3j0ta"
    fetch_api(channel_slug)
```

Replace the `channel_slug` with the slug of your desired are.na channel. Run the script, and it will download the PDF files to the specified folder.