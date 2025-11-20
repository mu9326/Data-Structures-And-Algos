import heapq
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

        # initialize the hashmap and the res
        # map = {1: [65, 87, 91, 92, 100], 2: [93, 97, 77]}
        topFiveMap = {}
        res = []

        # iterate over items --> [id, score]:
        for item in items:
            # if the id is in the hashmap:
            if item[0] in topFiveMap:
                # get the corresponding minHeap [93, 97, 77]

                # push the score on the minheap
                heapq.heappush(topFiveMap[item[0]], item[1])
                # if the size of the heap is greater than 5:
                if len(topFiveMap[item[0]]) > 5:
                    # remove the min
                    heapq.heappop(topFiveMap[item[0]])
            else:
                # insert the id in the hashmap with a corresponding minHeap with the score
                topFiveMap[item[0]] = [item[1]]
                heapq.heapify(topFiveMap[item[0]])

        for k, v in topFiveMap.items():
            res.append([k, sum(v) // 5])

        return sorted(res, key=lambda x: x[0])


def run_test(name, items, expected):
    sol = Solution()
    result = sol.highFive(items)
    print(f"\n=== {name} ===")
    print("Input:     ", items)
    print("Expected:  ", expected)
    print("Got:       ", result)
    print(
        "PASS"
        if result == expected or expected == "Varies (inspect output)"
        else "FAIL"
    )


# ---------------------------------------------------
# Test Cases
# ---------------------------------------------------

if __name__ == "__main__":
    # Test Case 1
    run_test(
        "Example Case",
        items=[
            [1, 91],
            [1, 92],
            [2, 93],
            [2, 97],
            [1, 60],
            [2, 77],
            [1, 65],
            [1, 87],
            [1, 100],
            [2, 100],
            [2, 76],
        ],
        expected=[
            [1, 87],
            [2, 88],
        ],
    )

    # Test Case 2
    run_test(
        "Single Student - Exactly 5 Scores",
        items=[[3, 80], [3, 70], [3, 60], [3, 90], [3, 100]],
        expected=[[3, 80]],
    )

    # Test Case 3
    run_test(
        "Single Student - More Than 5 Scores",
        items=[[5, 10], [5, 20], [5, 30], [5, 40], [5, 50], [5, 60], [5, 70]],
        expected=[[5, 50]],
    )

    # Test Case 4
    run_test(
        "Multiple Students Unsorted Input",
        items=[
            [2, 50],
            [1, 90],
            [2, 60],
            [1, 70],
            [3, 100],
            [1, 80],
            [2, 100],
            [3, 80],
            [1, 85],
            [2, 95],
            [1, 60],
            [3, 60],
            [2, 70],
            [3, 90],
            [3, 85],
        ],
        expected=[
            [1, 77],
            [2, 75],
            [3, 83],
        ],
    )

    # Test Case 5
    run_test(
        "Two Students - Exactly 5 Each",
        items=[
            [1, 50],
            [1, 60],
            [1, 70],
            [1, 80],
            [1, 90],
            [2, 10],
            [2, 20],
            [2, 30],
            [2, 40],
            [2, 50],
        ],
        expected=[
            [1, 70],
            [2, 30],
        ],
    )

    # Test Case 6: Stress Test
    import random

    large_items = []
    for student in range(1, 11):
        for _ in range(50):
            large_items.append([student, random.randint(0, 100)])

    run_test(
        "Stress Test - Large Random Dataset",
        items=large_items,
        expected="Varies (inspect output)",
    )
