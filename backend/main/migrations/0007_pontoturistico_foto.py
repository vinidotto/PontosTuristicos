# Generated by Django 5.1 on 2024-11-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_pontoturistico_endereco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(null=True, upload_to='pontos_turisticos'),
        ),
    ]
