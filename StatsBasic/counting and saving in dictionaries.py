#string
line='My name is Bibek Thapa. I am CSIT student. My favourite animal is zebra. Currently coding in python'
#alphabet to compare
alphabet=[]
for i in range (0,26):
    alphabet.append(chr(i+97))
print (alphabet)
#counting character
count_char={}
for ch in line:
    df=ch.lower()
    if (df in alphabet):
        if (df in count_char):
            count_char[df]+=1
        else:
            count_char.update({df:1})
    
print (count_char)
    

