import webbrowser
import requests
import os


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
    response = requests.get(url, allow_redirects=True)
    cd = response.headers.get("Content-Disposition", "")
    if "filename=" in cd:
        filename = cd.split("filename=")[-1].strip('"; ')
    else:
        filename = response.url.split("?")[0].rsplit("/", 1)[-1]

    # fallback на оригинальное имя, если в новом нет расширения
    original = url.rsplit("/", 1)[-1]
    
    if "." not in filename and "." in original:
        filename = original

    if directory:
        os.makedirs(directory, exist_ok=True, )
        filepath = os.path.join(directory, filename)
    else:
        filepath = filename

    with open(filepath, "wb") as f:
        f.write(response.content)

    return filepath


def open_url(url: str) -> None:
    """
    Opens a URL in the default web browser.

    Args:
        url (str): URL to open.
    """
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    webbrowser.open(url)
