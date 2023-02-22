const fs = require('fs');
const path = require('path');
const translate = require('@vitalets/google-translate-api');
const cheerio = require('cheerio');

// Define the folder path containing the HTML files
const folderPath = '/home/user-04/20220220/202023/www.classcentral.com/';

// Define the target language
const targetLang = 'hi';

// Loop through all the HTML files in the folder
fs.readdirSync(folderPath).forEach(file => {
  if (path.extname(file).toLowerCase() === '.html' || path.extname(file).toLowerCase() === '.htm') {
    const filePath = path.join(folderPath, file);
    
    // Read the contents of the HTML file
    const htmlContent = fs.readFileSync(filePath, 'utf-8');

    // Parse the HTML content using Cheerio
    const $ = cheerio.load(htmlContent);

    // Find all the visible text in the HTML content and translate it to Hindi
    $('body').find('*').each(async function() {
      const text = $(this).text().trim();
      if (text !== '') {
        const translation = await translate(text, {to: targetLang});
        $(this).text(translation.text);
      }
    });

    // Save the translated HTML content to the file
    fs.writeFileSync(filePath, $.html(), 'utf-8');
  }
});
