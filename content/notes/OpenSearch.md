---
tags:
  - software-engineering
draft: true
aliases:
  - Knowledge/Tech-Science/OpenSearch
---
> [!SUMMARY] OpenSearch is a distributed search and analytics engine built on Apache Lucene (a powerful search & retrieval library).

> [!example] References
> - OpenSearch [docs](https://opensearch.org/docs/)
> - My Demo/Tutorial Github [Repo](https://github.com/prasanth-ntu/opensearch-tutorial-1)

# Dev Tools → Console

> [!TIP] Think of **Dev Tools Console** as:
> **Postman + SQL console + admin shell for OpenSearch**
> But **safer** and **faster** for experimentation.
## What it is

> [!SUMMARY] An **interactive API console** for running **any OpenSearch REST API**.
  
It understands OpenSearch syntax, auto-completes APIs, and shows responses nicely.

## What you can do there
- Search & queries (`GET`)
- Index management (`PUT`, `DELETE`, `GET`)
- Mappings
- Document operations (CRUD)
- Aggregations
- Cluster & health checks
- Bulk operations
- Security APIs
- Debugging / experimentation

# Query DSL
## What it is

> [!SUMMARY] **Query DSL is OpenSearch’s JSON-based language for defining search, filtering, and relevance logic in the Search API.**

**Query DSL** stands for **Query Domain Specific Language**.

In **OpenSearch / Elasticsearch**, it is:
> **A JSON-based language used to describe search and filtering logic**

You use it inside the `_search` API to tell OpenSearch **what to search**, **how to match**, and **how to combine conditions**.

## **What “DSL” means in general**

A **Domain Specific Language** is a language designed for **one specific problem domain**.

Examples:
- **SQL** → relational databases
- **Regex** → pattern matching
- **Query DSL** → search & relevance
- **KQL / Lucene** → search filters

So **Query DSL** is the _search language_ of OpenSearch.

## **What you can express with Query DSL**

Using Query DSL, you can define:
- 🔍 **Full-text search** (match, match_phrase)
- 🎯 **Exact matches** (term, terms)
- 🔗 **Boolean logic** (bool: must / should / must_not)
- 📊 **Filtering** (filter)
- 🧮 **Scoring & relevance**
- 📈 **Aggregations** (group by, stats)
- 📍 **Range queries** (dates, numbers)
- 🧠 **Fuzzy / typo-tolerant search**
    
All in **structured JSON**.