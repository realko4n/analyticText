from spacy.lang.ru import Russian
from spacy.lang.ru.stop_words import STOP_WORDS

model = Russian()

text = model("Хороший фильм, было интересно смотреть, приятный сюжет")

print(text)
text_list = [word for word in text]
print(text_list)