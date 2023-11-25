import sys

# Unnecessary commentaries for this code
def main():
    """
    Main function to look proffesional
    Prints "Hello" + every command like argument you entered
    """
    print("Hello", end=" ") # printing first word, which is "Hello"

    # For every system line argument it will type argument + ", "
    for i in sys.argv[1:len(sys.argv)]:
        print(i, end=", ")
    # Empty print for termianl not to look ugly.
    print() 
    
if __name__ == "__main__":
    main()
