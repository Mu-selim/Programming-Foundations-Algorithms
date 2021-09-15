def countdown_with_step(start, step):
    if start == 0:
        print(0)
        return
    elif start < 0:
        print()
        return
    else:
        print(start, " ", end="")
        return countdown_with_step(start-step, step)

countdown_with_step(100, 5)
countdown_with_step(100, 7)