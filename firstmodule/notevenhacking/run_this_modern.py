#!/usr/bin/exec-suid -- /usr/bin/python3 -I

# this is the legacy way...


print("script running")

ff = open("/flag", "r")

print("flag file opened")

flag = ff.read()

print("flag read")

ff.close()

print(flag)

