# ✦ EduMind AI — Smart Student Assistant

A dark-mode AI learning workspace built with Python, Streamlit and Google's Gemini API.

## Features
- **AI Study Chat:** Ask academic questions and receive structured explanations.
- **PDF Summarizer:** Extract text from text-based PDFs and generate study notes.
- **Quiz Generator:** Create multiple-choice practice questions from a topic or pasted notes.
- **Smart Study Planner:** Generate a timetable based on subjects, available hours and duration.
- **Cloud-ready:** Deploy the app on Streamlit Community Cloud and keep the API key in platform Secrets.

## Technology
- Python 3.11 or 3.12
- Streamlit — user interface
- Google Gemini API (`google-genai`) — AI responses
- pypdf — PDF text extraction
- Streamlit Community Cloud — hosting

## 1. Install the software
1. Install Python 3.11 or 3.12 from https://www.python.org/downloads/
2. During Windows installation, tick **Add Python to PATH**.
3. Install Visual Studio Code from https://code.visualstudio.com/
4. Extract the `EduMind_AI.zip` folder.
5. In VS Code, choose **File → Open Folder** and select `EduMind_AI`.

## 2. Create a virtual environment (Windows)
Open **Terminal → New Terminal** in VS Code and run these commands one by one:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If `py -3.12` is not recognized, try:
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Get your Gemini API key
1. Open https://aistudio.google.com/app/apikey
2. Sign in with your Google account.
3. Create an API key and copy it.
4. In the project, open `.streamlit`.
5. Make a copy of `secrets.toml.example` and rename the copy to **`secrets.toml`**.
6. Open `secrets.toml` and replace the example value:

```toml
GEMINI_API_KEY = "your_real_key_here"
```

Keep the key private. Do not upload `secrets.toml` to GitHub or share it in screenshots. The `.gitignore` file excludes it.

## 4. Run the app locally
In the VS Code terminal (with `.venv` activated), run:

```powershell
python -m streamlit run app.py
```

Your browser should open the app at `http://localhost:8501`. If it does not, copy that address into Chrome.

To stop the app, click the terminal and press **Ctrl + C**.

## 5. Deploy to the cloud (Streamlit Community Cloud)
1. Create/sign in to GitHub at https://github.com/
2. Create a **public** repository, for example `edumind-ai`.
3. Upload the project files to the repository. Do **not** upload `.streamlit/secrets.toml`.
4. Open https://share.streamlit.io/ and sign in with GitHub.
5. Click **Create app** and select your repository, branch (`main`) and main file path (`app.py`).
6. Open **Advanced settings → Secrets** and paste:

```toml
GEMINI_API_KEY = "your_real_key_here"
```

7. Click **Deploy**. Streamlit will build the app and provide a public `*.streamlit.app` URL.

Your app is now hosted in the cloud. Gemini processes AI requests through Google's API. The Streamlit app host and Gemini API are separate cloud services.

## 6. How to use the app
- **AI Study Chat:** Type a question in the chat box and press Enter.
- **PDF Summarizer:** Upload a text-based PDF, choose the summary style, then click Generate summary.
- **Quiz Generator:** Enter a topic, choose difficulty and number of questions, then generate.
- **Study Planner:** Enter subjects, daily study hours and plan duration, then generate.

## Project structure

```text
EduMind_AI/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml.example
└── src/
    ├── __init__.py
    ├── ai_service.py
    ├── document_utils.py
    └── ui.py
```

## Important notes
- A Gemini API key and internet connection are required for AI features.
- API availability, model access and usage limits depend on Google's current terms and account eligibility. Check the AI Studio dashboard for current limits.
- PDF summarization works with selectable text. Scanned PDFs need OCR, which is not included in this starter version.
- Uploaded PDF text is sent to Gemini when you request a summary. Do not upload confidential or sensitive documents.
- Chat and generated results are held in the current Streamlit session; this starter version does not provide permanent user accounts or database storage.
- The free cloud hosting/API tiers may have limits and can change. Check current provider terms before a public demonstration.

## Troubleshooting
**`streamlit` is not recognized**
```powershell
python -m streamlit run app.py
```

**Gemini key not found**
- Confirm the filename is exactly `.streamlit/secrets.toml`.
- Confirm the key name is exactly `GEMINI_API_KEY`.
- Restart Streamlit after changing secrets.

**No text extracted from PDF**
- Try a PDF where you can select and copy text. Scanned image PDFs are not supported by this version.

**AI request fails**
- Check your internet connection and API key.
- Check API access, model availability and usage limits in Google AI Studio.
