"""

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater
than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

from operator import itemgetter


class Solution:
    @staticmethod
    def get_height(person):
        return person[0]

    @staticmethod
    def get_tall_people_in_front(person):
        return person[1]

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(people) == 0:
            return []

        # Sort first by people in front and then by height
        people_partially_sorted = sorted(people, key=itemgetter(1, 0))

        assert(len(people_partially_sorted) > 0)
        people_sorted = [people_partially_sorted[0]]

        for person_to_insert in people_partially_sorted:
            tall_people_seen = 0

            insertion_index = len(people_sorted)
            for i, person_in_line in enumerate(people_sorted):
                if Solution.get_height(person_in_line) >= Solution.get_height(person_to_insert):
                    tall_people_seen += 1



        return people_sorted


def main():
    sol = Solution()

    a = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(sol.reconstructQueue(a))


if __name__ == '__main__':
    main()
