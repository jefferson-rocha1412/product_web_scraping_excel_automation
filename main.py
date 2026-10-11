# MAIN PROGRAM

from excel_writer.excel_writer import excel_writer
from logger.logger import logger_setup

def main():
    # CREATE THE LOGGER OBJECT
    logger = logger_setup()

    logger.info('Main program has started.')

    try:
        # CALL THE EXCEL WRITER MODULE
        excel_writer()
    except Exception as e:
        logger.error(f'Main program finished with error.'
                    f'Error details: {e}')

if __name__ == "__main__":
    main()