import requests
from urllib.parse import quote

class JournalEntryAPI:
    def __init__(self, base_url, sid=None):
        self.base_url = base_url.rstrip("/")
        self.sid = sid

    def get_journal_entries(self):
        doctype = quote("Journal Entry")
        url = f"{self.base_url}/api/resource/{doctype}"
        headers = {}
        cookies = {}

        if self.sid:
            cookies["sid"] = self.sid

        try:
            response = requests.get(url, headers=headers, cookies=cookies)
            response.raise_for_status()
            data = response.json()
            return {
                "success": True,
                "data": data.get("data", [])
            }
        except requests.exceptions.HTTPError as http_err:
            return {"success": False, "error": f"HTTP error occurred: {http_err}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
