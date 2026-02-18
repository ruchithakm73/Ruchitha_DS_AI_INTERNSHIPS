#Coin Task
prob_head=1/2
prob_six=1/6
prob_head_six_independent=prob_head*prob_six
print(f"Probability of flipping Heads on a coin :{prob_head}\nProbability of rolling a 6 on a die :{prob_six}")
print("Probability of A ^ B :",prob_head_six_independent)

#Marbal Task
total_marbles=10
red=5
blue=5

prob_1st_red=red/total_marbles

red-=1
total_marbles-=1

prob_2nd_red=red/total_marbles
prob_red_red_dependent=prob_1st_red*prob_2nd_red

print(f"Probability of 1st marble being Red:{prob_1st_red}\nProbability of 2nd marble being Red:{prob_2nd_red}")
print("Probability of both marbles being Red (P(A ^ B)) :",prob_red_red_dependent)