#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % coverage3 run --branch TestCollatz.py

To obtain coverage of the test:
    % coverage3 report -m
"""

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
    ##Own Test cases
    def test_read_2 (self) :
        r = StringIO("300 400 \n")
        i,j = collatz_read(r)
        self.assertEqual(i,300)
        self.assertEqual(j,400)
    def test_read_3 (self) :
        r    = StringIO("")
        i = collatz_read(r)
        self.assertEqual(i, [])
   
    def test_read_4 (self) :
        r = StringIO("40 30 \n")
        i,j = collatz_read(r)
        self.assertEqual(j,30)
        self.assertEqual(i,40)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)
    ###Own test cases
    def test_eval_5 (self) :
        v = collatz_eval(1,1)
        self.assertEqual(v,1)
    def test_eval_6 (self) :
        v = collatz_eval(9,9)
        self.assertEqual(v,20)
    def test_eval_7 (self) :
        v = collatz_eval(5,1)
        self.assertEqual(v,8)
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    def test_print_2 (self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")
    def test_print_3 (self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")
    def test_print_4 (self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")


    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    def test_solve_2 (self) :
        r = StringIO("1 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    def test_solve_3 (self):
        r = StringIO("1 5\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 5 8\n")
    def test_solve_4 (self):
        r = StringIO("1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n")


# ----
# main
# ----

main()

"""
% coverage3 run --branch TestCollatz.py
FFFF..F
======================================================================
FAIL: test_eval_1 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 47, in test_eval_1
    self.assertEqual(v, 20)
AssertionError: 1 != 20

======================================================================
FAIL: test_eval_2 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 51, in test_eval_2
    self.assertEqual(v, 125)
AssertionError: 1 != 125

======================================================================
FAIL: test_eval_3 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 55, in test_eval_3
    self.assertEqual(v, 89)
AssertionError: 1 != 89

======================================================================
FAIL: test_eval_4 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 59, in test_eval_4
    self.assertEqual(v, 174)
AssertionError: 1 != 174

======================================================================
FAIL: test_solve (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 78, in test_solve
    self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
AssertionError: '1 10 1\n100 200 1\n201 210 1\n900 1000 1\n' != '1 10 20\n100 200 125\n201 210 89\n900 1000 174\n'
- 1 10 1
?      ^
+ 1 10 20
?      ^^
- 100 200 1
+ 100 200 125
?          ++
- 201 210 1
?         ^
+ 201 210 89
?         ^^
- 900 1000 1
+ 900 1000 174
?           ++


----------------------------------------------------------------------
Ran 7 tests in 0.004s

FAILED (failures=5)



% coverage3 report -m
Name           Stmts   Miss Branch BrMiss  Cover   Missing
----------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      0      0    97%   86
----------------------------------------------------------
TOTAL            51      1      6      0    98%
"""
