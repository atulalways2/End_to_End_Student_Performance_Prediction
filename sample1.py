# def total(*args):
#     return sum(args)

# print(total(2,2))


import time
def timer_dec(base_fn):
    def enhanced_fn():
        start_time = time.time()
        base_fn()
        end_time = time.time()
        print(f"Task time took to execute: {end_time - start_time}")
    return enhanced_fn

@timer_dec
def brew_tea():
    print("Brewing Tea..")
    time.sleep(2)
    print("Tea prepared!")


# using the function:
brew_tea()