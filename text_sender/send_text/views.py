from django.shortcuts import render
from twilio.rest import Client
from .forms import TextForm

def index(request):
    form = TextForm()
    return render(request, 'send_text/index.html', {'form': form})

def text_sent(request):
    if request.method == 'POST':
        receiveForm = TextForm(request.POST)

        if receiveForm.is_valid():
            sendTo = receiveForm.cleaned_data['phoneNumber']
            messageTo = receiveForm.cleaned_data['textMessage']
            print(sendTo, "This is the error message")
            # sendTo = sendTo.replace(" ", "")
            # sendTo = sendTo.replace("-", "")
            # sendTo = "+1" + sendTo

            # Your Account SID from twilio.com/console
            account_sid = "AC0deb9fbfb2685b645931b126f1a6a753"
            # Your Auth Token from twilio.com/console
            auth_token  = "20d418ac1ff49b8b44a8b42a636ed5da"

            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to=sendTo, 
                from_="+19712973741",
                body=messageTo)

    return render(request, 'send_text/text_sent.html')