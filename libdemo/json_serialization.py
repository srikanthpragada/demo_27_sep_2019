import json


class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"


t = Time(1, 2, 3)
print(t)

json_object = json.dumps(t.__dict__)
print(json_object)
d = json.loads(json_object)
print(d, type(d))
