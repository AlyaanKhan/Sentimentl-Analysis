from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def analyze_sentiment(text):
    # Tokenize input text and convert to PyTorch tensor
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get predicted label (0: very negative, 4: very positive)
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits, dim=1).item()

    # Map class ID to sentiment
    sentiment_map = {
        0: 'very negative',
        1: 'negative',
        2: 'neutral',
        3: 'positive',
        4: 'very positive'
    }

    return sentiment_map[predicted_class_id]
