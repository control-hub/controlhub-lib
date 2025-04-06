import webbrowser
import requests
import os

def download(url: str, directory: str = 'download') -> None:
    """
    Downloads a file from the specified URL and saves it to the given directory.

    Args:
        url (str): URL of the file to download.
        directory (str): Directory to save the file. Defaults to 'download'.
    """
    if directory:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    request = requests.get(url)
    
    filename = url.split('/')[-1]
    filepath = os.path.join(directory, filename) if directory else filename
    
    with open(filepath, 'wb') as f:
        f.write(request.content)

def open_url(url: str) -> None:
    """
    Opens a URL in the default web browser.

    Args:
        url (str): URL to open.
    """
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
        
    webbrowser.open(url)