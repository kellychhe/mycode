#!/usr/bin/env python3

proto = ["ssh", "http", "https"]

proto.pop(0)
print(proto)

proto.extend(["ssh", "dns", "ssh"])
print(proto)

print(proto.count("ssh"))

proto.sort()
print(proto)

proto.reverse()
print(proto)
