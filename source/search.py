import json
from google_images_search import GoogleImagesSearch

class ImageSearch():
    def __init__(self):
        with open("config/tokens.json", "r") as f:
            data = json.load(f)
            self.gis = GoogleImagesSearch(data['google_api'], data['google_cx'])

    def search(self, keyword):
        """ Search for an image """

        try:
            params = { 'q' : keyword, 'num' : 1, 'safe': 'off' }
            self.gis.search(search_params=params)
            for image in self.gis.results():
                return image.url
        except Exception as e:
            return None