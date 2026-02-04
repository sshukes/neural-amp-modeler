# File: parameters.py
# Created Date: Tuesday March 11th 2025
# Author: Steven Atkinson (steven@atkinson.mn)

import json
from pathlib import Path
from typing import Optional

_PARAMETERS_DIR = Path.home() / ".nam" / "train_gui"
_PARAMETERS_JSON_PATH = _PARAMETERS_DIR / "parameters.json"
_LAST_PARAMETER_FILE_KEY = "last_parameter_file"


def get_last_parameter_file() -> Optional[Path]:
    s = _get_settings()
    last_path = s.get(_LAST_PARAMETER_FILE_KEY)
    if last_path is None:
        return None
    assert isinstance(last_path, str)
    return Path(last_path)


def set_last_parameter_file(path: Path):
    s = _get_settings()
    s[_LAST_PARAMETER_FILE_KEY] = str(path)
    _write_settings(s)


def _get_settings() -> dict:
    """
    Make sure that parameters.json exists; if it does, then read it. If not, empty dict.
    """
    if not _PARAMETERS_JSON_PATH.exists():
        return dict()
    else:
        with open(_PARAMETERS_JSON_PATH, "r") as fp:
            return json.load(fp)


class _WriteSettings(object):
    def __init__(self):
        self._oserror = False

    def __call__(self, *args, **kwargs):
        if self._oserror:
            return
        try:
            return _write_settings_unsafe(*args, **kwargs)
        except OSError as e:
            if "Read-only filesystem" in str(e):
                print(
                    "Failed to write parameters settings--check that your user data "
                    "directory is writable."
                )
                self._oserror = True
            else:
                raise e


_write_settings = _WriteSettings()


def _write_settings_unsafe(obj: dict):
    _PARAMETERS_DIR.mkdir(parents=True, exist_ok=True)
    with open(_PARAMETERS_JSON_PATH, "w") as fp:
        json.dump(obj, fp, indent=4)
