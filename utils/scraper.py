# '''instaLooter user <username> insta_scrape_dwnld/instalooter --dump-only --extended-dump'''

import json
from instalooter.looters import ProfileLooter
from pathlib import Path
from os.path import realpath
from sys import stdout

class Insta_Scraper():
    def __init__(self, dir=None):
        self.scrape_dir = Path("instalooter") if dir is None else Path(dir)
        self.scrape_dir = Path(realpath(self.scrape_dir)).absolute()
        self.scrape_dir.mkdir(
            parents = True,
            exist_ok = True
        )
    
    def scrape(self, username: str):
        all_medias = list()

        try:
            print("Username: `{}`".format(username))

            user_dir = self.scrape_dir.joinpath(username)
            user_dir.mkdir(parents=True, exist_ok=True)
            temp_dir = user_dir.joinpath("temp")
            temp_dir.mkdir(parents=True, exist_ok=True)

            print("Output Dir: `{}`".format(user_dir.absolute()))

            medias = ProfileLooter(username).medias()
            total = medias.__length_hint__()
            print("Total Media Count: {}".format(total))
            
            count = 0
            for media in medias:
                count += 1
                print("Scraped Count: {}/{}".format(count, total), end="\r")
                all_medias.append(media)
                temp_filename = "{id}_{shortcode}.json".format_map(media)
                temp_filepath = temp_dir.joinpath(temp_filename)
                with open(temp_filepath, "w", encoding='utf-8') as file:
                    json.dump(media, file, indent=2)

            all_medias_filename = "{}.json".format(username)
            all_medias_filepath = user_dir.joinpath(all_medias_filename)
            with open(all_medias_filepath, "w", encoding="utf-8") as file:
                json.dump(all_medias, file, indent=2)
        
            status = True
            error = ""
        except Exception as err:
            status = False
            error = str(err)
        finally:
            print()
            stdout.flush()
            return (all_medias, status, error)

if __name__ == "__main__":
    username = input("Enter a Username: ")
    print(
        json.dumps(
            Insta_Scraper("../data").scrape(username)[0],
            indent = 2
        )
    )