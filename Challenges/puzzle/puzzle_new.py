# Source Generated with Decompyle++
# File: puzzle_new.pyc (Python 3.12)

import base64
import io
from urllib.parse import urlparse
import pygame
import random

def uri_to_pygame_image(uri):
    parsed_uri = urlparse(uri)
    base64_string = parsed_uri.path.split(',')[1]
    image_data = base64.b64decode(base64_string)
    image_stream = io.BytesIO(image_data)
    image = pygame.image.load(image_stream, 'png')
    return image

pygame.init()
screen = pygame.display.set_mode((640, 480))
image = uri_to_pygame_image(uri)
screen.blit(image, (0, 0))
piece_width = 120
piece_height = 120
(image_width, image_height) = image.get_size()
num_rows = image_height // piece_height
num_cols = image_width // piece_width
pieces = []
# WARNING: Decompyle incomplete