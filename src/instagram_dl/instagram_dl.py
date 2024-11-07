import httpx
import json
import re
import pathlib
from typing import Dict
from urllib.parse import quote

INSTAGRAM_DOCUMENT_ID = "8845758582119845" #constant ID used for identifying instagram posts via shortcodes.

class InstagramDL_InvalidURL(Exception):
    pass

class InstagramDL_DownloadException(Exception):
    pass

class InstagramDL_PathNotFound(Exception):
    pass

class InstagramDL_UnknownException(Exception):
    pass

class Reel:
    """
    Reel class used to get metadata for of the Instagram post.
    
    Functions:
        download
        get_bytes
    """
    
    def __init__(self, URL: str):
        self.URL : str = URL
        self.__validate_url()


    @property
    def shortcode(self):
        if "http" in self.URL:
            return self.URL.split("/reel/")[-1].split("/")[0]
        else:
            raise InstagramDL_UnknownException("Couldn't retrieve shortcode from the URL, make sure your link works in browser as well.")

        
    def __validate_url(self):
        """Validates that the URL is a proper URL."""
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        if bool(re.match(regex, self.URL)):
            pattern = re.compile(r'(http:|https:\/\/)?(www\.)?instagram\.com\/reel\/([a-zA-Z0-9-_]{5,15})(\/)?(\?.*)?')
            if pattern.match(self.URL):
                return True
            else:
                raise InstagramDL_InvalidURL("Parameter provided is not an Instagram URL.") 
        else:
            raise InstagramDL_InvalidURL("Parameter provided is not a proper URL.") 
        
    def __str__(self):
        return str(self.URL)
    
    def scrape_post(self):
        """Scrape single Instagram post data."""
        
        variables = quote(json.dumps({
        'shortcode':self.shortcode,
        'fetch_tagged_user_count':None,
        'hoisted_comment_id':None,
        'hoisted_reply_id':None
        }, 
        separators=(',', ':')))
        
        body = f"variables={variables}&doc_id={INSTAGRAM_DOCUMENT_ID}"
        url = "https://www.instagram.com/graphql/query"
        result = httpx.post(
            url=url,
            headers={"content-type": "application/x-www-form-urlencoded"},
            data=body
        )
        data = json.loads(result.content)
        return data["data"]["xdt_shortcode_media"]
    
    def download(self, path: pathlib.Path = pathlib.Path("video.mp4")) -> None:
        """Downloads the Reel post and saves it to the specified path."""
        
        if not path.parent.exists(): path = pathlib.Path.cwd() / path
        
        metadata = self.scrape_post()
        video_url = metadata["video_url"]
        with httpx.Client() as client:
            response = client.get(video_url, stream=True)
            if response.status_code == 200:
                path.parent.mkdir(parents=True, exist_ok=True)
                
                with path.open('wb') as f:
                    for chunk in response.iter_bytes():
                        f.write(chunk)
                print(f"Download successful! File saved as {path}")
            else:
                print(f"Failed to download file. Status code: {response.status_code}")
        
        
        
        
    