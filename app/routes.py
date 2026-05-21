import os
from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import ResumeAnalysis
from .resume_parser import extract_text_from_pdf
from .resume_parser import extract_email
from .resume_parser import extract_name
from .skill_matcher import find_matching_skills
from .skill_matcher import calculate_resume_score
router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
def get_db():
db = SessionLocal()
try:
yield db
finally:
db.close()
@router.post("/analyze")
async def analyze_resume(
file: UploadFile = File(...),
db: Session = Depends(get_db)
):
file_path = os.path.join(UPLOAD_DIR, file.filename)
with open(file_path, "wb") as buffer:
buffer.write(await file.read())
text = extract_text_from_pdf(file_path)
email = extract_email(text)
candidate_name = extract_name(text)
matched_skills, missing_skills = find_matching_skills(text)
score = calculate_resume_score(text)
analysis = ResumeAnalysis(
candidate_name=candidate_name,
email=email,
score=score,
matched_skills=", ".join(matched_skills),
missing_skills=", ".join(missing_skills)
)
db.add(analysis)
db.commit()
db.refresh(analysis)
return {
"candidate_name": candidate_name,
"email": email,
"score": score,
"matched_skills": matched_skills,
"missing_skills": missing_skills
}
