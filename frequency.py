test_dict={
    "codingal": 2,
    "is":2,
    "the":4,
    "best":5
    
}

print("the dictonary is " , str(test_dict))

k = 2 
res= 0 

for key in test_dict:
    if test_dict[key]==k:
        res = res + 1

print(res)