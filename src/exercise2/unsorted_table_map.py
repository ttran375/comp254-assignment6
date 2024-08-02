# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from map_base import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    # ----------------------------- nonpublic behaviors -----------------------------
    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key greater than or equal to k.

        Return high + 1 if no such item qualifies.

        That is, j will be returned such that:
           all items of slice table[low:j] have key < k
           all items of slice table[j:high+1] have key >= k
        """
        if high < low:
            return high + 1  # no element qualifies
        mid = (low + high) // 2
        if k == self._table[mid]._key:
            return mid  # found exact match
        if k < self._table[mid]._key:
            return self._find_index(k, low, mid - 1)  # Note: may return mid
        return self._find_index(k, mid + 1, high)  # answer is right of mid

    # ----------------------------- public behaviors -----------------------------
    def __init__(self):
        """Create an empty map."""
        self._table = []  # list of _Item's

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:  # Found a match:
                item._value = v  # reassign value
                return  # and quit
        # did not find match for key
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j, entry in enumerate(self._table):
            if k == entry._key:  # Found a match:
                self._table.pop(j)  # remove item
                return  # and quit
        raise KeyError("Key Error: " + repr(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key  # yield the KEY

    def containKey(self, k):
        """Check if key k exists in the map.

        Returns True if key exists, otherwise False.
        """

        # Find the index where the key k would be located
        index = self._find_index(k, 0, len(self._table) - 1)

        # Returns True if the key is found within the bounds of the table and matches the key at the
        # found index
        return index < len(self._table) and self._table[index]._key == k
