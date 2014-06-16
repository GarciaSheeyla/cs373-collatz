#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------
def collatz_eval (i, j) :
   """
   i is the beginning of the range, inclusive
   j is the end       of the range, inclusive
   return the max cycle length in the range [i, j]
   """
   # <your code>
   assert i > 0
   assert j > 0
   if i > j:
      i,j = j,i

   m = j // 2
   if i < m:
    i = m
   global cache

   cache = [0 for x in range(1000000)]

   maxLR = 0
   for currentNum in range(i,(j+1)):

     maxL =  cache[currentNum]
     if maxL != 0:
       
       if maxLR < maxL:    
         maxLR = maxL
     else:
       cycleLenCurrent = collatz_cycleLen(currentNum)
       if maxLR < cycleLenCurrent:
         maxLR = cycleLenCurrent
   
   return maxLR
def collatz_inCache(t):
    if t < 999999:
        if cache[t] != 0:
          return True
        else:
          return False

def collatz_cycleLen(p):
  if p > 999999:
      return 0
  length = 0
  pop = p
  global cache
  if (p == 1):
      cache[pop] = 1
  while (p > 1):
    if (p % 2 == 0):
        length += 1
        p = p // 2
        if collatz_inCache(p) and p <= 999999:
            cache[pop] = cache[p] + length 
            break
        collatz_cycleLen(p)
        
    else:
        p = p + (p >> 1) + 1
        length += 2
        if collatz_inCache(p) and p <= 999999:
            cache[pop] = cache[p] + length 
            break
        collatz_cycleLen(p)
  return cache[pop]
# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
"""
To run the program
    % coverage3 run --branch RunCollatz.py < RunCollatz.in

To obtain coverage of the run:
    % coverage3 report -m

"""

# ----
# main
# ----
import sys
collatz_solve(sys.stdin, sys.stdout)

"""
% coverage3 run --branch RunCollatz.py < RunCollatz.in > RunCollatz.out



% coverage3 report -m
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz         18      0      6      0   100%
RunCollatz       5      0      0      0   100%
---------------------------------------------------------
TOTAL           23      0      6      0   100%
"""
