import io
import requests

from PIL import Image, ImageDraw, ImageFont
from flask import make_response


def create_background(color: str):
    """
    Function Create image of given color
    """
    img = Image.new("RGB", (3000, 2005), color=color)
    return img


class ImageProcessing:
    """
    Class Processes the image and make response
    """

    def __init__(self, filepath: str, text: str, size: int, color: str):
        try:
            self.image = Image.open(filepath)
        except AttributeError:
            self.image = filepath
        except FileNotFoundError:
            res = requests.get(filepath, stream=True)
            res.raw.decode_content = True
            self.image = Image.open(res.raw)
        self.font = ImageFont.truetype("font/AlternateGotNo2D.otf", size)
        self.text = self.wrap_text(text)
        self.color = color

    def wrap_text(self, text):
        new_text = ""
        new_sentence = ""
        for word in text.split(" "):
            delim = " " if new_sentence != "" else ""
            new_sentence = new_sentence + delim + word
            if len(new_sentence) > 25:
                new_text += "\n" + new_sentence
                new_sentence = ""
        new_text += "\n" + new_sentence
        return new_text

    def texted_image(self):
        texted_img = self.image
        darw = ImageDraw.Draw(texted_img)
        w, h = texted_img.size
        x, y = w / 2, h / 2
        w_, h_ = darw.multiline_textsize(self.text, font=self.font, spacing=3)
        x -= w_ / 2
        y -= h_ / 2
        darw.multiline_text(
            align="center", xy=(x, y), text=self.text, fill=self.color, font=self.font
        )

        return texted_img

    def response(self):
        buffer = io.BytesIO()
        self.texted_image().save(buffer, format="png")
        buffer.seek(0)
        res = make_response(buffer.getvalue())
        res.mimetype = "image/png"
        return res


def colored_back(b_color: str, text: str, f_color: str, font_size=300):
    """
    Function return the response of text added image of given color
    """
    return ImageProcessing(
        create_background(b_color), text, size=font_size, color=f_color
    ).response()


def image_back(path: str, text: str, color: str, font_size=300):
    """
    Function return the response of text added given image
    """
    return ImageProcessing(path, text, size=font_size, color=color).response()


def in_build_image_back(name: str, text: str, color: str, font_size=300):
    """
    Function similar to image_back specially for build in images
    """
    return ImageProcessing(
        f"images/{name}.jpg", text, size=font_size, color=color
    ).response()