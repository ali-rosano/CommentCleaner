import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
from dotenv import load_dotenv
import os

#loading of .env variables and data
load_dotenv()
path_to_data = os.getenv('PATH_TO_DATA_CSV')
df = pd.read_csv(path_to_data)

def clean_data(df):
    '''
    This functions gets the df and returns the same df with some changes:
    # Convert boolean columns -> 'int'
    create generic column - Hate and delete all the other type.
    '''
    bool_col = df.select_dtypes(include = ['bool'])
    df[bool_col.columns] = df[bool_col.columns].astype(int)
    
    df['Hate'] = df.select_dtypes( include= ['int']).any(axis=1).astype(int)
    df_sum = df.drop(df.columns[[0,1,3,4,5,6,7,8,9,10,11,12,13,14]], axis=1, inplace=True)
    
    return df_sum

def X_y_split(df_sum):
    '''
    This function receives the dataframe. It returns the X 
    and the y  as two different variables.
    '''
    X = df_sum['Text']
    y = df_sum['Hate'].values

    return X, y


def vectorize_comment(X):
    # set up dictionary size q-ty of words
    MAX_FEATURES=100000

    # set up vetorizer
    vectorizer = TextVectorization(max_tokens=MAX_FEATURES,output_sequence_length=1800,output_mode='int')

    vectorizer.adapt(X.values) #teach the vectorizer all the words in the text(train the vectorizer)

    vectorized_comment = vectorizer(X.values) # vectorise text from numpy format (tokenization)
    
    return vectorized_comment





