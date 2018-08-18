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
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        # Sort first by people in front and then by height
        people_partially_sorted = sorted(people, key=itemgetter(1, 0))

        print(people_partially_sorted)
        exit(0)

        while len(people_sorted) < len(people):
            num_people_in_front = 0

            for person in people:
                if person[1] == num_people_in_front:
                    pass

            num_people_in_front += 1

        people_sorted = []
        return people_sorted


def main():
    sol = Solution()

    a = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(sol.reconstructQueue(a))


if __name__ == '__main__':
    main()
