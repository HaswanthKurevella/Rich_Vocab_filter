# Extracting Rich Vocabulary Words from a PDF

This project provides a Python script to extract rich vocabulary words from a PDF file. The script performs the following steps:

1. Extracts text from the PDF.
2. Tokenizes the text into words.
3. Filters out common English words (stopwords).
4. Counts the frequency of each word.
5. Selects and prints the top 100 least frequent (uncommon) words.

## Prerequisites

Before running the script, make sure you have Python installed along with the necessary libraries:  

- **PyMuPDF (`fitz` module)**  
  _PyMuPDF is a Python binding for MuPDF, a lightweight and high-performance PDF and XPS viewer. It allows for the opening, manipulation, and saving of various document formats, including PDF and XPS. The module provides powerful rendering capabilities, enabling users to convert document pages into images for visual representation. Additionally, PyMuPDF supports comprehensive text extraction, allowing users to extract text, images, and other data from documents for further analysis. Its versatility and efficiency make it a popular choice for developers working with document processing in Python._

- **nltk (Natural Language Toolkit)**  
  _The Natural Language Toolkit (NLTK) is a leading platform for building Python programs to work with human language data. It offers a comprehensive suite of libraries and programs for symbolic and statistical natural language processing (NLP) tasks. NLTK provides easy-to-use interfaces to over 50 corpora and lexical resources, including WordNet. It includes text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning. Widely used in education and research, NLTK supports the development of complex language-based applications._

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

