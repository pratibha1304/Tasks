from twilio.rest import Client


account_sid = 'ACc60dc2690e5187073f403f5cbab0f00f'
auth_token = 'ffbb2854427181bb7c29a19820c15f97'
twilio_number = '+17627060872'  
destination_number = '+919414806786'  
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hellooooooo idiot",
    from_=twilio_number,
    to=destination_number
)

print(f"Message sent with SID: {message.sid}")
