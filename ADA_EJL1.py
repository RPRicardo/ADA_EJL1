def remover_duplicados(nums):
    if not nums:
        return 0

    # Índice para el próximo elemento único
    k = 1
    
    # Recorre el arreglo y reemplaza duplicados
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

# Ejemplo de uso
nums = [1, 1, 2, 3, 4, 4, 5, 5, 5,6,7,9,9]
k = remover_duplicados(nums)
print("k =", k)  # Output: 2
print("nums =", nums[:k])  # Output: [1, 2]
