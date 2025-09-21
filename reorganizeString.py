import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        # iterate over the string
        # add each character to the hashmap
        s_map = {}
        for c in s:
            s_map[c] = 1 + s_map.get(c, 0)

        print(s_map)

        # add [-count, char] to a list
        maxHeap = [[-count, char] for char, count in s_map.items()]
        # heapify the list
        heapq.heapify(maxHeap)

        # initialize the res string
        res = ""

        char_on_hold = ""

        # while the heap is not empty:
        while len(maxHeap) > 0:
            # count, char = get the most frequent char
            count, char = maxHeap[0]
            # if char == char_on_hold and len of heap is 1:
            if char == char_on_hold and len(maxHeap) == 1:
                return ""
            # if char_on_hold is not equal to char:
            if char != char_on_hold:
                # append the char to the res string
                heapq.heappop(maxHeap)
                res += char
                count += 1
                if count != 0:
                    heapq.heappush(maxHeap, [count, char])
            # elif it is equal to char_on_hold:
            elif char == char_on_hold:
                # get the next most freq_char
                prev_count, prev_char = heapq.heappop(maxHeap)
                count, char = heapq.heappop(maxHeap)
                # append the char to string and
                # increase its count by 1
                res += char
                count += 1
                if count != 0:
                    heapq.heappush(maxHeap, [count, char])
                    heapq.heappush(maxHeap, [prev_count, prev_char])

            char_on_hold = char

        # return the res string
        return res


print(Solution().reorganizeString("aba"))
