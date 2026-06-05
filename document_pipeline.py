import os
import re
from config import DOCS_PATH
 
 
def load_documents():
    """Load all .txt housing documents from the docs folder."""
    documents = []
    for filename in sorted(os.listdir(DOCS_PATH)):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCS_PATH, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            # Derive a readable property name from the filename,
            # e.g. "DonnybrookApartmentsReviews.txt" -> "Donnybrook Apartments Reviews"
            property_name = filename.replace(".txt", "")
            # Split on capital letters to insert spaces, e.g. "DonnybrookApartments" -> "Donnybrook Apartments"
            property_name = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", property_name)
            documents.append({
                "property": property_name,
                "filename": filename,
                "text": text,
            })
    print(f"Loaded {len(documents)} document(s): {[d['property'] for d in documents]}")
    return documents
 
 
def chunk_document(text, property_name):
    max_chars = 300
    overlap_sentences = 1
    min_length = 50
 
    # Split into sentences on .  !  ? followed by whitespace or end of string.
    # Also treat newlines as sentence boundaries for list-style content
    # (e.g. amenity bullet points, which don't end with punctuation).
    sentences = re.split(r"(?<=[.!?])\s+|\n", text)
    sentences = [s.strip() for s in sentences if s.strip()]
 
    chunks = []
    prefix = property_name.lower().replace(" ", "_")
    counter = 0
    current_sentences = []
    current_length = 0
 
    for sentence in sentences:
        # If adding this sentence would exceed max_chars, flush the current chunk
        if current_length + len(sentence) > max_chars and current_sentences:
            chunk_text = " ".join(current_sentences).strip()
            if len(chunk_text) >= min_length:
                chunks.append({
                    "text": chunk_text,
                    "property": property_name,
                    "chunk_id": f"{prefix}_{counter}",
                })
                counter += 1
 
            # Carry the last sentence forward as overlap into the next chunk
            current_sentences = current_sentences[-overlap_sentences:]
            current_length = sum(len(s) for s in current_sentences)
 
        current_sentences.append(sentence)
        current_length += len(sentence)
 
    # Flush any remaining sentences as the final chunk
    if current_sentences:
        chunk_text = " ".join(current_sentences).strip()
        if len(chunk_text) >= min_length:
            chunks.append({
                "text": chunk_text,
                "property": property_name,
                "chunk_id": f"{prefix}_{counter}",
            })
 
    return chunks
