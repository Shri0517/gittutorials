from textblob import TextBlob

words = ["Artifical","Intelligance"]
corrected_words= []

for i in words:
    print("wrong words:",words)
    print("corrected_words:",words)
    
    print(corrected_words.append(TextBlob(i)))
    
    
for i in corrected_words:
    print(i.correct(),end = " ")
    
    