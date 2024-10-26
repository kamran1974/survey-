from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=11)
    createddate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

qualitychoices =(
    (1,'good'),
    (2,'moderate'),
    (3,'poor'),
    (4,'terrible')

)

class Opinion(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    question1 = models.IntegerField(choices=qualitychoices)#کیفیت غذا
    question2 = models.IntegerField(choices=qualitychoices)#کیفیت پذیرایی
    idea = models.TextField()
    submitted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}{self.get_question1_display()}{self.question2}'







