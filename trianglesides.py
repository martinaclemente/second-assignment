import os
import sys

def is_triangle(x, y, z):
    if x < y+z and y < z+x and z < x+y:
        return True
    else:
        return False

def largestPerimeterTriangle(sides):
    triangle = [-1]
    sides = sorted(sides, reverse=True)
    
    print(sides)
    
    for idx in range(2, len(sides)):
        for jdx in range(1, idx):
            for kdx in range(0, jdx):
                print("checking {} {} {}".format(sides[idx], sides[jdx], sides[kdx]))
                if is_triangle(sides[idx], sides[jdx], sides[kdx]):
                    print("valid")
                    triangle = (sides[idx], sides[jdx], sides[kdx])
                    return triangle
                    
    return triangle
    

if __name__ == '__main__':
    output_file = open(os.environ['OUTPUT_PATH'], 'w')

    total_sides = int(input())

    sides = list(map(int, input().rstrip().split()))

    result = largestPerimeterTriangle(sides)

    output_file.write(' '.join(map(str, result)))
    output_file.write('\n')

    output_file.close()