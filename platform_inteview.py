def sort(width:int = 0, height:int = 0, length:int = 0, mass:int = 0):
    """
    w*h*l >= 1M or max([w,h,l]) >= 150: is_bulky
    mass >= 20: is_heavy
    is_bulky/is_heavy: t/t | t/f | f/t | f/f
    ff: STANDARD; tt: REJECTED; t/f f/t: SPECIAL
    """
    break_running = False
    delivery = None
    if None in [width, height, length, mass]:
        print("no input can be None")
        break_running = True
    if not break_running and not all(isinstance(v, int) for v in [width, height, length, mass]):
        print("all input must be integer type")
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
