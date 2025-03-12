from gameclass import Game
from ConvertPrice import ConvertUSDToCad

testobj = Game()

testobj.setGameName = "elden ring"
testobj.setGamePrice = 79.99
print(testobj.gamePrice())
testobj.setGameSteamappid = int("1245620")

testobj.setToListOfStores("1")
testobj.setToListOfStores("2")
testobj.setToListOfStores("15")

testobj.setToListOfStores("4")

testobj.setStoreAndSavings(1, 25)
testobj.setStoreAndSavings(2, 0)
testobj.setStoreAndSavings(15, 40)

testobj.setStoreAndSavings(4, 10)

testobj.setStoreAndPrice(1, 45)
testobj.setStoreAndPrice(2, 60)
testobj.setStoreAndPrice(15, 36)

testobj.setStoreAndPrice(4, 54)

print(testobj.storesWithPrice())
ConvertUSDToCad.convertListOfPricesFromGame(testobj)
print(testobj.storesWithPrice())