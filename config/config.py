class Config:
    # BOOK DATA DICTIONARY SEETINGS
    TITLE = 'Title'
    PRICE = 'Price'
    RATING = 'Rating'
    AVAILABILITY = 'Availability'
    URL = 'Url'

    # EXCEL SETTINGS
    FILENAME = 'books_data.xlsx'
    SHEET_NAME = 'summary'

    # FOLDERS
    OUTPUT = 'output'

    # LOGGING SETTINGS
    LOG_FILENAME = 'log_results.log'
    LOG_FOLDER = 'log'
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

    # REQUESTS CONFIGURATION
    TIMEOUT = 10
    WEB_URL = 'https://books.toscrape.com/catalogue/page-1.html'

