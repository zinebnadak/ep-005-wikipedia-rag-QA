# Episode 005 - Wikipedia RAG Q&A

> [One sentence single takeaway from this project.]

## The Problem / The Question
Second RAG build. Wikipedia as the data source, same overall pattern as my first project (ha.ax) but rebuilt with evaluation, better chunking, hybrid search, and reranking — because you don't own a pattern after building it once. I also wanted to stress-test it: does a standard RAG pipeline break when the data gets messier? Wikipedia text is noisier than a university website. Inconsistent heading structure, much longer articles, irrelevant sections mixed into the prose, tables and infoboxes interrupting flow. I wanted to measure how a RAG pipeline actually behaves on large, unstructured, real-world corpora.

## What I built
An AI-powered tool that lets you explore and study Wikipedia articles through a retrieval-based chat. 

## Features
- provide a valid wikipedia URL 
- ask questions about the content using natural language
- Session management to maintain context between questions

## What I Learned
- [Specific finding — not generic]
- [The thing that surprised me]
- [The assumption that broke]
- [The detail worth remembering]

## How to Run
Step-by-step instructions. 

## Tech Used
- Lightweight but effective text embeddings using paraphrase-MiniLM-L6-v2
- [Library or tool and why it was chosen]

## References
- [Inspo](https://medium.com/@perfectsolution808/wikipedia-based-q-a-chatbot-a-beginners-approach-using-free-tools-5067d501a6ab)
- [Wikipedia](https://www.wikipedia.org/)