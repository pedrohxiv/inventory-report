from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        id="1",
        product_name="Test Product",
        company_name="Test Company",
        manufacturing_date="2023-07-17",
        expiration_date="2023-12-31",
        serial_number="1793ZTM",
        storage_instructions="Lorem ipsum dolor sit amet."
    )

    assert product.id == "1"
    assert product.product_name == "Test Product"
    assert product.company_name == "Test Company"
    assert product.manufacturing_date == "2023-07-17"
    assert product.expiration_date == "2023-12-31"
    assert product.serial_number == "1793ZTM"
    assert product.storage_instructions == "Lorem ipsum dolor sit amet."
