from twilio.rest import Client


account_sid = ''
auth_token = '7'
twilio_number = ''  
destination_number = ''  
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hellooooooo idiot",
    from_=twilio_number,
    to=destination_number
)

print(f"Message sent with SID: {message.sid}")
