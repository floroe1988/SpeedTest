from src.GetConnectionSpeed import getConnectionSpeed
from src.StoreConnectionSpeed import storeConnectionSpeed

def main():
    result = getConnectionSpeed()
    storeConnectionSpeed(result)
    print("all done")

if __name__ == "__main__":
    main()
