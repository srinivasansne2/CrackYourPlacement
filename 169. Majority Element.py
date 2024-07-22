import sys
with open("user.out",'w') as f:
    for line in sys.stdin:
        l = sorted(map(int, line.rstrip()[1:-1].split(',')))
        f.write(str(l[len(l)//2])+'\n')
exit(0)