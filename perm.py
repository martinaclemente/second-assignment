def generate_permutations(arr, start, end, result):
    if start == end:
        result.append(arr[:])
    else:
        for i in range(start, end + 1):
            arr[start], arr[i] = arr[i], arr[start]
            generate_permutations(arr, start + 1, end, result)
            arr[start], arr[i] = arr[i], arr[start]

def main(n):
    nums = list(range(1, n + 1))
    result = []
    generate_permutations(nums, 0, n - 1, result)
    result.sort()

    output = f"{len(result)}\n"
    for perm in result:
        output += " ".join(map(str, perm)) + "\n"
    return output 

output = main(3)
print(output)

# also this program was done with colab and i couldnt copy the LARGE output 
# without creating a txt file since the terminal wasn't showing me enough characters


#with open('/content/permutations_output.txt', 'w') as f:
#    f.write(output)

#large input command above, remove the #