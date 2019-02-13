import numpy as np


def C(n):
    if n < 2:
        return 0
    return np.math.factorial(n) / (np.math.factorial(2) * np.math.factorial(n - 2))


def calculate_Fit(queens):
    Board = np.zeros((8, 8))
    for q in range(queens.__len__()):
        i = int(str(queens[q][0]) + str(queens[q][1]) + str(queens[q][2]), 2)
        Board[i][q] = 1

    sumOflines = sum([C(sum(Board[line])) for line in range(8)])
    sumOfDiagonals = sum([C(Board.trace(offset=diag)) for diag in range(9)])
    sumOfDiagonals += sum([C(Board.trace(offset=-diag)) for diag in range(1, 9)])
    sumOfDiagonals += sum([C(Board[::-1].trace(offset=diag)) for diag in range(9)])
    sumOfDiagonals += sum([C(Board[::-1].trace(offset=-diag)) for diag in range(1, 9)])

    return sumOflines + sumOfDiagonals


if __name__ == '__main__':

    # First step, create the initial instances for the Queens
    # each queen can be in the one of the 8 lines, that will be interpreted by
    # 000 to 111
    # initial matrix is 30 x 24
    # 0.90 percent to reproduce and 0.10 will have mutation

    number_peaple = 100
    population = np.random.randint(2, size=(number_peaple, 24))
    maxOfgenerations = 60
    realizacoes = 10
    reproduction_rate = 0.9
    mutation_rate = 0.1

    for generation in range(maxOfgenerations):
        # second step, calculate the fit of each one
        Fit = np.zeros((number_peaple, 1))
        p = 0
        for person in population:
            # transform to calculate the attacks
            queens = []
            aux = []  # rainhas que ja atacaram
            for i in range(0, len(person), 3):
                queens.append(person[i:i + 3])
            Fit[p] = calculate_Fit(queens)
            p += 1

        Total_Attacks = Fit.min()
        indice = np.where(Fit == Fit.min())[0][0]
        best = population[indice]
        if Total_Attacks == 0:
            break

        Fit = (Fit.max() - Fit)
        relative_fit = np.array(Fit / Fit.sum(), ndmin=2)
        slices = np.zeros((relative_fit.shape[0], 2))
        slices[0] = [0.0, relative_fit[0]]
        for i in range(1, slices.shape[0]):
            slices[i] = [slices[i - 1][1], slices[i - 1][1] + relative_fit[i][0]]

        # third and four steps natural selection and crossover
        sizeOfnewpopulation = int(reproduction_rate * number_peaple)
        new_population = np.zeros((sizeOfnewpopulation, 24))
        for i in range(0, sizeOfnewpopulation, 2):
            random_perceent1 = np.random.rand()
            random_perceent2 = np.random.rand()
            for s in range(slices.__len__()):
                if random_perceent1 >= slices[s][0] and random_perceent1 < slices[s][1]:
                    person_ind1 = s
                if random_perceent2 >= slices[s][0] and random_perceent2 < slices[s][1]:
                    person_ind2 = s

            # fourth step crossover
            person1 = population[person_ind1]
            person2 = population[person_ind2]
            # multi-ponto
            points = sorted(np.random.randint(24, size=(2)))
            First_son = np.concatenate((person1[:points[0]], person2[points[0]:points[1]], person1[points[1]:]), axis=0)
            second_son = np.concatenate((person2[:points[0]], person1[points[0]:points[1]], person2[points[1]:]),
                                        axis=0)
            new_population[i] = First_son
            new_population[i + 1] = second_son

        # fifth step X-men
        sizeOfmutation = int(mutation_rate * number_peaple)
        indices = np.random.randint(24, size=(sizeOfmutation))  # random people of population
        mutants = np.zeros((sizeOfmutation, 24))
        j = 0
        for i in indices:
            indice = np.random.randint(24, size=(1))
            if population[i][indice] == 1:
                mutants[j] = population[i]
                mutants[j][indice] = 0
            elif population[i][indice] == 0:
                mutants[j] = population[i]
                mutants[j][indice] = 1
            j += 1
        population = np.array(np.concatenate((new_population, mutants)), dtype=np.int32)
