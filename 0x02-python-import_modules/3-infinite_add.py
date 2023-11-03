#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argc = len(sys.argv) - 1
sum = 0
if argc == 0:
    print("{}".format(sum))
elif argc == 1:
    print("{}".format(sys.argv[1]))
else:
  for i in range(0, argc):
    sum += int(sys.argv[i+1]))
   print("{}".format(sum))
