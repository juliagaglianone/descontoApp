from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService

if __name__ == "__main__":
    # Instancia o serviço
    service = PedidoService()

    # Cria pedidos com diferentes descontos
    pedido1 = Pedido("Leonardo", DescontoVIP())
    pedido1.valor_original = 100.0

    pedido2 = Pedido("Maria", DescontoNormal())
    pedido2.valor_original = 200.0

    pedido3 = Pedido("Carlos", DescontoPremium())
    pedido3.valor_original = 150.0

    # Adiciona os pedidos ao serviço
    service.adicionar_pedido(pedido1)
    service.adicionar_pedido(pedido2)
    service.adicionar_pedido(pedido3)

    # Processa e exibe o resultado
    print("Processando Pedidos:")
    service.processar_pedidos()