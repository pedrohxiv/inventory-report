from datetime import date
from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report
from typing import List


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        oldest_manufacturing_date = self._get_oldest_manufacturing_date()
        closest_expiration_date = self._get_closest_expiration_date()
        largest_inventory_company = self._get_largest_inventory_company()

        return (
           f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
           f"Closest expiration date: {closest_expiration_date}\n"
           f"Company with the largest inventory: {largest_inventory_company}\n"
        )

    def _get_oldest_manufacturing_date(self) -> str:
        oldest_manufacturing_date = '3000-12-31'

        for inventory in self.inventories:
            for product in inventory.data:
                if product.manufacturing_date < oldest_manufacturing_date:
                    oldest_manufacturing_date = product.manufacturing_date

        return oldest_manufacturing_date

    def _get_closest_expiration_date(self) -> str:
        closest_expiration_date = '3000-12-31'

        for inventory in self.inventories:
            for product in inventory.data:
                if (
                    product.expiration_date >= str(date.today()) and
                    product.expiration_date < closest_expiration_date
                ):
                    closest_expiration_date = product.expiration_date

        return closest_expiration_date

    def _get_largest_inventory_company(self) -> str:
        company_inventory: dict[str, int] = {}

        for inventory in self.inventories:
            for product in inventory.data:
                if product.company_name in company_inventory:
                    company_inventory[product.company_name] += 1
                else:
                    company_inventory[product.company_name] = 1

        return max(company_inventory, key=lambda x: company_inventory[x])
