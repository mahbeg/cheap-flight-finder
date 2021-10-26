from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "AC02eb6168ed1b353ac28b579f9d3685e0"
        self.auth_token = "200e0443774151eaa9ec59201b6553b5"
        self.phone_number = "+19168238745"

    def send_sms(self, text):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=text,
            from_=self.phone_number,
            to="+989036347342"
        )

        print(message.status)
        return message.status
