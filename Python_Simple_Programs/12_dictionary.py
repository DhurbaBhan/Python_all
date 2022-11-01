mydict={
    "name":"Dhurba",
    "age": 45,
    "address": "kirtipur",
    "another_dict": {"sub":"python","framework":"django",1:2}
}
print(mydict)
print(mydict.keys()) 
print(list(mydict.keys()) )
print(list(mydict.values()) )
print(mydict["another_dict"]["sub"])

di={
    "suvam":"python",
    "sonali":"c",
    "suvam":"java",
    "resham":"c++"
    }
print(di)