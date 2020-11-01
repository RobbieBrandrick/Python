def permutation(str, prefix):
  if len(str) == 0:
    return prefix
  else:
    for i in range(0, len(str) - 1):
        rem = str[0 : i] + str[i + 1]
        print(rem)
        permutation(rem, prefix + str[i:1])

permutation("abc", "")