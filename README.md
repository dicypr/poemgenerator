# 🖋️ Inkwell — AI Creative Writing Studio

> Transform ideas into poetry, prose, and lyrics with AI-powered literary assistance

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Groq](https://img.shields.io/badge/Groq-000000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEyIDJMMiAxMmwxMCAxMCAxMC0xMEwxMiAyeiIgZmlsbD0iI2ZmZiIvPjwvc3ZnPg==)](https://groq.com)

---

## ✨ Features

- **🪶 Poetry Generator** — 9 style presets (Keats, Plath, Whitman, Rumi, Gulzar…), 8 forms
- **📖 Prose Writer** — 8 style presets (Carver, Poe, Márquez, Nabokov…), 6 forms  
- **🎵 Lyrics Composer** — 7 style presets (Dylan, Gulzar, Blues…), 5 structures
- **🎨 Customization** — Tone selector, length control, custom instructions
- **🎚️ Temperature Control** — Adjust creativity from precise to wild
- **💾 Export** — Download output as `.txt`
- **🔄 Regenerate** — One-click regeneration with the same parameters
- **🎨 Beautiful UI** — Custom literary aesthetic with warm editorial design

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- A free Groq API key from [console.groq.com](https://console.groq.com)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dicypr/poemgenerator.git
   cd poemgenerator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. **Enter your API key** in the sidebar when the app opens

---

## ☁️ Deploy on Streamlit Cloud (Free)

1. Push this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Point to your repo and set `app.py` as the main file
4. **(Optional)** In **Advanced settings → Secrets**, add:

   ```toml
   GROQ_API_KEY = "gsk_your_key_here"
   ```

5. Click **Deploy** — done! ✨

> **Note:** If you add the secret, users won't need to enter their own API key. If you skip it, users can enter their own key in the sidebar.

---

## 🎯 How It Works

1. **Choose your mode** — Poem, Prose, or Lyrics
2. **Select style & form** — From romantic poetry to blues lyrics
3. **Set the tone** — Melancholic, playful, dark, hopeful, etc.
4. **Add your seed idea** — A topic, image, or feeling
5. **Customize** (optional) — Add specific instructions
6. **Hit Write** — Watch AI craft your literary piece
7. **Download or regenerate** — Save or try variations

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io) — Interactive Python web apps
- **AI Backend:** [Groq](https://groq.com) — Ultra-fast LLM inference
- **Models:** LLaMA 3.3 70B, Mixtral 8x7B
- **Styling:** Custom CSS with literary fonts (Cormorant Garamond, DM Mono, Outfit)

---

## 🔑 Get a Groq API Key

Get your free API key at [console.groq.com](https://console.groq.com)

Groq offers:
- ⚡ Ultra-fast inference
- 🆓 Generous free tier
- 🤖 Access to top open-source models

---

## 📸 Screenshots

> *Add screenshots of your app here for better engagement on LinkedIn!*

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**DICYPR**

- GitHub: [@dicypr](https://github.com/dicypr)
- LinkedIn: [Connect with me!](https://linkedin.com/in/yourprofile)

---

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

---

## 🙏 Acknowledgments

- Powered by [Groq's](https://groq.com) lightning-fast inference API
- Built with [Streamlit](https://streamlit.io)
- Inspired by the timeless craft of literary writing

---

<div align="center">
  <strong>Made with ❤️ and ☕ by DICYPR</strong>
</div>
