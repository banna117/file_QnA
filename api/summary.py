from fastapi import APIRouter
import os

from services.summarizer import summarize_text

router = APIRouter()

TEXT_DIR = "storage/texts/"

@router.get("/summary/{doc_id}")
def get_summary(doc_id: str):
    path = os.path.join(TEXT_DIR, f"{doc_id}.txt")
    if not os.path.exists(path):
        return {"error": "문서를 찾을 수 없습니다."}

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    summary = summarize_text(text)
    return {
        "doc_id": doc_id,
        "summary": summary
    }