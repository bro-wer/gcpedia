from django.views.generic import TemplateView
from django.shortcuts import redirect
from . import models

def createNewQuestion(questionContent, questionComments, questionSolved, questionSource, questionTags):

    try:
        questionSource = models.Quiz_source.objects.get(sourceName = questionSource)
        return models.Quiz_question.objects.create(questionContent=questionContent,
                                                   questionComments= questionComments,
                                                   questionSolved = questionSolved,
                                                   questionSource = questionSource)
    except Exception as e:
        return models.Quiz_question.objects.create(questionContent=questionContent,
                                                   questionComments= questionComments,
                                                   questionSolved = questionSolved)

def processAnswers(newQuestion, request_dict):
    for key in request_dict.keys():
        if key.startswith("answerText_") and len(request_dict[key]) > 1:
            answerText = request_dict[key]
            answerIsValid = (key.replace("answerText_", "answerCorrect_") in request_dict.keys())
            models.Quiz_answer.objects.create(answerIsValid = answerIsValid,
                                              answerText = answerText,
                                              parentQuestion = newQuestion)


class HomePage(TemplateView):
    template_name = "quiz/index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        questionsList = models.Quiz_question.objects.all()
        tagsList = models.Quiz_tag.objects.all()

        context.update({
            'questionsList': questionsList,
            'tagsList': tagsList,
            })
        return context

class NewQuestion(TemplateView):
    template_name = "quiz/newquestion.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        sourceList = models.Quiz_source.objects.all()
        tagsList = models.Quiz_tag.objects.all().order_by('tagName')

        context.update({
            'sourceList': sourceList,
            'tagsList': tagsList,
            })
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("POST")
            print(request.body)
            print(str(request.POST))
            request_dict = {}

            for key,value in request.POST.items():
                print("\n###")
                print(key)
                print(value)
                request_dict[key] = value

            newQuestion = createNewQuestion(questionContent = request_dict['question-content'],
                                            questionComments = request_dict['question-comment'],
                                            questionSolved = ("questionSolved" in request_dict.keys()),
                                            questionSource = request_dict["questionSource"],
                                            questionTags = "missing value")
            processAnswers(newQuestion, request_dict)

        return redirect(request.META.get('HTTP_REFERER'))
