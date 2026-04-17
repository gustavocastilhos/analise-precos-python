#preço das maças ao longo do tempo

import matplotlib.pyplot as plt
import numpy as np

dado = np.loadtxt('apples_ts.csv',delimiter=',',usecols=np.arange(1,88,1))

np.arange(1,88,1)

dadoTransporto =  dado.T
datas = dadoTransporto [:,0]
precos = dadoTransporto[:,1:6]

#print(dadoTransporto)
datas= np.arange(1,88,1)

Moscow = precos[:,0]
Kaliningrad=precos[:,1]
Petersburg=precos[:,2]
Krasnodar=precos[:,3]
Ekaterinburg=precos[:,4]

#plt.plot(datas,precos[:,0])
#plt.show()
#print(Moscow.shape)
#print(Moscow[0:12])
MoscowAno1 = Moscow[0:12]
MoscowAno2 = Moscow[13:25]
MoscowAno3 = Moscow[25:37]
MoscowAno4 = Moscow[37:49]
#print(np.mean([Kaliningrad[3],Kaliningrad[5]])) #media
Kaliningrad[4] = np.mean([Kaliningrad[3],Kaliningrad[5]]) #arrumando erro no grafico

plt.plot(np.arange(1,13,1),MoscowAno1)
plt.plot(np.arange(1,13,1),MoscowAno2)
plt.plot(np.arange(1,13,1),MoscowAno3)
plt.plot(np.arange(1,13,1),MoscowAno4)

plt.legend(['ano1','ano2','ano3','ano4'])
plt.show()

plt.plot(datas,Kaliningrad)
plt.show()

x=datas
y= 0.45*x+80
#print(np.sqrt(np.sum(np.power(Moscow-y,2))))
print(np.linalg.norm(Moscow-y))

Y= Moscow
X= datas
n= np.size(Moscow)
#print((x**2).shape)

a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y)) / (n*np.sum(X**2)-np.sum(X)**2)
b = np.mean(Y) - a*np.mean(X)
y = a*X+b
print(np.linalg.norm(Moscow-y))

plt.plot(datas,Moscow)
plt.plot(x,y)
plt.plot(41.5,41.5*a+b,'*r')
plt.show()


