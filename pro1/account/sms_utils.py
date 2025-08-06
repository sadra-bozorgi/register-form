import requests
from django.conf import settings

def send_sms(phone, code):
    url = "https://api.sms.ir/v1/send/verify" 
    api_key = settings.SMS_API_KEY

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'text/plain',
        'x-api-key':  settings.SMS_API_KEY,
    }

    payload = {
    "mobile": phone,
    "templateId": 123456,
    "parameters": [
      {
        "name": "CODE",
        "value": code
      }
    ]
}

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("پیام ارسال شد")
    else:
        print("خطا در ارسال پیام:", response.status_code, response.text)
