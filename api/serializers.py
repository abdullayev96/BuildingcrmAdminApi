from accounts.models import *
from reports.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class ReportOfWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportOfWorks
        fields = '__all__'


class ReportOfInOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportOfInOut
        fields = '__all__'


class ReportOfEquipmentInOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportOfEquipmentInOut
        fields = '__all__'


class ExpensesOfMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesOfMoney
        fields = '__all__'

class ReportOfInstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportOfInstrument
        fields = '__all__'


class ReportOfDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportOfDay
        fields = '__all__'


class ReportOfMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportOfMonth
        fields = '__all__'

        