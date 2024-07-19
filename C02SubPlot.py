import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Load data
df = px.data.gapminder()

# Create figures
fig1 = px.scatter(
    df, x="gdpPercap", y="lifeExp", color="continent",
    hover_name="country", log_x=True
)
fig2 = px.line(
    df, x="year", y="gdpPercap", color="continent",
    line_group="country", hover_name="country", line_shape="spline",
    render_mode="svg"
)

# Create subplot with one shared x-axis and one independent y-axis
fig = make_subplots(rows=2, cols=1, shared_xaxes=False, vertical_spacing=0.03)

# Add traces to subplots
fig.add_trace(fig1['data'][0], row=1, col=1)
fig.add_trace(fig2['data'][0], row=2, col=1)

# Show (50%-50% Height)
fig.update_layout(title='Multiple Graphs in Same Page')
fig.show()
