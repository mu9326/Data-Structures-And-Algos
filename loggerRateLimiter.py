# Input
# [
#     "Logger",
#     "shouldPrintMessage",
#     "shouldPrintMessage",
#     "shouldPrintMessage",
#     "shouldPrintMessage",
#     "shouldPrintMessage",
#     "shouldPrintMessage",
# ]
# [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"], [21, "bar"]]

# allowed_timestamp
# {"foo": 21, "bar": 31}


# Output
# [null, true, true, false, false, false, true]


class Logger:
    def __init__(self):
        self.allowed_timestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.allowed_timestamps:
            if timestamp < self.allowed_timestamps[message]:
                return False
        # \                self.allowed_timestamps[message] = timestamp + 10
        #                 return True

        self.allowed_timestamps[message] = timestamp + 10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
