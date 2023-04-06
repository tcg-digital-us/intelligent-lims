import os, toml, re

class ConfigNotFoundError(Exception):
    pass

def _load_config():
    try:
        main_file_path = os.path.abspath(os.path.dirname(__file__))
        config_file_path = os.path.join(main_file_path, 'config.toml')
        with open(config_file_path) as f:
            config = toml.load(f)
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}
    
def base_urls():
    config = _load_config()
    base_urls = config.get('base_urls', None)
    if base_urls is None:
        raise ConfigNotFoundError("base_urls could not be found in config")
    return base_urls

def app_host():
    config = _load_config()
    app_host = config.get('app_host')

    # Regular expression pattern to match an IPv4 address followed by a colon and a port number
    pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)"

    match = re.match(pattern, app_host)

    if match:
        ip, port = match.groups()
        return ip, port
    else:
        raise ConfigNotFoundError("app_host could not be found in config")

