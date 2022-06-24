from testing import *

def print_tests():
    import pkgutil
    print([name for _, name, _ in pkgutil.iter_modules(['testing'])])
    
def main():
    print_tests()
    Tree_Tests.binary_tree()
    
if __name__ == "__main__":
    main()