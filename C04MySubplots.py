import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# # 饼状图（不兼容子图）
# labels = ['A', 'B', 'C', 'D']
# values = [30, 25, 20, 25]
# fig1 = go.Figure(go.Pie(labels=labels, values=values))

# 折线图
x = [1, 2, 3, 4]
y = [10, 11, 12, 13]
fig2 = px.scatter(
    x=x, y=y
)

# 条形统计图
x = ['A', 'B', 'C', 'D']
y = [20, 14, 23, 25]
fig3 = px.bar(
    x=x, y=y
)

# Create subplot with one shared x-axis and one independent y-axis
fig = make_subplots(rows=2, cols=1, shared_xaxes=False, vertical_spacing=0.03)

# Add traces to subplots
fig.add_trace(fig2['data'][0], row=1, col=1)
fig.add_trace(fig3['data'][0], row=2, col=1)

# Show (1600px Total Height)
container = go.FigureWidget(fig)
container.update_layout(height=1600, title='Multiple Graphs with Scrollbar')
container.show()
