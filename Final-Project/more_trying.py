def check_int(number, maximum):
    try:
        if 0 < int(number) <= maximum:
            return int(number)
        else:
            return 404
    except ValueError:
        return 404