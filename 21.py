def Non_Diagonal(array):
    elements = []
    for j in range(len(array)):
        for i in range(len(array[j])):
            if i!=j:
                elements.append(array[j][i])
    return elements
