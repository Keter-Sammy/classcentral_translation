import os
from bs4 import BeautifulSoup
from translate import Translator

# Define the folder path containing the HTML files
folder_path = '/home/user-04/20220220/202023/www.classcentral.com/'

# Define the source and target languages
source_language = 'en'
target_language = 'hi'

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
                # Translate the text using the translate package
                translator = Translator(from_lang=source_language, to_lang=target_language)
                translation = translator.translate(tag.strip())

                # Replace the original text in the HTML content with the translated text
                tag.replace_with(translation)

        # Save the translated HTML content to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
