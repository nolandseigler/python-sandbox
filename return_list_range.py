def every_three_nums(start):
    if start > 100:
        return []
    return list(range(start, 101, 3))