# UniProt_Web_Scraper

UniProt Web Scraper is a Python library for scraping protein information from the UniProt website. UniProt is a widely used protein database that contains a vast amount of protein sequences, annotations, and other relevant information.

This library provides a convenient way to programmatically access and extract data from UniProt, allowing researchers, bioinformaticians, and developers to automate the retrieval of protein information for their projects.

## Prerequisites

- Python 3.x
- Selenium library (`pip install selenium`)
- Chrome WebDriver

## Setup

1. Install the required Python packages by running the following command:
   ```pip install selenium pyperclip```
   
2. Download and install the Chrome WebDriver from the official website: [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/)

3. Set the path to the Chrome WebDriver executable in your system's PATH variable.

## Usage

1. Modify the script to specify the entry ID of the UniProt page you want to scrape:
```python
entry_id = "P12345"  # Replace with the desired UniProt entry ID
```

2. Uncomment the line `# chrome_options.add_argument("--headless")` if you want to run the script in headless mode without displaying the browser window.

3. Run the script using the following command:

4. The script will navigate to the UniProt webpage, extract the sequence, mass, and function information, and print the results.

## Notes

- The script uses the `pyperclip` library to copy the sequence to the clipboard. Make sure you have a compatible clipboard manager installed.

- By default, the script uses the Chrome browser. If you prefer a different browser, modify the code accordingly.

- Remember to comply with the terms of service and usage policies of the website you are scraping.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
