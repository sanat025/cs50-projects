import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data.json")


def parse_amount(text: str) -> float:
    """
    Convert user input like '120', '120.50', '₹120', '₹1,200.50' into a float.
    Raises ValueError for invalid or non-positive values.
    """
    cleaned = text.strip().replace("₹", "").replace(",", "")
    amount = float(cleaned)

    if amount <= 0:
        raise ValueError("Amount must be positive")

    return amount


def categorize(description: str) -> str:
    """
    Categorize an expense description using simple keywords.
    """
    d = description.lower()

    if any(word in d for word in ["pizza", "burger", "restaurant", "food", "cafe"]):
        return "Food"

    if any(word in d for word in ["uber", "ola", "bus", "train", "metro", "fuel", "petrol", "ride", "taxi"]):
        return "Transport"

    if any(word in d for word in ["rent", "electricity", "bill", "wifi", "recharge", "gas", "water"]):
        return "Bills"

    if any(word in d for word in ["book", "course", "tuition", "fees", "class", "school"]):
        return "Education"

    return "Other"


def budget_status(spent: float, budget: float) -> str:
    """
    Return budget usage status:
    - OK: spent < 80% of budget
    - Warning: 80% <= spent <= 100%
    - Exceeded: spent > 100%
    """
    if budget <= 0:
        raise ValueError("Budget must be positive")
    if spent < 0:
        raise ValueError("Spent cannot be negative")

    ratio = spent / budget

    if ratio < 0.8:
        return "OK"
    if ratio <= 1.0:
        return "Warning"
    return "Exceeded"


def load_transactions(path: Path = DATA_FILE) -> list[dict]:
    """
    Load transactions from a JSON file. Returns an empty list if file doesn't exist.
    """
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_transactions(transactions: list[dict], path: Path = DATA_FILE) -> None:
    """
    Save transactions to a JSON file.
    """
    path.write_text(json.dumps(transactions, indent=2), encoding="utf-8")


def add_transaction(transactions: list[dict], kind: str, amount: float, description: str) -> None:
    """
    Add a transaction to the list. kind must be 'expense' or 'income'.
    """
    if kind not in {"expense", "income"}:
        raise ValueError("kind must be 'expense' or 'income'")

    transactions.append(
        {
            "kind": kind,
            "amount": amount,
            "description": description.strip(),
            "category": categorize(description),
            "timestamp": datetime.now().isoformat(timespec="seconds"),
        }
    )


def total_income(transactions: list[dict]) -> float:
    return sum(t["amount"] for t in transactions if t["kind"] == "income")


def total_expense(transactions: list[dict]) -> float:
    return sum(t["amount"] for t in transactions if t["kind"] == "expense")


def show_summary(transactions: list[dict]) -> None:
    """
    Print summary and category breakdown.
    """
    income = total_income(transactions)
    expense = total_expense(transactions)
    net = income - expense

    print("\n--- Summary ---")
    print(f"Income : ₹{income:.2f}")
    print(f"Expense: ₹{expense:.2f}")
    print(f"Net    : ₹{net:.2f}")

    by_cat: dict[str, float] = {}
    for t in transactions:
        if t["kind"] == "expense":
            by_cat[t["category"]] = by_cat.get(t["category"], 0.0) + t["amount"]

    if by_cat:
        print("\nExpenses by category:")
        for cat, amt in sorted(by_cat.items(), key=lambda x: x[1], reverse=True):
            print(f"  {cat:<10} ₹{amt:.2f}")


def prompt_amount() -> float:
    """
    Keep asking until the user enters a valid positive amount.
    """
    while True:
        try:
            return parse_amount(input("Amount: "))
        except ValueError:
            print("Invalid amount. Enter a positive number like 120 or ₹1,200.50.")


def main() -> None:
    transactions = load_transactions()

    while True:
        print("\nExpense Tracker")
        print("1) Add expense")
        print("2) Add income")
        print("3) Summary")
        print("4) Budget check")
        print("5) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            amt = prompt_amount()
            desc = input("Description: ").strip()
            add_transaction(transactions, "expense", amt, desc)
            save_transactions(transactions)
            print("Saved expense.")

        elif choice == "2":
            amt = prompt_amount()
            desc = input("Description: ").strip()
            add_transaction(transactions, "income", amt, desc)
            save_transactions(transactions)
            print("Saved income.")

        elif choice == "3":
            show_summary(transactions)

        elif choice == "4":
            budget = prompt_amount()
            spent = total_expense(transactions)
            status = budget_status(spent, budget)
            print(f"Spent ₹{spent:.2f} / Budget ₹{budget:.2f} => {status}")

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
