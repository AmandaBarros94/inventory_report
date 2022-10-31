class SimpleReport:
    oldest_date = ""
    newest_date = ""
    more_products = ""

    @staticmethod
    def generate(product_list):
        oldest_date = min(
            [product["data_de_fabricacao"] for product in product_list]
        )

        expiration_date = min(
            [product["data_de_validade"] for product in product_list]
        )

        company_list = [product["nome_da_empresa"] for product in product_list]
        more_products = max(company_list, key=company_list.count)

        return (
           f"Data de fabricação mais antiga: {oldest_date}\n"
           f"Data de validade mais próxima: {expiration_date}\n"
           f"Empresa com mais produtos: {more_products}"
        )
