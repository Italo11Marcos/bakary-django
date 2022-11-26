# Generated by Django 4.1.3 on 2022-11-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padaria', '0003_produto_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='valor',
            new_name='valorPedido',
        ),
        migrations.AddField(
            model_name='pedido',
            name='valorProduto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
