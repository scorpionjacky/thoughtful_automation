### Objective

Imagine you work in Thoughtful’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

### Rules

Sort the packages using the following criteria:
- A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is heavy when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:
- STANDARD: standard packages (those that are not bulky or heavy) can be handled normally.
- SPECIAL: packages that are either heavy or bulky can't be handled automatically.
- REJECTED: packages that are REJECTED both heavy and bulky are rejected.

### Implementation

Implement the function `sort(width, height, length, mass)` (units are centimeters for the dimensions and kilogram for the mass). This function must return a string: the name of the stack where the package should go.

### Test Cases:

```python
# None input

assert sort(149,149,149, None) is None

# parameters must all be integers

assert sort(100,100,150, '') is None

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
all input must be integer type
all input must be larger than 0
all input must be larger than 0
```
