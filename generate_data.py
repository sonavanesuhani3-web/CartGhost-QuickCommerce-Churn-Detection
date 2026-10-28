import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

num_orders = 13000
num_users = 2500

# Fix: numeric_number aivaji fake.random_number vaparla ahe
user_ids = [f"USR_{fake.random_number(digits=6, fix_len=True)}" for _ in range(num_users)]

data = []
end_date = datetime.now()
start_date = end_date - timedelta(days=180)

for i in range(1, num_orders + 1):
    u_id = random.choice(user_ids)
    o_date = fake.date_time_between(start_date=start_date, end_date=end_date)
    delivery_mins = random.choices([12, 18, 25, 40, 55], weights=[0.4, 0.3, 0.15, 0.1, 0.05])[0]
    amount = round(random.uniform(99.0, 1800.0), 2)
    items = random.randint(1, 8)
    rating = random.choices([5, 4, 3, 2, 1, None], weights=[0.5, 0.25, 0.1, 0.05, 0.05, 0.05])[0]
    
    data.append({
        'order_id': f"ORD_{i:06d}",
        'user_id': u_id,
        'order_timestamp': o_date.strftime('%Y-%m-%d %H:%M:%S'),
        'delivery_time_mins': delivery_mins,
        'order_amount': amount,
        'item_count': items,
        'rating': rating
    })

df = pd.DataFrame(data)
df.to_csv('cartghost_orders.csv', index=False)
print("CartGhost synthetic dataset successfully created: cartghost_orders.csv")