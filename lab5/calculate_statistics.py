import statistics

def calculate_statistics(c):
    for i in range(len(c)):
        values = []
        for j in range(len(c[i])):
            values.append(c[i][j][1])
        stat = [statistics.mean(values), statistics.mode(values), statistics.median(values)]
        print('Начало - ', c[i][0][0], 'Конец - ', c[i][len(c[i]) - 1][0], ':')
        print('Ср. знач. - ', statistics.mean(values))
        print('Мод - ', statistics.mode(values))
        print('Медиана - ', statistics.median(values))
    return stat
