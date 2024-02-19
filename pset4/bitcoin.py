import sys
import requests
import json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

obj = response.json()
# print(json.dumps(obj, indent=1)) Helps visualize the data while indented.
usd_data = obj["bpi"]["USD"]
amount = usd_data["rate_float"]

try:
    if sys.argv[1].isalpha() == True:
        sys.exit("Command-line argument is not a number")
    else:
        print(f"${float(sys.argv[1]) * amount:,.4f}")

except IndexError:
    sys.exit("Missing command-line argument")