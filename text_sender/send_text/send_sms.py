from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0deb9fbfb2685b645931b126f1a6a753"
# Your Auth Token from twilio.com/console
auth_token  = "20d418ac1ff49b8b44a8b42a636ed5da"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16786620491", 
    from_="+19712973741",
    body="Hello, does this work?!")

print(message.sid)