#!/usr/bin/env python3
from random import randint
def main():
  outfile = open("RunCollatz.in","w")
  s = " "
  for l in range (1000):
    i = randint(1,200)
    j = randint(1,100)
    s = str(i) + " " + str(j) + "\n"  
    outfile.write(s)
  outfile.close()
main()

