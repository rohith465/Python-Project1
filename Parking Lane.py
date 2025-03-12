class ParkingLot:
    def __init__(self):
        self.lanes = [[None for _ in range(4)] for _ in range(5)]

    def park_vehicle(self, vehicle_number):
        for lane in self.lanes:
            for i in range(len(lane)):
                if lane[i] is None:
                    lane[i] = vehicle_number
                    print(f"Vehicle {vehicle_number} parked in lane {self.lanes.index(lane) + 1}, space {i + 1}.")
                    return
        print("Parking lot is full.")

    def exit_vehicle(self, vehicle_number):
        for lane in self.lanes:
            for i in range(len(lane)):
                if lane[i] == vehicle_number:
                    lane[i] = None
                    print(f"Vehicle {vehicle_number} has exited from lane {self.lanes.index(lane) + 1}, space {i + 1}.")
                    return
        print("Vehicle not found.")

    def display_parking(self):
        print("\nCurrent Parking Status:")
        for lane_index, lane in enumerate(self.lanes):
            print(f"Lane {lane_index + 1}: ", end="")
            for space in lane:
                if space is None:
                    print("[Empty]", end=" ")
                else:
                    print(f"[{space}]", end=" ")
            print()


def main():
    parking_lot = ParkingLot()

    while True:
        action = input("Enter 'park' to park a vehicle or 'exit' to remove a vehicle (or 'quit' to exit): ").strip().lower()
        
        if action == 'park':
            vehicle_number = input("Enter vehicle number: ").strip()
            parking_lot.park_vehicle(vehicle_number)
            parking_lot.display_parking()
        
        elif action == 'exit':
            vehicle_number = input("Enter vehicle number to exit: ").strip()
            parking_lot.exit_vehicle(vehicle_number)
            parking_lot.display_parking()
        
        elif action == 'quit':
            print("Exiting the parking management system.")
            break
        
        else:
            print("Invalid input. Please enter 'park', 'exit', or 'quit'.")


if __name__ == "__main__":
    main()
