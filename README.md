# FAQ Chatbot Using NLP

## Overview

This project is a simple FAQ Chatbot built using Python, Pandas, and Scikit-learn.

The chatbot answers user questions by finding the most similar question from a predefined FAQ dataset using TF-IDF Vectorization and Cosine Similarity.

## Features

* FAQ-based question answering
* TF-IDF text vectorization
* Cosine similarity matching
* Unknown question detection
* Easy-to-update CSV dataset

## Technologies Used

* Python
* Pandas
* Scikit-learn
* NLP
* TF-IDF Vectorization
* Cosine Similarity

## Project Structure

chatbox.py - Main chatbot program

faq_data.csv - FAQ dataset

## How to Run

1. Install dependencies:

pip install pandas scikit-learn

2. Run the program:

python chatbox.py

## Sample Output

You: What is Python?

Bot: Python is a programming language.

You: What is cricket?

Bot: Sorry, I don't know the answer to that question.
