import numpy as np

# Rules
rules = {
    'S': [['NP']],
    'P': [['VP','PP']],
    'O': [['NP']],
    'PEL': [['NP']],

    'NP': [['Noun'], ['NP', 'Noun'], ['NP', 'Pronoun'], ['NP', 'Verb'], ['Noun', 'Noun'], ['Noun', 'Pronoun'],
           ['Noun', 'Verb'], ['baju'], ['bapak'], ['ibu']],
    'VP': [['Verb'], ['Adv', 'VP'], ['Adj', 'VP'], ['Noun', 'VP'], ['Adv', 'Verb'], ['Adj', 'Verb'], ['Noun', 'Verb'],
           ['disetrika']],
    'PP': [['Prep', 'NP'], ['Prep', 'Noun'], ['oleh']],

    'Noun': [['bapak'], ['ibu'], ['baju']],
    'Pronoun': [['itu'], ['saya']],
    'Verb': [['disetrika']],
    'Prep': [['oleh']]
}


# pembuatan filling table
def create_table(n):
    rows, cols = (n + 1, n)
    arr = [[[] for i in range(cols)] for j in range(rows)]
    return arr


# pengisian cell awal pada filling table
def filling_bottom(table, str):
    for i in range(len(str)):
        for lhs, rule in rules.items():
            for rhs in rule:
                if len(rhs) == 1 and rhs[0] == str[i]:
                    table[i][i].append(lhs)


# menemukan kombinasi antara cell tertentu pada filling table
def combination(com1, com2):
    temp = []
    mesh = np.array(np.meshgrid(com1, com2))
    comb = mesh.T.reshape(-1, 2)
    for com in comb:
        list_convert = list(com)
        temp.append(list_convert)

    return temp


# mengisi sisa cell pada filling table
def filling_all(table, str):
    for j in range(0, len(str)):
        for i in range(j, -1, -1):
            for k in range(i, j + 1):
                for lhs, rule in rules.items():
                    for rhs in rule:
                        com = combination(table[i][k], table[k + 1][j])
                        if rhs in com:
                            table[i][j].append(lhs)


# menampilkan hasil akhir dari filling table
def print_table(table):
    for tab in table:
        print(tab)


# fungsi main, fungsi yang pertama kali dijalankan
if __name__ == '__main__':
    string = input("Input string: ")
    str_split = string.split()
    table = create_table(len(str_split))
    filling_bottom(table, str_split)
    filling_all(table, str_split)
    print_table(table)

    if table[1][len(str_split) - 1]:
        print(string + " (Accepted)")
    else:
        print(string + " (Not accepted)")
