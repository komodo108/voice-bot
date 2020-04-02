import json, random
from google_images_search import GoogleImagesSearch

MAX_SEARCH = 10

class ImageSearch():
    def __init__(self):
        with open("config/tokens.json", "r") as f:
            data = json.load(f)
            self.gis = GoogleImagesSearch(data['google_api'], data['google_cx'])

    def search(self, keyword):
        """ Search for an image """

        try:
            # Search for the image of space
            num = random.randint(0, MAX_SEARCH - 1)
            params = { 'q' : keyword, 'num' : MAX_SEARCH, 'safe': 'off' }
            self.gis.search(search_params=params)

            # Return the random result
            counter = 0
            for image in self.gis.results():
                if counter == num or counter == MAX_SEARCH - 1:
                    return image.url
                counter = counter + 1
            
        except Exception as e:
            print('[ERROR] ' + e)
            return None