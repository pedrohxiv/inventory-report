from inventory_report.importers import IMPORTERS
from inventory_report.inventory import Inventory
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from typing import List


def process_report_request(file_paths: List[str], report_type: str) -> str:
    validate_report_type(report_type)
    inventories = create_inventories(file_paths)
    report = generate_report(report_type, inventories)
    return report


def validate_report_type(report_type: str) -> None:
    if report_type not in ["simple", "complete"]:
        raise ValueError("Report type is invalid.")


def create_inventories(file_paths: List[str]) -> List[Inventory]:
    inventories = []
    for path in file_paths:
        file_extension = get_file_extension(path)
        if file_extension in IMPORTERS:
            inventory = import_inventory(file_extension, path)
            inventories.append(inventory)
    return inventories


def get_file_extension(path: str) -> str:
    return path.split(".")[-1]


def import_inventory(file_extension: str, path: str) -> Inventory:
    ImporterClass = IMPORTERS[file_extension]
    importer = ImporterClass(path)
    products = importer.import_data()
    return Inventory(products)


def generate_report(report_type: str, inventories: List[Inventory]) -> str:
    if report_type == "simple":
        report = generate_simple_report(inventories)
    elif report_type == "complete":
        report = generate_complete_report(inventories)
    return report


def generate_simple_report(inventories: List[Inventory]) -> str:
    simple_report = SimpleReport()
    for inventory in inventories:
        simple_report.add_inventory(inventory)
    return simple_report.generate()


def generate_complete_report(inventories: List[Inventory]) -> str:
    complete_report = CompleteReport()
    for inventory in inventories:
        complete_report.add_inventory(inventory)
    return complete_report.generate()
