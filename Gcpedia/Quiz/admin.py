from django.contrib import admin
from . import models


# define admin views

class Quiz_answer_Admin(admin.ModelAdmin):
    list_display = ['parentQuestion', 'answerIsValid', 'answerText']
    list_filter = ['parentQuestion']

class Quiz_question_Admin(admin.ModelAdmin):
    list_display = ['questionId', 'questionContent', 'questionSource', 'questionSolved']
    list_editable = ['questionSource']
    list_filter = ['questionSource', 'questionSolved']

class Quiz_sourceAdmin(admin.ModelAdmin):
    list_display = ('sourceName', 'shortName')
    list_editable = ['shortName']
    search_fields = ('sourceName', 'shortName')


# Register your models here.
admin.site.register(models.Quiz_answer, Quiz_answer_Admin)
admin.site.register(models.Quiz_source, Quiz_sourceAdmin)
admin.site.register(models.Quiz_tag)
admin.site.register(models.Quiz_question, Quiz_question_Admin)
