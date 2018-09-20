from django.views.generic import TemplateView
from . import models

# Create your views here.
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

        print(str(len(models.Quiz_question.objects.all())))

        return context
