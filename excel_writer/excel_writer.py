import pandas as pd
import os
from data_extraction.data_extraction import data_extraction
from config.config import Config
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment
from logger.logger import logger_setup

def excel_writer():
    # CREATE THE LOGGER SETUP
    logger = logger_setup()

    # CREATE THE FOLDER AND SAVE PATH
    os.makedirs(Config.OUTPUT, exist_ok=True)
    save_path = os.path.join(Config.OUTPUT, Config.FILENAME)

    books_data = data_extraction()

    if books_data is not None:
        # SAVE INTO DATA FRAME
        data_frame = pd.DataFrame(books_data)

        try:
            # SAVE INTO EXCEL
            with pd.ExcelWriter(save_path) as writer:
                data_frame.to_excel(writer, sheet_name=Config.SHEET_NAME, index=False)

                ##-- FORMATTING THE SUMMARY SHEET --##
                summary_sheet = writer.sheets[Config.SHEET_NAME]

                # FORMAT THE COLUMN HEADERS
                for cell in summary_sheet[1]:
                    cell.font = Font(bold=True)
                    cell.alignment = Alignment(horizontal='center')

                # FORMAT THE WIDTH
                for column_number, column in enumerate(summary_sheet.columns, start=1):
                    max_length = 0

                    # GET THE COLUMN LETTER
                    column_letter = get_column_letter(column_number)

                    for cell in column:
                        if cell.value is not None:

                            # WRAP THE CELLS
                            cell.alignment = Alignment(wrap_text=True)

                            # GET THE LENGTH OF THE CELL TEXT
                            length = len(str(cell.value))

                            # GET THE MAXIMUM LENGTH VALUE
                            max_length = max(max_length, length)

                    # ADJUST THE COLUM WIDTH
                    summary_sheet.column_dimensions[column_letter].width = min(max_length + 2, 50)
        except PermissionError:
            logger.error('Error saving please close the file and try again.')

    else:
        logger.info('Books data returns none.')

if __name__ == "__main__":
    excel_writer()