try:
    age_str = input("Enter your age:")
    num = int(age_str)
except ValueError:
    print(f"'{age_str}'. Please enter a whole numerical value for age.")
else:
    if num % 2 == 0:
        print(f"{num}is an even number.")
    else:
        print(f"{num}is an odd number.")
