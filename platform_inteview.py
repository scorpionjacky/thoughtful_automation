def sort(width = 0, height = 0, length = 0, mass = 0):
    """
    w*h*l >= 1M or max([w,h,l]) >= 150: is_bulky
    mass >= 20: is_heavy
    is_bulky/is_heavy: t/t | t/f | f/t | f/f
    ff: STANDARD; tt: REJECT; t/f f/t: SPECIAL
    """
    break_running = False
    delivery = None
    if None in [width, height, length, mass]:
        print("no input can be None")
        break_running = True
    if not break_running and min([width, height, length, mass]) <= 0:
        print("all input must be larger than 0")
        break_running = True
    if not break_running:
        is_bulky = is_heavy = False
        volume = width * height * length
        max_dim = max([width, height, length])
        if volume >= 1000000 or max_dim >= 150:
            is_bulky = True
        if mass >= 20:
            is_heavy = True
        # is_bulky/is_heavy: t/t | t/f | f/t | f/f
        if not is_bulky and not is_heavy:
            delivery = "STANDARD"
        elif is_bulky and is_heavy:
            delivery = "REJECTED"
        else:
            delivery = "SPECIAL"
    return delivery
