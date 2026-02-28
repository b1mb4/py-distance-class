class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            val = other.km
        elif isinstance(other, (int, float)):
            val = other
        else:
            return NotImplemented
        return Distance(self.km + val)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            val = other.km
        elif isinstance(other, (int, float)):
            val = other
        else:
            return NotImplemented
        self.km += val
        return self

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        new_km = self.km * other
        return Distance(new_km)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("devision by zero")
        new_km = round(self.km / other, 2)
        return Distance(new_km)

    def __get__km(self, other):
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        return NotImplemented

    def __eq__(self, other):
        other_km = self.__get__km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km == other_km
    def __lt__(self, other):
        other_km = self.__get__km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km < other_km

    def __le__(self, other):
        other_km = self.__get__km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km <= other_km

    def __ge__(self, other):
        other_km = self.__get__km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km >= other_km

    def __gt__(self, other):
        other_km = self.__get__km(other)
        if other_km is NotImplemented:
            return NotImplemented
        return self.km > other_km
