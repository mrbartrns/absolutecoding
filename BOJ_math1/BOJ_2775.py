import sys

def solve(level, width):
    sum1 = 1
    sum2 = 1
    num = 0
    flag = True
    lst1 = [1]
    lst2 = [1]
    for i in range(1, width): #맨 처음 호까지의 리스트를 만듬, 0층
        i += 1
        lst1.append(i)
#리스트의 값을 더하고 새로운 리스트에 추가:1층 이상, 홀수층: lst2, 짝수층 : lst1
    else:
        while flag:
            num += 1
            for j in range(1, len(lst1)):
                sum1 += lst1[j]
                lst2.append(sum1)
            lst1 = [1]
            sum1 = 1
            if num == level:
                flag = False
                return lst2[width - 1]
            else:
                num += 1
                for j in range(1, len(lst2)):
                    sum2 += lst2[j]
                    lst1.append(sum2)
                lst2 = [1]
                sum2 = 1
                if num == level:
                    flag = False
                    return lst1[width - 1]


testcase = int(sys.stdin.readline())
for i in range(0, testcase):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(solve(k, n))