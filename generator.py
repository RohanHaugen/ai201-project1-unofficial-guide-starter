from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL
 
_client = Groq(api_key=GROQ_API_KEY)
 
SYSTEM_PROMPT = """You are a housing advisor helping Towson University students find off-campus housing.
 
CRITICAL RULES — follow these without exception:
1. Answer ONLY using the information provided in the CONTEXT block in the user message.
2. Do NOT use any outside knowledge, general facts, or assumptions from your training data.
3. If the context does not contain enough information to answer the question, say exactly:
   "I don't have enough information in my sources to answer that."
4. Do NOT make up apartment names, prices, distances, or amenities not found in the context.
5. Do NOT speculate or extrapolate beyond what the context explicitly states.
 
FORMAT — every answer must follow this pattern:
- Include an inline citation at the end of each claim in the format (source: [source name]).
- Answer in 2-4 clear sentences.
- If multiple properties are relevant, cite each one inline.
- Do NOT include a source list at the end — that is handled separately by the system.
 
EXAMPLE of correct format:
"According to student reviews of University Village (source: University Village Reviews),
parking passes cost $250 and towing is aggressively enforced. Several reviewers also note
that there is no way to break the lease early without finding a replacement tenant
(source: University Village Reviews)."
"""
 
 
def generate_response(query, retrieved_chunks):
    if not retrieved_chunks:
        return (
            "I couldn't find anything relevant in the loaded housing sources. "
            "Try rephrasing your question — or check that your ingestion pipeline is working."
        )
 
    context_lines = ["CONTEXT:"]
    for i, chunk in enumerate(retrieved_chunks, 1):
        context_lines.append(f"[{i}] ({chunk['property']}): {chunk['text']}")
    context_block = "\n".join(context_lines)
 
    user_message = f"{context_block}\n\nQUESTION: {query}"
 
    response = _client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_message},
        ],
        temperature=0.2,
        max_tokens=512,
    )
 
    return response.choices[0].message.content.strip()
