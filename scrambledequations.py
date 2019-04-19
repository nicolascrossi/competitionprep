eqns = [
    '12:4 3 9 * /',
    '14:8 122 - 17 *',
    '2133:+ + 5 6 7 20',
    '1:* 7 7 1 /',
]

def check(nums, ops):
    #print(nums)
    #print(ops)
    if len(ops) == 0:
        return True
    output = []
    if '*' in ops or '/' in ops:
        if '*' in ops:
            for i in range(0, len(nums)-1):
                for j in range(i+1, len(nums)):
                    tempN = nums.copy()
                    tempO = ops.copy()
                    tempN.remove(nums[i])
                    tempN.remove(nums[j])
                    tempO.remove('*')
                    tempN.append(nums[i] * nums[j])
                    
                    ret = check(tempN, tempO)
                    if ret == True:
                        output.append(nums[i] * nums[j])
                    elif len(ret) > 1:
                        output.extend(ret)
                    else:
                        output.append(ret)
        if '/' in ops:
            for i in range(0, len(nums)-1):
                for j in range(i+1, len(nums)):
                    tempN = nums.copy()
                    tempO = ops.copy()
                    tempN.remove(nums[i])
                    tempN.remove(nums[j])
                    tempO.remove('/')
                    tempN.append(nums[i] / nums[j])
                    
                    ret = check(tempN, tempO)
                    #print("ret", ret)
                    if ret == True:
                        #print(nums[i] / nums[j])
                        output.append(nums[i] / nums[j])
                        #print('test output', output)
                    elif len(ret) > 1:
                        output.extend(ret)
                    else:
                        output.append(ret)

                    tempN.remove(nums[i] / nums[j])

                    tempN.append(nums[j] / nums[i])
                    ret = check(tempN, tempO)
                    if ret == True:
                        output.append(nums[j] / nums[i])
                    elif len(ret) > 1:
                        output.extend(ret)
                    else:
                        output.append(ret)
    else:
        if '+' in ops:
            for i in range(0, len(nums)-1):
                for j in range(i+1, len(nums)):
                    tempN = nums.copy()
                    tempO = ops.copy()
                    tempN.remove(nums[i])
                    tempN.remove(nums[j])
                    tempO.remove('+')
                    tempN.append(nums[i] * nums[j])
                    
                    ret = check(tempN, tempO)
                    if ret == True:
                        output.append(nums[i] + nums[j])
                    elif len(ret) > 1:
                        output.extend(ret)
                    else:
                        output.append(ret)
        if '-' in ops:
            for i in range(0, len(nums)-1):
                for j in range(i+1, len(nums)):
                    tempN = nums.copy()
                    tempO = ops.copy()
                    tempN.remove(nums[i])
                    tempN.remove(nums[j])
                    tempO.remove('-')
                    tempN.append(nums[i] - nums[j])
                    
                    ret = check(tempN, tempO)
                    if ret == True:
                        output.append(nums[i] - nums[j])
                    elif len(ret) > 1:
                        output.extend(ret)
                    else:
                        output.append(ret)

                    tempN.remove(nums[i] - nums[j])

                    tempN.append(nums[j] - nums[i])

                    ret = check(tempN, tempO)
                    if ret == True:
                        output.append(nums[j] - nums[i])
                    elif len(ret) > 1:
                        output.extend(ret)
                    else:
                        output.append(ret)
    #print('Output', output)
    return output

for eqn in eqns:
    data = eqn.split(':')
    sum = data[0]
    data = data[1].split(' ')
    nums = []
    ops = []
    for i in data:
        try:
            nums.append(int(i))
        except:
            ops.append(i)
    if not len(nums) - 1 == len(ops):
        print('FALSE')
    else:
        output = check(nums, ops)
        equal = False
        #print(output)
        for i in output:
            if type(i) == type(1) and int(i) == int(sum):
                equal = True
                print("TRUE")
                break
        if not equal:
            print("FALSE")