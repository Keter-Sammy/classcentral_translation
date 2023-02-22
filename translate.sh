#!/bin/bash

# Define the folder path containing the HTML files
folder_path="/home/user-04/20220220/202023/www.classcentral.com"

# Define the source and target languages
source_language="en"
target_language="hi"

# Loop through all the HTML files in the folder
for file in "$folder_path"/*.html "$folder_path"/*.htm; do
    # Translate the visible text in the HTML file using sed
    sed -i "/<[^>]*>/d; /^\s*$/d; s/.*/echo '&' | translate-shell -s $source_language -t $target_language/e" "$file"
done
