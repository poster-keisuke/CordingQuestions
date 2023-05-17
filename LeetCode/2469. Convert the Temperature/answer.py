# 2469. Convert the Temperature
# https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = 273.15
        return [celsius + kelvin, celsius * 1.80 + 32.00]
