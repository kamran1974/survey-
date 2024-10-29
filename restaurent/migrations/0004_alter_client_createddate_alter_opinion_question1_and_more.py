# Generated by Django 5.1.2 on 2024-10-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurent', '0003_alter_opinion_question1_alter_opinion_question2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='createddate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='question1',
            field=models.IntegerField(choices=[(1, 'good'), (2, 'moderate'), (3, 'poor'), (4, 'terrible')]),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='question2',
            field=models.IntegerField(choices=[(1, 'good'), (2, 'moderate'), (3, 'poor'), (4, 'terrible')]),
        ),
    ]