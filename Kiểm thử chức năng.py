def calculate_insurance_fee(age, driving_years, accident_count):
    if age < 18:
        return "Không được phép mua bảo hiểm"
    elif 18 <= age <= 25:
        fee = 2000000
    else:
        fee = 1000000

    if driving_years < 1:
        fee += 500000

    if accident_count > 0:
        fee += 1000000

    return fee

# Ví dụ kiểm tra
age = 24
driving_years = 2
accident_count = 0
result = calculate_insurance_fee(age, driving_years, accident_count)
print(f"Phí bảo hiểm: {result}")
