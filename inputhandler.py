class InputHandler:
    """
    This class acts as a utility class containing static methods 
    for handling input in other modules.
    """
    def input_integer_range(message, low, high):
        """
        Method for handling integer input within a desired range,
        will run until valid input is given
        """
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


    def input_integer(message):
        """
        Method for handling integer input of any value, 
        will run until valid input is given
        """
        while(True):
            try:
                    num = int(input(message))
                    return num
                    break
            except:
                print('Only enter a whole number, please')
        
    
    def input_bool(message):
        """
        Method for handling yes or no input,
        returns True or False depending on input
        will run until valid input is given
        """
        while(True):
            value = input(message)
            if value.lower() == 'y':
                return True
                break
            elif value.lower() == 'n':
                return False
                break
            else:
                print('please enter value y(es) or n(o)')
