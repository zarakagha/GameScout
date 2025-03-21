import backend.database as database

Gamestores = database.Gamestores()

class StoreIDAction:
    def StoreIDToNameWithPrice(StorePriceSavingsDeal):
        StoreNameWithPrice = {}
        for key in StorePriceSavingsDeal:
            match key:
                case 1:
                    StoreNameWithPrice["Steam"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 2:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["GamersGate"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 3:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["GreenManGaming"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 7:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["GOG"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 8:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["Origin"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 11:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["Humble Store"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 13:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["Uplay"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 15:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["Fanatical"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 21:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["WinGameStore"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 23:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["GameBillet"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 24:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["Voidu"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 25:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["Epic Games Store"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 27:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["Gamesplanet"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 28:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["Gamesload"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 30:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["IndieGala"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 31:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["Blizzard Shop"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 33:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["DLGamer"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 34:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["Noctre"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case 35:
                    isenabled = StoreIDAction.checkEnabled(key)
                    if isenabled:
                        StoreNameWithPrice["DreamGame"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                    else:
                        continue
                case _:
                    continue
        return StoreNameWithPrice
    
    def checkEnabled(storeID):
        sql = "SELECT enabled FROM Gamestores WHERE id = %s;"
        game = Gamestores.select(sql, storeID)
        return bool(game[0]["enabled"])
        