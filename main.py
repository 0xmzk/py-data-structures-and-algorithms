from tests import *

def tests():
    import pkgutil
    print([name for _, name, _ in pkgutil.iter_modules(['tests'])])
    
def main():
    tests()
    

if __name__ == "__main__":
    main()