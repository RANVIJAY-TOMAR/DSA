class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> bag = new HashSet<>();

        for (int i = 0 ; i < nums.length ; i++){
            if (bag.contains(nums[i])){
                return true ;
            }
            bag.add(nums[i]);
        }
        return false ;
    }
}
