from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}
    if request.method=="POST":
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse(str(TFD.cleaned_data))
        else:
            return HttpResponse('Topic in not inserted')

    return render(request,'insert_topic.html',d)