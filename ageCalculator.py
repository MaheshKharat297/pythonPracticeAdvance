def ageCalculate(age):
    days_per_year = 365
    weeks_per_year = 52
    months_per_year = 12

    max_age_years = 90
    max_age_days = max_age_years * days_per_year
    max_age_weeks = max_age_years * weeks_per_year
    max_age_months = max_age_years * months_per_year

    remain_age_years = max_age_years - age
    remain_age_days = max_age_days - (age*days_per_year)
    remain_age_weeks = max_age_weeks - (age*weeks_per_year)
    remain_age_months = max_age_months - (age*months_per_year)

    print(f"The person having {remain_age_years} in years")
    print(f"The person having {remain_age_days} in days")
    print(f"The person having {remain_age_weeks} in weeks")
    print(f"The person having {remain_age_months} in months")

age = int(input("Please enter person current age : "))
ageCalculate(age)
