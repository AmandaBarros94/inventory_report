from inventory_report.inventory.product import Product


def test_relatorio_produto():
    mock_product = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1",
    )

    assert str(mock_product) == (
        f"O produto {mock_product.nome_do_produto}"
        f" fabricado em {mock_product.data_de_fabricacao}"
        f" por {mock_product.nome_da_empresa} com validade"
        f" até {mock_product.data_de_validade}"
        f" precisa ser armazenado {mock_product.instrucoes_de_armazenamento}."
    )
