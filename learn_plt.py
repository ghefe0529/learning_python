import numpy as np 
import matplotlib.pyplot as plt
'''
# 两个窗口
data = np.arange(100,201)
plt.plot(data)
data2 = np.arange(200,301)

plt.figure()

plt.plot(data2)

plt.show()

#一个窗口
data = np.arange(100,201)
# 1行2列，第1个位置
plt.subplot(1,2,1)
plt.plot(data)
data2 = np.arange(200,301)
# 1行2列，第2个位置
plt.subplot(1,2,2)

plt.plot(data2)

plt.show()


plt.plot([1,2,3],[3,6,9],'-r')
plt.plot([1,2,3],[2,4,9], ':g')
plt.show()

# 散点图
N = 20
# plt.scatter(x,y,color颜色,size大小,alpha透明度)
plt.scatter(np.random.rand(N)*100, np.random.rand(N)*100,c='r',s=100,alpha=0.8)
plt.scatter(np.random.rand(N)*100, np.random.rand(N)*100,c='g',s=200,alpha=0.5)
plt.scatter(np.random.rand(N)*100, np.random.rand(N)*100,c='b',s=300,alpha=0.2)
plt.show()

# 饼状图
labels = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
data = np.random.rand(7) * 100
plt.pie(data,labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.legend()

plt.show()

# 条形图
N = 7
x = np.arange(N)
data = np.random.randint(low=0,high=100,size=N)
colors = np.random.rand(N*3).reshape(N, -1)
labels = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

plt.title('Weekday Data')
plt.bar(x,data, alpha=0.8, color = colors, tick_label=labels)
plt.show()


# 直方图

data = [np.random.randint(0, n, n) for n in [3000,4000,5000]]
print(data)
labels = ['3K','4K','5K']
bins = [0,100,500,1000,2000,3000,4000]

plt.hist(data,bins=bins, label=labels)
plt.legend()
plt.show()

# legend()用于显示图例（小框框）：
x = np.arange(1, 11)

fig = plt.figure(1)
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)
l1, = ax1.plot(x, x*x, 'r')             #这里关键哦
l2, = ax2.plot(x, x*2, 'b')           # 注意

plt.legend([l1, l2], ['first', 'second'], loc = 'center')             #其中，loc表示位置的；

plt.show()

'''
# 动态更新
# plt.axis([xmin, xmax, ymin, ymax])
plt.axis([0,100,0,1])
# 开启交互式
    # plt.ion()
x = []
y = []
i = 0
for j in range(10):
    x.append(i)
    y.append(np.random.random())
    plt.cla()
    plt.plot(x,y)
    # 显示停留1秒
    # plt.pause(1)
    # 关闭交互式
    # plt.ioff()
    plt.show()
    i += 1
'''

# 动态图
import matplotlib.animation as animation 
fig = plt.figure() 
axes1 = fig.add_subplot(111) 
line, = axes1.plot(np.random.rand(10)) 
#因为update的参数是调用函数data_gen,
#所以第一个默认参数不能是framenum 
def update(data): 
  line.set_ydata(data) 
  return line, 
# 每次生成10个随机数据 
def data_gen(): 
  while True: 
    yield np.random.rand(10) 
ani = animation.FuncAnimation(fig, update, data_gen, interval=2*1000)
plt.show()
'''
   

