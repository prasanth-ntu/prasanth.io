#@ TEst

# Example
## Load email data from sklearn and extract relevant information from it using `email` and `re`.
```python
from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset="train")
data = newsgroups_train["data"]
sample_data = data[10]
print(sample_data)
```

```output
From: irwin@cmptrc.lonestar.org (Irwin Arnstein)
Subject: Re: Recommendation on Duc
Summary: What's it worth?
Distribution: usa
Expires: Sat, 1 May 1993 05:00:00 GMT
Organization: CompuTrac Inc., Richardson TX
Keywords: Ducati, GTS, How much? 
Lines: 13

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

```python
import email
# Parse a string into a Message object model.
msg = email.message_from_string(sample_data)
print(f'datatype of msg: {type(msg)}')
print(f'From: {msg["From"]}')
print(f'Subject: {msg["Subject"]}')
print(f'Distribution: {msg["Distribution"]}')
print(f'Lines: {msg["Lines"]}')
print(f'Payload: {msg.get_payload()}')
```

```output
datatype of msg: <class 'email.message.Message'>

From: irwin@cmptrc.lonestar.org (Irwin Arnstein)
Subject: Re: Recommendation on Duc
Distribution: usa
Lines: 13
Payload: I have a line on a Ducati 900GTS 1978 model with 17k on the clock.  Runs
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

**Extracting only the subject and body**, and stripping any email address using [[re]].
```python
text = f"{msg['Subject']}\n\n{msg.get_payload()}"

import re
# Strip any remaining email addresses
text = re.sub(r"[\w\.-]+@[\w\.-]+", "", text)
print (text)
```

```output
Re: Recommendation on Duc

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
    DoD #0826          (R75/6)
-----------------------------------------------------------------------
```
For interactive regex playground example, check out [[re#Example]]