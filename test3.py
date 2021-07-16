import os
import pickle
f = open("filePaths.pkl","rb")
a  = pickle.load(f)
f.close()
a = {
    "a":"meherab",
    "name":"meherab",
    "age":17
}

# path = list(a.keys())
# print(path[1])

print(a["a"])

# os.startfile(path)


# a = [[4.528321,"d"],[1.1548745,"b"],[3.1544218,"c"],[4.18124,"a"]]
# # a = ["4","1","3","4"]
# a.sort()
# print(a)