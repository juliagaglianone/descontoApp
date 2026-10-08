from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.use_cases.criar_pedido import CriarPedido

if __name__ == "__main__":
    
    database = MemoryDatabase()
    repository = MemoryPedidoRepository(database)
    use_case = CriarPedido(pedido_gateway=repository)
    controller = PedidoController(criar_pedido_use_case=use_case)

    pedido1 = controller.criar_pedido(cliente="Cliente 1", valor_original=100.0, tipo_desconto="normal")
    pedido2 = controller.criar_pedido(cliente="Cliente 2", valor_original=100.0, tipo_desconto="vip")
    pedido3 = controller.criar_pedido(cliente="Cliente 3", valor_original=100.0, tipo_desconto="premium")

    print("\nLista dos Pedidos:")
    for pedido in controller.listar_pedidos():
        print(f"Cliente: {pedido.cliente} | Original: R${pedido.valor_original:.2f} | Final: R${pedido.valor_final():.2f}")