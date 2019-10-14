def array123(nums):
  for n in range(0,len(nums)-2):
    if nums[n] == 1 and nums[n+1] == 2 and nums[n+2] == 3:
      return True
  return False
