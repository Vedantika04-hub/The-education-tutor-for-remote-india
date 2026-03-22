from fastapi import FastAPI, UploadFile, File
from ingest import ingest_pdf
from query import get_relevant_chunks
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_location = f"data/textbooks/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    ingest_pdf(file_location)

    return {"message": "PDF uploaded and processed"}

@app.get("/ask/")
def ask_question(q: str):
    chunks = get_relevant_chunks(q)

    # Context Pruning Applied Here 🔥
    context = "\n".join(chunks)

    # Simple answer (can connect OpenAI later)
    answer = f"Based on textbook:\n{context[:500]}..."

    return {
        "question": q,
        "answer": answer
    }

    if chunks is None:
    return {"answer": "Please upload a textbook first"}
