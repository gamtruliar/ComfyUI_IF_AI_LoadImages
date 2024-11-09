import os
import glob
import shutil
import sys
import folder_paths

from .IFLoadImagesSNode import IFLoadImagess




NODE_CLASS_MAPPINGS = {
    "IF_LoadImagesS": IFLoadImagess,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IF_LoadImagesS": "IF Load Images 🖼️",
}

WEB_DIRECTORY = "./web"
__all__ = [
    "NODE_CLASS_MAPPINGS", 
    "NODE_DISPLAY_NAME_MAPPINGS", 
    "WEB_DIRECTORY", 
    ]
