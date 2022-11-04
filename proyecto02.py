def get_values(a1: float, a2: float, a3: float, c: float):
    return {'a1':a1,'a2':a2,'a3':a3,'c':c}


def solve(row1: dict, row2: dict, row3: dict):
    a11 = float(row1.get('a1'))
    a12 = float(row1.get('a2'))
    a13 = float(row1.get('a3'))
    
    a21 = float(row2.get('a1'))
    a22 = float(row2.get('a2'))
    a23 = float(row2.get('a3'))

    a31 = float(row3.get('a1'))
    a32 = float(row3.get('a2'))
    a33 = float(row3.get('a3'))

    c1 = float(row1.get('c'))
    c2 = float(row2.get('c'))
    c3 = float(row3.get('c'))

    det = a11*((a22*a33)-(a32*a23)) - a12*((a21*a33)-(a31*a23)) + a13*((a21*a32)-(a31*a22))
    det_x = c1*((a22*a33)-(a32*a23)) - a12*((c2*a33)-(c3*a23)) + a13*((c2*a32)-(c3*a22))
    det_y = a11*((c2*a33)-(c3*a23)) - c1*((a21*a33)-(a31*a23)) + a13*((a21*c3)-(a31*c2))
    det_z = a11*((a22*c3)-(a32*c2)) - a12*((a21*c3)-(a31*c2)) + c1*((a21*a32)-(a31*a22))

    if det != 0:
        x = det_x/det
        y = det_y/det
        z = det_z/det

        print(f'\nx = {x}, y = {y}, z = {z}\n')

    else:
        print('No solution')


def main():
    row1 = get_values(2, 1, -3, 7)
    row2 = get_values(5, -4, 1, -19)
    row3 = get_values(1, -1, -4, 4)

    solve(row1, row2, row3)


if __name__ == '__main__':
    main()
