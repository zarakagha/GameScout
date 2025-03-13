class StoreIDAction:
    def StoreIDToNameWithPrice(StorePriceSavingsDeal):
        StoreNameWithPrice = {}
        for key in StorePriceSavingsDeal:
            match key:
                case 1:
                    StoreNameWithPrice["Steam"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 2:
                    StoreNameWithPrice["GamersGate"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 3:
                    StoreNameWithPrice["GreenManGaming"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 7:
                    StoreNameWithPrice["GOG"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 8:
                    StoreNameWithPrice["Origin"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 11:
                    StoreNameWithPrice["Humble Store"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 13:
                    StoreNameWithPrice["Uplay"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 15:
                    StoreNameWithPrice["Fanatical"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 21:
                    StoreNameWithPrice["WinGameStore"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 23:
                    StoreNameWithPrice["GameBillet"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 24:
                    StoreNameWithPrice["Voidu"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 25:
                    StoreNameWithPrice["Epic Games Store"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 27:
                    StoreNameWithPrice["Gamesplanet"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 28:
                    StoreNameWithPrice["Gamesload"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 30:
                    StoreNameWithPrice["IndieGala"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 31:
                    StoreNameWithPrice["Blizzard Shop"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 33:
                    StoreNameWithPrice["DLGamer"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 34:
                    StoreNameWithPrice["Noctre"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case 35:
                    StoreNameWithPrice["DreamGame"] = [round(StorePriceSavingsDeal.get(key)[0], 2), StorePriceSavingsDeal.get(key)[1], StorePriceSavingsDeal.get(key)[2]]
                case _:
                    continue
        return StoreNameWithPrice