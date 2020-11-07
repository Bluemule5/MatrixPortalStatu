# Quote board matrix display
# uses AdafruitIO to serve up a quote text feed and color feed
# random quotes are displayed, updates periodically to look for new quotes
# avoids repeating the same quote twice in a row

import time
import board
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal

# --- Display setup ---
matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=True)

# Create a new label with the color and text selected
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(0, (matrixportal.graphics.display.height // 2) - 1),
    scrolling=True,
)

# Static 'Connecting' Text
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(2, (matrixportal.graphics.display.height // 2) - 1),
)

SCROLL_DELAY = 0.02
UPDATE_DELAY = 600
UPDATE_DATA_INTERVAL = 1

# PATH to your JSON URL
JSON_URL = "http://your_url_here/"

matrixportal.set_text(" ", 1)
# data = matrixportal.network.fetch(JSON_URL)

def get_new_data(JSON_URL):
    return matrixportal.network.fetch(JSON_URL)

def get_new_json():
    data = get_new_data(JSON_URL)
    new_dict = data.json()
    return new_dict

def get_minute():
    new_time = str(time.localtime())
    new_time_split = new_time.split(",")
    minutes = new_time_split[4]
    minute = minutes.split('=')[1]
    return int(minute)

color_dict = get_new_json()
starting_minute = get_minute()

while True:
    current_minute = get_minute()
    time_diff = current_minute - starting_minute
    if time_diff >= UPDATE_DATA_INTERVAL or time_diff < 0:
        color_dict = get_new_json()
        starting_minute = get_minute()

    # Set the quote text
    matrixportal.set_text(color_dict["quote"])

    # Set the text color
    matrixportal.set_text_color(color_dict["color"])

    # Scroll it
    matrixportal.scroll_text(SCROLL_DELAY)
