# Generated by Django 4.1.3 on 2022-11-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padaria', '0002_delete_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.TextField(default='padrão'),
            preserve_default=False,
        ),
    ]
