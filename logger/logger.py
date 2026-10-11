import logging
import os

from config.config import Config



def logger_setup():
    # CREATE THE FILE PATH FOLDER
    os.makedirs(Config.LOG_FOLDER, exist_ok=True)

    file_path = os.path.join(Config.LOG_FOLDER, Config.LOG_FILENAME)

    # LOGGING SET UP
    logging.basicConfig(
        filename=file_path,
        level=logging.INFO,
        format=Config.LOG_FORMAT
    )

    return logging.getLogger(__name__)