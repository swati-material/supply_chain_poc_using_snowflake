from faker import Faker
import random
from datetime import datetime, timedelta
import csv

fake = Faker()

# Function to generate synthetic shopping data
def generate_shopping_data(num_records):
    data = []
    for _ in range(num_records):
        user = fake.user_name()
        user_id = fake.random_number(digits=6)
        session = fake.random_int(min=1, max=100)
        user_session = fake.uuid4()
        event_type = 'cart'
        product = fake.word()
        product_id = fake.random_number(digits=6)
        brand = fake.company()
        category = fake.word()
        category_code = fake.random_number(digits=4)
        price = round(random.uniform(10, 5000), 2)  # Random price between $10 and $5000
        event_time = fake.date_time_between(start_date='-1y', end_date='now').isoformat()

        data.append({
            'User': user,
            'user_id': user_id,
            'session': session,
            'user_session': user_session,
            'event_type': event_type,
            'product': product,
            'product_id': product_id,
            'brand': brand,
            'category': category,
            'category_code': category_code,
            'price': price,
            'event_time': event_time
        })

    return data

# Function to write data to CSV file
def write_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for record in data:
            writer.writerow(record)

# Main function to generate and save synthetic data
def main():
    num_records = 1000
    shopping_data = generate_shopping_data(num_records)
    
    # Write data to CSV file
    filename = 'shopping_data.csv'
    write_to_csv(shopping_data, filename)
    print(f"Generated {num_records} shopping records. Data saved to {filename}")

if __name__ == "__main__":
    main()
