

line = int(input())
dataset = []
for i in range(line):
    dataset.append(input())

dataset = "\n".join(dataset)

months = { i :[] for i in range(1,13)}

def get_clean_data(row):
    """
    takes in a row "MonthNum_60 764544"
    and returns [12, 764544]

    """
    month , data = row.split()
    _ , right = month.split("_")

    right = int(right)
    m = right % 12
    m = m if m !=0 else 12

    return m,int(data)



for row in dataset.splitlines():
    m,d = get_clean_data(row)
    months[m].append(d)


for i in months:
    print(sum(months[i])/len(months[i]))
