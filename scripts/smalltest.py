# Test for small machines
#   Skip java and clang
import util
import os
import config

def smalltest(b="unstable"):
    # Build debug and release modes
    for d in [True, False]:
        util.buildz3(branch=b, everything=False, clean=True, debug=d,  java=False, static=False, jobs=config.NUMJOBS, clang=False)
        util.testz3py(branch=b, debug=b, clang=False)
        util.test_benchmarks_using_latest('regressions/smt2', branch=b, debug=b, clang=False)

if __name__ == "__main__":
    smalltest()
