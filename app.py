import streamlit as st
from src.ai_service import ask_gemini
from src.document_utils import extract_pdf_text
from src.ui import load_styles, header, feature_card, sidebar_brand

st.set_page_config(page_title="EduMind AI | Student Workspace", page_icon="✦", layout="wide", initial_sidebar_state="expanded")
load_styles()
sidebar_brand()

with st.sidebar:
    st.markdown("### WORKSPACE")
    page = st.radio(
        "Navigate",
        ["Overview", "AI Study Chat", "PDF Summarizer", "Quiz Generator", "Study Planner"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown('<div class="sidebar-note"><span class="status-dot"></span> AI engine · Gemini</div>', unsafe_allow_html=True)
    st.caption("EduMind AI · Learn smarter")

header("Your personal learning copilot", "A focused workspace to understand concepts, learn from notes, and plan your progress.")

if "chat" not in st.session_state:
    st.session_state.chat = []

def run_ai(prompt, context=""):
    with st.spinner("EduMind is thinking…"):
        try:
            return ask_gemini(prompt, context)
        except Exception as exc:
            st.error(f"AI request failed: {exc}")
            return None

if page == "Overview":
    st.markdown('<div class="hero"><div class="eyebrow">✦ YOUR AI-POWERED STUDY SPACE</div><h1>Make learning<br><span>feel effortless.</span></h1><p>Ask better questions. Understand difficult topics. Turn your notes into knowledge.</p></div>', unsafe_allow_html=True)
    st.markdown("### Your learning toolkit")
    c1, c2 = st.columns(2)
    with c1:
        feature_card("◈", "AI Study Chat", "Get clear, step-by-step explanations for difficult concepts.", "Ask questions in natural language.")
        feature_card("▤", "PDF Summarizer", "Upload a PDF and turn long notes into concise study material.", "Works with text-based PDFs.")
    with c2:
        feature_card("✧", "Quiz Generator", "Create practice MCQs from a topic or your own notes.", "Test your understanding.")
        feature_card("⌁", "Smart Study Planner", "Build a realistic timetable around your subjects and available time.", "Stay consistent, not overwhelmed.")
    st.markdown('<div class="notice"><b>Getting started</b><br>To activate AI features, add your Gemini API key in the setup instructions. Your key is never placed in the source code.</div>', unsafe_allow_html=True)

elif page == "AI Study Chat":
    st.markdown("## ◈ AI Study Chat")
    st.caption("Ask anything from programming and databases to mathematics and communication skills.")
    for item in st.session_state.chat:
        with st.chat_message(item["role"]):
            st.markdown(item["content"])
    question = st.chat_input("Ask a study question…")
    if question:
        st.session_state.chat.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)
        context = "\n".join(f'{m["role"].upper()}: {m["content"]}' for m in st.session_state.chat[-8:])
        answer = run_ai(
            "You are EduMind, a patient and expert academic tutor. Explain accurately in simple language, use examples, define technical terms, and structure long answers with headings. If uncertain, say so.\n\nConversation:\n" + context
        )
        if answer:
            st.session_state.chat.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.markdown(answer)
    if st.button("Clear conversation", type="secondary"):
        st.session_state.chat = []
        st.rerun()

elif page == "PDF Summarizer":
    st.markdown("## ▤ PDF Summarizer")
    st.caption("Upload class notes, a chapter, or study material. EduMind will create revision-ready notes.")
    uploaded = st.file_uploader("Choose a PDF file", type=["pdf"], help="Use a text-based PDF. Scanned image-only PDFs may not contain extractable text.")
    style = st.selectbox("Summary style", ["Detailed study notes", "Short revision summary", "Key points and definitions", "Exam-focused notes"])
    if uploaded:
        if uploaded.size > 15 * 1024 * 1024:
            st.error("Please upload a PDF smaller than 15 MB.")
        else:
            with st.spinner("Reading your PDF…"):
                text = extract_pdf_text(uploaded.getvalue())
            if not text.strip():
                st.warning("No readable text was found. This may be a scanned PDF. Try a text-based PDF.")
            else:
                st.success(f"Extracted text from your PDF · {len(text):,} characters")
                with st.expander("Preview extracted text"):
                    st.text(text[:3500] + ("…" if len(text) > 3500 else ""))
                if st.button("✦ Generate summary", type="primary"):
                    result = run_ai(
                        f"Create {style.lower()} from the supplied study material. Preserve important facts and terminology. Do not invent information. Use clear headings and bullet points.",
                        text[:45000]
                    )
                    if result:
                        st.markdown('<div class="result-panel">', unsafe_allow_html=True)
                        st.markdown(result)
                        st.markdown('</div>', unsafe_allow_html=True)
                        st.download_button("Download summary (.md)", result, file_name="edumind_summary.md", mime="text/markdown")

elif page == "Quiz Generator":
    st.markdown("## ✧ Quiz Generator")
    st.caption("Create a quick practice test and check your understanding.")
    topic = st.text_input("Topic", placeholder="e.g. SQL joins, operating systems, probability")
    level = st.select_slider("Difficulty", options=["Beginner", "Intermediate", "Advanced"], value="Intermediate")
    count = st.slider("Number of questions", 3, 10, 5)
    source = st.text_area("Optional: paste your notes or syllabus", height=130, placeholder="Paste the material you want the quiz to cover…")
    if st.button("Generate my quiz", type="primary", disabled=not topic.strip()):
        prompt = f"""Create {count} multiple-choice questions on {topic}. Difficulty: {level}.
Use the supplied notes as the source if provided. Give four options (A-D) per question, then an answer key with a one-sentence explanation. Ensure exactly one correct answer per question. Format in Markdown."""
        result = run_ai(prompt, source[:30000])
        if result:
            st.session_state.quiz_result = result
    if st.session_state.get("quiz_result"):
        st.markdown('<div class="result-panel">', unsafe_allow_html=True)
        st.markdown(st.session_state.quiz_result)
        st.markdown('</div>', unsafe_allow_html=True)
        st.download_button("Download quiz (.md)", st.session_state.quiz_result, file_name="edumind_quiz.md", mime="text/markdown")

elif page == "Study Planner":
    st.markdown("## ⌁ Smart Study Planner")
    st.caption("Tell EduMind what you need to study and how much time you have.")
    subjects = st.text_area("Subjects and topics", placeholder="1. DBMS – normalization and SQL joins\n2. Python – functions and OOP\n3. Mathematics – probability", height=150)
    hours = st.slider("Study hours available per day", 1, 12, 4)
    days = st.slider("Plan duration (days)", 1, 30, 7)
    preference = st.selectbox("Preferred study style", ["Balanced sessions with breaks", "Short focused sessions", "Long deep-work sessions"])
    if st.button("Build my study plan", type="primary", disabled=not subjects.strip()):
        prompt = f"""Create a practical {days}-day study timetable for a student with {hours} study hours per day.
Study style: {preference}. Subjects and topics:\n{subjects}
Include daily time blocks, short breaks, revision, and practice. Prioritize difficult topics sensibly. Do not schedule more than the available hours. Format as a clear Markdown table and add brief tips."""
        result = run_ai(prompt)
        if result:
            st.session_state.study_plan = result
    if st.session_state.get("study_plan"):
        st.markdown('<div class="result-panel">', unsafe_allow_html=True)
        st.markdown(st.session_state.study_plan)
        st.markdown('</div>', unsafe_allow_html=True)
        st.download_button("Download study plan (.md)", st.session_state.study_plan, file_name="edumind_study_plan.md", mime="text/markdown")

st.markdown('<div class="footer">EDUMIND AI <span>·</span> Learn with clarity. Grow with confidence.</div>', unsafe_allow_html=True)
