from django.contrib import admin
from reports.models import * 

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass

@admin.register(ReportOfWorks)
class ReportOfWorksAdmin(admin.ModelAdmin):
    pass

@admin.register(ReportOfInOut)
class ReportOfInOutAdmin(admin.ModelAdmin):
    pass

@admin.register(ReportOfInstrument)
class ReportOfInstrumentAdmin(admin.ModelAdmin):
    pass

@admin.register(ExpensesOfMoney)
class ExpensesOfMoneyAdmin(admin.ModelAdmin):
    pass


@admin.register(ReportOfEquipmentInOut)
class ReportOfEquipmentInOutAdmin(admin.ModelAdmin):
    pass


@admin.register(ReportOfDay)
class ReportOfDayAdmin(admin.ModelAdmin):
    pass

@admin.register(ReportOfMonth)
class ReportOfMonthAdmin(admin.ModelAdmin):
    pass

