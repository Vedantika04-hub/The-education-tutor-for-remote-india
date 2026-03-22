# 📚 AI Tutor – Low-Cost Intelligent Tutoring System

## 🚀 Overview

AI Tutor is a low-cost, intelligent tutoring web application designed for students in low-resource environments such as rural India. It can ingest full state-board textbooks (PDFs) and provide accurate, curriculum-aligned answers while minimizing API costs and data usage.

This system uses **Context Pruning + Retrieval-Augmented Generation (RAG)** to ensure only the most relevant content is processed for each query.

---

## 🎯 Problem Statement

Traditional AI tutors rely on large models that:

* Require high internet bandwidth
* Have high latency
* Are expensive per query

This makes them impractical for rural or low-connectivity regions.

---

## 💡 Our Solution

We built an AI Tutor that:

* Works with **entire textbooks**
* Uses **local embeddings (no API cost)**
* Applies **Context Pruning** to reduce unnecessary data transfer
* Provides fast and relevant answers

---

## 🧠 Key Features

* 📄 Upload and process large textbook PDFs
* 🔍 Intelligent semantic search using FAISS
* ✂️ Context Pruning (only relevant chunks sent to model)
* ⚡ Fast responses with minimal latency
* 💸 Reduced API cost (compared to baseline RAG)
* 🌐 Simple web interface

---

## 🏗️ Tech Stack

### Backend

* FastAPI
* Python
* FAISS (Vector Search)
* Sentence Transformers (Embeddings)

### Frontend

* HTML
* CSS
* JavaScript

---

## 📂 Project Structure

```
ai-tutor/
│
├── backend/
│   ├── main.py
│   ├── ingest.py
│   ├── query.py
│   ├── utils.py
│   ├── requirements.txt
│   └── data/
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── README.md
```

---

## ⚙️ How It Works

### 1️⃣ PDF Ingestion

* Upload textbook PDF
* Extract text
* Split into chunks
* Generate embeddings
* Store in FAISS vector database

### 2️⃣ Query Processing

* User asks a question
* System converts query into embedding
* Searches top relevant chunks

### 3️⃣ Context Pruning (Core Innovation)

* Only top **K relevant chunks** are selected
* Entire textbook is NOT sent to the model
* Reduces:

  * API cost 💸
  * Latency ⚡
  * Data usage 📉

---

## ▶️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/ai-tutor.git
cd ai-tutor
```

### 2. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Run Backend Server

```bash
uvicorn main:app --reload
```

Server will run on:

```
http://127.0.0.1:8000
```

---

### 4. Run Frontend

* Open `frontend/index.html` in browser

---

## 📌 API Endpoints

### Upload PDF

```
POST /upload/
```

### Ask Question

```
GET /ask/?q=your_question
```

---

## 📊 Cost Optimization Strategy

| Feature            | Baseline RAG | Our System   |
| ------------------ | ------------ | ------------ |
| Full document sent | ❌ Yes        | ✅ No         |
| Context pruning    | ❌ No         | ✅ Yes        |
| Embeddings         | Paid API     | Local (Free) |
| Cost per query     | High         | Very Low     |

---

## 🔥 Future Improvements

* 🌍 Multi-language support (Marathi + Hindi)
* 🎙️ Voice-based interaction
* 🧑‍🎓 Personalized learning paths
* 📶 Offline / low-internet mode
* 🤖 Integration with LLM APIs (OpenAI / Gemini)

---

## 👨‍💻 Author

Vedantika Jadhav
B.Tech CSE (AIML)

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
