from src.repositories.pedido_repository import PedidoRepository
from src.models.pedido import Pedido

class PedidoService:
    """Classe de serviço para regras de negócio e intermediação com o repositório"""

    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    def adicionar_pedido(self, pedido: Pedido):
        self.repository.adicionar_pedido(pedido)

    def processar_pedidos(self):
        pedidos = self.repository.listar_pedidos()
        for pedido in pedidos:
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")