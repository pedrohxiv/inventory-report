from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        id="1",
        product_name="Test Product",
        company_name="Test Company",
        manufacturing_date="2023-07-17",
        expiration_date="2023-12-31",
        serial_number="1793ZTM",
        storage_instructions="Lorem ipsum dolor sit amet."
    )

    assert str(product) == (
        "The product 1 - Test Product "
        "with serial number 1793ZTM "
        "manufactured on 2023-07-17 "
        "by the company Test Company "
        "valid until 2023-12-31 "
        "must be stored according to the following instructions: "
        "Lorem ipsum dolor sit amet.."
    )
