book=open("pg25990.txt")
for line in book:
    for words in line.split():
        print(words.lower())