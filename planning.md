# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
I chose reviews of off campus housing for Towson University. This knowledge is hard to find through official channels due to no review system on the university's option list for off campus housing, and while a tool does exist for that, the reviews on it are scarce and inconsistent in distribution.
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 |What do students recommend as the best off campus housing option? |Towson Place due to low price, closeness to campus, and lack of major problems. |
| 2 |What are the benefits and downsides of Towson Place? |Benefits include low price and low distance to campus, downsides include loud noises and weed smell. |
| 3 |What are the benefits and downsides of University Village? |Benefits include low price and low distance to campus. Downsides include cheap furnishings and old apartments. |
| 4 |What do students say are the benefits of Aspen? |Benefits include close to campus and individual leases. |
| 5 |How long of a walk do students say Donnybrook apartments is from campus? |Students say the walk is around 15 minutes. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
