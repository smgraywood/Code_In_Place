Write a program that asks the user to enter an image file, loads that file and applies the “Code in Place” filter.

Photo of Stanford Main Quad on a nice day.
Same photo as previous but tinted pinkish purple.
To apply the Code in Place filter, you are going to change every pixel to have the following new red, green and blue values, based off the pixels old red, green and blue values:

new red value = old red value * 1.5
new green value = old green value * 0.7
new blue value = old blue value * 1.5
Problem written by Chris Piech. Inspired by image library and examples from Nick Parlante.

------

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    # Apply the filter
    for pixel in image:
        pixel.red = pixel.red * 1.5
        pixel.green = pixel.green * 0.7
        pixel.blue = pixel.blue * 1.5
    # TODO: your code here


    # Show the image after the transform
    image.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
