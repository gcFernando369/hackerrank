from heapq import heapify, heappush, heappop
from copy import copy

def update(users_hash, users_list):
    for user in users_list:
        if user in users_hash: users_hash[user] += 1
        else: users_hash[user] = 1
    return users_hash

def processLogs(logs, threshold):
    users = {}

    for log in logs:
        s, r, _ = log.strip().split(' ')
        users_list = [s]
        if r != s: users_list.append(r)
        users = update(users, users_list)
    
    user_ids, counts = [], []
    for user_id, count in users.items():
        if count >= threshold:
            user_ids.append(user_id)
            counts.append(-count)
    
    counts_copy = copy(counts)
    heapify(counts_copy)
    out = []
    while len(counts) > 0: 
        val = heappop(counts_copy)
        idx_val = counts.index(val)
        out.append(user_ids[idx_val])
        del user_ids[idx_val]
        del counts[idx_val]
    
    return out