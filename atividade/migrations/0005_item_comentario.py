# Generated by Django 4.2.3 on 2023-07-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0004_itemchoise_areachoise'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='comentario',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
