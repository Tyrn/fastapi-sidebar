import os.path
import markdown
import pout
from NetscapeBookmarksFileParser import *
from NetscapeBookmarksFileParser import parser


def openfile(filename):
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text)
    data = {"text": html}
    return data


def netsc_parse(file_name: str, log_name=""):
    with open(file_name) as file:
        ks = NetscapeBookmarksFile(file).parse()
        if log_name:
            with pout.tofile(log_name):
                pout.v(ks)
        return ks
