import pyttsx3   #text to speech
import speech_recognition as sr   #performing speechrecognition tasks.
import smtplib  #simple mail transefer protocol used for sending and routing email msg  between servers and email clients. 
import imaplib   # For receiving emails (IMAP protocol)
import email      # For parsing and handling email content
# Initialize TTS engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand. Please try again.")
            return take_command()

def send_email():
    speak("Who do you want to send email to?")
    receiver_email = take_command().replace(" ", "") + "@gmail.com"

    speak("What is the subject?")
    subject = take_command()

    speak("What should I say in the email?")
    message = take_command()

    email_content = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_password_or_app_password")
        server.sendmail("your_email@gmail.com", receiver_email, email_content)
        server.quit()
        speak("Email has been sent successfully.")
    except Exception as e:
        print(e)
        speak("Something went wrong while sending the email.")

def read_email():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("your_email@gmail.com", "your_password_or_app_password")
        mail.select("inbox")

        result, data = mail.search(None, "ALL")
        mail_ids = data[0].split()
        latest_email_id = mail_ids[-1]

        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        sender = msg["From"]
        subject = msg["Subject"]
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = msg.get_payload(decode=True).decode()

        speak(f"Email from {sender}")
        speak(f"Subject is: {subject}")
        speak(f"Message is: {body[:200]}")  # Limit reading to 200 characters

        mail.logout()
    except Exception as e:
        print(e)
        speak("Could not read the email.")

def main():
    speak("Welcome to voice-controlled email system.")
    while True:
        speak("Do you want to send or read email?")
        command = take_command()
        if "send" in command:
            send_email()
        elif "read" in command:
            read_email()
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        else:
            speak("Please say send, read or exit.")

if __name__ == "__main__":
    main()
