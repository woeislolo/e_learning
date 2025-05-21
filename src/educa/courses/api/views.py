from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from courses.models import *
from .serializers import *


class SubjectListView(generics.ListAPIView):
    """ Вернет список доступных дисциплин """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """ Вернет информацию по конкретной дисциплине """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вернет список всех курсов с детальной информацией, 
    либо детальную информацию по конкретному курсу,
    либо зачислит студента на конкретный курс """
    # list, retrieve + enroll
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True,
            methods=['post'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated]
            )
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})
    