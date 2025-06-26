print("\033c")
import random as rd

class Neuron():
  def __init__(self,num):
    self.weights = [0]*81
    self.num = num
    self.range1 = range(rd.randint(1,10),rd.randint(1,10))
    self.range2 = range(rd.randint(1,10),rd.randint(1,10))
    
    
    
  def in_range(self,value):
    if (value[0] in self.range1 and value[1] in self.range2):
      return True
    return False
    
    
  def light(self,value):
    self.weights[self.num.index(value)] += 1
  
class NN():
  def __init__(self,amount,num):
    self.amount = amount
    self.neurons = []
    for i in range(self.amount):
      self.neurons.append(Neuron(num))
          
  def learning(self,data,epochs):
    for epoch in range(epochs):
      data = []
      for i in range(81):
        x = rd.randint(1,9)
        y = rd.randint(1,9)
        data.append([x,y,x*y])
      print(epoch)
      for value in data:
        for neuron in self.neurons:
          if neuron.in_range(value):
            neuron.light(value[2])
            
  def check(self,values):
    ans = [0]*81
    for neuron in self.neurons:
      if neuron.in_range(values):
        dep = (len(neuron.range1)*len(neuron.range2))
        for i in range(len(neuron.weights)):
          if neuron.weights[i] > 0:
            ans[i] += neuron.weights[i]/(dep*dep)
    
    
    return ans.index(max(ans))+1
        
data = []
num = list(range(1,82))

Bob = NN(400000,num)
Bob.learning(data,20)
while True:
  
  x,y = list(map(int,input("введи два множителя через пробел:\n").split()))
  print(f"{x}*{y}={Bob.check([x,y])}")
