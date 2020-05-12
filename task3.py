#task 3

import string
dict1={}
book=open("pg25990.txt")



for line in book:
   
    for words in line.split():
       
       
        if words in dict1:
            count+=1
            dict1.update({count:words})
            
        else:
            count=1
            dict1.update({count:words})
            
            
            
        
   

print(dict1)




for i in sorted(dict1.keys(),reverse=True)[:20]:
       print(i)
        
        
        
print(dict1[1])
