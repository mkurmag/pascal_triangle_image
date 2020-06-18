from PIL import Image, ImageColor

BLACK = ImageColor.getcolor('black', '1')
WHITE = ImageColor.getcolor('white', '1')


def draw_line(value, x, image):
    """
    Draw vertial line at x
    """
    bits = reversed(bin(value))

    for bit_index, bit_value in enumerate(bits):
        if bit_value == '1':
            image.putpixel((x, bit_index), BLACK)


def draw(values):
    """
    Draw image from list of values
    """
    width = len(values)
    hight = len(bin(max(values)))
    image = Image.new('1', (width, hight), WHITE)  # '1' - black&white image

    for index, val in enumerate(values):
        draw_line(val, index, image)

    image = image.transpose(Image.FLIP_TOP_BOTTOM)

    image_big = image.resize((width*50, hight*50))
    image.save('out.png')
    image_big.save('out_big.png')


if __name__ == "__main__":
    draw([1, 2, 5])
