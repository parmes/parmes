# http://stackoverflow.com/questions/10657383/stitching-photos-together
from PIL import Image

def merge_images(file1, file2, file3):
    """Merge two images into one, displayed side by side
    :param file1: path to first input image file
    :param file2: path to second input image file
    :param file3: path to output image file
    """
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height), color=(255,255,255,255))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))

    result.save (file3)

def merge_horizontal(input_paths, outpath):
    """Horizontally merge several images into one, displayed side by side
    :param input_paths: list of path to input image files
    :param outpath: path to output image file
    """
    result_width = 0
    result_height = 0

    for path in input_paths:
      image = Image.open(path)
      (width, height) = image.size
      result_width += width
      result_height = max(result_height, height)

    result = Image.new('RGB', (result_width, result_height), color=(255,255,255,255))

    xpos = 0
    for path in input_paths:
      image = Image.open(path)
      (width, height) = image.size
      result.paste(im=image, box=(xpos, 0))
      xpos += width

    result.save (outpath)
