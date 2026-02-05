purchases = {
    "Apple": 50,
    "Banana": 30,
    "Milk": 60
}

for name, amount in purchases.items():
    print(f"{name}: spent ₹{amount}")
    
    print(f"Total items purchased: {len(purchases)}")
    print("Fruit Names:",list(purchases.keys()))
    
    n=int(input("Enter the number of fruits: "))
    user_purchases={}
    
    for i in range(n):
        fruit=input("Enter fruit name: ")
        cost=int(input("Enter cost {name}: "))
        user_purchases[fruit]=cost
        
    print("User Purchases:",user_purchases)
    
    fruits=max(user_purchases,key=user_purchases.get)
    fruits=min(user_purchases,key=user_purchases.get)
    print(f"Fruit with highest cost: {fruits} costing ₹{user_purchases[fruits]}")