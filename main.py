from logic_gate import LogicGate

def main():
    #             X1 X2 OR
    matrix_or_1 = ((0, 1, 1),
                   (1, 0, 1),
                   (0, 0, 0),
                   (1, 1, 1))

    #             X1 X2 AND
    matrix_and_1 = ((0, 0, 0),
                    (0, 1, 0),
                    (1, 0, 0),
                    (1, 1, 1))

    gate_or = LogicGate()
    gate_or.generate_values()
    gate_or.train(matrix_or_1, 1)

    gate_and = LogicGate()
    gate_and.generate_values()
    gate_and.train(matrix_and_1, 1)

    print("Resultados OR: ")
    print(gate_or.activation_function(1, 0))
    print(gate_or.activation_function(0, 0))
    print(gate_or.activation_function(0, 1))
    print(gate_or.activation_function(1, 1))

    print("\nResultados AND: ")
    print(gate_and.activation_function(1, 0))
    print(gate_and.activation_function(0, 0))
    print(gate_and.activation_function(0, 1))
    print(gate_and.activation_function(1, 1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
