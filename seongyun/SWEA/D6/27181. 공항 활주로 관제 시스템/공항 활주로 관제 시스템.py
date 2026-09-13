import heapq

planes = set()
diverting_planes = []
landing_planes = []
latest_urg = {}

def init(P, fids, urg):
    planes.clear()
    diverting_planes.clear()
    landing_planes.clear()
    latest_urg.clear()
    for idx in range(P):
        planes.add(fids[idx])
        diverting_planes.append((urg[idx], -fids[idx]))
        landing_planes.append((-urg[idx], fids[idx]))
        latest_urg[fids[idx]] = urg[idx]
    heapq.heapify(diverting_planes)
    heapq.heapify(landing_planes)


def request(fid, u):
    planes.add(fid)
    heapq.heappush(diverting_planes, (u, -fid))
    heapq.heappush(landing_planes, (-u, fid))
    latest_urg[fid] = u


def renew(fid, u):
    latest_urg[fid] = u
    heapq.heappush(diverting_planes, (u, -fid))
    heapq.heappush(landing_planes, (-u, fid))


def cancel(fid):
    planes.discard(fid)


def clear_landing():
    if not planes:
        return -1
    
    while landing_planes:
        u, fid = heapq.heappop(landing_planes)
        u = -u
        if fid in planes and latest_urg[fid] == u:
            planes.remove(fid)
            return fid
    return -1


def divert():
    if not planes:
        return -1
        
    while diverting_planes:
        u, fid = heapq.heappop(diverting_planes)
        fid = -fid
        if fid in planes and latest_urg[fid] == u:
            planes.remove(fid)
            return fid
    return -1


def main():
    tokens = []
    while True:
        try:
            tokens.extend(input().split())
        except EOFError:
            break

    if not tokens:
        return

    it = iter(tokens)
    out = []
    
    T = int(next(it))
    for tc in range(1, T + 1):
        P = int(next(it))
        M = int(next(it))
        
        fids = [0] * P
        urg = [0] * P
        for i in range(P):
            fids[i] = int(next(it))
            urg[i] = int(next(it))
            
        init(P, fids, urg)
        out.append('#%d' % tc)
        
        for _ in range(M):
            op = int(next(it))
            if op == 1:
                fid = int(next(it)); u = int(next(it))
                request(fid, u)
            elif op == 2:
                fid = int(next(it)); u = int(next(it))
                renew(fid, u)
            elif op == 3:
                fid = int(next(it))
                cancel(fid)
            elif op == 4:
                out.append(str(clear_landing()))
            else:
                out.append(str(divert()))
                
    print('\n'.join(out))


main()