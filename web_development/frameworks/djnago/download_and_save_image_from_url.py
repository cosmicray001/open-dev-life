import logging

import requests
from hashlib import sha256
from datetime import datetime

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

logger = logging.getLogger(__name__)


@staticmethod
def get_image_object_from_url(image_url):
    try:
        response = requests.get(image_url, allow_redirects=False)
        seed_str = response.url + str(datetime.now())
        unique_name = sha256(seed_str.encode()).hexdigest()
        unique_name = unique_name[:20]
        image_path = f'media/content_dir/{unique_name}.png'
        image = default_storage.save(image_path, ContentFile(response.content))
        return image
    except Exception as ex:
        logger.error(str(ex), exc_info=True)
    return None
