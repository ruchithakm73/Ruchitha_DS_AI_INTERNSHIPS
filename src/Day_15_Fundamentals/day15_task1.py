sample_space=[("Click","Click"),("Click","Scroll"),("Click","Exit"),("Scroll","Click"),("Scroll","Scroll"),("Scroll","Exit"),("Exit","Click"),("Exit","Scroll"),("Exit","Exit")]
print("Sample Space:")
print(sample_space)
print("Total Outcomes:", len(sample_space))
event_click=[]
for items in sample_space:
    if "Click" in items:
        event_click.append(items)      
click_probability = len(event_click) / len(sample_space)
print("\nOutcomes with at least one Click:")
print(event_click)
print("\nProbability (at least one Click):",click_probability)

#Dice Rolling
import random
trials=1000
sum7_count=0
for item in range(trials):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    if dice1+dice2 == 7:
        sum7_count+=1
    probability=sum7_count/trials
print("\n\nDice Rolling Experiment:\nTotal Trials:", trials)
print("Number of times sum = 7:", sum7_count)
print("Probability of sum = 7:", probability)