from imagekitio import ImageKit
import os
from functools import lru_cache


@lru_cache
def get_imagekit():
    return ImageKit(
        public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
        private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
        url_endpoint=os.getenv("IMAGEKIT_URL_ENDPOINT")
    )