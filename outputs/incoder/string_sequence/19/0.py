
def string_sequence(n: int) -> str:
    """ Return a string containing vertical line-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(100)
    '0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80|81|82|83|84|85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|100'
    """
    return f"|{n}"


@dataclass(frozen=True)
class StringSequence:
    """ A sequence of strings. """

    sequence: Sequence[str]

    def __str__(self) -> str:
        """ Return a string representation of the sequence. """
        return f"StringSequence[{', '.join(map(str, self))}]"

    def __repr__(self) -> str:
        """ Return a string representation of the sequence. """
        return f"StringSequence[{', '.join(map(repr, self))}]"

    def __len__(self) -> int:
        """ Return the length of the sequence. """
        return len(self.sequence)

    def __getitem__(self, index: int) -> Optional[str]:
        """ Return the element at the given index. """
        return self.sequence[index]

    def __iter__(self) -> Iterator[str]:
        """ Return an iterator over the sequence. """
        return iter(self.sequence)

    def __contains__(self, item: str) -> bool:
        """ Return whether the sequence contains the given item. """
        return item in self.sequence

    def __add__(self, other: Any) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(self.sequence + other.sequence)

    def __radd__(self, other: Any) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(other.sequence + self.sequence)

    def __mul__(self, n: int) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(self.sequence * n)

    def __rmul__(self, n: int) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(n * [self.sequence])

    def __truediv__(self, n: int) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(self.sequence / n)

    def __rtruediv__(self, n: int) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(n / [self.sequence])

    def __floordiv__(self, n: int) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(self.sequence // n)

    def __rfloordiv__(self, n: int) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(n // [self.sequence])

    def __mod__(self, n: int) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(self.sequence % n)

    def __rmod__(self, n: int) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(n % [self.sequence])

    def __pow__(self, n: int) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(self.sequence ** n)

    def __rpow__(self, n: int) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(n ** [self.sequence])

    def __neg__(self) -> "StringSequence":
        """ Return the concatenation of the two sequences. """
        return StringSequence(self.sequence[::-1])

    def __pos__(self) -> "String