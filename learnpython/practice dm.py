import string

with open("names.txt","a+") as file:
        file.seek(0)
        text=file.read()
text=text.lower()
text=text.translate(str.maketrans('','',string.punctuation))
words=text.split()
words_count={}
for word in words:
    if word in words_count:
        words_count[word]+=1
    else:
        words_count[word]=1
for words,count in words_count.items():
    print(f"{words}:{count}")

