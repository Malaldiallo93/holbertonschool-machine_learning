#!/usr/bin/env python3
"""
Class Dataset to load and preprocess the dataset
"""
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds


class Dataset:
    """
    Class to load and prepare a dataset for machine translation
    """
    def __init__(self):
        """
        Initialize the dataset by loading and tokenizing
        """
        self.data_train, self.data_valid = tfds.load(
            'ted_hrlr_translate/pt_to_en',
            split=['train', 'validation'],
            as_supervised=True
        )
        self.tokenizer_en, self.tokenizer_pt = self.tokenize_dataset(
            self.data_train
        )

    def tokenize_dataset(self, data):
        """
        Creates sub-word tokenizers for the dataset.

        Args:
            data (tf.data.Dataset): A dataset containing tuples (pt, en),
                                    where `pt` is a Portuguese sentence and
                                    `en` is an English sentence.

        Returns:
            tuple: (tokenizer_pt, tokenizer_en)
                   Portuguese and English tokenizers, respectively.
        """
        tokenizer_pt = tfds.deprecated.text.SubwordTextEncoder.\
            build_from_corpus(
                (pt.numpy() for pt, _ in data),
                target_vocab_size=2 ** 15
            )
        tokenizer_en = tfds.deprecated.text.SubwordTextEncoder.\
            build_from_corpus(
                (en.numpy() for _, en in data),
                target_vocab_size=2 ** 15
            )
        return tokenizer_pt, tokenizer_en
