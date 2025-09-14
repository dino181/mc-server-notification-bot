import json
import os
from typing import Any
import shutil


def load_config(file_path: str = "./data/config.json") -> dict[str, Any]:
    if not os.path.exists(file_path):
        shutil.copy("./default_config.json", file_path)

    with open(file_path, "r") as file:
        config = json.load(file)

    return config


def save_config(config: dict[str, Any], file_path: str = "./data/config.json") -> bool:
    if not os.path.exists(file_path):
        return False

    try:
        with open(file_path, "w") as file:
            config = json.dump(config, file)
        return True

    except Exception:
        return False

