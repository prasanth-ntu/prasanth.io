---
tags:
  - Python
  - Programming
  - Coding
  - Library
title: Regex (re)
---
# Online Platforms

To try out, visit 
- https://regex101.com/ 
- https://regexr.com/

# Example

## [[email#Load email data from sklearn and extract relevant information from it using `email` and `re`.]]
![[regex-email-example.png]]

- REGULAR EXPRESSION
```
[\w\.-]+@[\w\.-]+
```
- TEST STRING
```
Subject: Re: Recommendation on Duc

I have a line on a Ducati 900GTS 1978 model with 17k on the clock.  Runs
very well, paint is the bronze/brown/orange faded out, leaks a bit of oil
and pops out of 1st with hard accel.  The shop will fix trans and oil 
leak.  They sold the bike to the 1 and only owner.  They want $3495, and
I am thinking more like $3K.  Any opinions out there?  Please email me.
Thanks.  It would be a nice stable mate to the Beemer.  Then I'll get
a jap bike and call myself Axis Motors!

-- 
-----------------------------------------------------------------------
"Tuba" (Irwin)      "I honk therefore I am"     CompuTrac-Richardson,Tx
irwin@cmptrc.lonestar.org    DoD #0826          (R75/6)
-----------------------------------------------------------------------
```

## Date validation

Regex to validate 8 digit number (e.g., DDMMYYYY)

- REGULAR EXPRESSION
```
^\d{8}$
```
- TEST STRING
```
12345678
```