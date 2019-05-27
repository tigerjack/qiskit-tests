from sympy import *


def get_angles(a, b, c, d):
    s = _compute_angles(a, b, c, d)
    if len(s) != 0:
        print("Not phasing")
        res = _final_contraint(s)
        if len(res) != 0:
            return res
    print("Phasing...")
    matr = Matrix([[a, b], [c, d]])
    # matr[0] = simplify(matr[0])
    print(matr)
    print(f"det = {simplify(matr.det())}")
    matr_phased = matr / _my_sqrt(simplify(matr.det()))
    matr_phased = simplify(matr_phased/ exp(I * arg(matr_phased[0])))
    print(matr_phased)
    s = _compute_angles(matr_phased[0], matr_phased[1], matr_phased[2],
                        matr_phased[3])
    return _final_contraint(s)

def _compute_angles(a, b, c, d):
    return _compute_angles_solve(a, b, c, d)

def _compute_angles_solve(a, b, c, d):
    theta, phi, lamb = symbols('\\theta \\phi \\lambda', real=True)
    a_eq = Eq(cos(theta / 2), a)
    b_eq = Eq(-exp(I * lamb) * sin(theta / 2), b)
    c_eq = Eq(exp(I * phi) * sin(theta / 2), c)
    d_eq = Eq(exp(I * (phi + lamb)) * cos(theta / 2), d)
    return solve([a_eq, b_eq, c_eq, d_eq], [theta, phi, lamb],
                check=False, dict=True)

def _compute_angles_nonlinsolve(a, b, c, d):
    theta, phi, lamb = symbols('\\theta \\phi \\lambda', real=True)
    a_eq = cos(theta / 2)- a
    b_eq = -exp(I * lamb) * sin(theta / 2)- b
    c_eq = exp(I * phi) * sin(theta / 2)- c
    d_eq = exp(I * (phi + lamb)) * cos(theta / 2)- d
    return nonlinsolve([a_eq, b_eq, c_eq, d_eq], [theta, phi, lamb])

def _final_contraint(result):
    print(result)
    print(len(result))
    res = []
    for sol in result:
        print(f"sol={sol}")
        to_add = True
        for k, v in sol.items():
            print(f"k={k}, v={v}")
            if str(k) == '\\theta' and (v < 0 or v > pi):
                to_add = False
                print(f"breaking bcz of theta={v}")
                break
            elif str(k) == '\\phi' and (v < 0 or v >= 2 * pi):
                print(f"breaking bcz of phi={v}")
                to_add = False
                break
        if to_add:
            print("Adding")
            res.append(sol)
    print("Done")
    return simplify(res)


def _my_sqrt(z):
    x, y = symbols('x y', real=True)
    sol = solve((x + I * y)**2 - z, (x, y))
    return sol[0][0] + sol[0][1] * I
