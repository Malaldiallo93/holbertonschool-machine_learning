# Transformer Applications

Machine learning translation for English to Portuguese using the transformer model and the Tensorflow Datasets ted_hrlr_translate/pt_to_en.

## Requirements

- Python 3.8
- Tensorflow 2.6
- NumPy 1.19.2
- pycodestyle 2.6

## Tasks

| Task                                                      | Description                                                                               |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [Dataset](./0-dataset.py)                                 | Class that loads and preps a dataset for machine translation                              |
| [Dataset](./1-dataset.py)                                 | Class update with method to encode translation into tokens                                |
| [Dataset](./2-dataset.py)                                 | Class update with method that axts as a tensorflow wrapper for the encode instance method |
| [Pipeline](./3-dataset.py)                                | Class that set up the data pipeline for training a transformer model                      |
| [Create Masks](./4-create_masks.py)                       | Function that creates all masks for training/validation                                   |
| [Train](./5-train.py) & [Transformer](./5-transformer.py) | Adjust transformer for previous project + function to train transformer                   |

Resources
Read or watch:

How machines Read
Sub-word tokenizers
Summary of the tokenizers
Subword Tokenization
Notes on BERT tokenizer and model
What is AutoTokenizer?
Training a new tokenizer from an old one
TFDS Overview
How Transformers Work: A Detailed Exploration of Transformer Architecture
References:

tfds
tfds.load
AutoTokenizer
encode
tf.py_function
TFDS Keras Example
tf.linalg.band_part
Customizing what happens in fit
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to use Transformers for Machine Translation
How to write a custom train/test loop in Keras
How to use Tensorflow Datasets