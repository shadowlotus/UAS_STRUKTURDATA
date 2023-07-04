def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr

    tengah = len(arr) // 2
    kiri_setengah = arr[:tengah]
    kanan_setengah = arr[tengah:]

    kiri_setengah = merge_sort_descending(kiri_setengah)
    kanan_setengah = merge_sort_descending(kanan_setengah)

    return merge_descending(kiri_setengah, kanan_setengah)


def merge_descending(kiri, kanan):
    merged = []
    i = j = 0

    while i < len(kiri) and j < len(kanan):
        if kiri[i] >= kanan[j]:
            merged.append(kiri[i])
            i += 1
        else:
            merged.append(kanan[j])
            j += 1

    while i < len(kiri):
        merged.append(kiri[i])
        i += 1

    while j < len(kanan):
        merged.append(kanan[j])
        j += 1

    return merged
data = input("Masukkan data (pisahkan dengan spasi): ").split()
data = [int(x) for x in data]

sorted_data = merge_sort_descending(data)

print("Data setelah diurutkan: ", sorted_data)
