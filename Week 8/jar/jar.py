class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        # Inital number of cookies in the jar = 0.
        self.size = 0

    def __str__(self):
         return f"🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError(f"Deposit would result in exceeding capacity [{self._capacity}] of the jar!")
        # Deposit n cookies to jar.
        self._size += n     # Need not call setter-getter pair since checking conditional is unnecessary.

    def withdraw(self, n):
        if n > self._size:
            raise ValueError(f"Not enough cookies! Current balance - {self._size}")
        # Give n cookies from the jar.
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        # Ensure capacity is an integer.
        if not type(capacity) == int:
            raise ValueError("Capacity must be a positive integer")

        # Ensure capacity is a positive number.
        elif capacity < 0:
            raise ValueError("Capacity must be a positive integer")

        self._capacity = int(capacity)


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError("Size greater than capacity")

        self._size = size


def main():
    ...

if __name__ == "__main__":
    main()
