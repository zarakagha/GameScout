class StoreIDAction:
    def StoreIDToNameWithPrice(StoreIDWithPrice):
        StoreNameWithPrice = {}
        for key in StoreIDWithPrice:
            match key:
                case 1:
                    StoreNameWithPrice["Steam"] = round(StoreIDWithPrice.get(key), 2)
                case 2:
                    StoreNameWithPrice["GamersGate"] = round(StoreIDWithPrice.get(key), 2)
                case 3:
                    StoreNameWithPrice["GreenManGaming"] = round(StoreIDWithPrice.get(key), 2)
                case 7:
                    StoreNameWithPrice["GOG"] = round(StoreIDWithPrice.get(key), 2)
                case 8:
                    StoreNameWithPrice["Origin"] = round(StoreIDWithPrice.get(key), 2)
                case 11:
                    StoreNameWithPrice["Humble Store"] = round(StoreIDWithPrice.get(key), 2)
                case 13:
                    StoreNameWithPrice["Uplay"] = round(StoreIDWithPrice.get(key), 2)
                case 15:
                    StoreNameWithPrice["Fanatical"] = round(StoreIDWithPrice.get(key), 2)
                case 21:
                    StoreNameWithPrice["WinGameStore"] = round(StoreIDWithPrice.get(key), 2)
                case 23:
                    StoreNameWithPrice["GameBillet"] = round(StoreIDWithPrice.get(key), 2)
                case 24:
                    StoreNameWithPrice["Voidu"] = round(StoreIDWithPrice.get(key), 2)
                case 25:
                    StoreNameWithPrice["Epic Games Store"] = round(StoreIDWithPrice.get(key), 2)
                case 27:
                    StoreNameWithPrice["Gamesplanet"] = round(StoreIDWithPrice.get(key), 2)
                case 28:
                    StoreNameWithPrice["Gamesload"] = round(StoreIDWithPrice.get(key), 2)
                case 29:
                    StoreNameWithPrice["2Game"] = round(StoreIDWithPrice.get(key), 2)
                case 30:
                    StoreNameWithPrice["IndieGala"] = round(StoreIDWithPrice.get(key), 2)
                case 31:
                    StoreNameWithPrice["Blizzard Shop"] = round(StoreIDWithPrice.get(key), 2)
                case 33:
                    StoreNameWithPrice["DLGamer"] = round(StoreIDWithPrice.get(key), 2)
                case 34:
                    StoreNameWithPrice["Noctre"] = round(StoreIDWithPrice.get(key), 2)
                case 35:
                    StoreNameWithPrice["DreamGame"] = round(StoreIDWithPrice.get(key), 2)
                case _:
                    continue
        return StoreNameWithPrice