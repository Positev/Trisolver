def tritest(a,b,c):

    for i in [a,b,c]:
        if not ((isinstance(i, int) or isinstance(i, float)) and i > 0 and i <= 1000) :
            return f"{a}, {b}, {c}, Not a triangle\n"

    is_iso = a == b or b == c or a == c
        
    is_eq = a == b and b == c and a == c

    is_sca = a != b and b != c
        
    longest_side = max(a,b,c)    
    others = [a,b,c]
    others.remove(longest_side)
    is_acute  =  longest_side ** 2 < sum([x ** 2 for x in others])
        
    is_obtuse = longest_side ** 2 > sum([x ** 2 for x in others])
        
    is_right = longest_side ** 2 == sum([x ** 2 for x in others])

    if longest_side > sum(others):
        return f"{a}, {b}, {c}, Not a triangle\n"

    tri_type = "Error" 
    if is_eq:
        tri_type = "EQ"
    
    elif is_iso:
        tri_type = "ISO"

    elif is_sca:
        tri_type = "SCA"

    angle_type = "Error" 
    
    if is_right:
        angle_type = "RIGHT"
    
    elif is_obtuse:
        angle_type = "OBTUSE"

    elif is_acute:
        angle_type = "ACUTE"

    return f"{a}, {b}, {c}, {tri_type}-{angle_type}\n"

    
print (tritest(3,4,5))
        
bounds = [1,2,100,199,200]

used_inputs = []

with open("output.csv", 'w') as f:
    lines = []
    for i in bounds:
        for j in bounds:
            for k in bounds:
                if ([i,j,k] not in used_inputs):
                    used_inputs.append([i,j,k])
                    out = tritest(i,j,k)
                    lines.append(out)
                    print(out)
    print(len(lines))
    f.writelines(lines)
