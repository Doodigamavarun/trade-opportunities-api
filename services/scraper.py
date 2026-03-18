import requests

def get_market_data(sector: str):
    try:
        url = f"https://api.duckduckgo.com/?q={sector}+india+market+news&format=json"
        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        topics = data.get("RelatedTopics", [])

        results = []
        for item in topics[:5]:
            if "Text" in item:
                results.append(item["Text"])

        return results

    except Exception:
        return None
