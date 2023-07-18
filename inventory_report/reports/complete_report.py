from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        oldest_manufacturing_date = self._get_oldest_manufacturing_date()
        closest_expiration_date = self._get_closest_expiration_date()
        largest_inventory_company = self._get_largest_inventory_company()
        stocked_products_by_company = self._get_stocked_products_by_company()

        return (
           f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
           f"Closest expiration date: {closest_expiration_date}\n"
           f"Company with the largest inventory: {largest_inventory_company}\n"
           f"Stocked products by company:\n"
           f"{stocked_products_by_company}"
        )

    def _get_stocked_products_by_company(self) -> str:
        company_inventory: dict[str, int] = {}

        for inventory in self.inventories:
            for product in inventory.data:
                if product.company_name in company_inventory:
                    company_inventory[product.company_name] += 1
                else:
                    company_inventory[product.company_name] = 1

        company_and_stock = ""

        for company, stock in company_inventory.items():
            company_and_stock += f"- {company}: {stock}\n"

        return company_and_stock
