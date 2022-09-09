class MyModule:
    def sum(a, b): 
        return a+b

    def bmi(w, h):  
        return float(w)/(float(h)/100)**2

    def bmi_2(w, h):
        return w/(h/100)**2
    
if __name__ == "__main__":
    two_sum = MyModule.sum(1.5,2.5)
    print(two_sum) # 4.0
    
    bmi = MyModule.bmi("70",173)
    print(bmi) # 23.38868655818771

    # bmi_2 = MyModule.bmi_2("70",173) #會引發錯誤
    # print(bmi_2) # 23.38868655818771