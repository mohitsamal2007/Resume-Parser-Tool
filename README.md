# 📄 AI Resume Parser

An AI-powered Resume Parser built using Python that extracts and organizes important information from resumes automatically. This project helps streamline recruitment and HR processes by converting unstructured resume data into structured information.

---

# 🚀 Features

- Extracts text from PDF resumes
- Parses candidate details automatically
- Extracts:
  - Name
  - Email
  - Phone Number
  - Skills
  - Education
  - Experience
- NLP-based text processing
- Streamlit web interface
- Easy-to-use and customizable

---

# 🛠️ Technologies Used

- Python
- Streamlit
- spaCy
- PyPDF2
- Regular Expressions (re)
- Pandas

---

# 📂 Project Structure

```bash
resume-parser/
│
├── app.py                  # Streamlit application
├── parser.py               # Resume parsing logic
├── requirements.txt        # Required libraries
├── resumes/                # Sample resumes
└── README.md               # Project documentation
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/resume-parser.git
cd resume-parser
```

---

## 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit spacy PyPDF2 pandas
```

Download spaCy model:

```bash
python -m spacy download en_core_web_sm
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🧠 How It Works

1. Upload resume in PDF format
2. Extract text from resume
3. Apply NLP techniques
4. Identify important entities
5. Display structured information

---

# 📌 Extracted Information

The parser can extract:

- Candidate Name
- Email Address
- Contact Number
- Technical Skills
- Educational Qualifications
- Work Experience

---

# 📸 Workflow

1. Open Streamlit application
2. Upload resume PDF
3. Click Parse Resume
4. View extracted information instantly

---

# 🔧 Future Improvements

- Multiple resume format support
- Better skill extraction using AI
- Resume ranking system
- Database integration
- Cloud deployment

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a branch
3. Commit changes
4. Push changes
5. Open Pull Request

---

# 📜 License

This project is for educational purposes only.

---

# 👨‍💻 Author

Developed by Mohit Samal
