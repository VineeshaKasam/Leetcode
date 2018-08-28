/**
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {

        if(nums.length < 2)
            return null;

        int[] res = new int[2];
        Map<Integer,Integer> mp = new HashMap<Integer, Integer>();

        for(int i=0; i< nums.length; i++)
        {
            Integer diff = (Integer) (target - nums[i]);
            if(mp.containsKey(diff))
            {
                res[0] = mp.get(diff);
                res[1] = i;
                return res;
            }
            else
            {
                mp.put(nums[i], i);
            }

        }
        return null;

    }
}