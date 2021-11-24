import requests
from config import API_KEY as api_key

## I've used landscapes and cityscapes in searches here, you could use whatever you want. Simply change the query="" in the URLs
landscapes_url = 'https://api.unsplash.com/search/photos?page=1&query=landscape&per_page=20&order_by=latest&orientation=landscape&color=blue'
cityscapes_url = 'https://api.unsplash.com/search/photos?page=1&query=cityscapes&per_page=20&orientation=landscape'
headers = {
    "Accept-Version": "v1",
    "Authorization": "Client-ID "+api_key
}

landscapes_res = requests.get(landscapes_url, headers=headers)
cityscapes_res = requests.get(cityscapes_url, headers=headers)

landscapes = landscapes_res.json()
cityscapes = cityscapes_res.json()

list_of_wallpapers = []
all_walls = [landscapes, cityscapes]


for collection in all_walls:
    for item in collection['results']:
        wallpaper_obj = {}
        wallpaper_obj['sponsorship'] = item['sponsorship']
        wallpaper_obj['url'] = item['urls']['full']
        list_of_wallpapers.append(wallpaper_obj)

results = filter(lambda item: item['sponsorship'] == None, list_of_wallpapers)
all_wallpapers = list(results)
