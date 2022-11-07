import json
import os

from django.core.management.base import BaseCommand
from django.utils.text import slugify


class CustomBaseCommand(BaseCommand):
    help = "Base command to import data"

    def get_file_path(self, file_name):
        """returns absolute path of file

        Args:
            file_name (str): name of file

        Returns:
            str: absolute file_path
        """
        file_path = os.path.dirname(__file__)
        file_path += f"/data/{file_name}"

        return file_path
