import random

class WasteManagementSystem:
    def __init__(self, num_bins, max_capacity):
        self.num_bins = num_bins
        self.max_capacity = max_capacity
        self.bins = [0] * num_bins

    def generate_waste(self):
        return random.randint(1, self.max_capacity)

    def dispose_waste(self):
        for _ in range(10):
            bin_index = random.randint(0, self.num_bins - 1)
            waste = self.generate_waste()
            if self.bins[bin_index] + waste <= self.max_capacity:
                self.bins[bin_index] += waste
                print(f"Waste disposed in bin {bin_index + 1}: {waste} units")
            else:
                print(f"Bin {bin_index + 1} is full! Overflow of {waste} units")

if __name__ == "__main__":
    num_bins = int(input("Enter the number of bins: "))
    max_capacity = int(input("Enter the maximum capacity of each bin: "))
    waste_system = WasteManagementSystem(num_bins, max_capacity)
    waste_system.dispose_waste()
