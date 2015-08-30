import time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 20      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()
print "strip initialize"

# Encode RGB values into a 32-byte color value
def encode(r, g, b):
	return strip.Color(r, g, b)

# Split a 32-byte merged color value into 8-byte RGB variables
def split(color):
	try: 
		return (uint8_t)(color>>16), (uint8_t)(color>>8), (uint8_t)(color>>0)
	except:
		return 0, 0, 0

# Wipe color across the display pixel by pixel
def colorWipe(color, wait_ms=10):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

# Fade from one color to another
def fade(color, n=10):
	re, ge, be = split(color)
	r, g, b = split(strip.getPixelColor(i))
	for i in range(strip.numPixels()):
		for i in range(n):
			strip.setPixelColor(r+(re-r)*i/n, g+(ge-g)*i/n, b+(be-b)*i/n)
			strip.show()