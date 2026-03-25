# 🖋 Inkwell — AI Creative Writing Studio

Poem, prose, and lyrics writer powered by **Groq's inference API**.

---

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Enter your Groq API key in the sidebar when the app opens.

---

## Deploy on Streamlit Cloud (free)

1. Push this folder to a **GitHub repo**
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Point to your repo and set `app.py` as the main file
4. In **Advanced settings → Secrets**, add:

```toml
GROQ_API_KEY = "gsk_your_key_here"
```

5. Click **Deploy** — done.

If you add the secret, users won't need to enter the key themselves.
If you skip it, users enter their own key in the sidebar.

---

## Get a Groq API key

Free at [console.groq.com](https://console.groq.com)

---

## Features

- **Poems** — 9 style presets (Keats, Plath, Whitman, Rumi, Gulzar…), 8 forms
- **Prose** — 8 style presets (Carver, Poe, Márquez, Nabokov…), 6 forms  
- **Lyrics** — 7 style presets (Dylan, Gulzar, Blues…), 5 structures
- Tone selector, length control, custom instructions
- Temperature slider for creativity control
- Download output as `.txt`
- Regenerate with one click
