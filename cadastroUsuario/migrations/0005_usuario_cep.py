# Generated by Django 4.2 on 2023-05-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroUsuario', '0004_usuario_nomerecado'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cep',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
