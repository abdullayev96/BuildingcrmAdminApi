from django.db import models
from accounts.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    langitude = models.FloatField()
    lotitude = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    balanace = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"


class ReportOfWorks(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reportofworks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reportofworks')
    title_of_work = models.CharField(max_length=100, verbose_name="Title of work")
    comment = models.TextField(null=True, blank=True)
    measure = models.CharField(max_length=64, null=True)
    count_of_work = models.IntegerField(null=True, verbose_name="Count of work")
    price = models.FloatField()
    summa = models.BigIntegerField(null=True, blank=True)
    comment_of_admin = models.TextField(null=True, blank=True, verbose_name="Comment of admin")

    def __str__(self):
        return f"M: {self._base_manager} | W: {self.title_of_work}"

    class Meta:
        verbose_name = "Report of Works"
        verbose_name_plural = "Reports of Works"


class ReportOfInOut(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reportofinouts')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reportofinouts')
    worker = models.CharField(max_length=100)
    work_time = models.IntegerField(verbose_name="Work time")
    all_work_time = models.IntegerField(verbose_name="All work time")
    day_wage = models.FloatField(verbose_name="Day wage")
    salary = models.FloatField()

    def __str__(self):
        return f"M: {self._base_manager} | W: {self.worker} | WT: {self.work_time}"

    class Meta:
        verbose_name = "Report of InOut"
        verbose_name_plural = "Reports of InOut"




class ReportOfEquipmentInOut(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = 'New'
        USED = 'Used'
    which_project_from = models.ForeignKey(Project, verbose_name="Which Project From",on_delete=models.CASCADE, related_name='reportofequipmentinouts')
    which_manager_from = models.ForeignKey(User, verbose_name="Which Manager From",on_delete=models.CASCADE, related_name='reportofequipmentinouts')
    which_project_to = models.CharField(verbose_name="Which Project To", max_length=100)
    which_manager_to = models.CharField(verbose_name="Which Manager To", max_length=100)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='reportofequipmentinouts')
    status = models.CharField(max_length=64, choices=StatusChoices.choices, default=StatusChoices.NEW)
    count = models.IntegerField()
    income_count = models.IntegerField(null=True, blank=True, verbose_name="Income Count")
    outlay_count = models.IntegerField(null=True, blank=True, verbose_name="Outlay Count")
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"M: {self._base_manager} | P: {self.which_project_from} | P: {self.which_project_to} | E: {self.equipment}"

    class Meta:
        verbose_name = "Report of Equipment InOut"
        verbose_name_plural = "Reports of Equipment InOut"





    
class ExpensesOfMoney(models.Model):
    taken_manager = models.ForeignKey(User, verbose_name="Manager Given", on_delete=models.CASCADE, related_name='expensesofmoney')
    given_manager = models.ForeignKey(User, verbose_name="Manager Taken",on_delete=models.CASCADE, related_name='expensesofmoney_given')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expensesofmoney')
    purpose = models.CharField(max_length=200, null=True)
    income = models.BigIntegerField(null=True, blank=True)
    outlay = models.BigIntegerField(null=True, blank=True)
    remaining_summ = models.BigIntegerField(null=True, blank=True, verbose_name="Remaining Summ")
    all_income = models.BigIntegerField(verbose_name="All Income", null=True, blank=True)
    all_outlay = models.BigIntegerField(verbose_name="All Outlay", null=True, blank=True)
    all_remining_summ = models.BigIntegerField(verbose_name="All Remaining Summ", null=True, blank=True)
    comment_of_admin = models.TextField(null=True, blank=True, verbose_name="Comment of Admin")

    def __str__(self):
        return f"M: {self._base_manager} | M: {self.given_manager} | P: {self.project}"

    class Meta:
        verbose_name = "Expenses of Money"
        verbose_name_plural = "Expenses of Money"

class ReportOfInstrument(models.Model):
    mechanic = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reportofinstruments')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reportofinstruments')
    instrument = models.CharField(max_length=100)
    what_work = models.CharField(max_length=200, verbose_name="What Work")
    who_fuel_taken_from = models.CharField(max_length=200, verbose_name="Who Fuel Taken From")
    taken_amount_of_fuel = models.FloatField(verbose_name="Taken Amount of Fuel")
    spending_fuel = models.FloatField(verbose_name="Spending Fuel")
    price_of_fuel = models.IntegerField(verbose_name="Price of Fuel")
    measure_of_work = models.CharField(max_length=64, null=True, verbose_name="Measure of Work")
    work_time = models.IntegerField(verbose_name="Work Time")
    work_price = models.FloatField(verbose_name="Price of Work")
    money_worked = models.BigIntegerField(verbose_name="Money Worked")
    exponse = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"I: {self.instrument} | W: {self.what_work}"


class ReportOfDay(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reportofdays')
    count_of_reports = models.IntegerField(verbose_name="Count of Reports")
    status_of_report = models.CharField(max_length=100, verbose_name="Status of Report")
    report_of_inout = models.BooleanField(verbose_name="InOut")
    report_of_works = models.BooleanField(verbose_name="Works")
    report_of_expenses = models.BooleanField(verbose_name="Expenses")
    report_of_instruments = models.BooleanField(verbose_name="Instruments")


    def __str__(self):
        return f"M: {self.manager} |S: {self.status_of_report} | C: {self.count_of_reports}"

    class Meta:
        verbose_name = "Report of Day"
        verbose_name_plural = "Reports of Day"


class ReportOfMonth(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reportofmonths')
    name_of_report = models.CharField(max_length=100, verbose_name="Name of Report")

    def __str__(self):
        return f"M: {self.manager} | N: {self.name_of_report}"

    class Meta:
        verbose_name = "Report of Month"
        verbose_name_plural = "Reports of Month"

