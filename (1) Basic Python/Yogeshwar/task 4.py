state = ['Gujarat','Maharastha','Rajasthan','Uttar Pradesh']
Capital = ['Gandhinagar','Mumbai','Jaipur','Lucknow']
d ={}
for key in state:
    for value in Capital:
        d[key]=value
        Capital.remove(value)
        break
print(d)