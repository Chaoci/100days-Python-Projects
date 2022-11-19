import requests

SHEETY_ENDPOINT = "https://api.sheety.co/0cc72aeabea665e303c02d94a6fbb2d2/flightDeals/prices"

SHEETY_TOKEN = {
    "Authorization":"Bearer 12344321chaefewierj"
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.destination_data={}
        
    def get_destination_data(self):
        response_sheet = requests.get(url=SHEETY_ENDPOINT,headers=SHEETY_TOKEN)
        data =response_sheet.json()
        self.destination_data = data["prices"]
        
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"],
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",json=new_data,headers=SHEETY_TOKEN)
            print(response.text)
    
    def get_customer_emails(self):
        customers_endpoint = "https://api.sheety.co/0cc72aeabea665e303c02d94a6fbb2d2/flightDeals/user"
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data