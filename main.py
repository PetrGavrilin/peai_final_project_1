from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch 
import streamlit as st


def translate_text(text):
# функция переводит вводимый текст
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")    
    transl_text = model.predict(text)
    return transl_text

def load_text():
    text = st.text_input("Enter your text in English")
    return text   
    
    
st.title('Перевод с русского на английский') # вывод шапки
text = load_text() # загрузка текста
result = st.button('Перевести') # присвоение статуса по нажатию кнопки

if result:
    ttext = translate_text(text)
    st.write(ttext) 
