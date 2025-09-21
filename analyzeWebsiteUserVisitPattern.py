from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    # youtube video - https://www.youtube.com/watch?v=cqC7kiLG0Dc
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        # initialize a dictionary
        G = defaultdict(list)

        # zip(timestamp, username, website)
        # This combines the three lists (or iterables) timestamp, username, and website into a single iterable of tuples, where each tuple groups together corresponding elements from each list.
        # The zipped tuples are sorted by the first element in each tuple by default (which is the timestamp here)
        # the hashmap will map the following -
        # "user" : ["website1", "website2", "website3"] --> hence, the chronological order of the websites is preserved (very important for this problem)

        # ex. before sorting
        # list(zip(timestamp, username, website))
        # [(3, 'alice', 'site3'), (1, 'bob', 'site1'), (2, 'alice', 'site2')]

        # ex. after sorting -
        # sorted(zip(timestamp, username, website))
        # [(1, 'bob', 'site1'), (2, 'alice', 'site2'), (3, 'alice', 'site3')]
        for t, user, web in sorted(zip(timestamp, username, website)):
            G[user].append(web)

        print(G)

        # initialize another dict to store the scores of each pattern
        scores = defaultdict(int)

        # iterate over the hashmap
        for user, websites in G.items():
            # initialize a set for each user
            seen_patterns = set()  # To avoid counting duplicate patterns per user
            n = len(websites)

            # iterate over the websites that the user has visited
            # for each website in websites
            for i in range(n):
                # form a pattern with two other websites from the list
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        pattern = (websites[i], websites[j], websites[k])
                        # if this pattern is not already seen in the set, add it to the set and increase its score in the dict scores
                        if pattern not in seen_patterns:
                            scores[pattern] += 1
                            seen_patterns.add(pattern)

        max_pattern, max_cnt = "", 0
        # iterate over dict scores
        for pattern, cnt in scores.items():
            # if the score of a certain pattern is more than our current count, update max_pattern and max_cnt
            # or if the two scores are equal, pick the pattern that is lexicographically smaller

            # ex. pattern1 = ("home", "about", "career") and pattern2 = ("home", "cart", "maps") --> pattern1 is smaller bcz a < c alphabetically
            if cnt > max_cnt or (cnt == max_cnt and pattern < max_pattern):
                max_pattern = pattern
                max_cnt = cnt

        return max_pattern

    # CHATGPT - "Apparently" optimized but not tested
    def mostVisitedPattern2(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        # Step 1: Group websites visited by each user in chronological order
        G = defaultdict(list)
        for _, user, web in sorted(zip(timestamp, username, website)):
            G[user].append(web)

        # Step 2: Count unique patterns per user
        scores = defaultdict(int)
        for user, websites in G.items():
            if len(websites) < 3:
                continue
            seen_patterns = set()
            for pattern in combinations(websites, 3):
                if pattern not in seen_patterns:
                    scores[pattern] += 1
                    seen_patterns.add(pattern)

        # Step 3: Find the pattern with the highest score (lexicographically smallest in ties)
        max_pattern, max_cnt = (), 0
        for pattern, cnt in scores.items():
            if cnt > max_cnt or (cnt == max_cnt and pattern < max_pattern):
                max_pattern = pattern
                max_cnt = cnt

        return list(max_pattern)


username = [
    "joe",
    "joe",
    "joe",
    "james",
    "james",
    "james",
    "james",
    "mary",
    "mary",
    "mary",
]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = [
    "home",
    "about",
    "career",
    "home",
    "cart",
    "maps",
    "home",
    "home",
    "about",
    "career",
]

print(Solution().mostVisitedPattern(username, timestamp, website))
