<h1 style="color:#FFFFFF;"> 1. Two Sum </h1>
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

<blockquote>
<h3 style="color: orange;">Example 1:</h3>
<p><strong>Input:</strong> nums = [2,7,11,15], target = 9 <br>
<strong>Output:</strong> [0,1] <br>
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].</p>
</blockquote>

<blockquote>
<h3 style="color: orange;">Example 2:</h3>
<p><strong>Input:</strong> nums = [3,2,4], target = 6 <br>
<strong>Output:</strong> [1,2]</p>
</blockquote>

<blockquote>
<h3 style="color: orange;">Example 3:</h3>
<p><strong>Input:</strong> nums = [3,3], target = 6 <br>
<strong>Output:</strong> [0,1]</p>
</blockquote>

**Constraints:**

- 2 <= nums.length <= 10<sup>4</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup> 
- -10<sup>9</sup> <= target <= 10<sup>9</sup>
- **Only one valid answer exists.**
 

**Follow-up:** Can you come up with an algorithm that is less than O(n<sup>2</sup>) time complexity?