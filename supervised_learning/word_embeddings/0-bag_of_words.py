#!/usr/bin/env python3
"""
    Bag Of Words
"""
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def tf_idf(sentences, vocab=None):
    """
    Creates a TF-IDF embedding for a list of sentences.
    
    :param sentences: List of sentences to analyze
    :param vocab: List of vocabulary words to use for the analysis (default: None)
    :return: embeddings, features
             - embeddings: numpy.ndarray of shape (s, f) containing the embeddings
               where s is the number of sentences and f is the number of features
             - features: list of the features used for embeddings
    """
    # Initialize TfidfVectorizer with the provided vocabulary if available
    vectorizer = TfidfVectorizer(vocabulary=vocab)
    
    # Fit the vectorizer to the sentences and transform them into TF-IDF embeddings
    tfidf_matrix = vectorizer.fit_transform(sentences)
    
    # Convert sparse matrix to dense array
    embeddings = tfidf_matrix.toarray()
    
    # Get the features (vocabulary terms)
    features = vectorizer.get_feature_names_out()
    
    return embeddings, features
