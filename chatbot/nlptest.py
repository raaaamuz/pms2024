import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import spacy
import os

# Load CSV data into a pandas DataFrame
path=os.path.join(os.getcwd(), "backend","chatbot","benchmark.csv")
print(path)
df = pd.read_csv(path)

# Preprocessing functions
def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove punctuation
    tokens = [word for word in tokens if word not in string.punctuation]
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return tokens

# Example query
user_query = "provide percentage distribution for productcode"

# NLP processing
tokens = preprocess_text(user_query)

# Extract key entities using spaCy
nlp = spacy.load("en_core_web_sm")
doc = nlp(user_query)
entities = [ent.text for ent in doc.ents]

# Formulate database query based on NLP analysis
database_query = None
for entity in entities:
    if entity in df.columns:
        database_query = df[entity].value_counts()
        break
else:
    for token in tokens:
        if token in df.columns:
            database_query = df[token].value_counts()
            break

# Display results
if database_query is not None and not database_query.empty:
    print(database_query)
else:
    print("No relevant information found.")
