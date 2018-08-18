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

        # Sort first by height then by number of tall people in front
        people_partially_sorted = sorted(people, key=itemgetter(0, 1))
        people_in_line = [None] * len(people)

        for person_to_insert in people_partially_sorted:

            tall_people_in_front = Solution.get_tall_people_in_front(person_to_insert)
            tall_people_seen = 0

            for i, person_in_line in enumerate(people_in_line):

                if not people_in_line[i] and tall_people_in_front == tall_people_seen:
                        people_in_line[i] = person_to_insert
                        break

                if not people_in_line[i] or Solution.get_height(people_in_line[i]) >= Solution.get_height(person_to_insert):
                    tall_people_seen += 1

        return people_in_line


def main():
    sol = Solution()

    a = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(sol.reconstructQueue(a))


if __name__ == '__main__':
    main()
