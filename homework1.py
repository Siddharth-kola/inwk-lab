#Home work 1


import string
list1=[]
list2=['hello','project','gutenberg','bird']
dict1={}
book=open("pg25990.txt")


#for capturing the book

for line in book:
   
    for words in line.split():
        #print(words.strip(string.punctuation).lower())
        list1.append(words.strip(string.punctuation).lower())
        
s=set(list1)
s1=set(list2)
print(s1.difference(s))
