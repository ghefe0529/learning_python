#GA遗传算法
import random

# 假设一个未编码的个体表示为：取，取，不取，不取，可用十进制10和12表示
def ga_encode(N, unit): # N:染色体长度； unit:个体表示（如12）
    unit = int(unit)
    unit_str = str(bin(unit))[2:].zfill(N)
    unit_list = []
    for s in unit_str:
        unit_list.append(s)
    return unit_list
def ga_decode(unit_list):
    l = ll = len(unit_list) - 1
    c = 0 
    while l >= 0:
        if unit_list[l] == '1':
            c += pow(2, ll-l)
        l -= 1
    return c


# 计算种群的适应性概率
def getRWSPList(population, w,v,W):
    n = len(population)
    v_list = []
    for i in population:
        unit_code = ga_encode(N, i)
        unit_w = 0
        unit_v = 0
        for j in range(N):
            unit_w += int(unit_code[j])*w[j]
            unit_v += int(unit_code[j])*v[j]
        if unit_w <= W:
            v_list.append(unit_v)
        else:
            v_list.append(0) # 超重
    p_list = [] # 每个个体的概率
    v_all = sum(v_list)
    for i in range(n):
        p_list.append(v_list[i]*1.0/v_all)
    return p_list

# 根据适应性概率随机选择一个个体
def RWS(population, plist): #plist为总群个体抽中概率list
    random.seed()
    r = random.random() # 获得随机数
    c = 0
    for (index, item) in enumerate(plist):
        c += item
        if r < c:
            return population[index]
# 交叉
# 获得随机couple组
def getRandomCouple(n): # n为个体总数
    random.seed()
    selected = [0]*n
    couples = []
    for i in range(n//2):
        pair = []
        while len(pair) < 2:
            unit_index = random.randint(0, n-1)
            if not selected[unit_index]:
                pair.append(unit_index)
                selected[unit_index] = True
        couples.append(pair)
    return couples

def crossover(population, couples, cross_p, N): #cross_p为交叉概率；N为编码长度
    random.seed()
    new_population = []
    for pair in couples:
        unit_one = ga_encode(N, population[pair[0]])
        unit_two = ga_encode(N, population[pair[1]])
        p = random.random()
        if p >= (1 - cross_p):
            # 交叉使用从随机位置交叉尾部
            random_loc = random.randint(0,N-1) # 获取随机位置
            new_population.append(unit_one[0:random_loc] + unit_two[random_loc:])
            new_population.append(unit_two[0:random_loc] + unit_one[random_loc:])
        else:
            new_population.append(unit_one)
            new_population.append(unit_two)
    for (index, unit) in enumerate(new_population):
        new_population[index] = ga_decode(unit) # 解码
    return list(set(new_population))
# 变异
def mutation(population, N, mutation_p):
    new_population = []
    random.seed()
    for unit in population:
        unit_code = ga_encode(N, unit)
        p = random.random() #获得随机概率
        if p > (1- mutation_p):
            random_loc = random.randint(0, N-1)
            v = unit_code[random_loc]
            unit_code[random_loc] = '0' if v == '1' else '1'
        new_population.append(ga_decode(unit_code))
    return list(set(new_population))

generation_count = 50
N = 4
n = pow(2, N)
w = [2,3,1,5]
v = [4,3,2,1]
W = 6
population = []

# 初始化种群
for i in range(n):
    population.append(i)
print("Original population:",population)

# 算法
c = 0
while c < generation_count:
    print('-'*10 + str(c)+'-'*10)
    # 种群选择
    plist = getRWSPList(population,w,v,W) # 获得总群概率list
    new_population = []
    for i in range(n): # 适者生存
        new_population.append(RWS(population, plist))
    new_population = list(set(new_population))
    print("After selection:", new_population)
    if len(new_population) == 1:
        population = new_population
        break
    
    # 种群交叉
    couples = getRandomCouple(len(new_population)) #随机配对
    new_population = crossover(new_population, couples, 0.8, N)
    print('After crossover:', new_population)
    if len(new_population) == 1:
        population = new_population
        break
    
    #种群变异
    new_population = mutation(new_population, N, 0.1)
    print('Afer mutation:' + str(new_population))
    if len(new_population) ==1:
        population = new_population
        break
    
    population = new_population
    c += 1

print(population)