# create a list
cast = ["Cleese", 'Palin', 'Jones', "Idle"]
print(cast)
print(len(cast))
print(cast[1])

# 'append()': add single data to the end of list
cast.append("haha")

# 'pop()': remove data from the end of list
cast.pop()

# 'extend()': add collection of data items to the end of list
cast.extend(['Alice', "Mike"])  

# 'remove()': remove a specific data item from list
cast.remove("Jones")

# 'insert()': add a data item before a specific slot location
cast.insert(0, "hahaha")

## exercise 1.1
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
# add 'year' into the list
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.append(1983)

# 'for' loop
for item in cast:
    print(item)

# apply 'for' loop to a list that contains another list
movies = ["The Holy Grail",
          1975,
          "Terry Jones & Terry Gilliam",
          91,
          ["Graham Chapman",
           ["Michael Palin",
            "John Cleese",
            "Terry Gilliam",
            "Eric Idle",
            "Terry Jones"]]]

print(movies)

for item in movies:
    print(item)

# 'isinstance()': check if a specific identifier holds data of a specific type
names = ['Michael', 'Terry']
isinstance(names, list) 

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)

# function
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item) 
            