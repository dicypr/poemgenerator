import streamlit as st
from groq import Groq
import time

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Inkwell — AI Creative Writer",
    page_icon="🖋️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# Custom CSS — Warm editorial / literary aesthetic
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;600&display=swap');

:root {
    --ink:        #1a1209;
    --paper:      #f5f0e8;
    --aged:       #e8dfc8;
    --sepia:      #c4a882;
    --rust:       #a0522d;
    --deep-rust:  #7a3e22;
    --muted:      #7a6e5f;
    --faint:      #b8ad9e;
    --white:      #fdfaf4;
}

html, body, [class*="css"] {
    background-color: var(--paper) !important;
    color: var(--ink) !important;
    font-family: 'Outfit', sans-serif;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: var(--ink) !important;
    border-right: 2px solid #2e2416;
}
section[data-testid="stSidebar"] * {
    color: var(--aged) !important;
    font-family: 'Outfit', sans-serif !important;
}
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stSlider label,
section[data-testid="stSidebar"] .stTextInput label,
section[data-testid="stSidebar"] .stTextArea label {
    color: var(--sepia) !important;
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-weight: 600;
}
section[data-testid="stSidebar"] [data-baseweb="select"] {
    background: #2a1f10 !important;
    border-color: #3d2f1a !important;
}
section[data-testid="stSidebar"] [data-baseweb="select"] * {
    background: #2a1f10 !important;
    color: var(--aged) !important;
}
section[data-testid="stSidebar"] input {
    background: #2a1f10 !important;
    border-color: #3d2f1a !important;
    color: var(--aged) !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.8rem !important;
}

/* ── Title area ── */
.inkwell-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.6rem;
    font-weight: 600;
    color: var(--ink);
    line-height: 1;
    letter-spacing: -0.02em;
}
.inkwell-subtitle {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: var(--muted);
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-top: 6px;
}
.divider {
    border: none;
    border-top: 1.5px solid var(--sepia);
    margin: 1.2rem 0 1.6rem 0;
    opacity: 0.4;
}

/* ── Mode pill tabs ── */
div[data-testid="stHorizontalBlock"] .stRadio label {
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.08em;
}

/* ── Labels ── */
.field-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 5px;
}

/* ── Text areas ── */
.stTextArea textarea {
    background: var(--white) !important;
    border: 1.5px solid var(--sepia) !important;
    border-radius: 4px !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.05rem !important;
    color: var(--ink) !important;
    line-height: 1.7 !important;
    padding: 1rem !important;
}
.stTextArea textarea:focus {
    border-color: var(--rust) !important;
    box-shadow: 0 0 0 2px rgba(160,82,45,0.12) !important;
}
.stTextInput input {
    background: var(--white) !important;
    border: 1.5px solid var(--sepia) !important;
    border-radius: 4px !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1rem !important;
    color: var(--ink) !important;
}

/* ── Output card ── */
.output-card {
    background: var(--white);
    border: 1.5px solid var(--sepia);
    border-left: 4px solid var(--rust);
    border-radius: 6px;
    padding: 2rem 2.2rem;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.2rem;
    line-height: 1.9;
    color: var(--ink);
    white-space: pre-wrap;
    position: relative;
    box-shadow: 4px 4px 18px rgba(100,70,30,0.08);
}
.output-card::before {
    content: '✦';
    position: absolute;
    top: -12px;
    left: 28px;
    background: var(--white);
    padding: 0 8px;
    color: var(--rust);
    font-size: 1rem;
}
.output-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 10px;
}

/* ── Buttons ── */
.stButton > button {
    background: var(--rust) !important;
    color: var(--white) !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 3px !important;
    padding: 0.55rem 1.6rem !important;
    transition: background 0.2s, transform 0.1s !important;
}
.stButton > button:hover {
    background: var(--deep-rust) !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Info box ── */
.info-box {
    background: #f0e8d8;
    border: 1px solid var(--sepia);
    border-radius: 4px;
    padding: 0.8rem 1rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: var(--muted);
    line-height: 1.6;
}

/* ── Selectbox ── */
[data-baseweb="select"] {
    border-color: var(--sepia) !important;
}

/* ── Spinner ── */
.stSpinner > div {
    border-top-color: var(--rust) !important;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Presets
# ─────────────────────────────────────────────

MODES = {
    "🪶 Poem": {
        "label": "Poem",
        "description": "A poem in the style and form you choose.",
        "prompt_placeholder": "A midnight thunderstorm over an old city…",
        "styles": [
            "Romantic (Keats / Shelley)",
            "Imagist (Pound / H.D.)",
            "Confessional (Plath / Sexton)",
            "Transcendentalist (Whitman / Emerson)",
            "Modernist (Eliot / Stevens)",
            "Haiku (Bashō)",
            "Ghazal (Rumi / Faiz)",
            "Urdu / Hindi poetry (Ghalib / Gulzar)",
            "Free verse — no style constraint",
        ],
        "forms": ["Free verse", "Sonnet", "Haiku", "Villanelle", "Ode", "Elegy", "Ghazal", "Any form"],
    },
    "📖 Prose": {
        "label": "Prose",
        "description": "A short prose piece — fiction or literary non-fiction.",
        "prompt_placeholder": "A letter never sent, found in the drawer of an old desk…",
        "styles": [
            "Minimalist (Carver / Hemingway)",
            "Gothic (Poe / Shirley Jackson)",
            "Magical Realism (Márquez / Borges)",
            "Stream of Consciousness (Woolf / Joyce)",
            "Lyrical / Poetic prose (Nabokov)",
            "Noir / Hard-boiled (Chandler)",
            "Fabulist (Kafka / Calvino)",
            "No style — plain literary",
        ],
        "forms": ["Flash fiction", "Short story opening", "Prose poem", "Personal essay", "Letter", "Monologue"],
    },
    "🎵 Lyrics": {
        "label": "Lyrics",
        "description": "Song lyrics with structure.",
        "prompt_placeholder": "Leaving a place you can never return to…",
        "styles": [
            "Folk / Americana (Dylan / Joni Mitchell)",
            "Classic Bollywood (Gulzar / Sahir)",
            "Blues / Soul",
            "Indie / Alternative",
            "Classical Ghazal",
            "Pop — emotional ballad",
            "Hip-hop / spoken word",
        ],
        "forms": ["Verse-Chorus-Verse", "Verse only", "Chorus only", "Full song structure", "Bridge + Chorus"],
    },
}

TONES = ["Melancholic", "Joyful", "Contemplative", "Angry / Defiant", "Tender / Intimate",
         "Ironic / Wry", "Mystical", "Nostalgic", "Urgent", "Detached / Cold"]

LENGTHS = {
    "Short  (~8–12 lines)": "short, around 8–12 lines",
    "Medium (~20–30 lines)": "medium length, around 20–30 lines",
    "Long   (~40–60 lines)": "long, around 40–60 lines",
}

MODELS = {
    "llama-3.3-70b-versatile": "Llama 3.3 70B — best quality",
    "llama3-8b-8192": "Llama 3 8B — fastest",
    "mixtral-8x7b-32768": "Mixtral 8x7B — balanced",
    "gemma2-9b-it": "Gemma 2 9B",
}


# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────

with st.sidebar:
    st.markdown("""
    <div style='font-family:"Cormorant Garamond",serif;font-size:1.6rem;font-weight:600;
    color:#c4a882;padding:0.4rem 0 0.2rem 0;letter-spacing:-0.01em;'>🖋 Inkwell</div>
    <div style='font-family:"DM Mono",monospace;font-size:0.6rem;color:#7a6e5f;
    letter-spacing:0.14em;text-transform:uppercase;margin-bottom:1.2rem;'>
    AI Creative Writing Studio</div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**Groq API Key**")
    api_key = st.text_input(
        "API Key",
        type="password",
        placeholder="gsk_…",
        label_visibility="collapsed",
        help="Get your free key at console.groq.com"
    )
    if not api_key:
        st.markdown("""
        <div class='info-box'>
        Get a free key at<br>
        <b>console.groq.com</b><br><br>
        For Streamlit Cloud, add it as a<br>
        secret: <code>GROQ_API_KEY</code>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**Model**")
    selected_model = st.selectbox(
        "Model",
        options=list(MODELS.keys()),
        format_func=lambda x: MODELS[x],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("**Creativity**")
    temperature = st.slider("Temperature", 0.3, 1.4, 0.85, step=0.05, label_visibility="collapsed")
    st.markdown(f"""<div style='font-family:"DM Mono",monospace;font-size:0.65rem;color:#7a6e5f;'>
    {"🧊 Precise" if temperature < 0.6 else "⚖️ Balanced" if temperature < 1.0 else "🔥 Wild"} · {temperature}</div>""",
    unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**Length**")
    length_label = st.selectbox("Length", list(LENGTHS.keys()), label_visibility="collapsed")

    st.markdown("---")
    st.markdown("""<div style='font-family:"DM Mono",monospace;font-size:0.6rem;color:#5a4e3f;
    line-height:1.7;'>Powered by Groq's inference API.<br>
    Your key is never stored.</div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Resolve API key (sidebar input or st.secrets)
# ─────────────────────────────────────────────

def get_api_key():
    if api_key and api_key.strip():
        return api_key.strip()
    try:
        return st.secrets["GROQ_API_KEY"]
    except Exception:
        return None


# ─────────────────────────────────────────────
# Prompt builder
# ─────────────────────────────────────────────

def build_system_prompt(mode_key, style, form, tone):
    mode = MODES[mode_key]
    label = mode["label"].lower()
    parts = [
        f"You are a master literary writer specialising in {label}.",
        f"Write in the style of: {style}.",
        f"Form: {form}.",
        f"Tone: {tone}.",
        "Rules:",
        "- Output ONLY the finished piece. No title, no preamble, no explanation, no commentary.",
        "- Do not add a heading like 'Here is your poem:' — just the text itself.",
        "- Honour line breaks, stanza breaks, and white space as part of the craft.",
        "- Be specific, concrete, and surprising. Avoid clichés.",
        "- Every word must earn its place.",
    ]
    if label == "poem":
        parts.append("- Use imagery, sound, and rhythm deliberately.")
    elif label == "prose":
        parts.append("- Open in the middle of something. No throat-clearing.")
    elif label == "lyrics":
        parts.append("- Mark structure clearly: [Verse 1], [Chorus], [Bridge] etc.")
    return "\n".join(parts)


def build_user_prompt(mode_key, topic, style, form, tone, length_label, custom_instructions):
    length_desc = LENGTHS[length_label]
    msg = f"Write a {length_desc} {MODES[mode_key]['label'].lower()} about:\n\n{topic}"
    if custom_instructions.strip():
        msg += f"\n\nAdditional instructions: {custom_instructions.strip()}"
    return msg


# ─────────────────────────────────────────────
# Generate
# ─────────────────────────────────────────────

def generate(api_key_val, model, system_prompt, user_prompt, temperature):
    client = Groq(api_key=api_key_val)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        temperature=temperature,
        max_tokens=1500,
        stream=False,
    )
    return response.choices[0].message.content.strip()


# ─────────────────────────────────────────────
# Main UI
# ─────────────────────────────────────────────

st.markdown("""
<div class='inkwell-title'>Inkwell</div>
<div class='inkwell-subtitle'>AI Creative Writing Studio · Poems · Prose · Lyrics</div>
<hr class='divider'>
""", unsafe_allow_html=True)

# Mode selector
mode_key = st.radio(
    "Writing mode",
    list(MODES.keys()),
    horizontal=True,
    label_visibility="collapsed",
)
mode = MODES[mode_key]

st.markdown("<div style='margin-top:1.4rem;'></div>", unsafe_allow_html=True)

col_left, col_right = st.columns([1.1, 1], gap="large")

with col_left:
    st.markdown(f"<div class='field-label'>Topic / Seed idea</div>", unsafe_allow_html=True)
    topic = st.text_area(
        "Topic",
        height=110,
        placeholder=mode["prompt_placeholder"],
        label_visibility="collapsed",
    )

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='field-label'>Style</div>", unsafe_allow_html=True)
        style = st.selectbox("Style", mode["styles"], label_visibility="collapsed")
    with col_b:
        st.markdown("<div class='field-label'>Form</div>", unsafe_allow_html=True)
        form = st.selectbox("Form", mode["forms"], label_visibility="collapsed")

    st.markdown("<div class='field-label'>Tone</div>", unsafe_allow_html=True)
    tone = st.selectbox("Tone", TONES, label_visibility="collapsed")

    st.markdown("<div class='field-label'>Custom instructions (optional)</div>", unsafe_allow_html=True)
    custom_instructions = st.text_area(
        "Custom instructions",
        height=70,
        placeholder="e.g. Include the word 'salt'. End on an image of water. Avoid rhyme.",
        label_visibility="collapsed",
    )

    st.markdown("<div style='margin-top:0.8rem;'></div>", unsafe_allow_html=True)
    write_btn = st.button("✦  Write", use_container_width=True)

with col_right:
    output_placeholder = st.empty()
    action_placeholder = st.empty()

    if "last_output" in st.session_state:
        output_placeholder.markdown(
            f"<div class='output-label'>{mode['label']} · {style}</div>"
            f"<div class='output-card'>{st.session_state['last_output']}</div>",
            unsafe_allow_html=True,
        )
        with action_placeholder.container():
            dl_col, reg_col = st.columns(2)
            with dl_col:
                st.download_button(
                    "⬇ Download .txt",
                    st.session_state["last_output"],
                    file_name="inkwell_output.txt",
                    mime="text/plain",
                    use_container_width=True,
                )
            with reg_col:
                if st.button("↺ Regenerate", use_container_width=True):
                    st.session_state.pop("last_output", None)
                    st.rerun()
    else:
        output_placeholder.markdown("""
        <div style='border:1.5px dashed #c4a882;border-radius:6px;padding:3rem 2rem;
        text-align:center;background:#fdfaf4;'>
            <div style='font-family:"Cormorant Garamond",serif;font-size:1.5rem;
            color:#b8ad9e;font-style:italic;'>Your writing will appear here…</div>
            <div style='font-family:"DM Mono",monospace;font-size:0.65rem;color:#c4a882;
            margin-top:0.6rem;letter-spacing:0.1em;'>Fill in the fields and press Write</div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Handle generation
# ─────────────────────────────────────────────

if write_btn:
    resolved_key = get_api_key()

    if not resolved_key:
        st.error("Please enter your Groq API key in the sidebar.")
    elif not topic.strip():
        st.warning("Please enter a topic or seed idea.")
    else:
        system_prompt = build_system_prompt(mode_key, style, form, tone)
        user_prompt   = build_user_prompt(mode_key, topic, style, form, tone, length_label, custom_instructions)

        with col_right:
            with st.spinner("Writing…"):
                try:
                    result = generate(resolved_key, selected_model, system_prompt, user_prompt, temperature)
                    st.session_state["last_output"] = result
                    st.session_state["last_mode"]   = mode["label"]
                    st.session_state["last_style"]  = style
                    st.rerun()
                except Exception as e:
                    err = str(e)
                    if "401" in err or "auth" in err.lower():
                        st.error("Invalid API key. Check your key at console.groq.com")
                    elif "rate" in err.lower():
                        st.error("Rate limit hit. Wait a moment and try again.")
                    else:
                        st.error(f"Error: {err}")
