
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
i    """
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
   for t in range (1,999999):
      cache[t] = collatz_cycleLen(t)  
   maxLR =
  i
   return maxL


def collatz_cycleLen(p):
  length = 1
  pop = p
  global cache
 
  while (p > 1):
    if (p % 2 == 0):
        length += 1
        p = p // 2
        
    else:
        p = p + (p >> 1) + 1
        length += 2
        
  cache[pop] = length  
  return cache[pop]
#-----------
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
