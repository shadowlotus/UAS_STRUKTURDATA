#Pendekatan rekursif
def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        return -1

arr = input("Masukkan elemen array (dipisahkan dengan spasi): ").split()
arr = [int(num) for num in arr]
x = int(input("Masukkan angka yang ingin dicari: "))

result = binary_search_recursive(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Elemen ditemukan pada indeks ke-", str(result))
else:
    print("Elemen tidak ditemukan")