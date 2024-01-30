pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
    let mut pointer = 0;
    for i in 0..nums.len(){
        if nums[i] != val {
            nums[pointer] = nums[i];
            pointer += 1;
        }
        println!("{:?}", nums);
       
    }
   
    pointer as i32
}



fn main() {
    // testcase 1 
    let mut nums = vec![3,2,2,3];
    let val = 3;
    let result = remove_element(&mut nums, val);
    assert_eq!(result, 2);
    println!("{}", result);
    // testcase 2 
    let mut nums = vec![0,1,2,2,3,0,4,2];
    let val = 2;
    let result = remove_element(&mut nums, val);
    assert_eq!(result, 5);
    println!("{}", result);
    
}