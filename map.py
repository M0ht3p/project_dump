#!/usr/bin/env python3

import plotly.express as px

def main():
    df = px.data.gapminder().query("year == 2007")

    fig = px.choropleth(
        df,
        locations="iso_alpha",
        color="gdpPercap",
        hover_name="country",
        color_continuous_scale="Plasma",
        title="Lightweight modern map"
    )

    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='natural earth'
        )
    )

    fig.show()

if __name__ == "__main__":
    main()