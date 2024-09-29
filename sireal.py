import pickle

data={}
for x in range (25):
    data[f"{x}"]=x*2

print(data)

bytes=pickle.dumps(data)
print(bytes)
bytes1=pickle.loads(bytes)
print(bytes1)
