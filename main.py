from spacy.lang.ru.stop_words import STOP_WORDS
import ru_core_news_md
from textblob import TextBlob
model = ru_core_news_md.load()

text = model("Плохо")

print(text)
text_list = [word.lemma_ for word in text]
filter_text_list = [elem for elem in text_list if not elem in STOP_WORDS]
print(text_list)
print(filter_text_list)

analys = TextBlob(str(filter_text_list))
sentiment = analys.sentiment.polarity

if sentiment > 0:
    print("pos")
elif sentiment < 0:
    print("neg")
else:
    print("neytral")