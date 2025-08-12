## Test Cases:

```python
# None value
print(sort(149,149,149, None))

# 0 or negative values
print(sort(149,149,149, 0))
print(sort(149,149,-1, 10))

# standard
print(sort(149,149,10, 15))

# special
# 1 dim beyond 150
print(sort(150,149,10, 15))
# mass >= 20
print(sort(49,49,49, 150))
# volumn >= 1M
print(sort(100,100,100, 10))

# reject
# both (all 3)
print(sort(100,100,150, 40))
```

## Output

```
no input can be None
None

all input must be larger than 0
None

all input must be larger than 0
None

STANDARD

SPECIAL

SPECIAL

SPECIAL

REJECTED
```
