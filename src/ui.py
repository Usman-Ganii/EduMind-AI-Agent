import streamlit as st

def load_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&family=Caveat:wght@500;600&display=swap');
    :root { color-scheme: dark; }
    html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
    .stApp { background: radial-gradient(ellipse at 15% 0%, rgba(91,67,170,.17), transparent 38%), #090d18; color: #edf0ff; }
    [data-testid="stHeader"] { background: rgba(9,13,24,.82); }
    [data-testid="stSidebar"] { background: #0d1322; border-right: 1px solid rgba(148,163,184,.13); }
    [data-testid="stSidebar"] * { color: #dce4fa; }
    h1,h2,h3 { letter-spacing: -.045em; color: #f4f5ff; }
    h1 { font-weight: 700; }
    p, label, .stMarkdown { color: #c4cbe0; }
    .hero { padding: 32px 36px 34px; border: 1px solid rgba(155,139,255,.22); border-radius: 24px; background: linear-gradient(120deg,rgba(92,65,175,.23),rgba(27,143,178,.10)),rgba(16,23,40,.88); margin: 10px 0 30px; box-shadow: 0 20px 60px rgba(0,0,0,.18); }
    .hero h1 { font-size: clamp(2.5rem,6vw,4.2rem); line-height: 1.02; margin: 15px 0; }
    .hero h1 span { color: #a99aff; font-family: 'Caveat', cursive; font-weight: 600; letter-spacing: 0; }
    .hero p { font-size: 1.08rem; max-width: 620px; color: #c2cbe0; }
    .eyebrow { color: #a99aff; font: 500 .72rem 'DM Mono',monospace; letter-spacing: .15em; }
    .brand { font-size: 1.35rem; font-weight: 700; letter-spacing: -.05em; padding: 12px 0 22px; color: #f5f3ff; }
    .brand span { color: #a99aff; }
    .feature { min-height: 148px; border: 1px solid rgba(145,160,195,.15); border-radius: 18px; padding: 20px; margin: 8px 0 14px; background: linear-gradient(145deg,rgba(23,33,55,.94),rgba(14,21,36,.96)); }
    .feature-icon { width: 38px; height: 38px; display: grid; place-items: center; border-radius: 12px; color: #c7bcff; background: rgba(139,117,255,.16); font-size: 1.25rem; margin-bottom: 12px; }
    .feature-title { color: #f4f5ff; font-weight: 650; font-size: 1.05rem; margin-bottom: 5px; }
    .feature-desc { color: #aab5ce; font-size: .91rem; line-height: 1.5; }
    .feature-foot { color: #8e9bb8; font-size: .78rem; margin-top: 9px; }
    .notice,.result-panel { border: 1px solid rgba(139,117,255,.22); background: rgba(93,75,164,.10); border-radius: 16px; padding: 18px 20px; margin: 18px 0; }
    .sidebar-note { font-size: .8rem; color: #9eabc6; padding: 10px 12px; border-radius: 12px; background: rgba(30,43,68,.65); }
    .status-dot { display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: #58d6a3; margin-right: 7px; box-shadow: 0 0 12px #58d6a3; }
    .stButton > button, .stDownloadButton > button { border: 1px solid rgba(173,157,255,.38); border-radius: 12px; padding: .62rem 1.15rem; color: #fff; font-weight: 600; background: linear-gradient(105deg,#735be8,#526bdc); box-shadow: 0 7px 22px rgba(91,82,205,.20); transition: all .2s ease; }
    .stButton > button:hover, .stDownloadButton > button:hover { transform: translateY(-2px); border-color: #b8aaff; box-shadow: 0 10px 28px rgba(105,91,225,.32); color: white; }
    .stButton > button[kind="secondary"] { background: rgba(30,41,63,.8); border-color: rgba(148,163,184,.22); }
    .stTextInput input, .stTextArea textarea, [data-baseweb="select"] > div { background: #111a2b !important; border-color: rgba(148,163,184,.22) !important; color: #edf0ff !important; border-radius: 11px !important; }
    [data-testid="stFileUploader"] { background: rgba(20,30,49,.65); border: 1px dashed rgba(159,145,255,.35); border-radius: 15px; padding: 10px; }
    [data-testid="stChatMessage"] { background: rgba(19,29,48,.7); border: 1px solid rgba(148,163,184,.12); border-radius: 15px; }
    .footer { text-align: center; color: #65728f; font: .68rem 'DM Mono',monospace; letter-spacing: .12em; padding: 34px 0 12px; }
    .footer span { color: #8e7bff; padding: 0 6px; }
    #MainMenu, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

def sidebar_brand():
    st.sidebar.markdown('<div class="brand">✦ EduMind<span>AI</span></div>', unsafe_allow_html=True)

def header(title, subtitle):
    st.markdown(f"### {title}")
    st.markdown(f"<p style='color:#94a3bd;margin-top:-8px'>{subtitle}</p>", unsafe_allow_html=True)

def feature_card(icon, title, description, foot):
    st.markdown(f"""
    <div class="feature">
      <div class="feature-icon">{icon}</div>
      <div class="feature-title">{title}</div>
      <div class="feature-desc">{description}</div>
      <div class="feature-foot">{foot}</div>
    </div>
    """, unsafe_allow_html=True)
