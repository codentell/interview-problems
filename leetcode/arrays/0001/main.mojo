from collections import Dict
from collections import List

fn two_sum_v1(nums: List[Int], target: Int) raises -> List[Int]:
    var indices = List[Int]()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if target - nums[i] == nums[j]: 
                indices.append(i)
                indices.append(j)
                return indices
    return indices

fn two_sum_v2(nums: List[Int], target: Int) raises -> List[Int]:
    var dictionary = Dict[Int, Int]()
    var complement : Int
    var indices = List[Int]()
    for i in range(len(nums)):
        dictionary[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dictionary and dictionary[complement] != i:
            indices.append(i)
            indices.append(dictionary[complement])
            return indices
    return indices


fn main() raises:
    var nums = List[Int](1,2,3)
    var target = 5
    var result1 = two_sum_v1(nums,target)
    print(result1.__str__())
    var result2 = two_sum_v2(nums,target)
    print(result2.__str__())