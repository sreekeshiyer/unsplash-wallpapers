from get_wallpapers import all_wallpapers
import re
import requests
import os

# CHANGE THIS PATH FOR YOUR PC
# If you are using Windows, use \\ as demonstrated
# Make sure the path ends with a '/' or a '\\'

directory = "C:\\Users\\zenon\\Pictures\\wallpapers\\"


def save_wallpapers(directory):

    print("\n")
    for wallpaper in all_wallpapers:
        url = wallpaper['url']
        res = requests.get(url, allow_redirects=True)

        fm = re.findall("fm=.*?&", str(url))
        fmat = fm[0][3:-1]
        index = all_wallpapers.index(wallpaper) + 1

        if index == len(all_wallpapers):
            print('Done')

        file_name = 'wallpaper'+str(index)+'.'+str(fmat)

        try:
            open(directory+file_name, 'wb').write(res.content)

        except:
            cmd = "mkdir "+directory
            os.system(cmd)
            open(directory+file_name, 'wb').write(res.content)
