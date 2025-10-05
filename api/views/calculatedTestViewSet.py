import json

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from api.models.answer import Answer
from api.models.calculatedTest import CalculatedTest
from api.models.question import Question
from api.models.test_user_question_answer import TestUserQuestionAnswer
from api.models.test import Test
from api.serializers.calculatedTestSerializer import CalculatedTestSerializer


class CalculatedTestViewSet(viewsets.ModelViewSet):
    queryset = CalculatedTest.objects.all()
    serializer_class = CalculatedTestSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data
        test = CalculatedTest()
        test.test = Test.objects.get(id=data['test_id'])
        test.user = request.user
        test.save()
        question_answer_list = []
        max_points = 0
        user_points = 0
        for el in json.loads(data['result']):
            question = Question.objects.get(id=el['QuestionId'])
            max_points += question.points
            answer = Answer.objects.get(id=el['AnswerId'])
            if answer.isCorrect:
                user_points += question.points
            question_answer = TestUserQuestionAnswer.objects.create(user=test.user,
                                                                    question=question,
                                                                    answer=answer)
            question_answer.save()
            question_answer_list.append(question_answer)
            question_answer.save()
        test.test_user_question_answer_list.set(question_answer_list)
        test.max_points = max_points
        test.user_points = user_points
        test.save()
        is_passed = test.test.pass_line <= (user_points / max_points)
        return Response({"isPassed": is_passed, "maxPoints": max_points, "userPoints": user_points}, status=201)
