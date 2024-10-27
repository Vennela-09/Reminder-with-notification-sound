from flask import Flask, render_template, request
import time
import threading
from playsound import playsound
from plyer import notification

app = Flask(__name__)

# Function to handle the reminder logic
def set_reminder(message, delay_in_seconds):
    time.sleep(delay_in_seconds)
    notification.notify(
        title="Reminder",
        message=message,
        timeout=10  # Notification duration in seconds
    )
    playsound("static/notification_sound.mp3")

# Home route to display the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and set the reminder
@app.route('/set_reminder', methods=['POST'])
def handle_set_reminder():
    message = request.form['message']
    reminder_time = int(request.form['time'])

    # Use threading to avoid blocking the web server while waiting for the reminder
    threading.Thread(target=set_reminder, args=(message, reminder_time)).start()

    return f"<h1>Reminder set for {reminder_time} seconds!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
