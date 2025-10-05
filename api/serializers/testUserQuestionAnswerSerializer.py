from rest_framework import serializers

from api.models.test_user_question_answer import TestUserQuestionAnswer
from api.serializers.answerSerializer import AnswerSerializer
from api.serializers.questionSerializers import QuestionSerializer
from api.serializers.userSerializer import UserSerializer


class TestUserQuestionAnswerSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    question = QuestionSerializer()
    answer = AnswerSerializer()

    class Meta:
        model = TestUserQuestionAnswer
        fields = ('id', 'user', 'question', 'answer',)
