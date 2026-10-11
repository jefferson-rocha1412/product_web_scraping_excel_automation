import requests
from config.config import Config
from logger.logger import logger_setup

def web_scraping():
    # CREATE THE LOGGER OBJECT
    logger = logger_setup()

    # START OF WEB SCRAPING
    logger.info('Web scraping started.')

    try:
        response = requests.get(Config.WEB_URL, timeout=Config.TIMEOUT)
        response.raise_for_status()
        html = response.text

        # RETURN THE HTML
        return html
    
    except requests.exceptions.ConnectionError:
        logger.error(F'Requests failed to connect to {Config.WEB_URL}.')
        return None
    except requests.exceptions.Timeout:
        logger.error(f'Requests failed to connect to {Config.WEB_URL}.'
                     f'Timeout reached {Config.TIMEOUT} seconds.')
        return None
    except requests.exceptions.RequestException as e:
        logger.error(e)
        return None

if __name__ == "__main__":
    web_scraping()