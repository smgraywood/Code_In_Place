We’re going to start by writing a function called find_flames (in the file forest_fire.py) that highlights the areas where a forest fire is active. You’re given a satellite image of Greenland’s 2017 fires (photo credit: Stef Lhermitte, Delft University of Technology).

Your job is to detect all of the “sufficiently red” pixels in the image, which are indicative of where fires are burning in the image. As we did in class with the “redscreening” example, we consider a pixel “sufficiently red” if its red value is greater than or equal to the average of the pixel’s three RGB values times a constant INTENSITY_THRESHOLD. 

Recall the average of a pixel, which has red, green and blue values is:

average = (red + green + blue) / 3
When you detect a “sufficiently red” pixel in the original image, you set its red value to 255 and its green and blue values to 0. This will highlight the pixel by making it entirely red. For all other pixels (i.e., those that are not “sufficiently red”), you should convert them to their grayscale equivalent, so that we can more easily see where the fire is originating from. You can grayscale a pixel by summing together its red, green, and blue values and dividing by three (finding the average), and then setting the pixel’s red, green, and blue values to all have this same “average” value.

Two side by side photos of smoke plumes from above. The first photo is a normal image, taken from a satellite, and the right image is the same as the previous except it is black and white and the forest fires are highlighted in red.
Original forest fire image on left, and highlighted version of image on right.

Once you highlight the areas that are on fire in the image (and greyscale all the remaining pixels), you should see an image like that shown on the right in the figure. On the left side of the example image, we should the original image for comparison. 

Note: to make this algorithm work on different images of fire, select an appropriate INTENSITY_THRESHOLD value.

Problem written by Sonja Johnson-Yu.

-------

"""
This program highlights fires in an image by identifying pixels
whose red intensity is more than INTENSITY_THRESHOLD times the
average of the red, green, and blue values at a pixel. Those
"sufficiently red" pixels are then highlighted in the image
and other pixels are turned grey, by setting the pixel red,
green, and blue values to be all the same average value.
"""

from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.0
DEFAULT_FILE = 'images/greenland-fire.png'

def find_flames(filename):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(filename)
    # TODO: your code here
    return image
def get_avg_pixel(red, green, blue):
    avg = (red + green + blue) // 3
    return avg
def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()

    for pixel in image:
        average = get_avg_pixel(pixel.red, pixel.green, pixel.blue)
        pixel.red= average
        pixel.green= average
        pixel.blue = average




def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
