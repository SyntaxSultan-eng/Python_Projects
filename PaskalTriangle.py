############## Треугольник паскаля через рекурсию + мемоизацию ######################

def paskal(num,memoize):
    if num == 0:
        return [1]
    if num == 1:
        return [1,1]
    array = []
    if num in memoize:
        return memoize[num]
    else:
        for i in range(num+1):
            if i % num == num or i % num == 0:
                array.append(1)
            else:
                item = paskal(num-1,memoize)[i-1]+paskal(num-1,memoize)[i]
                array.append(item)
        memoize[num] = array
        return array
num = int(input())
memoize = {}
print(paskal(num, memoize))

#####################################################################################
