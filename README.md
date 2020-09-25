- Python 3.7.4 +
- Libs used
    - [Instalooter](https://github.com/althonos/InstaLooter.git)
    - [FastAPI](https://fastapi.tiangolo.com/)

# 1. Usage:

```
git clone https://github.com/dostarora97/Insta-Scraper.git
cd Insta-Scraper
python3 -m pip install -r requirements.txt
```

## 1.1 Web UI:

### 1.1.1 Local Network
```
python3 main.py
```
Browse to: `localhost:5000`

### 1.1.2 Ngrok to Public URL
```
python3 ngrok.py
```
Browse to the `Public URL` displayed in console

## 1.2 CommandLine:
```
cd utils
python3 scraper.py
```

# 2. Note:
- Only public accounts are accessible
- **Only Captions** can be scraped as of now in [UI](https://github.com/dostarora97/Insta-Scraper#11-web-ui). Check [To-Do](https://github.com/dostarora97/Insta-Scraper#3-to-do)
- **All data** can be accessed through [CommandLine](https://github.com/dostarora97/Insta-Scraper#12-commandline)
- All the scraped data is saved in directory `Insta-Scraper/data/<username>`

# 3. To-Do:
## 3.1 Backend
- Cache System
- Private Accounts Scrape
- Extended Information Scrape (comments, likes, images, ..etc)
- Web-Socket media transfer
- Implement everything in GraphQl (specially useful for extended scrape option)
- Download Media as zip. Use [Snappy](https://github.com/google/snappy.git) for ultra-fast zipping.

## 3.2 UI
- Add Welcome Message
- Login creds form - For private accounts
- Select options for extended Information (comments, likes, images, ..etc)
- Media Scraping Progress Bar
- Data Download Option (with selective download)
- Regular Expression Search through captions
- Show approximate Download file size