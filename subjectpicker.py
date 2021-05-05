def main():
    import random
    random_num = random.randint(1, 3)
    if random_num == 1:
        answer = "Influenza"
    elif random_num == 2:
        answer = "Epilepsy"
    else:
        answer = "Chicken Pox"
    print("What topic? {}".format(answer))


main()
