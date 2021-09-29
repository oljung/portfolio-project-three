class InputHandler():
    def input_integer(message, low, high):
        while(True):
            try:
                num = int(input(message))
                if num >= low and num <= high:
                    return num
                    break
                else:
                    print('Number must be within desired range\n')
            except:
                print('Only enter a whole number within the desired range, please\n')