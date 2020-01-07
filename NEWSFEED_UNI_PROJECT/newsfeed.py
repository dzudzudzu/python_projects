#!/usr/bin/env python3
import datetime


class Posting():

    def __init__(self, content, timestamp):
        self._content = content
        self._timestamp = timestamp

    @property
    def content(self):
        return self._content

    @property
    def timestamp(self):
        return self._timestamp


def compare_timestep(a, b):
    return a.timestamp > b.timestamp


def create_newsfeed(P, N):
    # TODO begin
    # Implement your algorithm here. If you use functions, please define them within this function. You are
    # not allowed to use sort, sorted ....
    S = []
    def partition(L, start, end):
        follower = leader = start
        while leader < end:
            if (compare_timestep(L[leader],L[end])):
                L[follower], L[leader] = L[leader], L[follower]
                follower += 1
            leader += 1
        L[follower], L[end] = L[end], L[follower]
        return follower

    def _quicksort(L, start, end):
        if start >= end:
            return
        p = partition(L, start, end)
        _quicksort(L, start, p - 1)
        _quicksort(L, p + 1, end)

    def quicksort(L):
        _quicksort(L, 0, len(L) - 1)
    for i in range (0, len(P)):
         for k in range(0,len(P[i])):
            S.append(P[i][k])
    quicksort(S)
    while N < len(S):
        del S[N]
    # TODO end
    return S



if __name__ == '__main__':

    # This is just an example. Your algorithm will be tested with different data.
    now = datetime.datetime.now()

    P = [[], []]
    P[0].append(Posting("Post a", now))
    P[0].append(Posting("Post b", now - datetime.timedelta(hours=5)))
    P[0].append(Posting("Post c", now - datetime.timedelta(hours=6)))

    P[1].append(Posting("Post d", now - datetime.timedelta(hours=1)))
    P[1].append(Posting("Post e", now - datetime.timedelta(hours=4)))
    P[1].append(Posting("Post f", now - datetime.timedelta(hours=7)))

    for j in range(len(P)):
        print("Follower %i" % (j + 1))
        for i in range(len(P[j])):
            print(" ", P[j][i].content, P[j][i].timestamp)

    N = 3
    S = create_newsfeed(P, N)
    print("Newsfeed")
    for s in S:
        print(" ", s.content, s.timestamp)
