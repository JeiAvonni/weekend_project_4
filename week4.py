class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Income:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Property:
    def __init__(self, address):
        self.address = address
        self.expenses = []
        self.incomes = []
        self.roi = None

    def add_expense(self, expense):
        self.expenses.append(expense)

    def add_income(self, income):
        self.incomes.append(income)

    def calculate_roi(self):
        total_income = sum(income.amount for income in self.incomes)
        total_expense = sum(expense.amount for expense in self.expenses)
        self.roi = (total_income - total_expense) / total_expense * 100
        return self.roi


class User:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)


def main():
    users = []

    while True:
        print("\n1. Create User")
        print("2. Add Property")
        print("3. Calculate ROI")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user name: ")
            user = User(name)
            users.append(user)
            print(f"User '{name}' created successfully.")

        elif choice == '2':
            if not users:
                print("Please create a user first.")
                continue

            user_name = input("Enter user name: ")
            user = next((u for u in users if u.name == user_name), None)

            if user:
                address = input("Enter property address: ")
                property = Property(address)
                user.add_property(property)
                print("Property added successfully.")
            else:
                print("User not found.")

       
        elif choice == '3':
            if not users:
                print("Please create a user first.")
                continue

            user_name = input("Enter user name: ")
            user = next((u for u in users if u.name == user_name), None)

            if user:
                if not user.properties:
                    print("User has no properties.")
                    continue

                for i, prop in enumerate(user.properties):
                    print(f"{i+1}. {prop.address}")

                property_index = int(input("Enter property number to calculate ROI: ")) - 1

                if 0 <= property_index < len(user.properties):
                    property = user.properties[property_index]
                    roi = property.calculate_roi()
                    print(f"ROI for property '{property.address}': {roi:.2f}%")
                else:
                    print("Invalid property number.")
            else:
                print("User not found.")

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
