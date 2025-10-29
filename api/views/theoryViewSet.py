import base64

from django.core.files.base import ContentFile
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny

from api.models.article import Article
from api.models.articleImage import ArticleImage
from api.models.course import Course
from api.models.profile import Profile
from api.models.theory import Theory
from api.serializers.theorySerializer import TheorySerializer


class TheoryViewSet(viewsets.ModelViewSet):
    queryset = Theory.objects.all()
    serializer_class = TheorySerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        id = request.data.get('id')
        course_id = request.data.get('courseId')
        title = request.data.get('title')
        body = ""
        for item in request.data.get('articleItemsList'):
            order = item.get('order')
            type = item.get('type')
            text = item.get('text')
            if type == 'text':
                body += ">>>" + text + "\r\n"
            if type == 'img':
                if 'image_' in text:
                    img = ArticleImage.objects.get(name=text.split('\r\n')[0])
                else:
                    img = ArticleImage.objects.create()
                    format, imgstr = text.split(';base64,')
                    ext = format.split('/')[-1]
                    data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
                    img.image = data
                    img.save()
                    img.name = "image_" + str(img.id)
                    img.save()
                body += ">>>" + img.name + "\r\n"
        if id is not None:
            article = Theory.objects.get(id=id)
            article.body = body
            article.title = title
        else:
            article = Theory(title=title, body=body)
        article.save()
        course = Course.objects.get(id=course_id)
        course.theories.add(article)
        course.save()
        article.order = course.theories.count() - 1
        article.save()

        return HttpResponse(status=status.HTTP_201_CREATED)
