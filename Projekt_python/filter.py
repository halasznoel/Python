from bleach import clean
import re

whitelist = ['ul','li','ol','strong','b','br','p']

def clean_spaces_and_newlines(src):
    result = re.findall("\w+[,.!]?\\n?|<\w+>\\n?|</\w+>\\n?", src)
    return result

with open("page.html","r", encoding='UTF-8') as html_file:
    html = html_file.read()

    html_cleaned = clean(html, strip=True, tags=whitelist)

    html_cleaned = clean_spaces_and_newlines(html_cleaned)

    html_cleaned = " ".join(html_cleaned)

    #print(html_cleaned)

    with open("cleaned_text.txt","w", encoding='UTF-8') as outfile:
        outfile.write(html_cleaned)