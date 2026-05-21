import re
from PyPDF2 import PdfReader
def extract_text_from_pdf(file_path: str):
text = ""
reader = PdfReader(file_path)
for page in reader.pages:
text += page.extract_text()
return text
def extract_email(text: str):
pattern = r'[\w\.-]+@[\w\.-]+'
match = re.search(pattern, text)
return match.group(0) if match else "Not Found"
def extract_name(text: str):
lines = text.split('\n')
3
for line in lines:
if len(line.strip()) > 2:
return line.strip()
return "Unknown"
