import plotly.express as px
from pandas import DataFrame
from plotly.graph_objs._figure import Figure


class Badge:
    def __init__(self, df: DataFrame) -> None:
        """badge class for creating plotly badge-sized charts

        Args:
            df (DataFrame): a vector-like data
        """

        self.df = df

    def create(self, badge_height: int, badge_width: int, badge_color: str) -> Figure:
        """creates the badge

        Args:
            badge_height (int): badge height size (in pixels)
            badge_width (int): badge width size (in pixels)
            badge_color (str): badge color

        Returns:
            Figure: badge figure
        """

        # creating the figure with the linear plot graphed
        fig = (
            px.line(
                self.df,
                height=badge_height,
                width=badge_width,
                line_shape="spline",
            )
            .update_traces(line_color=badge_color)  # coloring the plot
            .update_xaxes(visible=False)  # hiding the x axes
            .update_yaxes(visible=False)  # hiding the y axes
        )

        # strip down the rest of the plot
        fig.update_layout(
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(t=0, l=0, b=0, r=0),
        )

        return fig
