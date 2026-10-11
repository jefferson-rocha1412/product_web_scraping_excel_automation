# Product Web Scraper & Excel Automation

A Python automation project that scrapes book product information from [Books to Scrape](https://books.toscrape.com/) and exports the extracted data into a formatted Excel workbook.

## Project Overview

This project demonstrates a simple end-to-end automation workflow:

**Website → Requests → BeautifulSoup → Data Extraction → Pandas → Excel/OpenPyXL**

The scraper currently processes the first catalogue page and extracts:

- Product title
- Price
- Rating
- Availability
- Product URL

The extracted data is converted into a pandas DataFrame and written to an Excel workbook with basic formatting.

## Features

- Web scraping with `requests`
- HTML parsing with `BeautifulSoup`
- Extraction of product information
- Data processing with `pandas`
- Excel file creation with `pandas`
- Excel formatting with `openpyxl`
- Automatic creation of output and log folders
- Logging of program activity and errors
- Request timeout and HTTP error handling
- Permission error handling when the Excel file is open
- Configuration separated into a dedicated `Config` class
- Modular project structure

## Project Structure

```text
product_web_scraping_excel_automation/
│
├── config/
│   └── config.py
│
├── data_extraction/
│   └── data_extraction.py
│
├── excel_writer/
│   └── excel_writer.py
│
├── logger/
│   └── logger.py
│
├── scraper/
│   └── web_scraper.py
│
├── data/
│
├── log/
│
├── output/
│
├── main.py
├── .gitignore
└── README.md
```

> The `data/` folder is included in the project structure for future expansion. The current version does not require input files because the data comes directly from the website.

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- pandas
- OpenPyXL

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd product_web_scraping_excel_automation
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the main program:

```bash
python main.py
```

The program will:

1. Request the Books to Scrape webpage.
2. Retrieve the HTML content.
3. Parse the HTML using BeautifulSoup.
4. Extract the product information.
5. Store the extracted information in a dictionary.
6. Convert the data into a pandas DataFrame.
7. Create a formatted Excel workbook.
8. Save the result in the `output/` folder.
9. Record program activity and errors in the `log/` folder.

## Output

The generated Excel file is:

```text
output/books_data.xlsx
```

The workbook contains a `summary` worksheet with:

- Title
- Price
- Rating
- Availability
- URL

The header row is formatted in bold and centered, and column widths are automatically adjusted with a maximum width limit.

## Error Handling

The project includes handling for common request failures:

- Connection errors
- Request timeouts
- Other HTTP/request exceptions
- Excel permission errors when the output file is currently open

Errors and program activity are recorded in the log file.

## Current Scope

This is the first version of the project. It currently scrapes the first catalogue page only.

Possible future improvements include:

- Scraping multiple catalogue pages
- Converting prices into numeric values
- Converting ratings such as `One`, `Two`, `Three`, etc. into numeric ratings
- Converting relative product URLs into absolute URLs
- Adding more Excel formatting
- Adding data validation and stronger extraction checks
- Adding automated tests
- Adding command-line configuration
- Expanding the scraper into a reusable scraping framework

## Learning Goals

This project was created as part of my Python automation learning journey, with a focus on:

- Web scraping
- Data extraction
- pandas
- Excel automation
- OpenPyXL
- Modular Python projects
- Logging
- Error handling
- Git and GitHub

## Disclaimer

This project uses [Books to Scrape](https://books.toscrape.com/), a website created for practicing web scraping. It is intended for educational and portfolio purposes.
