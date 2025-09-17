from fastapi import APIRouter, UploadFile, File
import uuid, os, shutil
from services.extractor import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = "storage/pdfs/"
TEXT_DIR = "storage/texts/"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(TEXT_DIR, exist_ok=True)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # 고유 ID 생성
    doc_id = str(uuid.uuid4())
    pdf_path = os.path.join(UPLOAD_DIR, f"{doc_id}.pdf")
    
    # PDF 저장
    with open(pdf_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    # 텍스트 추출
    extracted_text = extract_text_from_pdf(pdf_path)

    # 텍스트 저장
    text_path = os.path.join(TEXT_DIR, f"{doc_id}.txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    return {
        "doc_id": doc_id,
        "message": "PDF uploaded and text extracted successfully"
    }