import string
list1=[]
book=open("pg25990.txt")
for line in book:
   
    for words in line.split():
        #print(words.strip(string.punctuation).lower())
        list1.append(words)
        
print(len(list1)) 
