def iif(condition, true_part, false_part):
    return (condition and [true_part] or [false_part])[0]

def main():
    print (iif(1==1, 1==2, 2))

if __name__ == '__main__':
    main()