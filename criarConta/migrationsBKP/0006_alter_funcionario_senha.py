# Generated by Django 4.2 on 2023-05-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criarConta', '0005_funcionario_last_login_funcionario_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='senha',
            field=models.CharField(max_length=20),
        ),
    ]
