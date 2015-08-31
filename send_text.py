from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC0affff5dc7bd66c26e9dbd644e3f888d"
auth_token  = "fab9de97228cd6c546e5ef74bd1d364a"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Wha happened!?", to="+18046788930",  from_="+18047939984")
print message.sid
