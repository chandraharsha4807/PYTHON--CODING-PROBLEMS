def hcf(x, y):
      if (x> y):
          smaller = n[1]
      else:
          smaller = x
      for i in range(1, smaller +1):
          if ((x%i == 0) and (y%i == 0)):
              HCF = i
      return HCF



n = list(map(int, input().split(" ")))

HCF = hcf(n[0], n[1])
print(HCF)