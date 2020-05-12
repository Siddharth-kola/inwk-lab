
#task 2
import string
list1=[]
dict1={}
book=open("pg25990.txt")
for line in book:
   
    for words in line.split():
        #print(words.strip(string.punctuation).lower())
        list1.append(words.strip(string.punctuation).lower())
        if words in dict1:
            count+=1
            dict1.update({words:count})
            
        else:
            count=1
            dict1.update({words:count})
        
print(len(list1))    
#print(dict1)

for i in sorted(dict1.values(),reverse=True)[:20]:
       print(i)

import string
list1=[]
list2=[]
dict1={}
book=open("pg25990.txt")


#for capturing the book

for line in book:
   
    for words in line.split():
        #print(words.strip(string.punctuation).lower())
        list1.append(words.strip(string.punctuation).lower())
        if words in dict1:
            count+=1
            dict1.update({words:count})
            
        else:
            count=1
            dict1.update({words:count})
            
            
            
#for printing number of words      

print(len(list1))    





#total number of words used each time
 
print(dict1)



for i in sorted(dict1.values(),reverse=True)[:20]:
    
        print(i)
        list2.append(i)
        
        
print(list2)     
