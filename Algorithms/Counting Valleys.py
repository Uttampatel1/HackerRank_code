
def countingValleys(steps, path):
    # Write your code here
    # 1. Create a variable to keep track of the current level
    # 2. Create a variable to keep track of the number of valleys
    # 3. Loop through the path
        # 3.1. If the current level is 0 and the next step is a 'D', then we are entering a valley
        # 3.2. If the current level is -1 and the next step is a 'U', then we are exiting a valley
    # 4. Return the number of valleys

    current_level = 0
    number_of_valleys = 0
    for step in path:
        if step == 'U':
            current_level += 1
        else:
            current_level -= 1
        if current_level == 0 and step == 'U':
            number_of_valleys += 1
    return number_of_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
