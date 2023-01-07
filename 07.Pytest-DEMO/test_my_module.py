# test_module.py
from my_module import MyModule

def test_sum():
    assert MyModule.sum(1.5,3.5) == 5.0

def test_bmi():
    assert MyModule.bmi("70",173) == 23.38868655818771

# # 會引發錯誤的demo
# def test_bmi_2():
#     assert MyModule.bmi_2("70",173) == 23.38868655818771
