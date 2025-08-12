## Test Cases:

```python
# None input

assert sort(149,149,149, None) is None

# 0 or negative value input

assert sort(149,149,149, 0) is None

assert sort(149,149,-1, 15) is None

# standard
assert sort(149,149,10, 15) == "STANDARD"

# special

# 1 dim beyond 150
assert sort(150,149,10, 15) == "SPECIAL"

# mass >= 20
assert sort(49,49,49, 20) == "SPECIAL"
assert sort(49,49,49, 120) == "SPECIAL"

# volumn >= 1M
assert sort(100,100,100, 10) == "SPECIAL"

# rejected

# both
assert sort(100,100,150, 40) == "REJECTED"

```

## Output

```
no input can be None
all input must be larger than 0
all input must be larger than 0
```
