import io
import os
import urllib
from os import mkdir
from os.path import exists
from urllib import parse, request

import requests

from src.configuration import CONFIG


class WebImage:

    @staticmethod
    def get(url: str):
        filename = urllib.parse.urlencode({'image': url})
        img_path = CONFIG.get('CACHE_PATH') + '/img'
        if not (exists(img_path)):
            mkdir(img_path)
        fpath = (img_path + '/' + filename)
        if exists(fpath):
            return io.BytesIO(open(fpath, 'rb').read())
        else:
            with request.urlopen(url) as u:
                data = u.read()
            f = open(img_path + '/' + filename, 'wb')

            f.write(data)
            f.close()
            return io.BytesIO(data)