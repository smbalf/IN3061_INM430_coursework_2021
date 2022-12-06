from urllib.request import urlopen
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Princess Badoura, A tale from the Arabian Nights. By Laurence Housman
book_url = "http://www.gutenberg.org/files/135/135-0.txt"

book_raw = urlopen(book_url).read().decode('utf-8')

#print(len(book_raw))

word_tokens = word_tokenize(book_raw)
# print(word_tokens[1:40])

stop_words = stopwords.words('english')

smaller_tokens = word_tokens[10000:20000]

for word in smaller_tokens:
    if word in stop_words:
        smaller_tokens.remove(word)
    
print(smaller_tokens[1:50])