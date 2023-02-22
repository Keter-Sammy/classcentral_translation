from googletrans import Translator

translator = Translator()

# open the file
in_file = open("/home/user-04/20220220/202023/www.classcentral.com/index.html", "r")

# read the file content
file_content = in_file.read()

# translate the content
translated_text = translator.translate(file_content, dest='hi')

# write the translated content to the same file
out_file = open("/home/user-04/20220220/202023/www.classcentral.com/index.html", "w")
out_file.write(translated_text.text)

# close the files
in_file.close()
out_file.close()