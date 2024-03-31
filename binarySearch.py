import time
def line(arr,tr):
    i =0
    while i < len(arr):
        if arr[i] == tr:
            return "found"
        i += 1  # Increment the loop counter
    return "Not Found"



def search(arr,tr):
    low= 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==tr:
            return "found"
        elif tr>arr[mid]:
            low = mid+1
        else :
            high = mid

    return "Not Found"





arr= [2,3,4,6,7,9,11,12]
tar = 2
start_time = time.time()* 1000
print(start_time)
res = line(arr,tar)
end_time = time.time()* 1000
print(res)
print(end_time-start_time)

st_time = time.time() * 1000
result = search(arr,tar)
en_time = time.time()* 1000
print(en_time-st_time)
print(result)
