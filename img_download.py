import cloudscraper
import shutil
from time import sleep

scraper = cloudscraper.create_scraper()

def img_dwnld(image_url, dirname): # credit of https://www.dev2qa.com/how-to-download-image-file-from-url-use-python-requests-or-wget-module/
    filename = image_url.split("/")[-1]

    # Open the url image, set stream to True, this will return the stream content.
    r = scraper.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        shutil.move(filename, dirname)

def dwnld_batch(img_url_list, dirname):
    for img in img_url_list:
            img_dwnld(img, dirname)
