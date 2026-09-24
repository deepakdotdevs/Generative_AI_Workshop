# 🤖 Groq Chatbot

A simple AI chatbot built using **Python, Streamlit, and the Groq API**.

This project was developed during the **Generative AI & RAG Systems with Prompt Engineering** workshop at **K.R. Mangalam University**.

## ✨ Features

- 🤖 AI-powered chatbot
- ⚡ Fast responses using Groq API
- 💬 Interactive Streamlit chat interface
- 🔄 Conversation history using Streamlit session state
- 🎛️ Select different Groq-supported AI models
- 🗑️ Clear conversation option
- 🔐 API key input is handled securely
- 🧠 Suitable for experimenting with prompt engineering

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Groq API**
- **Requests**
- **JSON**
- **LLM / Generative AI**

## 📂 Project Structure

```text
Generative_AI_Workshop/
│
├── base.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

> ⚠️ The `.env` file contains sensitive information and must not be uploaded to GitHub.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/deepakdotdevs/Generative_AI_Workshop.git
```

### 2. Open the project

```bash
cd Generative_AI_Workshop
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the dependencies manually:

```bash
pip install streamlit requests python-dotenv
```

## 🔑 API Key Setup

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Never upload your `.env` file to GitHub.

Make sure `.gitignore` contains:

```text
.env
```

## ▶️ Run the Chatbot

Start the Streamlit application using:

```bash
streamlit run base.py
```

The application will open in your browser.

## 🧠 Prompt Engineering

This chatbot can be used to experiment with different prompting techniques, such as:

- Zero-shot prompting
- Few-shot prompting
- Role prompting
- Structured prompting
- Chain-of-thought-style prompting

Example:

```text
Solve the following problem carefully.

First identify the important information,
then perform the required calculations,
and finally provide a concise answer.
```

## 📚 Workshop Learning

Through this project, I explored:

- Generative AI fundamentals
- Large Language Models (LLMs)
- Prompt Engineering
- API integration
- Groq API
- Chatbot development
- Streamlit
- Conversation state management
- Secure API key handling

## 🔮 Future Improvements

- [ ] Add conversation export
- [ ] Add streaming responses
- [ ] Add system prompt customization
- [ ] Add RAG functionality
- [ ] Add document upload
- [ ] Add vector database
- [ ] Add AI agents
- [ ] Deploy the chatbot online

## 👨‍💻 Author

**Deepak Jangid**

B.Tech CSE Student  
K.R. Mangalam University

Interested in **Generative AI, AI Engineering, Web Development, and Software Development**.

---

⭐ If you find this project useful, consider giving it a star!
