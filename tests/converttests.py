import unittest
from pytocl import func_to_kernel, CLArgInfo, CLArgType

"""Tests for Parameters"""

def one_dim(dim1):
    pass

def two_dim(dim1, dim2):
    pass

def three_dim(dim1, dim2, dim3):
    pass

def array_params(dim1, float_array, int_array):
    pass

def scalar_params(dim1, f, i):
    pass

def output_params(dim1, out_f, out_i):
    pass

class TestParameters(unittest.TestCase):
    def test_one_dim(self):
        kernel = func_to_kernel(one_dim, (1,), [])
        expected_header = "kernel void one_dim()"
        self.assertIn(expected_header, kernel)
        expected_one_dim = "int dim1=get_global_id(0);"
        self.assertIn(expected_one_dim, kernel)

    def test_two_dim(self):
        kernel = func_to_kernel(two_dim, (1,1), [])
        expected_header = "kernel void two_dim()"
        self.assertIn(expected_header, kernel)
        expected_one_dim = "int dim1=get_global_id(0);"
        self.assertIn(expected_one_dim, kernel)
        expected_two_dim = "int dim2=get_global_id(1);"
        self.assertIn(expected_two_dim, kernel)

    def test_three_dim(self):
        kernel = func_to_kernel(three_dim, (1,1,1), [])
        expected_header = "kernel void three_dim()"
        self.assertIn(expected_header, kernel)
        expected_one_dim = "int dim1=get_global_id(0);"
        self.assertIn(expected_one_dim, kernel)
        expected_two_dim = "int dim2=get_global_id(1);"
        self.assertIn(expected_two_dim, kernel)
        expected_two_dim = "int dim3=get_global_id(2);"
        self.assertIn(expected_two_dim, kernel)

    def test_array(self):
        kernel = func_to_kernel(array_params, (1,), [CLArgInfo(CLArgType.float32_array, array_size=100), CLArgInfo(CLArgType.int32_array, array_size=10)])
        expected_header = "kernel void array_params(const global float* float_array,const global int* int_array)"
        self.assertIn(expected_header, kernel)
        expected_one_dim = "int dim1=get_global_id(0);"
        self.assertIn(expected_one_dim, kernel)
        
    def test_scalar(self):
        kernel = func_to_kernel(scalar_params, (1,), [CLArgInfo(CLArgType.float32), CLArgInfo(CLArgType.int32)])
        expected_header = "kernel void scalar_params(const float f,const int i)"
        self.assertIn(expected_header, kernel)
        expected_one_dim = "int dim1=get_global_id(0);"
        self.assertIn(expected_one_dim, kernel)

    def test_output(self):
        kernel = func_to_kernel(output_params, (1,), [CLArgInfo(CLArgType.float32_array, is_output=True, array_size=100),
                                                      CLArgInfo(CLArgType.int32_array, is_output=True, array_size=10)])
        expected_header = "kernel void output_params(global float* out_f,global int* out_i)"
        self.assertIn(expected_header, kernel)
        expected_one_dim = "int dim1=get_global_id(0);"
        self.assertIn(expected_one_dim, kernel)

"""Tests for Literals"""

def num_literal(dim):
    i = 5
    f = 3.4
    f_dec_pre = .4
    f_dec_post = 4.

class TestLiterals(unittest.TestCase):
    def test_num(self):
        kernel = func_to_kernel(num_literal, (1,), [])
        expected_int = "i=5"
        self.assertIn(expected_int, kernel)
        expected_float = "f=3.4f"
        self.assertIn(expected_float, kernel)
        expected_float_dec_pre = "f_dec_pre=0.4f"
        self.assertIn(expected_float_dec_pre, kernel)
        expected_float_dec_post = "f_dec_post=4.0f"
        self.assertIn(expected_float_dec_post, kernel)

"""Tests for For loops"""

def for_loop_one_arg(dim):
    for i in range(10):
        pass

def for_loop_two_arg(dim):
    for i in range(10, 20):
        pass

def for_loop_three_arg(dim):
    for i in range(10, 20, 2):
        pass

class TestForLoop(unittest.TestCase):
    def test_one_arg(self):
        kernel = func_to_kernel(for_loop_one_arg, (1,), [])
        expected_for = "for(int i=0;i<10;i++)"
        self.assertIn(expected_for, kernel)

    def test_two_arg(self):
        kernel = func_to_kernel(for_loop_two_arg, (1,), [])
        expected_for = "for(int i=10;i<20;i++)"
        self.assertIn(expected_for, kernel)

    def test_three_arg(self):
        kernel = func_to_kernel(for_loop_three_arg, (1,), [])
        expected_for = "for(int i=10;i<20;i+=2)"
        self.assertIn(expected_for, kernel)

"""Tests for While loops"""

def while_loop(dim):
    while True:
        pass

class TestWhileLoop(unittest.TestCase):
    def test_while_loop(self):
        kernel = func_to_kernel(while_loop, (1,), [])
        expected_while = "while(true)"
        self.assertIn(expected_while, kernel)

"""Tests for If statements"""

def if_statement(dim):
    if True:
        pass

def if_else_statement(dim):
    if True:
        pass
    else:
        pass

def if_comparison(dim):
    if dim > 4:
        pass

class TestIfStatement(unittest.TestCase):
    def test_if_statement(self):
        kernel = func_to_kernel(if_statement, (1,), [])
        expected_if = "if(true)"
        self.assertIn(expected_if, kernel)

    def test_if_else_statement(self):
        kernel = func_to_kernel(if_else_statement, (1,), [])
        expected_if = "if(true)"
        self.assertIn(expected_if, kernel)
        expected_else = "else"
        self.assertIn(expected_else, kernel)

    def test_if_comparison(self):
        kernel = func_to_kernel(if_comparison, (1,), [])
        expected_if = "if((dim>4))"
        self.assertIn(expected_if, kernel)

if __name__ == "__main__":
    unittest.main()