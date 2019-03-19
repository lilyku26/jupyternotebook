
# coding: utf-8

# In[14]:


#Learning Rate r=20
r=20
#Second part change learning rate , change to r=1


# In[15]:


import numpy as np
import matplotlib.pyplot as plt


# In[16]:


#ReLU = list
x1=-0.7; x2=0.2; x3=0.3; target=0.82
w1=-0.2; w2=0.1; w3=-0.9; b=0.4   #第一次的權重 + Bias
x=w1*x1+w2*x2+w3*x3+b
def relu(x):
    s = np.where(x < 0, 0, x)
    return s
y=relu(x)  #ReLU Function 
E=0.5*(target-y)**2   # Error
list = []

for i in range(100):
    w1=w1-r*(y-target)*y*(1-y)*x1
    w2=w2-r*(y-target)*y*(1-y)*x2
    w3=w3-r*(y-target)*y*(1-y)*x3
    b=b-r*(y-target)*y*(1-y)
    x=w1*x1+w2*x2+w3*x3+b
    y=relu(x)
    E=0.5*(target-y)**2 
    print("w1=",w1,"w2=",w2,"w3=",w3,"b=",b,"\nx=",x,",y=",y,",E=",E)
    list.append(E)
x =range(100)
plt.plot(x, list)  #    plt.plot(i,E)
plt.show()  #    plt.show()


# In[17]:


#Tanh = list1
x1=-0.7; x2=0.2; x3=0.3; target=0.82
w1=-0.2; w2=0.1; w3=-0.9; b=0.4   #第一次的權重 + Bias
x=w1*x1+w2*x2+w3*x3+b
y=np.tanh(x) #tanh Function 
E=0.5*(target-y)**2   # Error
list1 = []
for i in range(100):
    w1=w1-r*(y-target)*y*(1-y)*x1
    w2=w2-r*(y-target)*y*(1-y)*x2
    w3=w3-r*(y-target)*y*(1-y)*x3
    b=b-r*(y-target)*y*(1-y)
    x=w1*x1+w2*x2+w3*x3+b
    y=np.tanh(x)
    E=0.5*(target-y)**2 
    print("w1=",w1,"w2=",w2,"w3=",w3,"b=",b,"\nx=",x,",y=",y,",E=",E)
    list1.append(E)
x =range(100)
plt.plot(x, list1 )  #    plt.plot(i,E)
plt.show()  #    plt.show()


# In[18]:


#Linear X=Y   =list2
x1=-0.7; x2=0.2; x3=0.3; target=0.82
w1=-0.2; w2=0.1; w3=-0.9; b=0.4   #第一次的權重 + Bias
x=w1*x1+w2*x2+w3*x3+b
y=x  #Linear Function 
E=0.5*(target-y)**2   # Error
list2 = []
for i in range(100):
    w1=w1-r*(y-target)*y*(1-y)*x1
    w2=w2-r*(y-target)*y*(1-y)*x2
    w3=w3-r*(y-target)*y*(1-y)*x3
    b=b-r*(y-target)*y*(1-y)
    x=w1*x1+w2*x2+w3*x3+b
    y=x
    E=0.5*(target-y)**2 
    print("w1=",w1,"w2=",w2,"w3=",w3,"b=",b,"\nx=",x,",y=",y,",E=",E)
    list2.append(E)
x =range(100)
plt.plot(x, list2)  #    plt.plot(i,E)
plt.show()  #    plt.show()


# In[19]:


# Sigmoid function = list3
x1=-0.7; x2=0.2; x3=0.3; target=0.82
w1=-0.2; w2=0.1; w3=-0.9; b=0.4   #第一次的權重 + Bias
x=w1*x1+w2*x2+w3*x3+b
y=1/(1 + np.exp(-x))  #Sigmoid Function
E=0.5*(target-y)**2   # Error
print("w1=",w1,"w2=",w2,"w3=",w3,"b=",b,"\nx=",x,",y=",y,",E=",E)
list3 = []
for i in range(100):
    w1=w1-r*(y-target)*y*(1-y)*x1
    w2=w2-r*(y-target)*y*(1-y)*x2
    w3=w3-r*(y-target)*y*(1-y)*x3
    b=b-r*(y-target)*y*(1-y)
    x=w1*x1+w2*x2+w3*x3+b
    y=1/(1 + np.exp(-x))
    E=0.5*(target-y)**2
    print("w1=",w1,"w2=",w2,"w3=",w3,"b=",b,"\nx=",x,",y=",y,",E=",E)
    list3.append(E)
x =range(100)
plt.plot(x, list3)  #    plt.plot(i,E)
plt.show()  #    plt.show()


# In[20]:


#把圖片疊加
x=range(100)
plt.plot(x, list3, 'b-') #Sigmoid
plt.plot(x, list2, 'g-') #Linear
plt.plot(x, list1, 'r-') #Tanh
plt.plot(x, list, 'go')  #ReLU 

