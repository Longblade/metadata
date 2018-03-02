"""Helps to understand how the data base is."""
import os.path
from collections import Counter


def save_xml(file, filename):
    """
    :param      file: file to save.

    :param      filename: name of xml file.

    :return:    has not.

    Saves the result of RAM → XML translation.
    """
    with open(filename, "wb") as f:
        f.write(file.toprettyxml(encoding="utf-8", indent="  "))

