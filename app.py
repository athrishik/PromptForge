import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="PromptForge",
    page_icon="🔨",
    layout="wide",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  /* ---------- base theme ---------- */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
  }

  /* dark glassmorphism background */
  .stApp {
    background: linear-gradient(135deg, #0f0c1a 0%, #1a1030 50%, #0d1117 100%);
    background-attachment: fixed;
  }

  /* ---------- header ---------- */
  .pf-header {
    text-align: center;
    padding: 2rem 0 1rem;
  }
  .pf-header h1 {
    font-size: 2.8rem;
    font-weight: 700;
    background: linear-gradient(90deg, #8B5CF6, #a78bfa, #c4b5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
  }
  .pf-header p {
    color: #9ca3af;
    font-size: 1.05rem;
  }

  /* ---------- tabs ---------- */
  .stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: rgba(255,255,255,0.04);
    border-radius: 12px;
    padding: 6px;
  }
  .stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 10px 24px;
    font-weight: 600;
    font-size: 0.95rem;
    color: #9ca3af;
    background: transparent;
    border: none;
    transition: all 0.2s;
  }
  .stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #7c3aed, #8B5CF6) !important;
    color: #fff !important;
    box-shadow: 0 4px 15px rgba(139,92,246,0.4);
  }

  /* ---------- cards / glass boxes ---------- */
  .glass-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 16px;
    padding: 1.5rem;
    backdrop-filter: blur(10px);
  }

  /* ---------- output boxes ---------- */
  .output-box {
    background: rgba(139,92,246,0.08);
    border: 1px solid rgba(139,92,246,0.35);
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    color: #e9d5ff;
    font-family: 'Inter', monospace;
    font-size: 0.88rem;
    line-height: 1.7;
    white-space: pre-wrap;
    word-break: break-word;
    max-height: 480px;
    overflow-y: auto;
  }
  .output-original {
    background: rgba(239,68,68,0.07);
    border: 1px solid rgba(239,68,68,0.3);
    color: #fca5a5;
  }
  .output-polished {
    background: rgba(34,197,94,0.07);
    border: 1px solid rgba(34,197,94,0.3);
    color: #86efac;
  }

  /* ---------- checklist ---------- */
  .technique-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(139,92,246,0.15);
    border-radius: 12px;
    padding: 1rem 1.2rem;
  }
  .technique-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 6px 0;
    font-size: 0.92rem;
    color: #d1d5db;
    border-bottom: 1px solid rgba(255,255,255,0.05);
  }
  .technique-row:last-child { border-bottom: none; }
  .score-badge {
    display: inline-block;
    margin-top: 12px;
    background: linear-gradient(135deg, #7c3aed, #8B5CF6);
    color: #fff;
    font-weight: 700;
    font-size: 0.85rem;
    border-radius: 20px;
    padding: 4px 14px;
  }

  /* ---------- scorecard ---------- */
  .scorecard-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    font-size: 0.9rem;
    color: #d1d5db;
  }
  .scorecard-row:last-child { border-bottom: none; }
  .sc-added    { color: #4ade80; font-weight: 600; }
  .sc-enhanced { color: #a78bfa; font-weight: 600; }
  .sc-present  { color: #60a5fa; font-weight: 600; }
  .sc-notneed  { color: #6b7280; font-weight: 600; }

  /* ---------- explanation box ---------- */
  .explanation-box {
    background: rgba(139,92,246,0.06);
    border-left: 3px solid #8B5CF6;
    border-radius: 0 8px 8px 0;
    padding: 0.9rem 1.2rem;
    color: #c4b5fd;
    font-size: 0.9rem;
    line-height: 1.6;
    margin-top: 1rem;
  }

  /* ---------- section labels ---------- */
  .section-label {
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #8B5CF6;
    margin-bottom: 6px;
  }

  /* ---------- sidebar ---------- */
  section[data-testid="stSidebar"] {
    background: rgba(15,12,26,0.9);
    border-right: 1px solid rgba(139,92,246,0.15);
  }
  .ref-card {
    background: rgba(139,92,246,0.07);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 10px;
    padding: 0.9rem 1rem;
    font-size: 0.82rem;
    color: #c4b5fd;
    line-height: 1.6;
  }
  .ref-card b { color: #a78bfa; }

  /* ---------- copy button ---------- */
  .stButton > button {
    background: linear-gradient(135deg, #7c3aed, #8B5CF6);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    padding: 0.45rem 1.2rem;
    transition: all 0.2s;
    box-shadow: 0 4px 12px rgba(139,92,246,0.3);
  }
  .stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(139,92,246,0.45);
  }
  .stButton > button:disabled {
    background: rgba(139,92,246,0.2) !important;
    color: #6b7280 !important;
    cursor: not-allowed;
    box-shadow: none;
    transform: none;
  }

  /* ---------- inputs ---------- */
  .stTextInput > div > div > input,
  .stTextArea > div > div > textarea,
  .stSelectbox > div > div {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(139,92,246,0.25) !important;
    border-radius: 8px !important;
    color: #e5e7eb !important;
  }
  .stTextInput > div > div > input:focus,
  .stTextArea > div > div > textarea:focus {
    border-color: #8B5CF6 !important;
    box-shadow: 0 0 0 2px rgba(139,92,246,0.2) !important;
  }

  /* label colour */
  label, .stTextInput label, .stTextArea label, .stSelectbox label {
    color: #c4b5fd !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
  }
  div[data-testid="stWidgetLabel"] p {
    color: #c4b5fd !important;
  }

  /* remove streamlit footer */
  footer { visibility: hidden; }
  #MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="pf-header">
  <h1>🔨 PromptForge</h1>
  <p>Engineer better prompts — from first draft to production quality</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    gemini_key = st.text_input(
        "Gemini API Key",
        type="password",
        placeholder="AIza...",
        help="Required for Autopilot mode. Get a free key at aistudio.google.com",
    )

    st.markdown("---")
    st.markdown("### 📚 Technique Reference")
    st.markdown("""
<div class="ref-card">
  <b>1. Context</b><br>Background info the AI needs to give relevant answers.<br><br>
  <b>2. Role</b><br>Assign an expert persona to shape tone & depth.<br><br>
  <b>3. Examples</b><br>Show 1–2 sample outputs to anchor style & format.<br><br>
  <b>4. Chain-of-thought</b><br>Ask for step-by-step reasoning on complex tasks.<br><br>
  <b>5. Structure</b><br>Specify output format (bullets, JSON, table…).
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
<div style="background:rgba(139,92,246,0.1);border:1px solid rgba(139,92,246,0.3);
            border-radius:10px;padding:0.8rem 1rem;font-size:0.82rem;color:#c4b5fd;text-align:center;">
  🔍 <b>Test in TripleLens</b><br>
  Copy your polished prompt and paste it into TripleLens to compare outputs across models.
</div>
""", unsafe_allow_html=True)

# ── Tabs ───────────────────────────────────────────────────────────────────────
tab_builder, tab_autopilot = st.tabs(["🔨 Builder", "⚡ Autopilot"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — BUILDER
# ══════════════════════════════════════════════════════════════════════════════
with tab_builder:
    st.markdown("<br>", unsafe_allow_html=True)
    left_col, right_col = st.columns([3, 2], gap="large")

    with left_col:
        st.markdown('<div class="section-label">Prompt Components</div>', unsafe_allow_html=True)

        role = st.text_input(
            "🧑‍💼 Role",
            placeholder="Senior Python developer with 10 years experience",
            help="Who should the AI act as?",
        )
        context = st.text_area(
            "🗂️ Context",
            placeholder="Building a REST API with FastAPI, ~5K users, startup environment",
            height=100,
            help="What background info does the AI need?",
        )
        task = st.text_area(
            "🎯 Task *",
            placeholder="Review this endpoint for security issues and performance bottlenecks",
            height=120,
            help="Required — what should the AI do?",
        )
        constraints = st.text_input(
            "🚧 Constraints",
            placeholder="Under 500 words. Focus on critical issues only.",
            help="Rules, limits, or scope restrictions",
        )
        output_format = st.selectbox(
            "📄 Output Format",
            ["Paragraph", "Bullet points", "Numbered steps", "Table", "Code", "JSON", "Markdown"],
        )
        examples = st.text_area(
            "💡 Examples (optional)",
            placeholder="Paste 1–2 examples of the style or format you want…",
            height=90,
        )

        build_clicked = st.button("🔨 Build Prompt", use_container_width=True)

    with right_col:
        st.markdown('<div class="section-label">Output</div>', unsafe_allow_html=True)

        if build_clicked:
            if not task.strip():
                st.error("⚠️ Task is required — please describe what the AI should do.")
            else:
                # ── Assemble prompt ───────────────────────────────────────────
                parts = []
                if role.strip():
                    parts.append(f"You are {role.strip()}.")
                if context.strip():
                    parts.append(f"Context: {context.strip()}")
                parts.append(task.strip())
                if constraints.strip():
                    parts.append(f"Constraints: {constraints.strip()}")
                if output_format:
                    parts.append(f"Please format your response as {output_format.lower()}.")
                if examples.strip():
                    parts.append(f"Here are examples of the style I want:\n{examples.strip()}")

                assembled = "\n\n".join(parts)
                st.session_state["built_prompt"] = assembled

        if "built_prompt" in st.session_state and st.session_state["built_prompt"]:
            prompt_text = st.session_state["built_prompt"]
            st.markdown(f'<div class="output-box">{prompt_text}</div>', unsafe_allow_html=True)

            # copy button via JS hack
            safe = prompt_text.replace("`", "\\`").replace("$", "\\$")
            st.markdown(f"""
<button onclick="navigator.clipboard.writeText(`{safe}`).then(()=>{{
  this.textContent='✅ Copied!';setTimeout(()=>this.textContent='📋 Copy to Clipboard',2000);
}})"
style="margin-top:10px;background:linear-gradient(135deg,#7c3aed,#8B5CF6);color:#fff;
border:none;border-radius:8px;padding:8px 18px;font-weight:600;cursor:pointer;
box-shadow:0 4px 12px rgba(139,92,246,0.3);font-family:Inter,sans-serif;font-size:0.88rem;">
📋 Copy to Clipboard
</button>
""", unsafe_allow_html=True)

            # ── Technique checklist ───────────────────────────────────────────
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="section-label">Technique Checklist</div>', unsafe_allow_html=True)

            has_context     = bool(context.strip())
            has_role        = bool(role.strip())
            has_examples    = bool(examples.strip())
            has_structure   = output_format != "Paragraph"
            has_constraints = bool(constraints.strip())

            checks = [
                ("Context",     has_context),
                ("Role",        has_role),
                ("Examples",    has_examples),
                ("Structure",   has_structure),
                ("Constraints", has_constraints),
            ]
            score = sum(v for _, v in checks)

            rows_html = "".join(
                f'<div class="technique-row">'
                f'<span>{"✅" if v else "⬜"}</span>'
                f'<span style="flex:1">{name}</span>'
                f'<span style="font-size:0.75rem;color:{"#4ade80" if v else "#ef4444"}">'
                f'{"Present" if v else "Missing"}</span>'
                f'</div>'
                for name, v in checks
            )

            st.markdown(f"""
<div class="technique-card">
  {rows_html}
  <div class="score-badge">{score}/5 techniques applied</div>
</div>
""", unsafe_allow_html=True)
        else:
            st.markdown("""
<div class="glass-card" style="text-align:center;color:#6b7280;padding:3rem 1rem;">
  <div style="font-size:2.5rem;margin-bottom:0.8rem;">🔨</div>
  <div style="font-size:0.95rem;">Fill in the components on the left<br>and click <b>Build Prompt</b></div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — AUTOPILOT
# ══════════════════════════════════════════════════════════════════════════════
with tab_autopilot:
    st.markdown("<br>", unsafe_allow_html=True)

    rough_prompt = st.text_area(
        "✏️ Paste your rough prompt here",
        placeholder="e.g. write me some python code that scrapes a website",
        height=140,
    )

    has_key = bool(gemini_key.strip())
    polish_clicked = st.button(
        "⚡ Polish",
        disabled=not has_key,
        use_container_width=False,
        help="Add your Gemini API key in the sidebar to enable this.",
    )

    if not has_key:
        st.caption("🔒 Add your Gemini API key in the sidebar to enable Autopilot.")

    if polish_clicked and rough_prompt.strip():
        meta_prompt = f"""You are a prompt engineering expert. Analyze this rough prompt and rewrite it to be dramatically more effective.

Apply these techniques WHERE APPROPRIATE (don't force all of them):
1. Context — add relevant background info the AI needs
2. Role — assign a specific expert persona
3. Examples — include example outputs if it helps
4. Chain-of-thought — request step-by-step reasoning for complex tasks
5. Structured output — specify the desired response format

IMPORTANT: Keep the user's original intent. Don't over-engineer simple prompts. Only add techniques that genuinely improve the output.

Original prompt:
{rough_prompt.strip()}

Respond in EXACTLY this format:

POLISHED:
[your rewritten prompt]

SCORECARD:
- Context: [ADDED/ENHANCED/ALREADY_PRESENT/NOT_NEEDED]
- Role: [same options]
- Examples: [same options]
- Chain-of-thought: [same options]
- Structure: [same options]

EXPLANATION:
[2-3 sentences on what you changed and why]"""

        with st.spinner("⚡ Polishing your prompt with Gemini…"):
            try:
                from google import genai
                from google.genai import types

                client = genai.Client(api_key=gemini_key.strip())
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=meta_prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.3,
                        max_output_tokens=2048,
                    ),
                )
                raw = response.text
                st.session_state["autopilot_raw"]    = raw
                st.session_state["autopilot_input"]  = rough_prompt.strip()
                st.session_state["autopilot_error"]  = None

            except Exception as e:
                st.session_state["autopilot_error"] = str(e)
                st.session_state["autopilot_raw"]   = None

    # ── Display results ────────────────────────────────────────────────────────
    if st.session_state.get("autopilot_error"):
        st.error(f"❌ Gemini API error: {st.session_state['autopilot_error']}")

    elif st.session_state.get("autopilot_raw"):
        raw = st.session_state["autopilot_raw"]
        original_input = st.session_state.get("autopilot_input", "")

        # ── Parse sections ─────────────────────────────────────────────────────
        def extract_section(text, start_marker, end_markers):
            idx = text.find(start_marker)
            if idx == -1:
                return ""
            content_start = idx + len(start_marker)
            end_idx = len(text)
            for em in end_markers:
                ei = text.find(em, content_start)
                if ei != -1 and ei < end_idx:
                    end_idx = ei
            return text[content_start:end_idx].strip()

        polished    = extract_section(raw, "POLISHED:\n",     ["SCORECARD:", "EXPLANATION:"])
        scorecard_s = extract_section(raw, "SCORECARD:\n",    ["EXPLANATION:"])
        explanation = extract_section(raw, "EXPLANATION:\n",  [])

        # ── Parse scorecard lines ──────────────────────────────────────────────
        sc_map = {}
        for line in scorecard_s.splitlines():
            line = line.strip().lstrip("- ")
            if ":" in line:
                k, v = line.split(":", 1)
                sc_map[k.strip()] = v.strip().upper()

        sc_display = {
            "ADDED":          ("✅ Added",         "sc-added"),
            "ENHANCED":       ("🔄 Enhanced",       "sc-enhanced"),
            "ALREADY_PRESENT":("✓ Already present", "sc-present"),
            "NOT_NEEDED":     ("➖ Not needed",      "sc-notneed"),
        }

        # ── Before / After columns ─────────────────────────────────────────────
        col_orig, col_pol = st.columns(2, gap="medium")
        with col_orig:
            st.markdown('<div class="section-label">Original</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="output-box output-original">{original_input}</div>',
                        unsafe_allow_html=True)
        with col_pol:
            st.markdown('<div class="section-label">Polished</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="output-box output-polished">{polished}</div>',
                        unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Scorecard + Explanation ────────────────────────────────────────────
        sc_col, ex_col = st.columns([2, 3], gap="large")

        with sc_col:
            st.markdown('<div class="section-label">Technique Scorecard</div>',
                        unsafe_allow_html=True)
            sc_order = ["Context", "Role", "Examples", "Chain-of-thought", "Structure"]
            rows_html = ""
            for tech in sc_order:
                val   = sc_map.get(tech, "NOT_NEEDED")
                label, css = sc_display.get(val, ("➖ Not needed", "sc-notneed"))
                rows_html += (
                    f'<div class="scorecard-row">'
                    f'<span>{tech}</span>'
                    f'<span class="{css}">{label}</span>'
                    f'</div>'
                )
            st.markdown(f'<div class="technique-card">{rows_html}</div>', unsafe_allow_html=True)

        with ex_col:
            st.markdown('<div class="section-label">What Changed & Why</div>',
                        unsafe_allow_html=True)
            st.markdown(f'<div class="explanation-box">{explanation}</div>',
                        unsafe_allow_html=True)

        # ── Copy button ────────────────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        safe_polished = polished.replace("`", "\\`").replace("$", "\\$")
        st.markdown(f"""
<button onclick="navigator.clipboard.writeText(`{safe_polished}`).then(()=>{{
  this.textContent='✅ Copied!';setTimeout(()=>this.textContent='📋 Copy Polished Prompt',2000);
}})"
style="background:linear-gradient(135deg,#7c3aed,#8B5CF6);color:#fff;
border:none;border-radius:8px;padding:10px 22px;font-weight:600;cursor:pointer;
box-shadow:0 4px 12px rgba(139,92,246,0.3);font-family:Inter,sans-serif;font-size:0.9rem;">
📋 Copy Polished Prompt
</button>
""", unsafe_allow_html=True)

    elif not polish_clicked:
        st.markdown("""
<div class="glass-card" style="text-align:center;color:#6b7280;padding:3.5rem 1rem;margin-top:0.5rem;">
  <div style="font-size:2.5rem;margin-bottom:0.8rem;">⚡</div>
  <div style="font-size:0.95rem;">
    Paste a rough prompt above and hit <b>Polish</b>.<br>
    Gemini will rewrite it and show you exactly what techniques were applied.
  </div>
</div>
""", unsafe_allow_html=True)
