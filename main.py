from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from googletrans import Translator
import os
from bs4 import BeautifulSoup

os.environ["PATH"] += os.pathsep + "/home/user-04/Downloads/chromedriver_linux64"


# Function to translate a given text using Google Translate
def translate_text(text, dest_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_language)
    return translated_text.text

# Function to process a given HTML file using Selenium and Google Translate
def process_html_file(file_path, dest_language):
    # Open the HTML file in a browser using Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(f"file://{os.path.abspath(file_path)}")

    # Extract the visible text from the browser window (ignoring HTML tags)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    visible_text = [elem.text for elem in soup.find_all() if elem.text.strip() != '']

    # Translate each visible text element using Google Translate
    for i, text in enumerate(visible_text):
        translated_text = translate_text(text, dest_language)
        visible_text[i] = translated_text

    # Replace the original visible text with the translated text in the browser window
    visible_text_iter = iter(visible_text)
    for elem in soup.find_all():
        if elem.text.strip() != '':
            elem.string = next(visible_text_iter)

    # Save the updated HTML file
    with open(file_path, 'w') as f:
        f.write(str(soup))

    # Close the browser window
    driver.quit()

# Function to process a given folder and its subfolders recursively
def process_folder(folder_path, dest_language):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.html'):
                process_html_file(file_path, dest_language)

# Main function to translate all HTML files in a folder and its subfolders
def main(folder_path, dest_language):
    process_folder(folder_path, dest_language)

# Example usage:
main('/home/user-04/20220220/202023/www.classcentral.com', 'hi')
