from sympy import *


# \begin{bmatrix} a & c \\ b & d \end{bmatrix}
def get_angles(a, b, c, d):
    theta, phi, lamb = symbols('\\theta \\phi \\lambda', real=True)
    a_eq = Eq(cos(theta / 2), a)
    b_eq = Eq(exp(I * phi) * sin(theta / 2), b)
    c_eq = Eq(-exp(I * lamb) * sin(theta / 2), c)
    d_eq = Eq(exp(I * (phi + lamb)) * cos(theta / 2), d)
    # a_eq = Eq(exp(-I * (phi + lamb) / 2) * cos(theta / 2), a)
    # b_eq = Eq(exp(I * (phi - lamb) / 2) * sin(theta / 2), b)
    # c_eq = Eq(-exp(-I * (phi - lamb) / 2) * sin(theta / 2), c)
    # d_eq = Eq(exp(I * (phi + lamb) / 2) * cos(theta / 2), d)
    theta_constr1 = Eq(theta >= 0)
    theta_constr2 = Eq(theta <= pi)
    phi_constr1 = Eq(phi >= 0)
    phi_constr2 = Eq(phi < 2 * pi)
    res = solve(
        [
            a_eq,
            b_eq,
            c_eq,
            d_eq,
            # theta_constr1,
            # theta_constr2,
            # phi_constr1,
            # phi_constr2,
        ],
        # res = solve(
        #     [a_eq, b_eq, c_eq, d_eq],
        [theta, phi, lamb],
        check=False,
        # Sometimes set is better than dict for multiple solutions
        # set=True,
        domain='real',
        dict=True,
    )
    return res
