from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    graph = Chart(
        df,
        title=f"{y} for {x} in {target}",
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    ).properties(
        width=500,
        height=500,
    ).configure(
        background="#1d1c1c",
        padding={"left":15, "top":30, "right":15, "bottom":15}
    ).configure_title(
        fontSize=30,
        color="#9f9f9f"
    ).configure_axis(
        gridColor="#343333",
        domainOpacity=0.2,
        domainColor="light gray",
        labelColor="white"
    ).configure_legend(
        labelColor="white",
        titleColor='White',
        titlePadding=20
    ).interactive()

    return graph

