from core.config import settings
import requests


class TMDB:
    ROOT_URL = "https://api.themoviedb.org/3/"

    def __init__(self, id: int):
        url = f"{self.ROOT_URL}movie/{id}?api_key={settings.API_KEY}"
        response = requests.request("GET", url)

        self.movie = response.json()

    def __str__(self) -> str:
        return self.movie["original_title"]
