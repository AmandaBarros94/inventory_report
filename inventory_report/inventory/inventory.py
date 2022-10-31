import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        with open(path, "r") as file:
            if path.endswith(".csv"):
                fileCsv = csv.DictReader(file)
                data = [row for row in fileCsv]
            else:
                raise ValueError("Arquivo inválido")

        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)
