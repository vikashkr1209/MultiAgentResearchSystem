import streamlit as st
from pipeline import run_research_pipeline

# ── Page config ────────────────────────────────────────────────
st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔬",
    layout="wide"
)

# ── Custom CSS ─────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Inter:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0a0a0f;
    color: #e8e8f0;
}

.main { background-color: #0a0a0f; }

h1, h2, h3 { font-family: 'Syne', sans-serif; }

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #a78bfa, #38bdf8, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.1;
    margin-bottom: 0.3rem;
}

.hero-sub {
    color: #6b7280;
    font-size: 1rem;
    font-weight: 300;
    letter-spacing: 0.05em;
    margin-bottom: 2rem;
}

.step-card {
    background: #13131a;
    border: 1px solid #1e1e2e;
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
}

.step-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.step-search  { color: #38bdf8; border-left: 3px solid #38bdf8; }
.step-scrape  { color: #f59e0b; border-left: 3px solid #f59e0b; }
.step-report  { color: #34d399; border-left: 3px solid #34d399; }
.step-critic  { color: #f87171; border-left: 3px solid #f87171; }

.score-badge {
    display: inline-block;
    background: linear-gradient(135deg, #a78bfa, #38bdf8);
    color: white;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1.5rem;
    padding: 0.4rem 1rem;
    border-radius: 8px;
    margin-bottom: 1rem;
}

.stTextInput > div > div > input {
    background-color: #13131a !important;
    border: 1px solid #2d2d3f !important;
    color: #e8e8f0 !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.75rem 1rem !important;
}

.stButton > button {
    background: linear-gradient(135deg, #a78bfa, #38bdf8) !important;
    color: white !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.75rem 2.5rem !important;
    letter-spacing: 0.05em !important;
    transition: opacity 0.2s !important;
}

.stButton > button:hover { opacity: 0.85 !important; }

.status-dot {
    display: inline-block;
    width: 8px; height: 8px;
    border-radius: 50%;
    margin-right: 8px;
    animation: pulse 1.2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.3; }
}

.divider {
    border: none;
    border-top: 1px solid #1e1e2e;
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)


# ── Header ─────────────────────────────────────────────────────
st.markdown('<div class="hero-title">🔬 Research Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">MULTI-AGENT · WEB SEARCH · SCRAPE · WRITE · CRITIQUE</div>', unsafe_allow_html=True)

# ── Input ──────────────────────────────────────────────────────
col1, col2 = st.columns([4, 1])
with col1:
    topic = st.text_input("", placeholder="Enter a research topic  e.g.  Impact of AI on jobs in India...")
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    run = st.button("Research →")

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Pipeline ───────────────────────────────────────────────────
if run and topic.strip():

    # ── Step indicators ────────────────────────────────────────
    steps_col1, steps_col2, steps_col3, steps_col4 = st.columns(4)

    with steps_col1:
        s1 = st.empty()
        s1.markdown('<div class="step-card step-search"><span class="step-label">🔍 Step 1</span><br>Search Agent</div>', unsafe_allow_html=True)
    with steps_col2:
        s2 = st.empty()
        s2.markdown('<div class="step-card" style="border-left:3px solid #2d2d3f"><span class="step-label" style="color:#4b5563">📄 Step 2</span><br>Reader Agent</div>', unsafe_allow_html=True)
    with steps_col3:
        s3 = st.empty()
        s3.markdown('<div class="step-card" style="border-left:3px solid #2d2d3f"><span class="step-label" style="color:#4b5563">✍️ Step 3</span><br>Writer Chain</div>', unsafe_allow_html=True)
    with steps_col4:
        s4 = st.empty()
        s4.markdown('<div class="step-card" style="border-left:3px solid #2d2d3f"><span class="step-label" style="color:#4b5563">🧠 Step 4</span><br>Critic Chain</div>', unsafe_allow_html=True)

    # ── Progress placeholders ───────────────────────────────────
    result_area = st.empty()

    with st.spinner(""):

        # Run pipeline
        result_area.info("⏳ Agents are working... this may take 30-60 seconds.")
        state = run_research_pipeline(topic)

        # Update step indicators to done
        s1.markdown('<div class="step-card step-search"><span class="step-label">✅ Step 1</span><br>Search Done</div>', unsafe_allow_html=True)
        s2.markdown('<div class="step-card step-scrape"><span class="step-label">✅ Step 2</span><br>Scrape Done</div>', unsafe_allow_html=True)
        s3.markdown('<div class="step-card step-report"><span class="step-label">✅ Step 3</span><br>Report Done</div>', unsafe_allow_html=True)
        s4.markdown('<div class="step-card step-critic"><span class="step-label">✅ Step 4</span><br>Critic Done</div>', unsafe_allow_html=True)
        result_area.empty()

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # ── Results layout ─────────────────────────────────────────
    left, right = st.columns([3, 2])

    with left:
        # Report
        st.markdown('<div class="step-label step-report" style="font-size:0.8rem; letter-spacing:0.1em">✍️ RESEARCH REPORT</div>', unsafe_allow_html=True)
        st.markdown(state["report"])

    with right:
        # Critic Feedback
        st.markdown('<div class="step-label step-critic" style="font-size:0.8rem; letter-spacing:0.1em">🧠 CRITIC FEEDBACK</div>', unsafe_allow_html=True)
        st.markdown(state["feedback"])

        st.markdown('<hr class="divider">', unsafe_allow_html=True)

        # Expandable raw data
        with st.expander("🔍 Raw Search Results"):
            search = state["search_result"]
            if isinstance(search, list):
                for block in search:
                    if block.get("type") == "text":
                        st.write(block["text"])
            else:
                st.write(search)

        with st.expander("🌐 Scraped Content"):
            st.write(state["scraped_content"])

elif run and not topic.strip():
    st.warning("Please enter a research topic first.")

else:
    # Empty state
    st.markdown("""
    <div style="text-align:center; padding: 4rem 0; color: #374151;">
        <div style="font-size: 3rem; margin-bottom: 1rem">🔬</div>
        <div style="font-family: 'Syne', sans-serif; font-size: 1.1rem; color: #4b5563">
            Enter a topic above and hit Research →
        </div>
        <div style="font-size: 0.85rem; margin-top: 0.5rem; color: #374151">
            4 AI agents will search, scrape, write and critique a full report for you
        </div>
    </div>
    """, unsafe_allow_html=True)