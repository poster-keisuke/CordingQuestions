# 1603. Design Parking System
# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.empty = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.empty[carType - 1] > 0:
            self.empty[carType -1] -= 1
            return True

        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)