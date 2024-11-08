from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=11)
    createddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

qualitychoices =(
    (1, 'good'),
    (2,'moderate'),
    (3,'poor'),
    (4,'terrible')

)

class Opinion(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    question1 = models.IntegerField(choices=qualitychoices)#کیفیت غذا
    question2 = models.IntegerField(choices=qualitychoices)#کیفیت پذیرایی
    question3 = models.IntegerField(choices=qualitychoices)# آیس کارامل
    question4 = models.IntegerField(choices=qualitychoices)#چیز کیک 
    question5 = models.IntegerField(choices=qualitychoices)#شیک 
    question6 = models.BooleanField(blank= True)#اقلام میز 
    question7 = models.BooleanField(blank= True)#اقلام میز 
    question8 = models.BooleanField(blank= True)#اقلام میز 
    question9 = models.BooleanField(blank= True)#اقلام میز 
    question10 = models.BooleanField(blank= True)#اقلام میز  
    idea = models.TextField()
    submitted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}{self.get_question1_display()}{self.question2}{self.question3}{self.question4}{self.question5}{self.question6}{self.question7}{self.question8}{self.question9}{self.question10}{self.idea}'







