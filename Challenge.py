import heapq
import random

class IPTracker:
    def __init__(self):
        self.ip_count_map = {}
        self.top_100_list = []
        self.top_100_set = set()

    def requestHandled(self, ip):
        if ip in self.ip_count_map:
            self.ip_count_map[ip] = self.ip_count_map[ip] + 1
        else:
            self.ip_count_map[ip] = 1

        if ip in self.top_100_set:
            self.top_100_list.remove((self.ip_count_map[ip]-1, ip))
            heapq.heapify(self.top_100_list)
        else:
            self.top_100_set.add(ip)
        
        heapq.heappush(self.top_100_list, (self.ip_count_map[ip], ip))
        
        if len(self.top_100_list) > 100:
            removed_tuple = heapq.heappop(self.top_100_list)
            self.top_100_set.remove(removed_tuple[1])

    # Retrieves the top 100 most frequent ip addresses.
    def top100(self):
        result = [0 for x in range(len(self.top_100_list))]
        top_100_result_heap = self.top_100_list.copy()
        for i in range(len(self.top_100_set)):
            result[len(self.top_100_set)-(i+1)] = heapq.heappop(top_100_result_heap)
        return result

    def clear(self):
        self.ip_count_map = {}
        self.top_100_list = []
        self.top_100_set = set()


def main():
    obj = IPTracker()
    for x in range(0, 20000000):
        obj.requestHandled(str(random.randint(0,300)))
        # Just something to print progress for responsiveness
        if x % 20000 == 0:
            print(str(x) + "/20000000")
    print(obj.top100())

    obj.clear()

    print(obj.top100())

    obj.requestHandled(str(random.randint(0,300)))
    obj.requestHandled(str(random.randint(0,300)))
    obj.requestHandled(str(random.randint(0,300)))
    obj.requestHandled(str(random.randint(0,300)))

    print(obj.top100())

if __name__ == "__main__":
    main()
