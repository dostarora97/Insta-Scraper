- Python 3.7.4 +
- Libs used
    - [Instalooter](https://github.com/althonos/InstaLooter.git)
    - [FastAPI](https://fastapi.tiangolo.com/)

# 1. Usage:

```
git clone https://github.com/dostarora97/Insta-Scraper.git
cd Insta-Scraper
pip install -r requirements.txt
```

## 1.1 Web UI:
```
python main.py
```
Browse to: `localhost:5000`

## 1.2 CommandLine:
```
cd utils
python scraper.py
```

# 2. Note:
- Only public accounts are accesible
- All data is saved in dir `Insta-Scraper/data/<username>`

# 3. To-Do:
- Cache System
- Private Accounts Scrape (with Login Creds)
- Data Download Option
- Regular Expression Search
- Transfer Captions through Web-Sockets
- Caption Scrape Progress Bar
- Select options for information to Scrape
- Add Welcome Message
- Use graphql to provide option selection