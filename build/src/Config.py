# file: config.py
# author: Anthony Mesa

import os, toml, re
from pydantic import BaseModel, ValidationError
from typing import Tuple

class ConfigLoadError(Exception):
    pass

class Config(BaseModel):
    app_host: str
    base_urls: dict

def _load_config() -> Config:
    """Load config.toml and make it available

    Returns:
        Config: The configuration object.

    Raises:
        ConfigLoadError
    """

    main_file_path = os.path.abspath(os.path.dirname(__file__))
    config_file_path = os.path.join(main_file_path, 'config.toml')

    try:
        with open(config_file_path, "r") as f:
            toml_data = toml.load(f)
    except FileNotFoundError as e:
        raise ConfigLoadError(f"Error loading config file: {e}")

    try:
        config = Config(**toml_data)
    except ValidationError as e:
        raise ConfigLoadError(f"Error decoding TOML data from config: {e}")

    return config

class ConfigGetError(Exception):
    pass

def base_urls() -> dict:
    """Get the list of base urls from the config

    Returns:
        dict: base url id's mapped to their actual urls

    Raises:
        ConfigGetError
    """

    try:
        config = _load_config()
    except ConfigLoadError as e:
        raise ConfigGetError(f"Could not get base_urls from config: {e}")
    
    return config.base_urls

def app_host() -> Tuple[str, str]:
    """Get the app host ip address and port from the config

    Returns:
        str: The ip address.
        str: The port.

    Raises:
        ConfigGetError
    """

    try:
        config = _load_config()
    except ConfigLoadError as e:
        raise ConfigGetError(f"Could not get app_host from config: {e}")

    # Regular expression pattern to match an IPv4 address followed by a colon and a port number
    pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)"

    match = re.match(pattern, config.app_host)

    if match:
        ip, port = match.groups()
        return ip, port
    else:
        raise ConfigGetError(f"app_host in config is malformed: {e}")

