# +12138613602
# ACb7d155b3cb20b65733467e6b0a363cb7    acc sid
# 88ccd0b4fa948d9ce98c9519e2f6580c		auth token


from twilio.rest import Client

account = "ACb7d155b3cb20b65733467e6b0a363cb7"
token = "88ccd0b4fa948d9ce98c9519e2f6580c"
client = Client(account, token)

call = client.calls.create(to="+918961504835",from_="+12138613602",url="http://demo.twilio.com/docs/voice.xml")
print(call.sid)