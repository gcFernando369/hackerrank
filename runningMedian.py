from heapq import heappush, heappop


def runningMedian(a):
    medians = []    
    len_a = len(a)  

    if len_a > 0: medians.append(a[0])
    if len_a > 1: medians.append((a[0] + a[1]) / 2)
    if len_a > 2:
        m = medians[1]            
        if a[0] < a[1]: h_max, h_min = [a[0]], [a[1]]
        else: h_max, h_min = [a[1]], [a[0]]

        h_min_size, h_max_size = 1, 1
        max_, min_ = h_max[0], h_min[0]

        for i, item in enumerate(a[2:]):
            if item <= m:
                h_max.append(item)
                h_max_size += 1
                if item > max_: max_ = item
            else:
                h_min.append(item)
                h_min_size += 1
                if item < min_: min_ = item   
            

            if abs(h_min_size - h_max_size) > 1:
                if h_min_size > h_max_size:                    
                    h_min.remove(min_)
                    h_min_size -= 1
                    
                    h_max.append(min_) 
                    h_max_size += 1                                   
                    
                    max_ = min_
                    min_ = min(h_min)
                else:                
                    h_max.remove(max_)
                    h_max_size -= 1
                    
                    h_min.append(max_)
                    h_min_size += 1

                    min_ = max_
                    max_ = max(h_max)
            
            if i%2 == 0:
                if h_min_size >= h_max_size: m = min_
                else: m = max_
            else: m = (max_ + min_)/2
            medians.append(m)
    return medians


#a = [12, 4, 5, 3, 8, 7]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

medians = runningMedian(a)
print(medians)

#t = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
#print(t)
