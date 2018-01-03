# Generated by Django 2.0 on 2018-01-01 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=40, verbose_name='Sobrenome')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('datanascimento', models.DateField(verbose_name='Data de nascimento')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=4, verbose_name='Sexo')),
            ],
        ),
    ]
