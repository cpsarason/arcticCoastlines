from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse

from django.http import Http404

from . models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('GSHSS/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'GSHSS/index.html', context)

# def index(request):
#     return HttpResponse("Hello, world. You're at the GSHSS index.")
#
def detail(request, question_id):
    # more streamlined version from https://docs.djangoproject.com/en/2.0/intro/tutorial03/
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'GSHSS/detail.html', {'question': question})

    # First example from  https://docs.djangoproject.com/en/2.0/intro/tutorial03/
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question Does Not Exist")
    # return render(request, 'GSHSS/detail.html',{'question': question})
    #
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
