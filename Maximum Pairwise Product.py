# N = int(raw_input())
# arr = map(int,list(raw_input().split()))

arr = [1, 23, 1, 3, 2, 4, 6, 7, 5, 3, 3, 5, 2, 3, 9, 7, 5, 4]
output_arr = []
for i in range(0, len(arr) - 1):
    output_arr.append(arr[i] * arr[i + 1])

print sorted(output_arr)[-1:][0]

output_arr = []
curr_max = 0
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        print arr[i],arr[j]
        if (arr[i] * arr[j])>curr_max:
            curr_max = arr[i] * arr[j]

print curr_max

print sorted(arr)[-2::]

a  = b =0
for i in arr:
    if i>a:
        a = i
for i in arr:
    if i>b and i!=a:
        b=i

print a*b


# print hashmp
# curr_max = 0
# for i in arr:
#     if hashmp
