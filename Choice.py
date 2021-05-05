def main():
    import random
    random_num = random.randint(1, 2)
    if random_num == 1:
        answer = "Yes"
    else:
        answer = "No"
    print("Should I study? {}".format(answer))


main()
