# A BERT-base Relation Extraction for Special Cargo Domain

The code is part of my paper ["Relation Representation Learning for Special Cargo Ontology"](https://scholar.google.com/citations?user=DNUz3o4AAAAJ&hl=en&authuser=1) that investigates how to build an efficient information extraction model from low-resource domains based on available domain data for industry use cases. For this purpose, a model is designed for extracting and classifying instances of different relation types between each concept pair.
The model is a [BERT](https://arxiv.org/abs/1810.04805)-base model. BERT is a language model built based on multiple transformer layers and self-supervised learning that utilizes a large amount of corpus data to learn better feature representation of words. It has obtained state-of-the-art performance on several Natural Language Processing (NLP) tasks. I trained a domain specific relation representation on BERT using ["Matching the Blanks (MTB)"](https://arxiv.org/abs/1906.03158) method that only relies on an entity-linked corpus of cargo shipment domain. Due to the low-resource nature of the domain and availability of automatic entity resolution annotation systems for generating training samples, MTB approach is adapted to the special cargo domain by generating training data based on the relation statements with marked name entities replaced with a special symbol [BLANK].

The results of experiments show that the model could represent the complex semantic information of the special cargo domain, and tasks initialized with these representations achieve promising results.


## Training 

In the training process, MTB exploits a pair of relation representations for each pair of relation statements with the aim of learning an encoder that specifies whether or not two relation statements encode the similar relation using the following binary classifier. Therefore, given a pair of relation statements, MTB tries to learn an embedding model that their inner product is high when both contain the same entity pair and low when entity pairs are different. In the training setup, the loss of masked language models of BERT and MTB are minimized concurrently. We test various training data and BERT models for training the relation statement encoder in this architecture. The Figure below shows an overview of the training process in MTB. The figure depicts that two different relation statements are fed into BERT. The classifier is defined to learn a relation encoder that is utilized to specify if two relation representations embed the same relation. Parameters of the encoder is learned by minimizing the loss function.


<img src="https://github.com/VahidehReshadat/CargoRelationExtraction/blob/master/Bert_Imags/Presentation1-5.jpg" alt="overview of the training process with MTB" width="400"/>







----------------------

Using the MTB pre-train model on domain data, the relation extraction model is built. The architecture of relation statement classification using MTB is illustrated in Figure 5. As shown in the figure, the target entities are marked with special entity markers in the input. Then, the marked input text is fed into the BERT model, and the corresponding states of the beginning of the two entity markers are concatenated, and the relation representation is extracted. 

Figure 5 Architecture of the special cargo relation classifier. Target entities in the input (FAA and PharmaPort360) are represented using special markers showing the start ([E1] and [E2]) and the end ([/E1] and [/E2]) of each entity.

The generated relation representation from the BERT transformer is fed into a fully connected layer. This layer is either the normalization of the relation representation or linear activation function. The layer type is selected as a hyper-parameter. The last layer is a classification layer with softmax activation that produces the probability of each class. These layers are trainable using a few samples for each relation class.

## Overview
A PyTorch implementation of the models 
## Requirements
Requirements: Python (3.6+), PyTorch (1.2.0+), Spacy (2.1.8+)  

Pre-trained BERT model of HuggingFace.co (https://huggingface.co)   
Code structure adopted from:
[BertRE](https://github.com/plkmo/BERT-Relation-Extraction) and [anago](https://github.com/huggingface/hmtl)

