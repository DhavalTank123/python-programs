d = {
    "A": "abcd",
    1: 123,
    "rool_no ": 46
}
print(d)
print(type(d))
d["A"] = "dhaval"
del d["A"]
print(d)

d2={
    "A":"abcd",
    1:123,
    "dhaval":
        {
            "rool_no ": 46,
            "sname": "tank"
        }
}
print(d2["dhaval"]["sname"])
d3 = d2   # pointer object
del d3["A"]
print(d2)
d3 = d2.copy()   # not del in d2 only for d3
del d3[1]
print(d2)
d2.update({1:"abcd"})
print(d2.keys())
print(d2.items())
print(d2.values())

