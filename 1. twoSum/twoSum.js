/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    //判斷每陣列中一個元素是否比target小
    let result = Array();
    for(let i = 0; i<nums.length; i++){
        result = [];
        let match = -1;
        let remain = target - nums[i];
        for(let j = i+1; j < nums.length; j++){
            if(remain - nums[j] == 0){
                match = j
                break
            }
        }
        if( match != -1 ){
            result.push(i)
            result.push(match)
            break
        }
    }
    
    return result
};


let nums = [2, 7, 11, 13];
let target = 9;

var result = twoSum( nums, target );
console.log(result)