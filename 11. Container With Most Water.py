
def maxArea(height: List[int]) -> int:
    # starting max
    m = 0
    # two pointers
    i = 0
    j = len(height)-1
    # max height
    mh = max(height)
    while i < j:
        # set the area to the min height * the distance between the two col
        area = min(height[i], height[j]) * (j-i)

        # update max if necessary
        m = max(m, area)


        if mh * (j - i) <= m:
            break

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return m

f = open('user.out', 'w')
for case in map(loads, stdin):
    f.write(f"{maxArea(case)}\n")
f.flush()
exit(0)