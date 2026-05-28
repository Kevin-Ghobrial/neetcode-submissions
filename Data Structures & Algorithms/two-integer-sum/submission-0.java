class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int j = nums.length - 1; j > 0; j--){
            for(int i = 0; i < j; i++){
                if(nums[i] + nums[j] == target){
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{0};
    }
}
