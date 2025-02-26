from transformers import TFBartForConditionalGeneration, BartTokenizer


# Modell und Tokenizer laden
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = TFBartForConditionalGeneration.from_pretrained(model_name)


# Funktion zur Textzusammenfassung
def summarize_text(text, max_length=150, min_length=40):
    """
    Fasst den gegebenen Text zusammen.

    Args:
        text (str): Der zu zusammenfassende Text.
        max_length (int): Maximale Länge der Zusammenfassung.
        min_length (int): Minimale Länge der Zusammenfassung.

    Returns:
        str: Die zusammengefasste Version des Textes.
    """
    # Tokenisierung und Generierung der Zusammenfassung
    inputs = tokenizer(text, return_tensors='tf', max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs['input_ids'], 
        max_length=max_length, 
        min_length=min_length, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary
