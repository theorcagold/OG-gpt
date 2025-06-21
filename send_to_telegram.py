import requests

BOT_TOKEN = '7792542470:AAFXFpEeGeR1Y4scoAszD66J7oPpTu18QYY'
CHAT_ID = '6025372937'

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=payload)