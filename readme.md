## Unsplash Wallpapers

### Installation

Clone this Repository.

```bash
git clone https://github.com/sreekeshiyer/unsplash-wallpapers.git
```

-   Create a Virtual Environment.

```bash
# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate
# macOS
python3 -m venv .venv
source .venv/bin/activate
# Windows
py -3 -m venv .venv
.venv\scripts\activate
```

-   Upgrade pip and install the requests module.

```
python -m pip install --upgrade pip
python -m pip install requests
```

-   Register yourself at <a href="https://unsplash.com/developers" target="_blank">Unsplash Developers</a> and get an Access Key. <br/>Add this Access Key in `config.py` -

```python
#config.py
API_KEY = 'ENTER_YOUR_KEY_HERE'
```

-   I like landscapes and cityscapes as my wallpapers. If you prefer anything else, add it to the search query in `get_wallpapers.py`

```python
# get_wallpapers.py
#line 5
landscapes_url = 'https://api.unsplash.com/search/photos?page=1&query=[ENTER_YOUR_QUERY_HERE]]&per_page=20&order_by=latest&orientation=landscape&color=blue'
```

<br/>
You can actually search this query on their website to see if you get what you expect. 
<br/> You can modify per_page to change the number of results. The current setup gives you 20+20 i.e roughly 37-38 wallpapers (the sponsored results are removed)
<br/>

-   In `main.py` change the directory variable to your preferred directory.

```python
#main.py
#line 8
directory = "C:\\Users\\<user_name>\\Pictures\\walls\\"
```

-   Run the file.

```bash
python main.py
```

-   Check your results in the specified directory.

![WallsFolder](https://res.cloudinary.com/zenon-cloudinary/image/upload/v1637754987/unsplash-wallpapers-assets/Screenshot_470_czewgr.png)

<br/>

-   Under Settings=> Personalization => Background, browse for this folder and select slideshow.

![Settings](https://res.cloudinary.com/zenon-cloudinary/image/upload/v1637755065/unsplash-wallpapers-assets/Screenshot_471_pinrnu.png)

That's finally it, your wallpaper slideshow is ready. All you have to do now is to run this script again and enter 2 as input to reset this folder with fresh new wallpapers next time :)
