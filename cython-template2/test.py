import gpuadder
import numpy as np
import numpy.testing as npt
import gpuadder

def test_Double():
    arr = np.array([1.,2.,2.,2.], dtype=np.float64)
    adder = gpuadder.GPUAdder_Double(arr)
    adder.increment()
    
    adder.retreive_inplace()
    results2 = adder.retreive()

    npt.assert_array_equal(arr, [2.,3.,3.,3.])
    npt.assert_array_equal(results2, [2.,3.,3.,3.])

def test_Int():
    arr = np.array([1,2,2,2], dtype=np.int32)
    adder = gpuadder.GPUAdder_Int(arr)
    adder.increment()
    
    adder.retreive_inplace()
    results2 = adder.retreive()

    npt.assert_array_equal(arr, [2,3,3,3])
    npt.assert_array_equal(results2, [2,3,3,3])
    
