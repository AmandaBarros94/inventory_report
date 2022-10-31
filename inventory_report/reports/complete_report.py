from typing import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_report = SimpleReport.generate(list)
        inventory = Counter(product["nome_da_empresa"] for product in list)
        companies = ""
        for company in inventory:
            companies += f"- {company}: {inventory[company]}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies}"
        )
