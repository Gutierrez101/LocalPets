# Generated by Django 5.1.6 on 2025-03-01 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginaWeb', '0002_remove_tablavinculada_tablaprueva_delete_tablaprueva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='estado',
            field=models.CharField(choices=[('Perdido', 'Perdido'), ('Encontrado', 'Encontrado'), ('Adoptado', 'Adoptado')], default='Perdido', max_length=50),
        ),
    ]
