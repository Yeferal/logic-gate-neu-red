import random
from paint_table import paint_table

class LogicGate:

    def __init__(self):
        # self.matrix = matrix
        self.percent_error = 100
        self.threshold = 0.4
        self.bias = -self.threshold
        self.weights = [0.2, 0.6]

    def activation_function(self, x1: float, x2: float):
        value = x1 * self.weights[0] + x2 * self.weights[1] + self.bias

        # print(f"x1 * w1 + x2 * w2 + sesgo")
        # print(f"{x1} * {self.weights[0]} + {x2} * {self.weights[1]} + {self.bias}")
        # print(f"{x1*self.weights[0]} + {x2*self.weights[1]} + {self.bias}")
        # print(f"{value} > 0")

        result = 1 if value > 0 else 0
        return f"({x1} , {x2}) => {result})"

    def generate_values(self):
        self.threshold = round(random.uniform(0, 1), 1)
        self.bias = self.threshold * (-1)
        self.weights = [round(random.uniform(0, 1), 1), round(random.uniform(0, 1), 1)]
        print("Inicio")
        self.paint_data()
        print()

    def train_iteration(self, x1: float, x2: float, y):
        lmbda = 0.2
        w1 = self.weights[0]
        w2 = self.weights[1]
        z = x1 * w1 + x2 * w2 + self.bias
        z = round(z, 1)
        major_threshold = x1 * w1 + x2 * w2

        # activation = 1 if (z >= self.threshold) else 0
        activation = 1 if (z > 0) else 0
        # activation = y if (z >= 0) else 0
        e = (y - activation)

        dif_u = -(lmbda * e)
        new_u = self.threshold + dif_u
        new_u = round(new_u, 1)

        def_w1 = lmbda * e * x1
        new_w1 = w1 + def_w1
        new_w1 = round(new_w1, 1)

        def_w2 = lmbda * e * x2
        new_w2 = w2 + def_w2
        new_w2 = round(new_w2, 1)

        if y != 0:
            self.percent_error = abs(((activation - y) / y) * 100)
        # else:
        #     self.percent_error = abs(y * 100)

        data_row = ["", str(x1), str(w1), str(x2), str(w2), str(self.threshold),
                    str(self.bias), str(y), str(z), str(activation), str(e), str(new_u), str(new_w1),
                    str(new_w2), str(self.percent_error)]

        self.threshold = round(new_u, 1)
        self.bias = -self.threshold
        self.weights = [round(new_w1, 1), round(new_w2, 1)]
        return data_row

    def train(self, matrix, iterationes):
        data_table = [["Ite",'x1', 'w1', 'x2', 'w2', 'u', 'sesgo', 'y', 'z', 'activ', 'e', 'newU', 'newW1', 'newW2', 'percent_error']]

        num_interation = 1
        while self.percent_error >= 0:
            data_table.append([f"Iteration {num_interation}", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])
            for row_input in matrix:
                x1 = row_input[0]
                x2 = row_input[1]
                y = row_input[2]

                data_row = self.train_iteration(x1, x2, y)
                data_table.append(data_row)
                # if self.percent_error >= 99:
                #     break
            num_interation = num_interation + 1
            if iterationes < num_interation:
                break

        paint_table(data_table)

    def paint_data(self):
        print(f"Umbral: {self.threshold}, Sesgo: {self.bias}, Pesos: {self.weights}, %e: {self.percent_error}")
