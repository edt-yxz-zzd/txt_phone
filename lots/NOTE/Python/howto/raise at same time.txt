
try:
    raise ValueError(1)
except Exception:
    raise ValueError(2)

'''
Traceback (most recent call last):
  File "try_raise_both.py", line 3, in <module>
    raise ValueError(1)
ValueError: 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "try_raise_both.py", line 5, in <module>
    raise ValueError(2)
ValueError: 2
'''

