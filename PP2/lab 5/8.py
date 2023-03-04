import re
text = "asdAsdaSd"
print(re.findall('[A-Z][^A-Z]*', text))