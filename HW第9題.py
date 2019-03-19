
# coding: utf-8

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
x1=-0.7; x2=0.2; x3=0.3; target=0.82
w1=-0.2; w2=0.1; w3=-0.9; b=0.4   #第一次的權重 + Bias
x=w1*x1+w2*x2+w3*x3+b
y=1/(1 + np.exp(-x)) #Sigmoid Function 
E=0.5*(target-y)**2   # Error


# In[12]:


list = []
r = 20 #learning rate
for i in range(100):
    w1=w1-r*(y-target)*y*(1-y)*x1
    w2=w2-r*(y-target)*y*(1-y)*x2
    w3=w3-r*(y-target)*y*(1-y)*x3
    b=b-r*(y-target)*y*(1-y)
    x=w1*x1+w2*x2+w3*x3+b
    y=1/(1 + np.exp(-x))
    E=0.5*(target-y)**2 
    print("w1=",w1,"w2=",w2,"w3=",w3,"b=",b,"\nx=",x,",y=",y,",E=",E)
    list.append(E)
x =range(100)
plt.plot(x, list)#    plt.plot(i,E)
plt.show()#    plt.show()


# In[13]:


#Change Learning Rate to 1


# In[14]:


x1=-0.7; x2=0.2; x3=0.3; target=0.82
w1=-0.2; w2=0.1; w3=-0.9; b=0.4   #第一次的權重 + Bias
x=w1*x1+w2*x2+w3*x3+b
y=1/(1 + np.exp(-x)) #Sigmoid Function 
E=0.5*(target-y)**2   # Error
list1 = []
r = 1 #learning rate
for i in range(100):
    w1=w1-r*(y-target)*y*(1-y)*x1
    w2=w2-r*(y-target)*y*(1-y)*x2
    w3=w3-r*(y-target)*y*(1-y)*x3
    b=b-r*(y-target)*y*(1-y)
    x=w1*x1+w2*x2+w3*x3+b
    y=1/(1 + np.exp(-x))
    E=0.5*(target-y)**2 
    print("w1=",w1,"w2=",w2,"w3=",w3,"b=",b,"\nx=",x,",y=",y,",E=",E)
    list1.append(E)
x =range(100)
plt.plot(x, list1)#    plt.plot(i,E)
plt.show()#    plt.show()


# In[15]:


#將兩個圖疊在一起


# In[17]:


x =range(100)
plt.plot(x, list)#    plt.plot(i,E)
plt.plot(x, list1)
plt.show()#    plt.show()

