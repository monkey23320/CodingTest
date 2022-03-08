hr, mn = input().split()
mn = int(mn)
hr = int(hr)
if(mn < 45):
    hr = hr - 1
    mn = 60 + (mn-45)
    if(hr < 0):
        hr = 23
else:
    mn = mn - 45
print(hr, mn)