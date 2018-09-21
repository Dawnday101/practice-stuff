def rect(phrase="Thank You Justin!", width=5, height=5):
    let_order = phrase + ''.join(phrase[-2:0:-1])
    for y in range(0, (len(phrase) - 1) * height + 1):
        for x in range(0, (len(phrase) - 1) * width + 1):
            if x % (len(phrase) - 1) == 0 or y % (len(phrase) - 1) == 0:
                print(let_order[(x + y) % len(let_order)], end="")
            else:
                print(' ', end="")
        print()
    
rect("Thank You Justin!", 6, 3)
