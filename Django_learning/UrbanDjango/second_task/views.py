from django.shortcuts import render
from django.views.generic import TemplateView


def task2nd_view(request):
    return render(request, 'templates/second_task/func_template.html')


class View2ndTask(TemplateView):
    template_name = 'templates/second_task/classes_template.html'

# Create your views here.
