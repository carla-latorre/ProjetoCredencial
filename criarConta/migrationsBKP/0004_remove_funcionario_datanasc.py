# Generated by Django 4.2 on 2023-05-21 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('criarConta', '0003_alter_funcionario_doc_alter_funcionario_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='datanasc',
        ),
    ]