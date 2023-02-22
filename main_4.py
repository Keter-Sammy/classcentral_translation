import os
from googletrans import Translator
from bs4 import BeautifulSoup

# Initialize the translator
translator = Translator(service_urls=['translate.google.com'])

# Define the folder path containing the HTML files
folder_path = '/home/user-04/20220220/202023/www.classcentral.com/'

# Loop through all the HTML files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.html') or filename.endswith('.htm'):
        file_path = os.path.join(folder_path, filename)

        # Read the contents of the HTML file
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all the visible text in the HTML content and translate it to Hindi
        for tag in soup.find_all(text=True):
            if tag.strip() != '':
                translation = translator.translate(tag, src='en', dest='hi').text
                tag.replace_with(translation)

        # Save the translated HTML content to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
