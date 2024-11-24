# InstaPYDL

A Python package for downloading Instagram Reels and retrieving metadata. With **InstaPYDL**, you can validate Instagram Reel URLs, extract metadata, and download videos easily.

---

## Features

- **Validate URLs**: Ensures the provided URL is a valid Instagram Reel link.
- **Extract Metadata**: Scrapes metadata of the Instagram Reel, including the video URL.
- **Download Videos**: Downloads Instagram Reel videos directly to your system.

---

## Requirements

- Python 3.8 or higher
- The following Python libraries:
  - `httpx`

Install the required dependency with:

```bash
pip install httpx
```

## Installation

pip install instapydl

## Usage

You can create a Reel object by passing a valid Instagram Reel URL.

```py
from instapydl import Reel

reel = Reel("https://www.instagram.com/reel/shortcode/")


# Scrape and get metadata of that post
metadata = reel.scrape_post()
print(metadata)


# Download the video to the default path ("video.mp4")
reel.download()

# Download the video to a custom path
reel.download("C:/foo.mp4")
```

## Exceptions

```js
InstagramDL_InvalidURL: Raised when the URL provided is not valid.

InstagramDL_DownloadException: Raised when there is an error during the download process.

InstagramDL_PathNotFound: Raised when the specified path for saving the video is not found.

InstagramDL_UnknownException: Raised for unknown errors.
```

## Example workflow

```py
from instapydl import Reel

try: # Initialize Reel object with a valid Instagram Reel URL
    reel = Reel("https://www.instagram.com/reels/DCeuaixC0z4//")

        # Print the shortcode of the reel
        print("Shortcode:", reel.shortcode())

        # Scrape metadata
        metadata = reel.scrape_post()
        print("Reel Metadata:", metadata)

        # Download the reel to the current directory
        reel.download()
except InstagramDL_InvalidURL as e:
    print(f"Invalid URL: {e}")

except InstagramDL_UnknownException as e:
print(f"An unknown error occurred: {e}")
```

## Notes

- Ensure the URL you provide is accessible and works in a browser.
- The package currently supports only public Instagram posts.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Suggestions? Corrections? Pull requests?

Yes please!

### Acknowledgements

    Inspired by Instagram's public API structure and designed for ease of use.
