import uvicorn

from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import datetime
from utils.scraper import Insta_Scraper
from pathlib import Path
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

data_path = Path("./data")

scraper = Insta_Scraper(data_path)

def filter_data(scraped_data: list):
    filtered_data = list()
    for data in scraped_data:
        caption_edges = data["edge_media_to_caption"]["edges"]
        if len(caption_edges):
            caption = caption_edges[0]["node"]["text"]
        else:
            caption = ""
        filtered_data.append( {
            "id" : data["id"],
            "caption" : caption,
            "shortcode" : data["shortcode"],
            "display_url" : data["display_url"],
            "timestamp" : data["taken_at_timestamp"]
        })
    return filtered_data


class Scraped_Data(BaseModel):
    error: str = ""
    data: list = list()
    count: int = 0

class User(BaseModel):
    username: str
    status: Optional[bool] = None
    scraped_data: Optional[Scraped_Data] = None

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/scrape")
def scrape(user: User):
    scraped_user = User(
        username = user.username
    )

    try:
        scraped_medias = scraper.scrape(user.username)
        captionFilterData = filter_data(scraped_medias[0])
        captionsFilterFile_name = "{}-captionsFilter.json".format(user.username)
        captionsFilterFile_path = scraper.scrape_dir.joinpath(
            "{}/{}".format(user.username, captionsFilterFile_name))

        with open(captionsFilterFile_path, "w", encoding="utf-8") as captionsFilterFile:
            json.dump(captionFilterData, captionsFilterFile, indent=2)
    except Exception as err:
        print(err)
        scraped_user.status = False
        scraped_user.scraped_data = Scraped_Data()
    else:
        scraped_user.status = scraped_medias[1]
        scraped_user.scraped_data = Scraped_Data(
            data = captionFilterData,
            count = len(scraped_medias[0]),
            error = scraped_medias[2])
    finally:
        return scraped_user

def run():
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)

if __name__ == "__main__":
    run()