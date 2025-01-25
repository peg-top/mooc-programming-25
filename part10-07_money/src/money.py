# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self._euros == other._euros and self._cents == other._cents

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return (self._euros + self._cents / 100) < (other._euros + other._cents / 100)

    def __gt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return (self._euros + self._cents / 100) > (other._euros + other._cents / 100)

    def __ne__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return not self == other

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        total_euros = self._euros + other._euros
        total_cents = self._cents + other._cents
        if total_cents >= 100:
            total_euros += total_cents // 100
            total_cents = total_cents % 100
        return Money(total_euros, total_cents)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        total_self = self._euros * 100 + self._cents
        total_other = other._euros * 100 + other._cents
        if total_self < total_other:
            raise ValueError("a negative result is not allowed")
        total__cents = total_self - total_other
        _euros = total__cents // 100
        _cents = total__cents % 100
        return Money(_euros, _cents)


# e1 = Money(4, 10)
# e2 = Money(2, 5)

# print(e1)
# print(e2)