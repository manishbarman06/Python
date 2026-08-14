"""
For Loop
-> A for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or a range of numbes.
-> It executes a block of code a fixed number of times based on the length of the collection.
"""
print("\n-------- For Loop --------")
# for loop 
for i in range(5): # 0 to 4
    print("Hello!")

'''
Tracking Indexes with enumerate():
-> If you need both the index and the item value,
   wrap your collection in the enumerate() function.
'''
print("\n-------- enumerate() --------")
fruits = ["Apple", "Banana", "Mango"]
for index, value in enumerate(fruits):
    print(f"{index+1}. {value}")
    
'''
While Loop:
-> A while loop repeatedly executes a traget statement as long as a given condition remains true.
'''
print("\n-------- While Loop --------")
count = 1
while count <= 5:
    print(f"Count {count}")
    count += 1