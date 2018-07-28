import os
import pandas as pd
import numpy as np
import nltk
import PyPDF2
from sklearn.svm import SVC


def read_pdf(path):
	"""Parsing pdf file"""
    pdf_obj = open(path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
    return ''.join((pdf_reader.getPage(i).extractText() for i in range(pdf_reader.numPages)))

def extract_key_words(list_of_words, text):
	"""For each word in list_of_words, returns a list of 1s and 0s for presence/absence of words"""
    presence = []
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    for word in list_of_words:
        if word == 'r':
            presence.append(int('r' in tokens))	#Had to do it seperatly for 'r' as 'r' letter in text does not neccesarily imply R language in the text
        else:
            presence.append(word in text)
    return presence

df = pd.read_csv('Languages_Tech.csv')	#Reading the dataset

arr = list(df.columns)	#arr is the list of keywords (languages and technologies)
arr.remove('Link')		#"Link" is not a keyword
arr.remove('Title')		#"Title" is not a keyword
arr.remove('Query')		#"Query" is not a keyword

Y = df['Query'].as_matrix()	#Numpy matrix of target labels
del df['Query']			#Not a feature
del df['Link']			#Not a feature
del df['Title']			#Not a feature
X = df.as_matrix()		#Converting Pandas dataframe to a Numpy matrix

clf = SVC()
clf.fit(X, Y)			#Feeding training data to the classifier


# Predicting the class of job suitable for every resume in ./Resumes directory
for file_name in sorted(os.listdir('./Resumes')):
    if file_name.endswith('pdf'):
        print(file_name, clf.predict([extract_key_words(arr,
                                                        read_pdf('./Resumes/{}'.format(file_name)))])[0])
