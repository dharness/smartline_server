from django.http import HttpResponse
from twilio import twiml


# Create your views here.
def index(req):
    res = twiml.Response()
    res.say('Hello')
    return HttpResponse(res)
