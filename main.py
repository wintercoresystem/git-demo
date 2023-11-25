import sys

def main():
    print("Hello", end=" ")
    for i in sys.argv[1:len(sys.argv)]:
        print(i, end=", ")
    print()
    
if __name__ == "__main__":
    main()
