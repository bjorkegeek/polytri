from tests import *
from tests.helpers import *

from polytri import triangulate
import numpy as np

class TestTriangulate(unittest.TestCase):
    big_poly = [(525, 2808),
                (1212, 2990),
                (2505, 2384),
                (2869, 2363),
                (3717, 646),
                (2707, 0),
                (2586, 1091),
                (2909, 666),
                (3111, 585),
                (3151, 1131),
                (2566, 1717),
                (1374, 1495),
                (1071, 2343),
                (222, 80),
                (182, 1212),
                (0, 2464),
                (525, 3879),
                (1656, 3232),
                (687, 3313)]

    def test_basic_2d_box(self):
        poly = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tris = list(triangulate(poly))
        self.assertEqual(check_equality_issues(poly, tris), [])

    def test_convex_pentagon(self):
        poly = [(0, 0), (1, 0), (1, 1), (0.5, 1.5), (0, 1)]
        tris = list(triangulate(poly))
        self.assertEqual(check_equality_issues(poly, tris), [])

    def test_non_convex_pentagon(self):
        poly = [(0, 0), (1, 0), (1, 1), (0.5, 0.5), (0, 1)]
        tris = list(triangulate(poly))
        self.assertEqual(check_equality_issues(poly, tris), [])

    def test_big(self):
        poly = self.big_poly
        tris = list(triangulate(poly))
        self.assertEqual(check_equality_issues(poly, tris), [])

    def test_basic_3d_box(self):
        poly = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        poly2d = [(x,y) for x,y,_ in poly]
        tris = list(triangulate(poly))
        tris2d = [[(x,y) for x,y,_ in coords] for coords in tris]
        self.assertEqual(check_equality_issues(poly2d, tris2d), [])

    def test_3d_non_convex_pentagon(self):
        poly = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0.5, 0.5, 0), (0, 1, 0)]
        poly2d = [(x,y) for x,y,_ in poly]
        tris = list(triangulate(poly))
        tris2d = [[(x,y) for x,y,_ in coords] for coords in tris]
        self.assertEqual(check_equality_issues(poly2d, tris2d), [])

    def test_big_3d(self):
        for s, t, offs in [
            ([1, 0, 0], [0, 1, 0], [0, 0, 0]),
            ([1, 0, 0], [0, 1, 0], [5, 2, 1]),   # xposed
            ([1, 0, 0], [0, 1, 0], [-2, 5, 2]),  # other octant
            ([0, 1, 0], [1, 0, 0], [1,1, 1]),    # flipped axis
            ([1, 1, 1], [3, -7, 8], [90, -180, 4]),  # All weird
        ]:
            stack = [s, t]
            to_3d = np.vstack(stack).transpose()
            stack.append(np.cross(s, t))
            to_2d = np.linalg.inv(np.vstack(stack).transpose())[:2]

            poly_3d = [np.dot(to_3d, p) + offs for p in self.big_poly]
            tris_3d = list(triangulate(poly_3d))
            tris_2d = [[np.dot(to_2d, p - np.array(offs)) for p in tri]
                       for tri in tris_3d]
            self.assertEqual(check_equality_issues(self.big_poly, tris_2d), [])

    def test_bad_case(self):
        poly = [[-14, -5, 0.],
                [-11, 9, 0.],
                [-11, 9, 0.],
                [14, 5, 0.],
                [11, -9, 0.],
                [-14, -5, 0.]]
        poly2d = [(x, y) for x, y, _ in poly]
        tris = list(triangulate(poly))
        tris2d = [[(x, y) for x, y, _ in coords] for coords in tris]
        self.assertEqual(check_equality_issues(poly2d, tris2d), [])

    def test_issue_1(self):
        poly = [
            [1.0000, -0.5000, 1.0000],
            [0.7500, -0.4330, 1.0000],
            [0.5670, -0.2500, 1.0000],
            [0.5000, 0.0000, 1.0000],
            [0.5670, 0.2500, 1.0000],
            [0.7500, 0.4330, 1.0000],
            [1.0000, 0.5000, 1.0000],
            [1.0000, 1.0000, 1.0000],
            [-1.0000, 1.0000, 1.0000],
            [-1.0000, -1.0000, 1.0000],
            [1.0000, -1.0000, 1.0000]]
        tris = list(triangulate(poly))

        poly2d = [(x, y) for x, y, _ in poly]
        tris2d = [[(x, y) for x, y, _ in coords] for coords in tris]
        self.assertEqual(check_equality_issues(poly2d, tris2d), [])
