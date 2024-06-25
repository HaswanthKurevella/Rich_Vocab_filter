# Extracting Rich Vocabulary Words from a PDF

This project provides a Python script to extract rich vocabulary words from a PDF file. The script performs the following steps:

1. Extracts text from the PDF.
2. Tokenizes the text into words.
3. Filters out common English words (stopwords).
4. Counts the frequency of each word.
5. Selects and prints the top 100 least frequent (uncommon) words.

## Prerequisites

Before running the script, make sure you have Python installed along with the necessary libraries:  

- PyMuPDF (`fitz` module)
- nltk (Natural Language Toolkit)

You can install the required libraries using pip:  

```sh
pip install PyMuPDF nltk
```

## Usage Instructions


### Clone the repository:

```sh
git clone https://github.com/HaswanthKurevella/Rich_Vocab_filter.git
cd Rich_Vocab_filter
```
#### Using the Python Script:
Replace 'path_to_your_pdf_file.pdf' with the actual path to your PDF file in RichVocab.py.  
Run the script:  
```sh
python RichVocab.py
```
#### Using the Jupyter notebook
Open the RichVocab.ipynb file in Jupyter Notebook or Jupyter Lab.  
Replace 'path_to_your_pdf_file.pdf' with the actual path to your PDF file in the notebook.  
Run the notebook cells to perform the analysis.  

