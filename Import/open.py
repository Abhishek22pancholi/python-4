import os
#get a path to current folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

email_txt = os.path.join(BASE_DIR,"template","template.txt")

content = ""
# open a file for read
with open(email_txt,'r') as f:
    content = f.read()
        
print(content.format(name='Nobady'))

