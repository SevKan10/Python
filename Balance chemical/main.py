from sympy import symbols, Eq, solve

def balance_chemical_equation(equation):
    # Tạo các biến ký hiệu cho các nguyên tố và hệ số
    elements = symbols(' '.join(set(''.join(filter(str.isalpha, equation)))))
    coefficients = symbols(' '.join([f'a{i}' for i in range(1, len(elements) + 1)]))

    # Tách phương trình thành các thành phần bên trái và bên phải
    reactants, products = equation.split('->')

    # Tạo các phương trình cho sự cân bằng của mỗi nguyên tố
    balance_equations = []
    for element in elements:
        reactant_count = reactants.count(element)
        product_count = products.count(element)
        balance_equations.append(Eq(reactant_count, product_count))

    # Giải các phương trình để tìm các hệ số
    solution = solve(balance_equations, coefficients)

    # In ra phương trình đã cân bằng
    balanced_equation = equation
    for coeff, element in zip(solution.values(), elements):
        balanced_equation = balanced_equation.replace(element, str(coeff))

    print("Phương trình đã cân bằng:")
    print(balanced_equation)

# Sử dụng chương trình
chemical_equation = input("Nhập phương trình hóa học: ")
balance_chemical_equation(chemical_equation)
