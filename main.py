from spacy.lang.ru.stop_words import STOP_WORDS
import ru_core_news_md
from textblob import TextBlob
# from translate import Translator
from googletrans import  Translator
import asyncio
model = ru_core_news_md.load()

text = model("не очень фильм,")

print(text)
text_list = [word.lemma_ for word in text]
filter_text_list = [elem for elem in text_list if not elem in STOP_WORDS]
print(text_list)
print(filter_text_list)

ru_text = " ".join(filter_text_list)
# translator = Translator(from_lang="Russian", to_lang="English")
# eng_text = translator.translate(ru_text)
async def Tranlate_text(text):
    translator = Translator()
    translated = await translator.translate(text, src='ru', dest='en')

    return  translated.text
eng_text = asyncio.run(Tranlate_text(ru_text))

analys = TextBlob(eng_text)
sentiment = analys.sentiment.polarity

if sentiment > 0:
    print("Позитивный")
elif sentiment < 0:
    print("Негативный")
else:
    print("neytral")