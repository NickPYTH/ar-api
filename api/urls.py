from django.urls import include, path
from rest_framework import routers

from api.views.achievmentViewSet import AchievementViewSet
from api.views.answerViewSet import AnswerViewSet
from api.views.articleFireWorks import ArticleFireWorksViewSet
from api.views.articleImageViewSet import ArticleImageViewSet
from api.views.articleViewSet import ArticleViewSet
from api.views.calculatedTestViewSet import CalculatedTestViewSet
from api.views.courseViewSet import CourseViewSet
from api.views.profileViewSet import ProfileViewSet
from api.views.questionViewSet import QuestionViewSet
from api.views.testViewSet import TestViewSet
from api.views.theoryViewSet import TheoryViewSet
from api.views.theory_studentViewSet import TheoryAndStudentViewSet

router = routers.DefaultRouter() # upd
router.register(r'profiles', ProfileViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'tests', TestViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'articlesFireWorks', ArticleFireWorksViewSet)
router.register(r'calculatedTests', CalculatedTestViewSet)
router.register(r'articleImages', ArticleImageViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'theories', TheoryViewSet)
router.register(r'theoryAndStudent', TheoryAndStudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
