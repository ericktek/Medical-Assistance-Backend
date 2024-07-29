from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from nltk.tokenize import word_tokenize
import gensim.downloader as api
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import time
import nltk
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

print('Loading Word2Vec model...')
current_time = time.time()
word2vec_model = api.load('word2vec-google-news-300')


end_time = time.time()

print(f"Word2Vec model loaded in {end_time - current_time} seconds.")
print('Word2Vec model loaded.')

def clean_text(text):
    """
    Perform basic text cleaning on the input text.
    """
    # Remove special characters, punctuation, and numbers
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert text to lowercase
    cleaned_text = cleaned_text.lower()
    # Remove extra whitespace
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text

def tokenize_text(text):
    """
    Tokenize the input text using NLTK word_tokenize.
    """
    tokens = word_tokenize(text)
    return tokens

def remove_stopwords(tokens):
    """
    Remove stopwords from the tokenized text.
    """
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

def preprocess_text(text):
    """
    processing text recived
    """
    
    text = str(text)
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)
    tokens = remove_stopwords(tokens)
    return tokens

def aggregate_vectors(vectors):
    """
    Aggregate a list of word vectors into a single fixed-size representation.
    """
    if len(vectors) == 0:
        return np.zeros(word2vec_model.vector_size)
    else:
        return np.mean(vectors, axis=0)
    
def get_vectors(text, model):
  words = preprocess_text(text)
  word_vectors = []
  for word in words:
    if word in model:
        word_vectors.append(model[word])
    else:
        # Handle out-of-vocabulary words by using a zero vector
        word_vectors.append([0] * model.vector_size)
  if len(word_vectors) == 0:
    return np.zeros(word2vec_model.vector_size)
  else:
    return np.mean(word_vectors, axis=0)

def encrypt_message(message, key):
    iv = get_random_bytes(DES3.block_size)  # Generate a random IV of 8 bytes
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded_message = pad(message.encode(), DES3.block_size)
    ciphertext = cipher.encrypt(padded_message)
    return iv + ciphertext

def decrypt_message(encrypted_message, key):
    iv = encrypted_message[:DES3.block_size]
    ciphertext = encrypted_message[DES3.block_size:]
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(ciphertext)
    return unpad(decrypted_message, DES3.block_size).decode()

def extract_disease_and_differential(text):
    disease_pattern = r"\*\*Possible Disease:\*\*\s*(.*?)\s*\*\*Differential Diagnosis:\*\*(.*?)$"
    match = re.search(disease_pattern, text, re.DOTALL)
    if match:
        disease = match.group(1).strip()
        differential_text = match.group(2).strip()
        differential_diseases = re.findall(r"\*\s*(.*?)\s*(?:\n|$)", differential_text)
        return disease, differential_diseases
    else:
        return None, None

def generating_api_key():
    api_key = get_random_bytes(16)
    return api_key.hex()