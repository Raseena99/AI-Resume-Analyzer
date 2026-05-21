from sqlalchemy import Column, Integer, String, Float
from .database import Base
class ResumeAnalysis(Base):
__tablename__ = "resume_analysis"
id = Column(Integer, primary_key=True, index=True)
candidate_name = Column(String)
email = Column(String)
score = Column(Float)
matched_skills = Column(String)
missing_skills = Column(String)
