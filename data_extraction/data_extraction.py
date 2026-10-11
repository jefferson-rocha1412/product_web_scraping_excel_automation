from bs4 import BeautifulSoup
from scraper.web_scraper import web_scraping
from config.config import Config
from logger.logger import logger_setup

def data_extraction():
    # CREATE THE LOGGER OBJECT
    logger = logger_setup()

    # CREATE THE EMPTY LIST NEEDED
    titles = []
    prices = []
    ratings = []
    stocks = []
    urls = []

    web_html = web_scraping()

    if web_html is not None:
        # CREATE THE SOUP OBJECT
        soup = BeautifulSoup(web_html, 'html.parser')

        # CREATE THE BOOKS CONTAINER
        books = soup.find_all('article', class_="product_pod")

        for book in books:
            # FIND THE TITLE
            title_heading = book.find('h3')
            title_link = title_heading.find('a')
            title = title_link.get('title')
            titles.append(title)

            # FIND THE PRICE
            price_element = book.find('p', class_='price_color')
            price = price_element.get_text(strip=True)
            prices.append(price)

            # FIND THE RATING
            rating_element = book.find('p', class_='star-rating')
            rating = rating_element.get('class')[1]
            ratings.append(rating)

            # FIND THE STOCK AVAILABILITY
            stock_element = book.find('p', class_='instock availability')
            stock = stock_element.get_text(strip=True)
            stocks.append(stock)

            # FIND THE URL
            url = title_link.get('href')
            urls.append(url)

        # CREATE A DICTIONARY
        books_data = {
            Config.TITLE:titles,
            Config.PRICE:prices,
            Config.RATING:ratings,
            Config.AVAILABILITY:stocks,
            Config.URL:urls}

        return books_data

    else:
        logger.info('Data extracted returns none.')
        return None

if __name__ == "__main__":
    data_extraction()