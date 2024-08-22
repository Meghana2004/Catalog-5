class ChargingStation:
    def __init__(self, name, location, total_slots, fast_charging):
        self.name = name
        self.location = location
        self.total_slots = total_slots
        self.fast_charging = fast_charging
        self.slots = [False] * total_slots  

    def book_slot(self):
        for i in range(len(self.slots)):
            if not self.slots[i]:
                self.slots[i] = True  # Book the first available slot
                print(f"Slot booked at {self.name} in {self.location}")
                return True
        print(f"No slots available at {self.name} in {self.location}")
        return False

    def display_info(self):
        print(f"Station: {self.name}, Location: {self.location}, Fast Charging: {self.fast_charging}")


def main():
    stations = [
        ChargingStation("Station A", "Location 1", 5, True),
        ChargingStation("Station B", "Location 2", 3, False),
        ChargingStation("Station C", "Location 1", 2, True),
    ]

    location_filter = input("Enter location to search for charging stations: ")
    fast_charging_filter = input("Do you want fast charging? (yes/no): ")

    fast_charging_required = fast_charging_filter.lower() == "yes"
    filtered_stations = [
        station for station in stations
        if station.location.lower() == location_filter.lower() and station.fast_charging == fast_charging_required
    ]


    if not filtered_stations:
        print("No charging stations found with the given filters.")
    else:
        print("Available Charging Stations:")
        for station in filtered_stations:
            station.display_info()


        station_name = input("Enter the station name to book a slot: ")
        booked = False
        for station in filtered_stations:
            if station.name.lower() == station_name.lower():
                booked = station.book_slot()
                break

        if not booked:
            print("Booking failed. Please try again.")


if __name__ == "__main__":
    main()
