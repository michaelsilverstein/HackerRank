#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(raw_input())
    a = map(int, raw_input().split())
    
    #max 
    m = None
    r = None 
    for i in range(n):
        if i == 0: #initially
            m = a[i]
        #Is it bigger than max
        if a[i] > m:
        #Assign the runner up
            r = m 
        #Reassign the max
            m = a[i]
        #Is it bigger than the max
        if m > a[i] > r: 
            r = a[i]
print r            

