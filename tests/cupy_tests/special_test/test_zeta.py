import unittest

from cupy import testing
import numpy


@testing.gpu
@testing.with_requires('scipy')
class TestZeta(unittest.TestCase):

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(atol=1e-5, mod='sp', mod_name='special')
    def test_arange(self, xp, dtype, sp):
        a = testing.shaped_arange((2, 3), xp, dtype)
        b = testing.shaped_arange((2, 3), xp, dtype)
        return sp.zeta(a, b)

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(atol=1e-5, rtol=1e-6, mod='sp',
                                 mod_name='special')
    def test_linspace(self, xp, dtype, sp):
        a = numpy.linspace(-30, 30, 1000, dtype=dtype)
        b = numpy.linspace(-30, 30, 1000, dtype=dtype)
        a = xp.asarray(a)
        b = xp.asarray(b)
        return sp.zeta(a, b)

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(atol=1e-2, rtol=1e-3, mod='sp',
                                 mod_name='special')
    def test_scalar(self, xp, dtype, sp):
        return sp.zeta(dtype(2.), dtype(1.5))

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(atol=1e-2, rtol=1e-3, mod='sp',
                                 mod_name='special')
    def test_inf_and_nan(self, xp, dtype, sp):
        x = numpy.array([-numpy.inf, numpy.nan, numpy.inf]).astype(dtype)
        a = numpy.tile(x, 3)
        b = numpy.repeat(x, 3)
        a = xp.asarray(a)
        b = xp.asarray(b)
        return sp.zeta(a, b)
