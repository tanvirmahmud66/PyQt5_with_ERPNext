# services/login_api.py
import requests

class LoginAPI:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def login(self, username, password):
        url = f"{self.base_url}/api/method/login"
        try:
            res = self.session.post(url, data={"usr": username, "pwd": password})
            res.raise_for_status()
            return {
                "success": True,
                "sid": self.session.cookies.get("sid"),
                "session": self.session  # 🔁 pass session forward
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
