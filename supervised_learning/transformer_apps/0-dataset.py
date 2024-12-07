#!/usr/bin/env python3
"""
    Class Dataset to load and preprocess the dataset
"""
import tensorflow_datasets as tfds

class Dataset:
    """
        Class to load and prepare a dataset for machine translation
    """
    def __init__(self):
        """
            Class initializer
        """
        self.data_train, self.data_valid = \
            tfds.load('ted_hrlr_translate/pt_to_en',
                      split=['train', 'validation'],
                      as_supervised=True)
        self.tokenizer_en, self.tokenizer_pt = self.tokenize_dataset(self.data_train)

    def tokenize_dataset(self, data):
        """
            Creates sub-word tokenizers for our dataset
        :param data: tf.data.Dataset, tuple (pt, en)
            pt: tf.Tensor, Portuguese sentence
            en: tf.Tensor, English sentence
            max vocab size : 2**15
        :return: tokenizer_pt, tokenizer_en
            Respectively Portuguese and English tokenizers
        """
        # Convert tf.Tensors to strings for tokenizer
        pt_sentences = (pt.numpy().decode('utf-8') for pt, _ in data.as_numpy_iterator())
        en_sentences = (en.numpy().decode('utf-8') for _, en in data.as_numpy_iterator())

        self.tokenizer_pt = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(
            pt_sentences, target_vocab_size=2**15
        )
        self.tokenizer_en = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(
            en_sentences, target_vocab_size=2**15
        )
        return self.tokenizer_pt, self.tokenizer_en
