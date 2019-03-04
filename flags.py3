from bisect import bisect_left
def solution(A):
    # Initialize a list to store peak indices
    peaks = []
    i = 1
    while i < len(A) - 1:
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)
            # if A[i] is peak, next can be A[i+2]
            i += 2
        else:
            i += 1
    peak_count = len(peaks)
    if peak_count == 0:
        # No peaks, no flags
        return 0
    ans = 0
    for i in range(peak_count, 0, -1):
        flag_count, cur_peak, c = 1, peaks[0], 0
        while True:
            # Go to the next possible peak
            c = bisect_left(peaks, cur_peak + i)
            # If reached end, end loop, look for next size
            if c == peak_count or flag_count == i:
                break
            else:
                cur_peak = peaks[c]
                flag_count += 1
        # Max flag_count is the answer
        ans = max(ans, flag_count)
    return ans
