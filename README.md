# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

Off campus housing experiences at Towson University. This knowledge is valuable as the official sources for housing don't contain reviews from the people who have lived there. No information about the experience of going to classes is provided and sources about student experiences are not centralized and inconsistent across options.
---

## Document Sources


| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 |Reddit |School Subreddit |https://www.reddit.com/r/Towson/comments/1s2sakz/towson_off_campus_housing_apartments/ |
| 2 |Reddit |School Subreddit |https://www.reddit.com/r/Towson/comments/1jf521t/housing_recommendations/ |
| 3 |Reddit |School Subreddit |https://www.reddit.com/r/Towson/comments/1tkockc/off_campus_housing/ |
| 4 |Reddit |School Subreddit |https://www.reddit.com/r/Towson/comments/1e3iybd/recommended_housing_near_campus/ |
| 5 |Reddit |School Subreddit |https://www.reddit.com/r/Towson/comments/1czlqy8/any_off_campus_housing_thats_in_walking_distance/ |
| 6 |ApartmentRatings |Off Campus Community Reviews |https://www.apartmentratings.com/md/towson/university-village_410583050021285/ |
| 7 |Reddit |School Subreddit |https://www.reddit.com/r/Towson/comments/1qjhkt8/off_campus_housing/ |
| 8 |offcampushousing.towson.edu |Search Resource for Off Campus Housing |https://offcampushousing.towson.edu/housing/property/donnybrook-apartments/58xc37p |
| 9 |offcampushousing.towson.edu |Search Resource for Off Campus Housing |https://offcampushousing.towson.edu/housing/property/towson-promenade/33ewdrf |
| 10 |offcampushousing.towson.edu |Search Resource for Off Campus Housing |https://offcampushousing.towson.edu/housing/property/towsontown-place-apartments/ktw7f48 |

---

## Chunking Strategy


**Chunk size:**
300 characters
**Overlap:**
50 characters
**Why these choices fit your documents:**
I decided to also incorporate chunking by sentences, and 300 characters worked for most comments and reviews.
**Final chunk count:**
274
---

## Embedding Model


**Model used:**
all-MiniLM-L6-v2 via sentence-transformers

**Production tradeoff reflection:**
I would weigh context length limits and latency, the current model takes a while but it would be handy to have a bigger context window for more metadata.
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
I instructed it to only utilize information inside the context block, I instructed it to respond that it didnt know the answer when it didnt know, and i told it not to extrapolate information. The content roughly follows the form of answer (inline source), answer continues (inline source).
**How source attribution is surfaced in the response:**
There are instructions inside the prompt to give an example when referencing something, and there is an additional list of instructions put in a sources section below the response. The inline citations are accurate, and the citation list provides an extra layer of security. However, there is not irrelavent filtering, so the citation list can list sources that matched the context but don't show up in the answer due to the LLM not deeming them relavent.
---

## Evaluation Report


| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 |What is the closest housing to the campus? |Towson Place, York, and Altus are the closest housing options. |Aspen is the closest to campus (source: reddit_housing4). Other nearby options include Altus and the York, which are also close to campus. Additionally, Towson Place Apartments and University Village are almost on campus |Relavent |Accurate |
| 2 |What are the benefits and downsides of TowsonTown Place? |Benefits include low price and low distance to campus, downsides include loud noises and weed smell. |Towson Place, which is likely referring to TowsonTown Place, can have noise and weed issues (source: reddit_housing6). On the other hand, being "basically on campus" is a benefit of Towson Place (source: reddit_housing6). |partially relavent |partially accurate |
| 3 |What are the benefits and downsides of University Village? |Benefits include low price and low distance to campus. Downsides include cheap furnishings and old apartments. |University Village is considered to be not very expensive (source: reddit_housing5) and is located right next to West Village (source: reddit_housing5), making it a convenient option. However, one downside is that it has super thin walls, which means you will hear everything (source: reddit_housing5).|Partially relavent |Accurate |
| 4 |What do students say are the benefits of Aspen? |Benefits include close to campus and individual leases. | I don't have enough information in my sources to answer that, as the provided context does not mention any benefits of Aspen, but rather expresses negative experiences and comparisons to other housing options (source: reddit_housing3). The only positive aspect mentioned about Aspen is its proximity to campus (source: reddit_housing4).|Partially relavent |Partially accurate |
| 5 |How long of a walk do students say Donnybrook apartments is from campus? |Students say the walk is around 15 minutes. |Students mention that Donnybrook apartments is about a 15-minute walk from campus (source: reddit_housing1). Another student notes that it is a few miles away from one side of campus, but mentions that friends have walked (source: reddit_housing5). Additionally, the apartment's official information states it is 0.5 miles from Towson University Main Campus (source: Donnybrook Apartments Reviews). |Relavent |Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis


**Question that failed:**
What do students think about university village management
**What the system returned:**
There is no information provided about University Village management in the given context, only a mention of Towson Town Place having terrible management (source: Towson Town Place Reviews). University Village is discussed in terms of its proximity to campus, price, and thin walls, but not its management (source: reddit_housing5, reddit_housing4).
**Root cause (tied to a specific pipeline stage):**
The embedding model treats the phrase "UV" and "University Village" as seperate ideas, and thus did not utilize UniversityVillageReviews.txt
**What you would change to fix it:**
I would incorporate additional chunks gathered from specific documents when the document's name is mentioned during retrieval. I could also add instructions to manually reference university village when uv is mentioned, but that seems like it wouldn't be efficient in the long run.

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
I was able to follow the spec to implement chunking strategy, as I wrote out what my thought process for it was, and I was able to understand why I made the choices I did. It helped me first plan out my goals then work on implementing them, the structure was useful for focusing my work.
**One way your implementation diverged from the spec, and why:**
The main way it diverged was by me changing the size. I had initially chosen a context window of 200 characters, but that proved to be too short for even the reddit comments. I decided to then utilize 300 character windows, and additionally separate the chunks by sentences, which worked a lot better in terms of minimizing cut off sentences.
---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

I gave the AI my chunking strategy section and asked it to implement chunk_document(). It returned a function that did exactly what I asked it to, split the chunks every 200 characters with a 20 character overlap. I decided that this approach was creating too many split sentences and researched methods of preventing that from happening, and found sentence splitting. I then implemented a basic version of it, splitting every sentence into a chunk, before asking Claude to alter the inital code to maintain roughly a 300 character chunk size but seperating exclusively on punctuation.

**Instance 2**

I gave Claude a set of guidelines for what the LLM should and should not do and asked it to implement generate_response(). It returned a system prompt outlining what the LLM should and should not do and the generate_response function that outputs the user response. I overrode the system prompt by removing rules that indicated it should start off sentences with "according to" and added an example for what a correct response should look like.