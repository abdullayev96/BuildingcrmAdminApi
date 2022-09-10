from django.shortcuts import render
from rest_framework import viewsets
from accounts.models import User
from reports.models import *
from api.serializers import (
    UserSerializer, ProjectSerializer,
    EquipmentSerializer, ReportOfWorksSerializer,
    ReportOfInOutSerializer, ReportOfEquipmentInOutSerializer,
    ExpensesOfMoneySerializer, ReportOfInstrumentSerializer,
    ReportOfDaySerializer, ReportOfMonthSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class ReportOfWorksViewSet(viewsets.ModelViewSet):
    queryset = ReportOfWorks.objects.all()
    serializer_class = ReportOfWorksSerializer

class ReportOfInOutViewSet(viewsets.ModelViewSet):
    queryset = ReportOfInOut.objects.all()
    serializer_class = ReportOfInOutSerializer

class ReportOfEquipmentInOutViewSet(viewsets.ModelViewSet):
    queryset = ReportOfEquipmentInOut.objects.all()
    serializer_class = ReportOfEquipmentInOutSerializer

class ExpensesOfMoneyViewSet(viewsets.ModelViewSet):
    queryset = ExpensesOfMoney.objects.all()
    serializer_class = ExpensesOfMoneySerializer

class ReportOfInstrumentViewSet(viewsets.ModelViewSet):
    queryset = ReportOfInstrument.objects.all()
    serializer_class = ReportOfInstrumentSerializer

class ReportOfDayViewSet(viewsets.ModelViewSet):
    queryset = ReportOfDay.objects.all()
    serializer_class = ReportOfDaySerializer

class ReportOfMonthViewSet(viewsets.ModelViewSet):
    queryset = ReportOfMonth.objects.all()
    serializer_class = ReportOfMonthSerializer
