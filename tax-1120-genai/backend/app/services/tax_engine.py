def calculate_1120_tax(data: dict):

    gross_income = (
        data.get("gross_receipts", 0)
        - data.get("cogs", 0)
        + data.get("other_income", 0)
    )

    total_deductions = (
        data.get("total_deductions", 0)
        + data.get("depreciation", 0)
        + data.get("interest_expense", 0)
    )

    taxable_income = gross_income - total_deductions

    if taxable_income < 0:
        taxable_income = 0

    # NOL (80% cap)
    nol = min(data.get("nol_carryforward", 0), taxable_income * 0.8)
    taxable_income -= nol

    tax = taxable_income * 0.21

    return {
        "gross_income": gross_income,
        "taxable_income": taxable_income,
        "tax": tax,
        "nol_used": nol
    }