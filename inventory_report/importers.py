import csv
import json

from abc import ABC, abstractmethod
from inventory_report.product import Product
from typing import Dict, List, Type


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file:
            data = json.load(file)

        products = []

        for item in data:
            products.append(Product(**item))

        return products


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path) as file:
            data = csv.DictReader(file)

            products = []

            for item in data:
                products.append(Product(**item))

        return products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
