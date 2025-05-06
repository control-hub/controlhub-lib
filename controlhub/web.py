import webbrowser
import os
import wget


def download(url: str, directory: str = "download") -> str:
    """
    Downloads a file from the specified URL and saves it to the given directory.
    Handles HTTP 302 redirects and returns the final path of the downloaded file.

    Args:
        url (str): URL of the file to download.
        directory (str): Directory to save the file. Defaults to 'download'.

    Returns:
        str: The final path of the downloaded file.
    """
    if len(directory) > 0 and directory[-1] not in ("\\", "/"):
        directory += "\\"

    os.makedirs(directory, exist_ok=True)

    final_path = wget.download(url, out=directory)
    return final_path


def open_url(url: str) -> None:
    """
    Opens a URL in the default web browser.

    Args:
        url (str): URL to open.
    """
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    webbrowser.open(url)
