from django.shortcuts import render
from .models import Hiretuber
# Create your views here.

    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # tuber_id = models.IntegerField()
    # tuber_name = models.CharField(max_length=100)
    # city = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # message = models.TextField(blank=True)
    # user_id = models.IntegerField(blank=True)

def hiretuber(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']
        first_name = request.POST['first_name']

        # TODO: do all senitisation
        # hiretuber = Hiretuber(first_name=first_name)
        # hiretuber.save()
        # message.success(request, 'Thanks for reaching out!')
        # return redirect('youtuber')