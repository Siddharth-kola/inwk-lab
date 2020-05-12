#task 3

import string
dict1={}
book=open("pg25990.txt")  
  
for line in book:
   
    for words in line.split():
       
       
        if words in dict1:
            count+=1
            dict1.update({words.strip(string.punctuation):count})
            
        else:
            count=1
            dict1.update({words.strip(string.punctuation):count})
        
   

#print(dict1)
dict2={}
dict3={}
count=1
for i  in sorted(dict1.values(),reverse=True):
  #print(i)
  
  dict3.update({i:count})
  count+=1
print(dict3)

import math


import matplotlib.pyplot as pyplot
pyplot.clf()
#pyplot.xscale(2000)
#pyplot.yscale(2000)
pyplot.title('word frequency & rank')
pyplot.xlabel('frequency')
pyplot.ylabel('rank')

list4=[]
list5=[]
for k,v in dict3.items():
  list4.append(math.log10(k))
  list5.append(math.log10(v))

pyplot.plot(list4,list5)


pyplot.show()
        
