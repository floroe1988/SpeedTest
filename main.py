from src.GetConnectionSpeed import getConnectionSpeed
from src.StoreConnectionSpeed import storeConnectionSpeed

def main():
    '''
    Function to test the current internet down- and upload speed
    After speedtest has been performed, the result is sent to a spread sheet via an ifttt webhook
    '''
    
    result = getConnectionSpeed()
    storeConnectionSpeed(result)
    print("all done")

if __name__ == "__main__":
    main()
