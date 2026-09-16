# Problem Statement 1

## Q1. API Data Retrieval and Storage

You are tasked with fetching data from an external REST API, storing it in a local SQLite database, and displaying the retrieved data. The API provides a list of books in JSON format with attributes like title, author, and publication year.

**Implementation:** [`task1_books_api_sqlite.py`](./task1_books_api_sqlite.py)

I used an Open Library API to fetch the data in JSON Format .The code retrieves the title,author and publication year and store them in SQLite database using queries. After inserting the data it extracts them from the database and displays them. I also have added an API error handling by including a 10 sec timeout with a status check. I made sure records are cleared before inserting the latest API response as it kept on appending after every new run. 
---

## Q2. Data Processing and Visualization

Given a dataset containing information about students' test scores, fetch the data from an API, calculate the average score, and create a bar chart to visualize the data.

**Implementation:** [`task2_student_scores.py`](./task2_student_scores.py)

---

## Q3. CSV Data Import to a Database

Write a Python script that reads data from a CSV file containing user information (e.g., name, email) and inserts it into a SQLite database.

**Implementation:** [`task3_csv_to_sqlite.py`](./task3_csv_to_sqlite.py)

**CSV File:** [`users.csv`](./users.csv)

---

## Q4. Most Complex Python Code

[Authentication Anomaly Detection and Risk Scoring Model](https://github.com/jaden-mas1010/Design-of-an-Authentication-Anomaly-Detection-and-Risk-Scoring-Model-)

ML-based authentication anomaly detection — Isolation Forest model, a 12-rule detection engine, composite risk scorer, FastAPI service layer, SQLite persistence, 34 passing pytest tests. Built as my MSc dissertation in partnership with PMS Ltd.

---

## Q5. Most Complex Database Code

[Employee Device & Login Analysis — SQL Project](https://github.com/jaden-mas1010/SQL-PROJECT)

SQL-based employee device and login analysis using aggregations, `GROUP BY`, `HAVING`, `INNER JOIN`, `LEFT JOIN`, window functions with `PARTITION BY`, and queries for identifying anomalous login activity.

---

# Problem Statement - Assignment 2

## Q1. Where would you rate yourself on LLM, Deep Learning, AI and ML?

| Area | Rating |
|---|---|
| LLM | B |
| Deep Learning | C |
| AI | B |
| ML | B |

---

## Q2. What are the key architectural components to create a chatbot based on LLM? Please explain the approach on a high-level

### Overall Approach

For this task my goal of the architecture is to take the user questions, understand the context, fetch the required information depending on the user’s permission, generate a clean response which returns it safely to the user.

### Frontend

The frontend is the main interface that interacts with the user, receives their query, sends it to the backend and is also responsible for displaying the final response by the system.

### Backend

The backend is the main orchestrator where it initially receives the request from the frontend, checks the authentication and authorization of the user and if it is allowed to access the requested information. It decides whether to call RAG or APIs, assembles the system prompt, context and chat history, and sends a clean request to the LLM. Security controls should be enforced at this layer.

### RAG

RAG helps when the request requires information outside the LLM’s built-in knowledge or available context.

Before retrieval, documents are split into smaller chunks, converted into numerical embeddings using an embedding model, and stored in a vector database.

When the user asks a question, the query is also converted into an embedding. The query embedding is then used to search the vector database for semantically similar document chunks. The most relevant chunks are retrieved and passed to the LLM as additional context to help generate a grounded response.

### External APIs / Tools

When a user’s request requires a specific action, such as adding a reminder to a calendar, the system can select the appropriate API or tool to perform the requested task. The LLM can help determine which action or tool is required, but the backend should validate the user’s permissions and control the actual execution.

### Conversation Memory

Conversation memory helps maintain the history and context of the chat so that the user does not have to repeat everything continuously. This is managed by the backend, which can maintain recent messages or summarize older chat history to provide relevant context to the LLM.

### LLM

The LLM is responsible for understanding the instructions, context and rules given by the backend and generate the natural language response. It can receive the system instructions, user query, relevant conversation history and information retrieved through RAG.

### Security and Guardrails

Security and guardrails help make sure the user only gets access to the information or actions they are allowed to. Authentication checks who the user is, while authorization checks what the user is allowed to access or perform. Additional guardrails can also protect sensitive data, RAG and external tools from risks like prompt injection or unauthorized access.

### Logging and Monitoring

Logging and monitoring help us understand how the chatbot is performing and identify if something goes wrong. The system can monitor things like response time, failed requests, token usage, API or tool errors and LLM responses.

### High-Level Approach

At a high level, the chatbot works by receiving the user's query through the frontend and sending it to the backend, which acts as the main orchestrator.

The backend manages the conversation context, checks authentication and authorization, and decides whether the request can be answered directly by the LLM or whether additional information is required through RAG or an external API/tool.

If RAG is required, the query is converted into an embedding and used to search a vector database for relevant document chunks. If live information or an action is required, the backend can call the appropriate external API or tool after validating the user's permissions.

The backend then prepares the system prompt together with the user query, the relevant chat history and any procured context, and sends this to the LLM.

The LLM generates the natural-language response, which is returned to the backend and then displayed to the user through the frontend.

Throughout the process, security controls and logging/monitoring are used to make sure access is controlled and the chatbot is operating correctly.

---

## Q3. Please explain vector databases

### What is a Vector Database?
...

### How Vector Search Works
...

### Hypothetical Problem
...

### Options Considered
...

### Database Comparison

...

### My Selection
...

### Why I Selected It
...

---

## Repository Files

...
