# Read input as specified in the question.
# Print output as specified in the question.
# Staircase

# A child is running up a staircase with N steps, and can hop either 1
# step, 2 steps or 3 steps at a time. Implement a method to count how
# many possible ways the child can run up to the stairs. You need to
# return number of possible ways W.


def stair(n):                      
    w = 0                          
    #d = do aur t = teen               
    for d in range(int(1+n/2)):    
        for t in range(int(1+n/3)):
            if 2*d + 3*t == n:     
                w += 1             
    return w                       


n = int(input())
print(stair(n))
