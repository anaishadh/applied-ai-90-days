import requests

def search_web(query: str, num_results: int = 5):
    url = "https://duckduckgo.com/html/"
    params = {
        "q": query
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post(url, data=params, headers=headers)
    response.raise_for_status()

    return response.text[:5000]  # raw HTML (intentionally ugly)
