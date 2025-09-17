from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# 모델 로딩 (최초 1회만)
model_name = "digit82/kobart-summarization"  # 또는 원하는 한국어 요약 모델
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# 요약 함수
def summarize_text(text: str, max_len: int = 512) -> str:
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_len, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)