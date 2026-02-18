import streamlit as st
from google import genai
import time

st.set_page_config(
    page_title="DSA Instructor",
    page_icon="🧠",
    layout="wide",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

/* ─── Global ─── */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background-color: #0a0a0f;
    color: #e8e6f0;
}

/* ─── Hide Streamlit chrome ─── */
#MainMenu, footer, header { visibility: hidden; }

/* ─── Hero Banner ─── */
.hero {
    background: linear-gradient(135deg, #1a0533 0%, #0d1b3e 50%, #001a1a 100%);
    border: 1px solid #2a1a4e;
    border-radius: 20px;
    padding: 48px 40px 36px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
    text-align: center;
}
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 30% 50%, rgba(120,60,220,0.18) 0%, transparent 60%),
                radial-gradient(ellipse at 75% 20%, rgba(0,200,180,0.12) 0%, transparent 50%);
    pointer-events: none;
}
.hero h1 {
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -1px;
    margin: 0;
    background: linear-gradient(90deg, #c084fc, #60a5fa, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    color: #94a3b8;
    font-size: 1.05rem;
    margin-top: 10px;
    font-family: 'Space Mono', monospace;
}

/* ─── Chat Bubbles ─── */
.user-bubble {
    background: linear-gradient(135deg, #1e1b4b, #2e1065);
    border: 1px solid #4c1d95;
    border-radius: 16px 16px 4px 16px;
    padding: 14px 20px;
    margin: 20px 0 8px auto;
    max-width: 75%;
    font-family: 'Space Mono', monospace;
    font-size: 0.92rem;
    color: #c4b5fd;
    box-shadow: 0 4px 20px rgba(139,92,246,0.15);
}
.user-label {
    text-align: right;
    font-size: 0.7rem;
    color: #7c3aed;
    font-family: 'Space Mono', monospace;
    margin-bottom: 4px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* ─── Section cards ─── */
.section-card {
    background: #111120;
    border: 1px solid #1e2040;
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 20px;
}
.section-title {
    font-size: 0.75rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #60a5fa;
    font-family: 'Space Mono', monospace;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* ─── Resource links ─── */
.link-chip {
    display: inline-block;
    background: #1a1a2e;
    border: 1px solid #2d2d5e;
    border-radius: 8px;
    padding: 6px 14px;
    margin: 4px;
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    color: #93c5fd;
    text-decoration: none;
    transition: all 0.2s;
}
.link-chip:hover {
    background: #7c3aed22;
    border-color: #7c3aed;
    color: #c4b5fd;
}
.yt-chip {
    border-color: #ef444440;
    color: #fca5a5;
}
.yt-chip:hover {
    background: #ef444422;
    border-color: #ef4444;
    color: #fca5a5;
}

/* ─── Input ─── */
.stChatInput > div {
    background: #111120 !important;
    border: 1px solid #2d2d5e !important;
    border-radius: 14px !important;
}

/* ─── Spinner ─── */
.stSpinner > div { color: #7c3aed; }

/* ─── Images grid ─── */
.img-grid { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 10px; }
.img-grid img { border-radius: 10px; border: 1px solid #2d2d5e; flex: 1; min-width: 160px; max-width: 240px; object-fit: cover; height: 150px; }
</style>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>🧠 DSA Instructor</h1>
  <p>your personal data structures & algorithms mentor</p>
</div>
""", unsafe_allow_html=True)

# ── API Setup ──────────────────────────────────────────────────────────────────
API_KEY = "AIzaSyBIz3ps2rJShk7eaWSMX1_9_XU2VE8RW7Y"
client = genai.Client(api_key=API_KEY)

# ── Session state for chat history ────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Render chat history ────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<p class="user-label">▸ YOU</p><div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        with st.chat_message("assistant", avatar="🧠"):
            st.markdown(msg["content"])

# ── Resource helper ────────────────────────────────────────────────────────────
def get_resources(topic: str) -> dict:
    """Ask Gemini for curated resources as structured text."""
    res_prompt = f"""For the DSA topic "{topic}", give me EXACTLY this format (no markdown, no extra text):

BLOGS:
1. Title | https://url.com
2. Title | https://url.com
3. Title | https://url.com

YOUTUBE:
1. Title | https://youtube.com/watch?v=xxx
2. Title | https://youtube.com/watch?v=xxx
3. Title | https://youtube.com/watch?v=xxx

Only real, working URLs. Prefer GeeksforGeeks, Baeldung, JavaPoint for blogs. Prefer Abdul Bari, William Fiset, NeetCode for YouTube."""

    try:
        r = client.models.generate_content(model="gemini-2.5-flash", contents=res_prompt)
        lines = r.text.strip().splitlines()
        blogs, yt = [], []
        mode = None
        for line in lines:
            if "BLOGS:" in line:
                mode = "blog"
            elif "YOUTUBE:" in line:
                mode = "yt"
            elif "|" in line and mode:
                parts = line.split("|", 1)
                title = parts[0].strip().lstrip("123456789. ")
                url = parts[1].strip()
                if mode == "blog":
                    blogs.append((title, url))
                else:
                    yt.append((title, url))
        return {"blogs": blogs, "youtube": yt}
    except Exception:
        return {"blogs": [], "youtube": []}

# ── Main DSA handler ───────────────────────────────────────────────────────────
def handle_dsa(prompt: str):
    # Show user bubble
    st.markdown(f'<p class="user-label">▸ YOU</p><div class="user-bubble">{prompt}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant", avatar="🧠"):
        # ── 1. Main explanation ──
        with st.spinner("Generating explanation..."):
            main_prompt = f"""You are a Data Structures and Algorithms (DSA) assistant. Follow these rules strictly:

1. ONLY answer questions related to {prompt} and data structures, algorithms, time complexity, and space complexity.

2. For any non-DSA question (greetings, general questions, unrelated topics), respond ONLY with:
   "Please ask a DSA related question."
   — No extra text, no explanations.

3. When asked to explain or describe a Data structure and algorithm topic {prompt}, provide:
   - A clear, simple explanation
   - Time and space complexity (where applicable)
   - A Java code snippet with comments
   - Real-world examples and applications

4. When given a Data structure and algorithm  or {prompt} problem to solve, provide:
   - A step-by-step approach to solve it
   - A clean Java code snippet
   - Time and space complexity analysis

5. Do NOT greet the user, introduce yourself, or add any preamble or meta-commentary like "Sure, I'll help you with..." or "Great question!". Jump directly into the answer.

6. Keep explanations beginner-friendly but complete. """
            response = client.models.generate_content(model="gemini-2.5-flash", contents=main_prompt)
            explanation = response.text

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📖 EXPLANATION</div>', unsafe_allow_html=True)
        st.markdown(explanation)
        st.markdown('</div>', unsafe_allow_html=True)

        is_dsa = "Please ask a dsa related question" not in explanation

        if is_dsa:
            st.markdown('<hr class="divider">', unsafe_allow_html=True)


            # ── 2. Resources ──
            with st.spinner("Finding resources..."):
                resources = get_resources(prompt)

            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">📚 BLOGS & ARTICLES</div>', unsafe_allow_html=True)
            if resources["blogs"]:
                blog_html = ""
                for title, url in resources["blogs"]:
                    blog_html += f'<a href="{url}" target="_blank" class="link-chip">🔗 {title}</a>'
                st.markdown(blog_html, unsafe_allow_html=True)
            else:
                st.caption("No blogs found.")
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">▶️ YOUTUBE TUTORIALS</div>', unsafe_allow_html=True)
            if resources["youtube"]:
                yt_html = ""
                for title, url in resources["youtube"]:
                    yt_html += f'<a href="{url}" target="_blank" class="link-chip yt-chip">▶ {title}</a>'
                st.markdown(yt_html, unsafe_allow_html=True)
            else:
                st.caption("No YouTube links found.")
            st.markdown('</div>', unsafe_allow_html=True)

        st.session_state.messages.append({"role": "assistant", "content": explanation})

# ── Chat input ────────────────────────────────────────────────────────────────
st.markdown("---")
prompt = st.chat_input("Ask a DSA topic or problem (e.g. Binary Search Tree, Dijkstra's Algorithm...)")
if prompt:
    handle_dsa(prompt)