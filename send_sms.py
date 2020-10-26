import africastalking

username = "sandbox"
api_key = ""

africastalking.initialize(username, api_key)

sms = africastalking.SMS

try:
    response = sms.send("Hello, AT Ninja!", ["+254722000000"])
    print(response)
except Exception as e:
    print(f"Houston, something blew up: {e}")