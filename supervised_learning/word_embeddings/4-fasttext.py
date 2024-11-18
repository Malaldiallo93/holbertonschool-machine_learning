#!/usr/bin/env python3
"""
    Train fastText model
"""
import gensim  # Updated to match the expected import pattern

def fasttext_model(sentences, vector_size=100, min_count=5, negative=5,
                   window=5, cbow=True, epochs=5, seed=0, workers=1):
    """
    Creates, builds, and trains a gensim FastText model.
    Args:
        sentences (list): List of sentences to train the model on.
        vector_size (int): Dimensionality of the embedding vectors
            (default is 100).
        min_count (int): Minimum number of occurrences of a word for
            it to be used in training (default is 5).
        negative (int): Size of the negative sampling (default is 5).
        window (int): Maximum distance between the current and predicted
            word within a sentence (default is 5).
        cbow (bool): If True, uses CBOW model; if False, uses Skip-gram model
            (default is True).
        epochs (int): Number of epochs to train the model (default is 5).
        seed (int): Seed for random number generation (default is 0).
        workers (int): Number of CPU cores to use for training the model
            (default is 1).
    Returns:
        model (gensim.models.FastText): The trained FastText model.
    """
    # Create FastText model
    model = FastText(
        sentences=sentences,
        vector_size=vector_size,
        min_count=min_count,
        negative=negative,
        window=window,
        sg=0 if cbow else 1,  # CBOW: sg=0, Skip-gram: sg=1
        epochs=epochs,
        seed=seed,
        workers=workers
    )
    return model
