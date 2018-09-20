from django.db import models




class Quiz_tag(models.Model):
    tagName = models.CharField(max_length = 64, editable=True, default='missing tag', primary_key=True)

    def __str__(self):
        return str(self.tagName)

    def countQuestions(self):
        return Quiz_question.objects.filter(questionTags = self).count()

    votes = property(countQuestions)


class Quiz_source(models.Model):
    sourceName = models.CharField(max_length = 64, editable=True, default='missing source', primary_key=True)
    shortName = models.CharField(max_length = 8, editable=True, default='missing short name')

    def __str__(self):
        # return "{} ({})".format(self.sourceName, self.shortName)
        return "{}".format(self.sourceName)

class Quiz_question(models.Model):
    questionId = models.AutoField(primary_key=True)

    questionContent = models.TextField(default="Missing context", max_length = 1024, editable=True)
    questionComments = models.TextField(default="Missing context", max_length = 1024, editable=True)
    questionSolved = models.BooleanField(default=False)
    questionSource = models.ForeignKey(Quiz_source, on_delete=models.SET_NULL, null=True, related_name = "questionSource")
    questionTags = models.ManyToManyField(Quiz_tag)

    def __str__(self):
        return "({}) - {}...".format(str(self.questionId), str(self.questionContent[0:100]))

class Quiz_answer(models.Model):
    answerId = models.AutoField(primary_key=True)
    parentQuestion = models.ForeignKey(Quiz_question, on_delete=models.CASCADE)
    answerIsValid = models.BooleanField(default=False)
    answerText = models.TextField(default="Missing answer text", max_length = 256, editable=True)

    def __str__(self):
        return "Parent ({}): {}".format(str(self.parentQuestion.questionId),
                                        str(self.parentQuestion))
