public class Solution {
    public bool hasDuplicate(int[] nums) {
        //HashSet only contains unique values
        return new HashSet<int>(nums).Count < nums.Length;
    }
}