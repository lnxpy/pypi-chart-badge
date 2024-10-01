import plotly.express as px
from pandas import DataFrame
from plotly.graph_objs._figure import Figure


class Badge:
    def __init__(self, df: DataFrame) -> None:
        self.df = df

    def create_chart(
        self, badge_height: int, badge_width: int, badge_color: str
    ) -> Figure:
        fig = px.line(
            self.df, height=badge_height, width=badge_width, line_shape="spline"
        )

        fig.update_traces(line_color=badge_color)

        # hide and lock down axes
        fig.update_xaxes(visible=False, fixedrange=True)
        fig.update_yaxes(visible=False, fixedrange=True)

        # remove facet/subplot labels
        fig.update_layout(annotations=[], overwrite=True)

        # strip down the rest of the plot
        fig.update_layout(
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(t=0, l=0, b=0, r=0),
        )

        return fig
