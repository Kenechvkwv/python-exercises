# A python class that will calculate the body mass index for specified values of weight and height

class BMI:
    def __init__(self):
        self.__weight = 0.0
        self.__height = 0.0
        self.__bmi = 0.0

    def set_weight(self, weight):
        self.__weight = weight

    def set_height(self, height):
        self.__height = height

    def calc_bmi(self):
        self.__bmi = self.__weight / (self.__height / 100)**2

    def get_bmi(self):
        bmi = self.__bmi
        return bmi


def main():
    bmi_calculate = BMI()
    bmi_calculate.set_weight(70)  # kg
    bmi_calculate.set_height(175)  # centimeter
    bmi_calculate.calc_bmi()
    bmi = bmi_calculate.get_bmi()

    print("calculated BMI:", bmi)


main()
