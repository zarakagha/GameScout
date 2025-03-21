import backend.database as database

Gamestores = database.Gamestores()

class StoreIDAction:
    def StoreIDToNameWithPrice(StorePriceSavingsDeal): #function to match each store id with price
        StoreNameWithPrice = {}
        for key in StorePriceSavingsDeal: #iterates through storePriceSavingsDeal
            match key:
                case 1: #checks if the storeid is one and stores it into steam
                    StoreNameWithPrice["Steam"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 2:#checks if the storeid is one and stores it into steam
                    isenabled = StoreIDAction.checkEnabled(key)#checks if steam is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["GamersGate"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 3:#checks if the storeid is one and stores it into greenmangaming
                    isenabled = StoreIDAction.checkEnabled(key)#checks if greenmangaming is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["GreenManGaming"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 7:#checks if the storeid is one and stores it into gog
                    isenabled = StoreIDAction.checkEnabled(key)#checks if gog is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["GOG"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 8:#checks if the storeid is one and stores it into origin
                    isenabled = StoreIDAction.checkEnabled(key)#checks if origin is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["Origin"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 11:#checks if the storeid is one and stores it into humble store
                    isenabled = StoreIDAction.checkEnabled(key)#checks if humble store is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["Humble Store"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 13:#checks if the storeid is one and stores it into uplay
                    isenabled = StoreIDAction.checkEnabled(key)#checks if uplay is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["Uplay"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 15:#checks if the storeid is one and stores it into fanatical
                    isenabled = StoreIDAction.checkEnabled(key)#checks if fanatical is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["Fanatical"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 21:#checks if the storeid is one and stores it into wingamestore
                    isenabled = StoreIDAction.checkEnabled(key)#checks if winggamestore is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["WinGameStore"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 23:#checks if the storeid is one and stores it into gamebillet
                    isenabled = StoreIDAction.checkEnabled(key)#checks if gamebillet is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["GameBillet"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 24:#checks if the storeid is one and stores it into voidu
                    isenabled = StoreIDAction.checkEnabled(key)#checks if voidu is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["Voidu"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 25:#checks if the storeid is one and stores it into epic games store
                    isenabled = StoreIDAction.checkEnabled(key)#checks if epic games store is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["Epic Games Store"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 27:#checks if the storeid is one and stores it into gamesplanet
                    isenabled = StoreIDAction.checkEnabled(key)#checks if gameplanet is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["Gamesplanet"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 28:#checks if the storeid is one and stores it into gamesload
                    isenabled = StoreIDAction.checkEnabled(key)#checks if gamesload is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["Gamesload"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 30:#checks if the storeid is one and stores it into indiegala
                    isenabled = StoreIDAction.checkEnabled(key)#checks if indiegala is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["IndieGala"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 31:#checks if the storeid is one and stores it into blizzard
                    isenabled = StoreIDAction.checkEnabled(key)#checks if blizzard is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["Blizzard Shop"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 33:#checks if the storeid is one and stores it into dlgamer
                    isenabled = StoreIDAction.checkEnabled(key)#checks if dlgamer is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["DLGamer"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 34:#checks if the storeid is one and stores it into noctre
                    isenabled = StoreIDAction.checkEnabled(key)#checks if noctre is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["Noctre"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 35:#checks if the storeid is 35 and stores it into dreamgame
                    isenabled = StoreIDAction.checkEnabled(key) #checks if dreamgame is an enabled game store
                    if isenabled:
                        StoreNameWithPrice["DreamGame"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case _:
                    continue
        return StoreNameWithPrice
    
    def checkEnabled(storeID): #function to see if the store id is enabled
        sql = "SELECT enabled FROM Gamestores WHERE id = %s;" #pulls all enabled gamestores
        game = Gamestores.select(sql, storeID) #stores them into game
        return bool(game[0]["enabled"]) 
        