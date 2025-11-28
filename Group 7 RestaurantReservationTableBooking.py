# Sample tables (table number and capacity)
tables = [
    {"id": 1, "capacity": 2},
    {"id": 2, "capacity": 4},
    {"id": 3, "capacity": 6}
]

# List to store reservations
reservations = []

def show_tables():
    print("\n=== AVAILABLE TABLES ===")
    for t in tables:
        print(f"Table {t['id']} - Capacity: {t['capacity']}")

def show_reservations():
    print("\n=== CURRENT RESERVATIONS ===")
    if not reservations:
        print("No reservations yet.")
    else:
        for r in reservations:
            print(f"[ID {r['id']}] {r['name']} - {r['party_size']} people "
                  f"| Table {r['table']} | {r['time']}")

def make_reservation():
    name = input("Enter customer name: ")
    party = int(input("Enter number of people: "))
    time = input("Enter reservation time (HH:MM): ")

    # Find available table with enough capacity
    table = None
    for t in tables:
        if t["capacity"] >= party:
            table = t["id"]
            break

    if not table:
        print("❌ Sorry, no table available for that size.")
        return

    # Create reservation
    rid = len(reservations) + 1
    reservations.append({
        "id": rid,
        "name": name,
        "party_size": party,
        "table": table,
        "time": time
    })
    print(f"✅ Reservation successful! Table {table} booked for {name} at {time}.")

def search_reservation():
    keyword = input("Enter name to search: ").lower()
    found = [r for r in reservations if keyword in r["name"].lower()]
    if not found:
        print("No reservations found.")
    else:
        print("\n=== SEARCH RESULTS ===")
        for r in found:
            print(f"[ID {r['id']}] {r['name']} - Table {r['table']} at {r['time']}")

def cancel_reservation():
    rid = int(input("Enter reservation ID to cancel: "))
    for r in reservations:
        if r["id"] == rid:
            reservations.remove(r)
            print("❌ Reservation cancelled successfully.")
            return
    print("Reservation ID not found.")

def main():
    while True:
        print("\n===== RESTAURANT BOOKING MENU =====")
        print("1. Show Tables")
        print("2. Make Reservation")
        print("3. View All Reservations")
        print("4. Search Reservation")
        print("5. Cancel Reservation")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            show_tables()
        elif choice == "2":
            make_reservation()
        elif choice == "3":
            show_reservations()
        elif choice == "4":
            search_reservation()
        elif choice == "5":
            cancel_reservation()
        elif choice == "6":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main ()