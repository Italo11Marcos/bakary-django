# Generated by Django 4.1.3 on 2022-11-23 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padaria', '0005_pedido_codigo_alter_pedido_pagamento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='quantidadeProduto',
            field=models.IntegerField(default=1, verbose_name='Quantidade Produto'),
            preserve_default=False,
        ),
    ]
