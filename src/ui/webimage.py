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
        if url == '' or url is None:
            no_image_img = CONFIG.get('BASE_APP_PATH') + '/ui/no_image.jpg'
            return io.BytesIO(open(no_image_img, 'rb').read())
        else:
            filename = hash(urllib.parse.urlencode({'image': url}))
        img_path = CONFIG.get('CACHE_PATH') + '/img'
        if not (exists(img_path)):
            mkdir(img_path)
        fpath = (img_path + '/' + str(filename))
        if exists(fpath):
            return io.BytesIO(open(fpath, 'rb').read())
        else:
            with request.urlopen(url) as u:
                data = u.read()
            f = open(fpath, 'wb')

            f.write(data)
            f.close()
            return io.BytesIO(data)