from django.db import models
from datetime import datetime


systemchoices = (('0','System1'),('1','System2'),('2','System3'),('3','System4'))
processchoices = (('0','Process1'),('1','Process2'),('2','Process3'),('3','Process4'))
buchoices = (('0','BU1'),('1','BU2'),('2','BU3'),('3','BU4'))
sourcechoices = (('0','Email'),('1','Website'),('2','System'))
ageingchoices = (('0','current'),('1','aged'),('2','urgent'))
statuschoices = (('0','action needed'),('1','pending'),('2','completed'))
namechoices = (('0','Colleague1'),('1','Colleague2'),('2','Colleague3'))
passfailchoices = (('0','N/A'),('1','PASS'),('2','FAIL'))

# Create your models here.
class Task(models.Model):
    # system = models.CharField(max_length=20, choices=systemchoices, default='0')
    process = models.CharField(max_length=20, choices=processchoices, default='0')
    # business_segment = models.CharField(max_length=20, choices=buchoices, default='0')
    starting_date = models.DateTimeField(null=True, blank=True, default=datetime(1900,1,1,0,0))
    days_to_complete = models.SmallIntegerField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True, default=datetime(1900,1,1,0,0))
    ageing = models.CharField(max_length=20, choices=ageingchoices, default='0')
    # ticket_number = models.SmallIntegerField()
    # email_subject = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=20, choices=statuschoices, default='0')
    name = models.CharField(max_length=50, choices=namechoices, default='0')
    # contact = models.CharField(max_length=200, null=True, blank=True)
    supplier = models.CharField(max_length=200, null=True, blank=True)
    # supplier_number = models.SmallIntegerField(null=True, blank=True)
    # supplier_email = models.EmailField(null=True, blank=True)
    # action_started = models.DateTimeField(null=True, blank=True, default=datetime(1900,1,1,0,0))
    # output_number = models.IntegerField(null=True, blank=True)
    # complete = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True, default=datetime(1900,1,1,0,0))
    # pass_or_fail = models.CharField(max_length=50, choices=passfailchoices, default='0', null=True, blank=True)
    editing = models.BooleanField(default=False)


#    def __str__(self):
#        return self.system, self.process, self.business_segment
# Create your models here.
