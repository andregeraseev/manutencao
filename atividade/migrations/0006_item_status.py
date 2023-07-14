# Generated by Django 4.2.3 on 2023-07-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0005_item_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('concluido', 'Concluído'), ('em_manutencao', 'Em Manutenção'), ('pendente', 'Pendente')], default='Pendente', max_length=20),
        ),
    ]
