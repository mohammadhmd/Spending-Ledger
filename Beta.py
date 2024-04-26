ledger = []
import json
with open("Ledger.txt", "a") as database :
    json.dump(ledger, database, indent= 4)