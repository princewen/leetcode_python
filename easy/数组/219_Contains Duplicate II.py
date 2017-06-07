"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
只要有一组相同的数，他们的下表之差小于等于k，就返回True，题目理解有误，不过仍然使用字典保存结果

"""