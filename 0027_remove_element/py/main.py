import time 


def remove_element(nums, val) -> int: 
    currentIndex = 0
    length = len(nums)
    for index in range(0, length):
        if nums[index] != val:
            nums[currentIndex] = nums[index]
            currentIndex += 1
    return currentIndex

def main():
    t0 = time.time_ns()
    nums = [3,2,2,3]
    results = remove_element(nums, 3)
    print(nums)
    print(results)
    t1 = time.time_ns()
    timeslot = (t1 - t0) / 1000000000
    print(timeslot, "s")
    nums = [0,1,2,2,3,0,4,2]
    results = remove_element(nums, 2)
    print(nums)
    print(results)

main()