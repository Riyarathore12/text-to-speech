# text-to-speech
# 📧 Voice-Controlled Email System for Visually Impaired Users

A Python-based voice-operated email application designed to help visually impaired users **send and read emails** using **speech commands**. The system uses **speech recognition** and **text-to-speech (TTS)** to provide a completely hands-free experience.

---

## 👩‍💻 Features

- 🎤 Voice commands to control the entire app
- 📬 Read the latest email aloud
- 📨 Send email by speaking the receiver, subject, and message
- 🔊 Text-to-Speech (TTS) for audio responses
- 🌐 Gmail integration using SMTP and IMAP

---

## 🚀 Technologies Used

| Module            | Purpose                          |
|-------------------|----------------------------------|
| `speech_recognition` | Convert spoken words to text     |
| `pyttsx3`          | Offline text-to-speech           |
| `smtplib`          | Send email via Gmail (SMTP)      |
| `imaplib` + `email`| Fetch and parse emails (IMAP)    |
| `Python 3.x`       | Language used                    |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/voice-email-assistant.git
cd voice-email-assistant
