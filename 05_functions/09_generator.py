# def even_generator(limit):
#     li = []
#     for i in range(2, limit+1,2):
#         li.append(i)
#     return li

def even_generator(limit):
    for i in range(2, limit+1,2):
        # return i
        yield i  # we use yield keyword because it stores value in memory doesn't retruns the value only what return keyword used to do. 
    
for num in even_generator(10):
    print(num)




    