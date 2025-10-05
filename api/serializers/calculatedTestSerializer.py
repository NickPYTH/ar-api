from rest_framework import serializers

from api.models.calculatedTest import CalculatedTest
from api.serializers.testSerializer import TestSerializer
from api.serializers.testUserQuestionAnswerSerializer import TestUserQuestionAnswerSerializer
from api.serializers.userSerializer import UserSerializer


class CalculatedTestSerializer(serializers.HyperlinkedModelSerializer):
    test = TestSerializer()
    user = UserSerializer()
    test_user_question_answer_list = TestUserQuestionAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = CalculatedTest
        fields = ('id', 'user', 'test', 'test_user_question_answer_list')
