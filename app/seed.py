from db import connect_db
def seed_database():
    """Create a collection and insert seed data."""
    db = connect_db()
    try:
        collection = db["file"]
        collection.insert_many([
            {"name": "John Doe", "age": 28},
            {"name": "Jane Smith", "age": 34},
        ])
        print("Seed data inserted successfully.")
    except Exception as e:
        print(f"Error seeding database: {e}")
if __name__ == "__main__":
    seed_database()