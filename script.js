import { readFile, writeFile } from 'fs';
import translate from 'google-translate-api';

//read the file
readFile('index.html', 'utf8', (err,data) => {
  if (err) {
    throw err;
  }
  
  //translate the file
  translate(data, {to: 'hi'}).then(res => {
    const translatedText = res.text;

    //write the translated text back to the file
    writeFile('index.html', translatedText, (err) => {
      if (err) throw err;
      console.log('HTML file translated and saved!');
    });
  }).catch(err => {
    console.error(err);
  });
});