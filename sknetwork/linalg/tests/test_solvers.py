#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tests for randomized matrix factorization"""

import unittest
import numpy as np
from sknetwork.linalg import LanczosEig, HalkoEig, SparseLR
from sknetwork.toy_graphs import house_graph


class TestSolvers(unittest.TestCase):

    def setUp(self):
        self.adjacency = house_graph()
        n, m = self.adjacency.shape
        self.slr = SparseLR(self.adjacency, [(np.ones(n), np.ones(m))])

    def test_lanczos(self):
        solver = LanczosEig('LM')
        solver.fit(self.adjacency, 2)
        self.assertEqual(len(solver.eigenvalues_), 2)

        solver.fit(self.slr, 2)
        self.assertEqual(len(solver.eigenvalues_), 2)

        solver = LanczosEig('SM')
        solver.fit(self.adjacency, 2)
        self.assertEqual(len(solver.eigenvalues_), 2)

    def test_halko(self):
        solver = HalkoEig('LM')
        solver.fit(self.adjacency, 2)
        self.assertEqual(len(solver.eigenvalues_), 2)

        solver.fit(self.slr, 2)
        self.assertEqual(len(solver.eigenvalues_), 2)

        solver = HalkoEig('SM')
        solver.fit(self.adjacency, 2)
        self.assertEqual(len(solver.eigenvalues_), 2)
