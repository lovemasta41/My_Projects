def xswitch(x):
    return xswitch._system_dict.get(x,None)

xswitch._system_dict = {"files":1,"folders":2,"devices":3}

print(xswitch('files'))