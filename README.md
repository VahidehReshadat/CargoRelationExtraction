# Relation Extraction for Special Cargo Domain

The code is part of our paper ["Relation Representation Learning for Special Cargo Ontology"](https://scholar.google.com/citations?user=DNUz3o4AAAAJ&hl=en&authuser=1) that we proposed an ontology population pipeline for the special cargo domain, and as part of the ontology population task, we investigated how to build an efficient information extraction model from low-resource domains based on available domain data for industry use cases. For this purpose, a model is designed for extracting and classifying instances of different relation types between each concept pair.
The model is based on a relation representation learning approach built upon a Hierarchical Attention-based Multi-task architecture in the special cargo domain and applied for extracting and classifying instances of different relation types between each concept pair in the special cargo ontology. It is compared with a BERT-base model. We train a domain specific relation representation on BERT using MTB method that only relies on an entity-linked corpus of cargo shipment domain. 
The results of experiments show that the model could represent the complex semantic information of the domain, and tasks initialized with these representations achieve
promising results.

## Overview
A PyTorch implementation of the models 
## Requirements
Requirements: Python (3.6+), PyTorch (1.2.0+), Spacy (2.1.8+)  

Pre-trained BERT model of HuggingFace.co (https://huggingface.co)   
Code structure adopted from:
[BertRE](https://github.com/plkmo/BERT-Relation-Extraction) and [anago](https://github.com/huggingface/hmtl)

