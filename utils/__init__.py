from pyglet.image import load

def load_and_resize_image(image_path):
    """
    Load an image and resize it to 40x40 pixels.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    Image: The loaded and resized image.
    """
    image = load(image_path)
    image = image.get_texture()
    image.width = 40
    image.height = 40
    return image