from numpy.distutils.core import Extension

ext1 = Extension(name = 'fishpack.blktri',
                 sources = ['src/fishpack/blktri.f', 'src/fishpack/blktri.pyf', 'src/fishpack/comf.f'],
                 extra_f77_compile_args = ['-fPIC',
                                           '-std=legacy',
                                           '-freal-4-real-8',
                                           '-fdefault-real-8'],
                 )

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(name = 'fishpack',
          description = "pip-compatible FISHPACK",
          ext_modules = [ext1],
          version = '0.0.1'
          )