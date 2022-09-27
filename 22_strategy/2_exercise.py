from abc import ABC
import cmath
import math
from unittest import TestCase


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b*b - 4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        result = b*b - 4*a*c
        return result if result >= 0 else float('nan')


class QuadraticEquationSolver:
    def __init__(self, strategy=OrdinaryDiscriminantStrategy()) -> None:
        self.strategy = strategy

    def solve(self, a, b, c):
        disc = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        root_disc = cmath.sqrt(disc)
        return (
            (-b+root_disc)/(2*a),
            (-b-root_disc)/(2*a)
        )


if __name__ == '__main__':
    strategy = OrdinaryDiscriminantStrategy()
    solver = QuadraticEquationSolver(strategy)
    res = solver.solve(1, 10, 16)
    print(res)
    res = solver.solve(1, 4, 5)
    print(res)

    another_strategy = RealDiscriminantStrategy()
    solver = QuadraticEquationSolver(another_strategy)
    res = solver.solve(1, 10, 16)
    print(res)
    res = solver.solve(1, 4, 5)
    print(res)


class Evaluate(TestCase):
    def test_positive_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        res = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), res[0])
        self.assertEqual(complex(-8, 0), res[1])

    def test_positive_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        res = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), res[0])
        self.assertEqual(complex(-8, 0), res[1])

    def test_negative_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        res = solver.solve(1, 4, 5)
        self.assertEqual(complex(-2, 1), res[0])
        self.assertEqual(complex(-2, -1), res[1])

    def test_negative_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        res = solver.solve(1, 4, 5)
        self.assertTrue(math.isnan(res[0].real))
        self.assertTrue(math.isnan(res[1].real))
        self.assertTrue(math.isnan(res[0].imag))
        self.assertTrue(math.isnan(res[1].imag))
