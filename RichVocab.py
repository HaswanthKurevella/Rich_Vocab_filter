import fitz  # PyMuPDF
import nltk
from nltk.corpus import stopwords
import string

# Step 1: Extract Text from the PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Step 2: Tokenize and Filter Words
def tokenize_and_filter(text):
    nltk.download('punkt')
    nltk.download('stopwords')
    
    words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [
        word.lower() for word in words
        if word.isalpha() and word.lower() not in stop_words
    ]
    return filtered_words

# Step 3: Select Uncommon Words
def select_uncommon_words(words, top_n=100):
    word_freq = nltk.FreqDist(words)
    sorted_words = sorted(word_freq.items(), key=lambda item: item[1])
    uncommon_words = [word for word, freq in sorted_words[:top_n]]
    return uncommon_words

# Main function to perform the analysis
def analyze_pdf_for_rich_vocabulary(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    filtered_words = tokenize_and_filter(text)
    uncommon_words = select_uncommon_words(filtered_words)
    return uncommon_words

# Example usage
pdf_path = 'data.pdf'
top_100_words = analyze_pdf_for_rich_vocabulary(pdf_path)
print(top_100_words)
