# Generated by Django 4.0.4 on 2022-06-21 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='manager_mail',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
