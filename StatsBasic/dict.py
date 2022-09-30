import re
pattern = '[a-z]'
line='My name is Bibek Thapa. I am CSIT student. My favourite animal is Zebra. Currently coding in python.'
count_char={}
for match in re.finditer(pattern,line.lower()):
    if match in pattern:
        count_char[match]+=1
    else:
        count_char.update({match:1})
    

