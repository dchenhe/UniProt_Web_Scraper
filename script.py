'''
Copyright 2023 Dongchen_HE (dc23.he@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip

chrome_options = Options()
# chrome_options.add_argument("--headless")  # Enable headless mode to run without displaying the browser window
driver = webdriver.Chrome(options=chrome_options)

def get_info(entry_id):
    # Construct the UniProt URL for the given entry ID
    url = f"https://www.uniprot.org/uniprot/{entry_id}/entry#sequences"

    # Send a request to the webpage
    driver.get(url)

    # Find and click the "Copy Sequence" button
    copy_button = driver.find_element(By.XPATH, '//button[@class="button primary tertiary" and contains(text(), "Copy sequence")]')
    copy_button.click()

    # Wait for the sequence to be copied and retrieve it from the clipboard
    driver.implicitly_wait(1)
    copied_sequence = pyperclip.paste()

    # Extract mass and function information
    mass = driver.find_element(By.XPATH, '//*[@id="sequences"]/div/div[2]/div[2]/section/ul/li[2]/div/div[2]')
    mass_text = mass.text
    function = driver.find_element(By.XPATH, '//*[@id="function"]/div/div[2]/div[1]')
    function_text = function.text

    return copied_sequence, mass_text, function_text

sequence, mass, function = get_info('P12345')
print("Protein Sequence:", sequence)
print("Protein Mass:", mass)
print("Protein Function:", function)

