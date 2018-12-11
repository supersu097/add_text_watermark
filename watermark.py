from PIL import Image, ImageDraw, ImageFont
import setting
import os
import argparse

def main(image_files, do_override):
    for image_file in image_files:
        img = Image.open(image_file)
        size = img.size
        draw = ImageDraw.Draw(img)
        font_path = os.path.dirname(os.path.abspath(__file__))
        ttfront = ImageFont.truetype(os.path.join(font_path, 'arial.ttf'), 35)
        text = setting.text_watermark
        x = (size[0] - len(text)*18)
        y = (size[1] - 45)
        # rgb color reference
        # https://blog.csdn.net/daichanglin/article/details/1563299
        draw.text((x,y),text,fill=(192,192,192), font=ttfront)
        if do_override:
            img.save(image_file)
        else:
            split_text = os.path.splitext(image_file)
            filename = split_text[0]
            file_suffix = split_text[1]
            img.save(filename + '_new' + file_suffix)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Add text watermark on the bottom right of the image.')

    parser.add_argument(
        '-i', '--images',
        required=True,
        nargs='+',
        help='The image file you wanna add text watermark(support multiple files)')
    parser.add_argument(
        '-o', '--override',
        action='store_true',
        help="Pass this option which means you want to override the original image file")
    args = parser.parse_args()
    main(args.images, args.override)
