# Generated by Django 3.0.3 on 2020-02-25 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('TC', 'Tecnologia'), ('CR', 'Curiosidades'), ('GR', 'Geral'), ('CC', 'Ciência da Computação'), ('CS', 'Ciência de Dados')], default='GR', max_length=2),
        ),
    ]
