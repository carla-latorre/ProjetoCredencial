# Generated by Django 4.2 on 2023-05-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroUsuario', '0002_usuario_numcadastro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='iddadosmed',
        ),
        migrations.AddField(
            model_name='usuario',
            name='convenio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='possuialergia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='possuilesao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='problemasaude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='restricaoativ',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tpsanguineo',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usamedicamento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='DadosMedicos',
        ),
    ]