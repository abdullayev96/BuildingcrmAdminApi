from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    UserViewSet, ProjectViewSet,
    EquipmentViewSet, ReportOfWorksViewSet,
    ReportOfInOutViewSet, ReportOfEquipmentInOutViewSet,
    ExpensesOfMoneyViewSet, ReportOfInstrumentViewSet,
    ReportOfDayViewSet, ReportOfMonthViewSet
)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('projects', ProjectViewSet, basename='projects')
router.register('equipments', EquipmentViewSet, basename='equipments')
router.register('reportofworks', ReportOfWorksViewSet, basename='reportofworks')
router.register('reportofinouts', ReportOfInOutViewSet, basename='reportofinouts')
router.register('reportofequipmentinouts', ReportOfEquipmentInOutViewSet, basename='reportofequipmentinouts')
router.register('expensesofmoneys', ExpensesOfMoneyViewSet, basename='expensesofmoneys')
router.register('reportofinstruments', ReportOfInstrumentViewSet, basename='reportofinstruments')
router.register('reportofdays', ReportOfDayViewSet, basename='reportofdays')
router.register('reportofmonths', ReportOfMonthViewSet, basename='reportofmonths')


urlpatterns = [ 
    path('', include(router.urls))
]