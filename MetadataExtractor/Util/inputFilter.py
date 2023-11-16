import re
from tqdm import tqdm
import requests
import os, os.path
import uuid
import logging

log = logging.getLogger(__name__)
regex = re.compile(
    r"^(?:http|ftp)s?://"  # http:// or https://
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
    r"localhost|"  # localhost...
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
    r"(?::\d+)?"  # optional port
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


def isUrl(input):
    return re.match(regex, input) is not None


def getTmpFileName():
    tmp_dir = "./tmp"

    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    file = tmp_dir + "/" + str(uuid.uuid4())
    return file


def downloadFile(url):
    log.info("Downloading " + url)

    response = requests.get(url, stream=True)

    file = getTmpFileName()

    with open(file, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)

    log.info("Finished downloading " + url + " to " + file)

    return file
