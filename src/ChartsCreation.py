import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def chart_generation(stats):
    figures = []
    titles = []
    specs = []
    trace_type_to_subplot_type = {
        'bar': 'xy',
        'pie': 'domain',
        'heatmap': 'heatmap',
        'scatter': 'xy',
        'density_heatmap': 'heatmap'
    }

    # 1. Incoming vs Outgoing Calls (Bar Chart)
    data = {
        'Call Type': ['Incoming', 'Outgoing'],
        'Number of Calls': [stats['incoming'], stats['outgoing']]
    }
    df = pd.DataFrame(data)
    fig1 = px.bar(df, x='Call Type', y='Number of Calls', color='Call Type',
                  color_discrete_sequence=['skyblue', 'salmon'])
    fig1.update_layout(
        xaxis_title='Call Type',
        yaxis_title='Number of Calls',
        title_text='',
        xaxis_tickfont_size=16,
        yaxis_tickfont_size=16,
        xaxis_title_font_size=18,
        yaxis_title_font_size=18,
        showlegend=False
    )
    figures.append(fig1)
    titles.append('Incoming vs Outgoing Calls (Bar Chart)')

    # Pie chart
    fig2 = px.pie(df, values='Number of Calls', names='Call Type',
                  color='Call Type',
                  hole=.3,
                  color_discrete_sequence=['skyblue', 'salmon'])
    fig2.update_traces(textposition='inside',
                       texttemplate='%{percent:.1%}<br>(%{value})')
    fig2.update_layout(
        title_text='',
        legend_title_text='Call Type',
    )
    figures.append(fig2)
    titles.append('Incoming vs Outgoing Calls (Pie Chart)')

    # 2. Average Call Duration Statistics (Bar Chart)
    call_durations = [
        stats['call_duration']['incoming_calls']['average_duration'],
        stats['call_duration']['outgoing_calls']['average_duration'],
        stats['call_duration']['total_calls']['average_duration']
    ]
    labels = ['Incoming Calls', 'Outgoing Calls', 'Total Calls']
    data = {
        'Call Type': labels,
        'Average Duration (seconds)': call_durations
    }
    df = pd.DataFrame(data)
    fig3 = px.bar(df, x='Call Type', y='Average Duration (seconds)', color='Call Type',
                  color_discrete_sequence=['lightblue', 'lightblue', 'lightblue'])
    fig3.update_layout(
        xaxis_title='Call Type',
        yaxis_title='Average Duration (seconds)',
        title_text='',
        xaxis_tickfont_size=16,
        yaxis_tickfont_size=16,
        xaxis_title_font_size=18,
        yaxis_title_font_size=18,
        showlegend=False
    )
    figures.append(fig3)
    titles.append('Average Call Duration Statistics')

    # 3. Call Apps Usage (Stacked Bar Chart)
    apps_data = stats['call_apps']
    apps = list(apps_data.keys())
    incoming_calls = [apps_data[app]['incoming'] for app in apps]
    outgoing_calls = [apps_data[app]['outgoing'] for app in apps]
    data = {
        'Apps': apps,
        'Incoming Calls': incoming_calls,
        'Outgoing Calls': outgoing_calls
    }
    df = pd.DataFrame(data)
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(name='Incoming Calls', x=df['Apps'], y=df['Incoming Calls'], marker_color='skyblue'))
    fig4.add_trace(go.Bar(name='Outgoing Calls', x=df['Apps'], y=df['Outgoing Calls'], marker_color='salmon'))
    fig4.update_layout(
        barmode='stack',
        xaxis_title='Apps',
        yaxis_title='Number of Calls',
        title_text='',
        xaxis_tickfont_size=16,
        yaxis_tickfont_size=16,
        xaxis_title_font_size=18,
        yaxis_title_font_size=18,
        legend_title_text='Call Type',
        legend_font_size=16,
        showlegend=True
    )
    figures.append(fig4)
    titles.append('Call Apps Usage (Stacked Bar Chart)')

    # Pie chart for apps
    total_calls_per_app = {app: apps_data[app]['incoming'] + apps_data[app]['outgoing'] for app in apps}
    labels = list(total_calls_per_app.keys())
    sizes = list(total_calls_per_app.values())
    data = {
        'App': labels,
        'Total Calls': sizes
    }
    df = pd.DataFrame(data)
    fig5 = px.pie(df, values='Total Calls', names='App',
                  hole=.3,
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    fig5.update_traces(textposition='inside',
                       texttemplate='%{percent:.1%}<br>(%{value})')
    fig5.update_layout(
        title_text='',
        legend_title_text='App',
    )
    figures.append(fig5)
    titles.append('Call Apps Usage (Pie Chart)')

    # 4. Key Contacts (Horizontal Bar Chart)
    if len(stats['key_contacts']) != 0:
        contacts_data = stats['key_contacts']
        sorted_contacts = sorted(contacts_data.items(), key=lambda x: x[1], reverse=True)
        contacts, contact_counts = zip(*sorted_contacts)
        top_contacts = contacts[:10]
        top_counts = contact_counts[:10]
        data = {
            'Contacts': top_contacts,
            'Number of Calls': top_counts
        }
        df = pd.DataFrame(data)
        fig6 = px.bar(df, x='Number of Calls', y='Contacts', orientation='h', color='Number of Calls',
                      color_continuous_scale='Greens')
        fig6.update_layout(
            xaxis_title='Number of Calls',
            yaxis_title='Contacts',
            title_text='',
            xaxis_tickfont_size=16,
            yaxis_tickfont_size=16,
            xaxis_title_font_size=18,
            yaxis_title_font_size=18,
            showlegend=False,
            coloraxis_showscale=False  # Hide color scale for this chart
        )
        # Order the bars from longest at the top to shortest at the bottom
        fig6.update_yaxes(categoryorder='total descending')
        figures.append(fig6)
        titles.append('Top 10 Key Contacts by Number of Calls (Bar Chart)')

        # Pie chart for contacts
        data = {
            'Contacts': top_contacts,
            'Number of Calls': top_counts
        }
        df = pd.DataFrame(data)
        fig7 = px.pie(df, values='Number of Calls', names='Contacts', hole=.3,
                      color_discrete_sequence=px.colors.qualitative.Pastel)
        fig7.update_traces(textposition='inside',
                           texttemplate='%{percent:.1%}<br>(%{value})')
        fig7.update_layout(
            title_text='',
            legend_title_text='Contacts',
        )
        figures.append(fig7)
        titles.append('Top 10 Key Contacts by Number of Calls (Pie Chart)')

    # 5. Most Active Periods of Communication (Heatmap)
    if len(stats['activity_periods']) != 0:
        activity_data = pd.DataFrame(stats['activity_periods']).T
        activity_data.index = pd.to_datetime(activity_data.index).date  # Convert index to datetime
        activity_data = activity_data.sort_index()
        # Keep 'total_calls' for the line chart
        line_data = activity_data[['total_calls']].copy()
        # For the heatmap, drop 'total_calls'
        activity_data = activity_data.drop(columns='total_calls')
        activity_data.reset_index(inplace=True)
        activity_data_melt = activity_data.melt(id_vars='index', var_name='Time of Day', value_name='Calls')

        fig8 = px.density_heatmap(activity_data_melt, x='Time of Day', y='index', z='Calls',
                                  color_continuous_scale='Viridis')
        fig8.update_layout(
            xaxis_title='Time of Day',
            yaxis_title='Date',
            title_text='',
            xaxis_tickfont_size=16,
            yaxis_tickfont_size=16,
            xaxis_title_font_size=18,
            yaxis_title_font_size=18,
            coloraxis_colorbar=dict(
                title='Calls',
                lenmode='fraction',
                len=1.0,  # Set the length of the colorbar to 100% of the subplot height
                yanchor='middle',
                y=0.5  # Center the colorbar vertically in the subplot
            )
        )
        figures.append(fig8)
        titles.append('Most Active Periods of Communication (Heatmap)')

        # 6. Total Calls per Day (Line Chart)
        line_data.reset_index(inplace=True)
        fig9 = px.line(line_data, x='index', y='total_calls')
        fig9.update_layout(
            xaxis_title='Date',
            yaxis_title='Total Calls',
            title_text='',
            xaxis_tickfont_size=12,
            yaxis_tickfont_size=12,
            xaxis_title_font_size=14,
            yaxis_title_font_size=14,
        )
        fig9.update_traces(mode='lines+markers', marker=dict(size=6, color='royalblue'), line=dict(color='royalblue'))
        fig9.update_xaxes(tickangle=45, tickformat='%Y-%m-%d')
        figures.append(fig9)
        titles.append('Total Calls per Day (Line Chart)')

    # 7. Country Activity (Donut Chart)
    if 'country_activity' in stats and len(stats['country_activity']) != 0:
        country_data = stats['country_activity']
        # Optional: Limit to top N countries and group the rest as 'Others'
        top_n = 10
        sorted_countries = sorted(country_data.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_countries) > top_n:
            top_countries = sorted_countries[:top_n]
            others_total = sum(count for _, count in sorted_countries[top_n:])
            top_countries.append(('Others', others_total))
        else:
            top_countries = sorted_countries

        countries, counts = zip(*top_countries)
        data = {
            'Country': countries,
            'Number of Calls': counts
        }
        df = pd.DataFrame(data)
        fig10 = px.pie(df, values='Number of Calls', names='Country', hole=.3,
                       color_discrete_sequence=px.colors.qualitative.Pastel)
        fig10.update_traces(textposition='inside',
                            texttemplate='%{percent:.1%}<br>(%{value})')
        fig10.update_layout(
            title_text='',
            legend_title_text='Country',
        )
        figures.append(fig10)
        titles.append('Calls by Country (Donut Chart)')

    # 8. City Activity (Donut Chart)
    if 'city_activity' in stats and len(stats['city_activity']) != 0:
        city_data = stats['city_activity']
        # Optional: Limit to top N cities and group the rest as 'Others'
        top_n = 10
        sorted_cities = sorted(city_data.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_cities) > top_n:
            top_cities = sorted_cities[:top_n]
            others_total = sum(count for _, count in sorted_cities[top_n:])
            top_cities.append(('Others', others_total))
        else:
            top_cities = sorted_cities

        cities, counts = zip(*top_cities)
        data = {
            'City': cities,
            'Number of Calls': counts
        }
        df = pd.DataFrame(data)
        fig11 = px.pie(df, values='Number of Calls', names='City', hole=.3,
                       color_discrete_sequence=px.colors.qualitative.Pastel)
        fig11.update_traces(textposition='inside',
                            texttemplate='%{percent:.1%}<br>(%{value})')
        fig11.update_layout(
            title_text='',
            legend_title_text='City',
        )
        figures.append(fig11)
        titles.append('Calls by City (Donut Chart)')

    # Determine specs based on trace types
    for fig in figures:
        trace_type = fig.data[0].type
        subplot_type = trace_type_to_subplot_type.get(trace_type, 'xy')
        specs.append([{'type': subplot_type}])

    # Create a combined figure with subplots
    num_charts = len(figures)
    fig_combined = make_subplots(rows=num_charts, cols=1, subplot_titles=titles,
                                 vertical_spacing=0.02, specs=specs)

    # Add traces to the combined figure
    for i, fig in enumerate(figures):
        for trace in fig.data:
            fig_combined.add_trace(trace, row=i+1, col=1)

        # Update axes properties if needed
        fig_combined.update_xaxes(title_text=fig.layout.xaxis.title.text, row=i+1, col=1)
        fig_combined.update_yaxes(title_text=fig.layout.yaxis.title.text, row=i+1, col=1)

        # Update colorbar position for heatmap
        if 'coloraxis' in fig.layout:
            fig_combined.layout.coloraxis.colorbar.update(
                lenmode='fraction',
                len=.8 / num_charts,  # Adjust the colorbar height proportionally
                yanchor='middle',
                y=1 - (i + 0.5) / (num_charts + 4.3)  # Position the colorbar next to its subplot
            )

    # Adjust the layout of the combined figure
    fig_combined.update_layout(
        height=600 * num_charts,  # Adjust height as needed
        showlegend=False,
        title_text='Combined Call Statistics',
        title_font_size=24,
    )

    # Show the combined figure
    fig_combined.show()
