import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        with open(path, "r") as file:
            if path.endswith(".csv"):
                fileCsv = csv.DictReader(file)
                data = [row for row in fileCsv]
            elif path.endswith(".json"):
                data = json.load(file)
            elif path.endswith(".xml"):
                data = xmltodict.parse(file.read())["dataset"]["record"]

        if report_type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
