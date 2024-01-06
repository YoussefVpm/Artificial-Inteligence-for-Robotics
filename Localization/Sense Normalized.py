#The function sense, takes p and Z as inputs, 
#and outputs the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world. Later again normalizes the output
#thus the sum of q should be one.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    NormFactor=sum(q)
    for i in range(len(p)):
        q[i]=q[i]/NormFactor
    return q
print sense(p,Z)
