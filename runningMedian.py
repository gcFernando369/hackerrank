from heapq import heapify, heappush, heappop

def runningMedian(a):
    medians = []    
    len_a = len(a)

    if len_a > 0: medians.append(a[0])
    if len_a > 1: medians.append((a[0] + a[1]) / 2)
    if len_a > 2:
        m = medians[1]            
        if a[0] < a[1]: h_max, h_min = [-a[0]], [a[1]]
        else: h_max, h_min = [-a[1]], [a[0]]
    
        heapify(h_min)
        heapify(h_max)

        for i, item in enumerate(a[2:]):
            if item <= m: heappush(h_max, -item)
            else: heappush(h_min, item)

            h_max_size, h_min_size = len(h_max), len(h_min)
            if abs(h_max_size - h_min_size) > 1:
                if h_min_size > h_max_size:
                    val = heappop(h_min)
                    heappush(h_max, -val)
                else:
                    val = heappop(h_max)
                    heappush(h_min, -val)            

            h_max_size, h_min_size = len(h_max), len(h_min)
            if i%2 == 0:
                if h_min_size > h_max_size: m = h_min[0]
                else: m = -h_max[0]
            else: m = (h_min[0] - h_max[0])/2
            medians.append(m)

    return medians

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
medians = runningMedian(a)
print(medians)

