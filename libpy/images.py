# http://stackoverflow.com/questions/10657383/stitching-photos-together
from PIL import Image

def merge_images(file1, file2, file3):
    """Merge two images into one, displayed side by side
    :param file1: path to first input image file
    :param file2: path to second input image file
    :param file3: path to output image file
    :return: the merged Image object
    """
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))

    result.save (file3)
