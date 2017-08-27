from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt

class pds_charm:
    def __init__(self):
        pass

    def init_data(self):
        data = []
        self.len = 10
        for i in range(0,self.len):
            data.append({"A":i - 5, "B":10-i - 5, "C":i*2 - 5, "D":i/3 - 5})
        self.df = DataFrame(data, columns=["A","B","C","D"])

    def draw_plt(self):
        len = self.len

        A = self.df["A"]
        B = self.df["B"]
        C = self.df["C"]
        D = self.df["D"]

        plt.figure("stock")

        plt.subplot(311)
        plt.plot(B)
        zero_pos = -1

        for i in range(0,len):
            if A[i] == 0:
                zero_pos = i
        if zero_pos != -1:
            plt.annotate(
                         'zero: x ' + str(zero_pos) + ' y '+str(A[zero_pos]),
                         xy=(zero_pos, A[zero_pos]),
                         xytext=(zero_pos, A[zero_pos] + 3),
                         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
                        )

        plt.subplot(312)
        plt.plot(C)

        plt.subplot(313)
        plt.plot(D)

        plt.show()


if __name__ == "__main__":
    pdc = pds_charm()
    pdc.init_data()
    pdc.draw_plt()


