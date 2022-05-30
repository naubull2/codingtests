# coding: utf-8
# Copyright © 2021 naubull2 <naubull2@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Constraints:

	1 <= trips.length <= 1000
	trips[i].length == 3
	1 <= numPassengersi <= 100
	0 <= fromi < toi <= 1000
	1 <= capacity <= 105
"""
import pytest
from collections import defaultdict


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = defaultdict(dict)
        for t in trips:
            num, pickup, drop = t[0], t[1], t[2]
            locations[pickup]["up"] = locations[pickup].setdefault("up", 0) + num
            locations[drop]["down"] = locations[drop].setdefault("down", 0) + num

        # check validity
        cap = capacity
        for loc in sorted(locations.keys()):
            # unload first, then pickup
            cap += locations[loc].get("down", 0)  # may be empty if starting point
            cap -= locations[loc].get("up", 0)  # may be empty if final destination
            if cap < 0:
                return False
        return True


@pytest.mark.parametrize("", [])
def test():
    pass


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
