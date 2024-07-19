import plotly.graph_objects as go

#
# 创建饼状图
#

labels = ['A', 'B', 'C', 'D']
values = [30, 25, 20, 25]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()

#
# 创建折线图
#

x = [1, 2, 3, 4]
y = [10, 11, 12, 13]

fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
fig.show()

#
# 创建条形统计图
#

x = ['A', 'B', 'C', 'D']
y = [20, 14, 23, 25]

fig = go.Figure(data=[go.Bar(x=x, y=y)])
fig.show()
