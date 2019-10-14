def close_far(a, b, c):
  if (abs(a-b) <= 1 and (abs(b-c) >= 2 and abs(a-c) >= 2)) or ((abs(a-b) >= 2 and abs(b-c) >= 2) and abs(a-c) <= 1):
    return True
  else:
    return False
