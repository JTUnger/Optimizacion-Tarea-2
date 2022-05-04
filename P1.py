from gurobipy import *
import random

random.seed(10)

K = 30
n = 12
M = 5
D = 8
S = 2900

#rangos
N_ = range(1, n + 1)
K_ = range(1, K + 1)
M_ = range(1, M + 1)
D_ = range(1, D + 1)
J_ = range(1, M + 1)

#Conjuntos
G = {(i): random.randint(15000, 40000) for i in N_}
C = {(i, k): random.randint(5000, 10000) for i in N_ for k in K_}
d = {(i, k): random.randint(0, 7) for i in N_ for k in K_}
t = {(i,j): random.randint(9,12) for i in N_ for j in M_}
exp = {(i): random.randint(6,12) for i in N_}
# el 20% de los productos perteneceran a al subconjunto de productos P, que poseen demanda fija en tienda
P = random.choices(N_, k=int(n*0.2))
Q = {(p): random.randint(3,8) for p in P}
N_sin_P = []
for i in N_:
    if i not in P:
        N_sin_P.append(i)





#### ESCRIBA SU MODELO AQUI ####
m = Model()

#Variables
x = m.addVars(N_,M_,D_,K_, vtype = GRB.BINARY)
f = m.addVars(N_,K_,exp)
z = m.addVars(N_,K_,exp)


#Función Objetivo


#R1
m.addConstrs(sum(x[i,j,h,k] for i in N_) <= 1 for j in J_ for h in D_ for k in K_)

#R2


#R3


#R4
m.addConstrs(z[i,k,e] == z[i,k-1,e+1] - f[i,k,e] for i in N_sin_P for e in range(1,exp[i]) for k in range(2,K+1))

#R5


#R6


#R7


#R8


#R9


#R10



#Imprimir Valor Objetivo

#################################
