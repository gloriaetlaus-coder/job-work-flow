import os
from weasyprint import HTML

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(BASE_DIR, 'resume_general.html')
pdf_path = os.path.join(BASE_DIR, 'resume_general.pdf')

HTML(filename=html_path).write_pdf(pdf_path)
print(f'PDF generated: {pdf_path}')
