#The function sense, takes p and Z as inputs, 
#and outputs the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.

#Probability of cells
p=[0.2, 0.2, 0.2, 0.2, 0.2]

World color definition
world=['green', 'red', 'red', 'green', 'green']

Z = 'red'
pHit = 0.6
pMiss = 0.2

#create empty list with n elements as p 
q=[0]*len(p)

#sense function
def sense(p, Z):
    #
    for i in range(len(p)):
        if world[i] == Z:
            q[i] = p[i]*pHit
        else:
            q[i] = p[i]*pMiss
    #
    return q

print sense(p,Z)
