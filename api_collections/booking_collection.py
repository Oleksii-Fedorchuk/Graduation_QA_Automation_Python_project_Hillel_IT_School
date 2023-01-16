import datetime
import json
from Automation_tests.api_collections.base_api import BaseAPI
from Automation_tests.api_collections.config_file import USERNAME, PASSWORD


class BookingCollection(BaseAPI):
    def __init__(self):
        super().__init__()
        self._booking_url = "booking"
        self._token_url = "auth"
        self._update_url = "booking/787"

    def get_token(self):
        response = self.post(f"{self._token_url}", body={"username": USERNAME, "password": PASSWORD})
        return response

    def create_booking(self):
        checkin = datetime.date(2023, 1, 1)
        checkout = datetime.date(2024, 1, 1, )
        booking_data = {"firstname": "Oleksii",
                        "lastname": "Fedorchuk",
                        "totalprice": 25000,
                        "depositpaid": True,
                        "bookingdates": {
                            "checkin": checkin.strftime("%Y-%m-%d"),
                            "checkout": checkout.strftime("%Y-%m-%d")},
                        "additionalneeds": "Breakfast"}
        json.dumps(booking_data)
        response = self.post(f"{self._booking_url}", body=booking_data)
        return response

    def get_booking_id(self):
        response = self.get(f"{self._booking_url}",
                            params={"firstname": "sally", "lastname": "brown"})
        return response
