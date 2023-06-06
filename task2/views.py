from django.shortcuts import render
from tasks.forms import ReviewForm 
from django.views.generic.edit import FormView
from django.http import HttpResponse 
# Create your views here.


class ReviewEmailView(FormView):
    template_name = 'review.html':
    form_class = ReviewFOrm 

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review"
        return HttpResponse(msg)
