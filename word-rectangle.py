def rect(word="SHITPOST", width=5, height=5):
    let_order = word + ''.join(word[-2:0:-1])
    for y in range(0, (len(word) - 1) * height + 1):
        for x in range(0, (len(word) - 1) * width + 1):
            if x % (len(word) - 1) == 0 or y % (len(word) - 1) == 0:
                print(let_order[(x + y) % len(let_order)], end="")
            else:
                print(' ', end="")
        print()
    
rect("SHITPOST", 6, 3)