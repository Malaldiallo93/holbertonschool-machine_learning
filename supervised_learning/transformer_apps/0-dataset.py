#!/usr/bin/env python3
"""
Class Dataset to load and preprocess a dataset for machine translation
"""
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds
from transformers import AutoTokenizer


class Dataset:
    """
    Class to load and prepare a dataset for machine translation
    """
    def __init__(self):
        """
        Initialize the dataset by loading and tokenizing
        """
        # Load the training and validation datasets
        self.data_train, self.data_valid = tfds.load(
            'ted_hrlr_translate/pt_to_en',
            split=['train', 'validation'],
            as_supervised=True
        )
        # Create the tokenizers
        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train
        )

    def tokenize_dataset(self, data):
        """
        Creates sub-word tokenizers for the dataset using pre-trained models.

        Args:
            data (tf.data.Dataset): A dataset containing tuples (pt, en),
                                    where `pt` is a Portuguese sentence and
                                    `en` is an English sentence.

        Returns:
            tuple: (tokenizer_pt, tokenizer_en)
                   Portuguese and English tokenizers, respectively.
        """
        # Load pre-trained tokenizers
        tokenizer_pt = AutoTokenizer.from_pretrained(
            "neuralmind/bert-base-portuguese-cased",
            model_max_length=2**13
        )
        tokenizer_en = AutoTokenizer.from_pretrained(
            "bert-base-uncased",
            model_max_length=2**13
        )

        # Ensure tokenizers are trained with our data
        for pt, _ in data:
            tokenizer_pt.add_tokens(pt.numpy().decode('utf-8'))
        for _, en in data:
            tokenizer_en.add_tokens(en.numpy().decode('utf-8'))

        return tokenizer_pt, tokenizer_en
