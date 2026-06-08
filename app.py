import gradio as gr
import os
from document_pipeline import load_documents, chunk_document
from config import DOCS_PATH
import random
from embedretriever import embed_and_store, get_collection, retrieve
from generator import generate_response


collection = get_collection()
if collection.count() > 0:
    print(f"Vector store already populated ({collection.count()} chunks). Skipping ingestion.")
    print("To re-ingest, delete the ./chroma_db folder and restart.")
else:
    documents = load_documents()
    all_chunks = []
    for doc in documents:
        chunks = chunk_document(doc["text"], doc["property"])
        all_chunks.extend(chunks)
        print(f"Chunked {doc['property']} into {len(chunks)} chunks.")

    # Store chunks in the vector database
    if all_chunks:
        embed_and_store(all_chunks)
        print(f"Ingestion complete. {len(all_chunks)} chunks stored.")
    else:
        print("No chunks produced. check chunk_document()")

def handle_query(question):
    if not question.strip():
        return "Please enter a question.", ""
    retrieved = retrieve(question)
    answer_text = generate_response(question, retrieved)
    sources= set()
    for chunk in retrieved:
        sources.add(chunk["property"])
    sourcelist= "\n".join(f"• {s}" for s in sources)
    return answer_text, sourcelist


with gr.Blocks() as demo:
    inp = gr.Textbox(label="Your question")
    btn = gr.Button("Ask")
    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved from", lines=4)
    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

demo.launch()