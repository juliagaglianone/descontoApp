from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.presenters.pedido_presenter import PedidoPresenter
from src.app.use_cases.criar_pedido import CriarPedido

if __name__ == "__main__":

    database = MemoryDatabase()

    repository = MemoryPedidoRepository(database)

    use_case = CriarPedido(pedido_gateway=repository)

    presenter = PedidoPresenter()

    controller = PedidoController(criar_pedido_use_case=use_case, presenter=presenter)

    controller.criar_pedido(cliente="Cliente 1", valor_original=100.0, tipo_desconto="normal")
    controller.criar_pedido(cliente="Cliente 2", valor_original=100.0, tipo_desconto="vip")
    controller.criar_pedido(cliente="Cliente 3", valor_original=100.0, tipo_desconto="premium")

    print("\nLista dos Pedidos:")
    pedidos_formatados = controller.listar_pedidos()

    for pedido in pedidos_formatados:
        print(
            f"Cliente: {pedido['cliente']} | "
            f"Original: R${pedido['valor_original']:.2f} | "
            f"Desconto: R${pedido['valor_desconto']:.2f} | "
            f"Final: R${pedido['valor_final']:.2f} | "
            f"Tipo: {pedido['tipo_desconto'].capitalize()}"
        )