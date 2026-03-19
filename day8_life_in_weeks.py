def life_in_weeks(age):
    """
    Calculate and print how many weeks are left until age 90.
    Output format: "You have x weeks left."
    """
    years_left = 90 - int(age)
    weeks_left = max(0, years_left * 52)
    print(f"You have {weeks_left} weeks left.")


if __name__ == "__main__":
    try:
        age_input = input("Enter your current age in years: ")
        age = int(age_input)
        if age < 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid non-negative integer for age.")
    else:
        life_in_weeks(age)