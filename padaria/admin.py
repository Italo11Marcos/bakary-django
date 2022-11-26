from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from .models import CustomUsuario, Pedido, Produto, ItensPedido
from django.utils.html import format_html

admin.site.site_title = "Dolce Caffè"
admin.site.site_header = "Dolce Caffè"
admin.site.index_title = "Dolce Caffè"

@admin.register(CustomUsuario)
class CustomUsuario(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'cpf', 'estado', 'cidade', 'celular','last_login', 'date_joined', 'is_superuser', 'username', 'first_name', 'last_name', 'is_active', 'rua', 'numero', 'cep', 'dataNascimento', 'password']
    list_filter = ('is_superuser',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['codigo','pagamento','valorPedido','statusPedido','dataCriacao','dataAtualizacao','user','view_produtos_link']
    list_filter = ('statusPedido','pagamento',)
    search_fields = ('codigo__contains',)

    def view_produtos_link(self, obj):
        count = obj.produtos.count()
        url = (
            reverse("admin:padaria_produto_changelist")
            + "?"
            + urlencode({"pedidos__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Produtos</a>', url, count)

    view_produtos_link.short_description = "Produtos"

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao','sabor', 'tamanho', 'precoUnitario', 'image_tag', 'imagem']

@admin.register(ItensPedido)
class ItensPedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'produto', 'valorPedido', 'quantidadeProduto', 'valorProduto', 'dataCriacao', 'dataAtualizacao']
    list_filter = ('produto',)