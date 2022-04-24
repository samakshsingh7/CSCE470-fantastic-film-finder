nums = [1,3]
num = {1:3}
def printer():
    prettyNums = ""
    for i in range(len(nums)):
        prettyNums += (str(nums[i])+"\n")
    return prettyNums