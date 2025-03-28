# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# def chart_generation(stats, language='ru'):
#     translations = {
#         'eng': {
#             'bar_chart_title': 'Incoming vs Outgoing Calls (Bar Chart)',
#             'pie_chart_title': 'Incoming vs Outgoing Calls (Pie Chart)',
#             'average_duration_title': 'Average Call Duration Statistics',
#             'stacked_bar_title': 'Call Apps Usage (Stacked Bar Chart)',
#             'app_pie_chart_title': 'Call Apps Usage (Pie Chart)',
#             'key_contacts_bar_title': 'Top 10 Key Contacts by Number of Calls (Bar Chart)',
#             'key_contacts_pie_title': 'Top 10 Key Contacts by Number of Calls (Pie Chart)',
#             'heatmap_title': 'Most Active Periods of Communication (Heatmap)',
#             'line_chart_title': 'Total Calls per Day (Line Chart)',
#             'country_donut_title': 'Calls by Country (Donut Chart)',
#             'city_donut_title': 'Calls by City (Donut Chart)',
#             'xaxis_calls': 'Number of Calls',
#             'xaxis_date': 'Date',
#             'yaxis_contacts': 'Contacts',
#             'xaxis_time': 'Time of Day',
#             'yaxis_duration': 'Average Duration (seconds)',
#             'xaxis_apps': 'Apps',
#             'xaxis_app': 'App',
#             'xaxis_call_type': 'Сall Type',
#             'xaxis_calls_incoming': 'Incoming Calls',
#             'xaxis_calls_outgoing': 'Outgoing Calls',
#             'xaxis_calls_total': 'Total Calls',
#             'xaxis_calls_total': 'Total Calls',
#             'index': 'index',
#             'calls': 'Сalls',
#             'city': 'city',
#             'country':'Country',
#         },
#         'ru': {
#             'bar_chart_title': 'Входящие и исходящие звонки (Гистограмма)',
#             'pie_chart_title': 'Входящие и исходящие звонки (Круговая диаграмма)',
#             'average_duration_title': 'Средняя длительность звонков',
#             'stacked_bar_title': 'Использование приложений для звонков (Сложенная гистограмма)',
#             'app_pie_chart_title': 'Использование приложений для звонков (Круговая диаграмма)',
#             'key_contacts_bar_title': 'Топ-10 ключевых контактов по количеству звонков',
#             'key_contacts_pie_title': 'Топ-10 ключевых контактов (Круговая диаграмма)',
#             'heatmap_title': 'Активные периоды общения (Тепловая карта)',
#             'line_chart_title': 'Общее количество звонков в день (Линейный график)',
#             'country_donut_title': 'Звонки по странам (Круговая диаграмма)',
#             'city_donut_title': 'Звонки по городам (Круговая диаграмма)',
#             'xaxis_calls': 'Количество звонков',
#             'xaxis_date': 'Дата',
#             'yaxis_contacts': 'Контакты',
#             'xaxis_time': 'Время суток',
#             'yaxis_duration': 'Средняя длительность (секунды)',
#             'xaxis_apps': 'Приложения',
#             'xaxis_app': 'Приложение',
#             'xaxis_call_type': 'Тип звонка',
#             'xaxis_calls_incoming': 'Входящие звонки',
#             'xaxis_calls_outgoing': 'Исходящие звонки',
#             'xaxis_calls_total': 'Все звонки',
#             'index': 'индекс',
#             'calls': 'Звонки',
#             'city': 'Город',
#             'country': 'Страна',
#         }
#     }
#     text = translations[language]
#     figures = []
#     titles = []
#     specs = []
#     trace_type_to_subplot_type = {
#         'bar': 'xy',
#         'pie': 'domain',
#         'heatmap': 'heatmap',
#         'scatter': 'xy',
#         'density_heatmap': 'heatmap'
#     }

#     # 1. Incoming vs Outgoing Calls (Bar Chart)
#     data = {
#         text['xaxis_call_type']: [text['xaxis_calls_incoming'], text['xaxis_calls_outgoing']],
#         text['xaxis_calls']: [stats['incoming'], stats['outgoing']]
#     }
#     df = pd.DataFrame(data)
#     fig1 = px.bar(df, x=text['xaxis_call_type'], y=text['xaxis_calls'], color=text['xaxis_call_type'],
#                   color_discrete_sequence=['skyblue', 'salmon'])
#     fig1.update_layout(
#         xaxis_title=text['xaxis_call_type'],
#         yaxis_title=text['xaxis_calls'],
#         title_text='',
#         xaxis_tickfont_size=16,
#         yaxis_tickfont_size=16,
#         xaxis_title_font_size=18,
#         yaxis_title_font_size=18,
#         showlegend=False
#     )
#     figures.append(fig1)
#     titles.append(text['bar_chart_title'])

#     # Pie chart
#     fig2 = px.pie(df, values=text['xaxis_calls'], names=text['xaxis_call_type'],
#                   color=text['xaxis_call_type'],
#                   hole=.3,
#                   color_discrete_sequence=['skyblue', 'salmon'])
#     fig2.update_traces(textposition='inside',
#                        texttemplate='%{percent:.1%}<br>(%{value})')
#     fig2.update_layout(
#         title_text='',
#         legend_title_text=text['xaxis_call_type'],
#     )
#     figures.append(fig2)
#     titles.append(text['pie_chart_title'])

#     # 2. Average Call Duration Statistics (Bar Chart)
#     call_durations = [
#         stats['call_duration']['incoming_calls']['average_duration'],
#         stats['call_duration']['outgoing_calls']['average_duration'],
#         stats['call_duration']['total_calls']['average_duration']
#     ]
#     labels = [text['xaxis_calls_incoming'], text['xaxis_calls_outgoing'], text['xaxis_calls_total']]
#     data = {
#         text['xaxis_call_type']: labels,
#         text['yaxis_duration']: call_durations
#     }
#     df = pd.DataFrame(data)
#     fig3 = px.bar(df, x=text['xaxis_call_type'], y=text['yaxis_duration'], color=text['xaxis_call_type'],
#                   color_discrete_sequence=['lightblue', 'lightblue', 'lightblue'])
#     fig3.update_layout(
#         xaxis_title=text['xaxis_call_type'],
#         yaxis_title=text['yaxis_duration'],
#         title_text='',
#         xaxis_tickfont_size=16,
#         yaxis_tickfont_size=16,
#         xaxis_title_font_size=18,
#         yaxis_title_font_size=18,
#         showlegend=False
#     )
#     figures.append(fig3)
#     titles.append(text['average_duration_title'])

#     # 3. Call Apps Usage (Stacked Bar Chart)
#     apps_data = stats['call_apps']
#     apps = list(apps_data.keys())
#     incoming_calls = [apps_data[app]['incoming'] for app in apps]
#     outgoing_calls = [apps_data[app]['outgoing'] for app in apps]
#     data = {
#         text['xaxis_apps']: apps,
#         text['xaxis_calls_incoming']: incoming_calls,
#         text['xaxis_calls_outgoing']: outgoing_calls
#     }
#     df = pd.DataFrame(data)
#     fig4 = go.Figure()
#     fig4.add_trace(go.Bar(name=text['xaxis_calls_incoming'], x=df[text['xaxis_apps']], y=df[text['xaxis_calls_incoming']], marker_color='skyblue'))
#     fig4.add_trace(go.Bar(name=text['xaxis_calls_outgoing'], x=df[text['xaxis_apps']], y=df[text['xaxis_calls_outgoing']], marker_color='salmon'))
#     fig4.update_layout(
#         barmode='stack',
#         xaxis_title=text['xaxis_apps'],
#         yaxis_title=text['xaxis_calls'],
#         title_text='',
#         xaxis_tickfont_size=16,
#         yaxis_tickfont_size=16,
#         xaxis_title_font_size=18,
#         yaxis_title_font_size=18,
#         legend_title_text=text['xaxis_call_type'],
#         legend_font_size=16,
#         showlegend=True
#     )
#     figures.append(fig4)
#     titles.append(text['stacked_bar_title'])

#     # Pie chart for apps
#     total_calls_per_app = {app: apps_data[app]['incoming'] + apps_data[app]['outgoing'] for app in apps}
#     labels = list(total_calls_per_app.keys())
#     sizes = list(total_calls_per_app.values())
#     data = {
#         text['xaxis_app']: labels,
#         text['xaxis_calls_total']: sizes
#     }
#     df = pd.DataFrame(data)
#     fig5 = px.pie(df, values=text['xaxis_calls_total'], names=text['xaxis_app'],
#                   hole=.3,
#                   color_discrete_sequence=px.colors.qualitative.Pastel)
#     fig5.update_traces(textposition='inside',
#                        texttemplate='%{percent:.1%}<br>(%{value})')
#     fig5.update_layout(
#         title_text='',
#         legend_title_text=text['xaxis_app'],
#     )
#     figures.append(fig5)
#     titles.append(text['app_pie_chart_title'])

#     # 4. Key Contacts (Horizontal Bar Chart)
#     if len(stats['key_contacts']) != 0:
#         contacts_data = stats['key_contacts']
#         sorted_contacts = sorted(contacts_data.items(), key=lambda x: x[1], reverse=True)
#         contacts, contact_counts = zip(*sorted_contacts)
#         top_contacts = contacts[:10]
#         top_counts = contact_counts[:10]
#         data = {
#             text['yaxis_contacts']: top_contacts,
#             text['xaxis_calls']: top_counts
#         }
#         df = pd.DataFrame(data)
#         fig6 = px.bar(df, x=text['xaxis_calls'], y=text['yaxis_contacts'], orientation='h', color=text['xaxis_calls'],
#                       color_continuous_scale='Greens')
#         fig6.update_layout(
#             xaxis_title=text['xaxis_calls'],
#             yaxis_title=text['yaxis_contacts'],
#             title_text='',
#             xaxis_tickfont_size=16,
#             yaxis_tickfont_size=16,
#             xaxis_title_font_size=18,
#             yaxis_title_font_size=18,
#             showlegend=False,
#             coloraxis_showscale=False  # Hide color scale for this chart
#         )
#         # Order the bars from longest at the top to shortest at the bottom
#         fig6.update_yaxes(categoryorder='total descending')
#         figures.append(fig6)
#         titles.append(text['key_contacts_bar_title'])

#         # Pie chart for contacts
#         data = {
#             text['yaxis_contacts']: top_contacts,
#             text['xaxis_calls']: top_counts
#         }
#         df = pd.DataFrame(data)
#         fig7 = px.pie(df, values=text['xaxis_calls'], names=text['yaxis_contacts'], hole=.3,
#                       color_discrete_sequence=px.colors.qualitative.Pastel)
#         fig7.update_traces(textposition='inside',
#                            texttemplate='%{percent:.1%}<br>(%{value})')
#         fig7.update_layout(
#             title_text='',
#             legend_title_text=text['yaxis_contacts'],
#         )
#         figures.append(fig7)
#         titles.append(text['key_contacts_pie_title'])

#     # 5. Most Active Periods of Communication (Heatmap)
#     if len(stats['activity_periods']) != 0:
#         activity_data = pd.DataFrame(stats['activity_periods']).T
#         activity_data.index = pd.to_datetime(activity_data.index).date  # Convert index to datetime
#         activity_data = activity_data.sort_index()
#         # Keep 'total_calls' for the line chart
#         line_data = activity_data[['total_calls']].copy()
#         # For the heatmap, drop 'total_calls'
#         activity_data = activity_data.drop(columns='total_calls')
#         activity_data.reset_index(inplace=True)
#         activity_data_melt = activity_data.melt(id_vars='index', var_name=text['xaxis_time'], value_name=text['calls'])

#         fig8 = px.density_heatmap(activity_data_melt, x=text['xaxis_time'], y='index', z=text['calls'],
#                                   color_continuous_scale='Viridis')
#         fig8.update_layout(
#             xaxis_title=text['xaxis_time'],
#             yaxis_title=text['xaxis_date'],
#             title_text='',
#             xaxis_tickfont_size=16,
#             yaxis_tickfont_size=16,
#             xaxis_title_font_size=18,
#             yaxis_title_font_size=18,
#             coloraxis_colorbar=dict(
#                 title=text['calls'],
#                 lenmode='fraction',
#                 len=1.0,  # Set the length of the colorbar to 100% of the subplot height
#                 yanchor='middle',
#                 y=0.5  # Center the colorbar vertically in the subplot
#             )
#         )
#         figures.append(fig8)
#         titles.append(text['heatmap_title'])

#         # 6. Total Calls per Day (Line Chart)
#         line_data.reset_index(inplace=True)
#         fig9 = px.line(line_data, x='index', y='total_calls')
#         fig9.update_layout(
#             xaxis_title=text['xaxis_date'],
#             yaxis_title=text['xaxis_calls_total'],
#             title_text='',
#             xaxis_tickfont_size=12,
#             yaxis_tickfont_size=12,
#             xaxis_title_font_size=14,
#             yaxis_title_font_size=14,
#         )
#         fig9.update_traces(mode='lines+markers', marker=dict(size=6, color='royalblue'), line=dict(color='royalblue'))
#         fig9.update_xaxes(tickangle=45, tickformat='%Y-%m-%d')
#         figures.append(fig9)
#         titles.append(text['line_chart_title'])

#     # 7. Country Activity (Donut Chart)
#     if 'country_activity' in stats and len(stats['country_activity']) != 0:
#         country_data = stats['country_activity']
#         # Optional: Limit to top N countries and group the rest as 'Others'
#         top_n = 10
#         sorted_countries = sorted(country_data.items(), key=lambda x: x[1], reverse=True)
#         if len(sorted_countries) > top_n:
#             top_countries = sorted_countries[:top_n]
#             others_total = sum(count for _, count in sorted_countries[top_n:])
#             top_countries.append(('Others', others_total))
#         else:
#             top_countries = sorted_countries

#         countries, counts = zip(*top_countries)
#         data = {
#             text['country']: countries,
#             text['xaxis_calls']: counts
#         }
#         df = pd.DataFrame(data)
#         fig10 = px.pie(df, values=text['xaxis_calls'], names=text['country'], hole=.3,
#                        color_discrete_sequence=px.colors.qualitative.Pastel)
#         fig10.update_traces(textposition='inside',
#                             texttemplate='%{percent:.1%}<br>(%{value})')
#         fig10.update_layout(
#             title_text='',
#             legend_title_text=text['country'],
#         )
#         figures.append(fig10)
#         titles.append(text['country_donut_title'])

#     # 8. City Activity (Donut Chart)
#     if 'city_activity' in stats and len(stats['city_activity']) != 0:
#         city_data = stats['city_activity']
#         # Optional: Limit to top N cities and group the rest as 'Others'
#         top_n = 10
#         sorted_cities = sorted(city_data.items(), key=lambda x: x[1], reverse=True)
#         if len(sorted_cities) > top_n:
#             top_cities = sorted_cities[:top_n]
#             others_total = sum(count for _, count in sorted_cities[top_n:])
#             top_cities.append(('Others', others_total))
#         else:
#             top_cities = sorted_cities

#         cities, counts = zip(*top_cities)
#         data = {
#             text['city']: cities,
#             text['xaxis_calls']: counts
#         }
#         df = pd.DataFrame(data)
#         fig11 = px.pie(df, values=text['xaxis_calls'], names=text['city'], hole=.3,
#                        color_discrete_sequence=px.colors.qualitative.Pastel)
#         fig11.update_traces(textposition='inside',
#                             texttemplate='%{percent:.1%}<br>(%{value})')
#         fig11.update_layout(
#             title_text='',
#             legend_title_text=text['city'],
#         )
#         figures.append(fig11)
#         titles.append(text['city_donut_title'])

#     # Determine specs based on trace types
#     for fig in figures:
#         trace_type = fig.data[0].type
#         subplot_type = trace_type_to_subplot_type.get(trace_type, 'xy')
#         specs.append([{'type': subplot_type}])

#     # Create a combined figure with subplots
#     num_charts = len(figures)
#     fig_combined = make_subplots(rows=num_charts, cols=1, subplot_titles=titles,
#                                  vertical_spacing=0.02, specs=specs)

#     # Add traces to the combined figure
#     for i, fig in enumerate(figures):
#         for trace in fig.data:
#             fig_combined.add_trace(trace, row=i+1, col=1)

#         # Update axes properties if needed
#         fig_combined.update_xaxes(title_text=fig.layout.xaxis.title.text, row=i+1, col=1)
#         fig_combined.update_yaxes(title_text=fig.layout.yaxis.title.text, row=i+1, col=1)

#         # Update colorbar position for heatmap
#         if 'coloraxis' in fig.layout:
#             fig_combined.layout.coloraxis.colorbar.update(
#                 lenmode='fraction',
#                 len=.8 / num_charts,  # Adjust the colorbar height proportionally
#                 yanchor='middle',
#                 y=1 - (i + 0.5) / (num_charts + 4.3)  # Position the colorbar next to its subplot
#             )

#     # Adjust the layout of the combined figure
#     fig_combined.update_layout(
#         height=600 * num_charts,  # Adjust height as needed
#         showlegend=False,
#         title_text='Combined Call Statistics',
#         title_font_size=24,
#     )

#     # Show the combined figure
#     fig_combined.show()



import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import re

def chart_generation(stats, language='ru'):
    translations = {
        'eng': {
            'bar_chart_title': 'Incoming vs Outgoing Calls (Bar Chart)',
            'pie_chart_title': 'Incoming vs Outgoing Calls (Pie Chart)',
            'average_duration_title': 'Average Call Duration Statistics',
            'stacked_bar_title': 'Call Apps Usage (Stacked Bar Chart)',
            'app_pie_chart_title': 'Call Apps Usage (Pie Chart)',
            'key_contacts_bar_title': 'Top 10 Key Contacts by Number of Calls (Bar Chart)',
            'key_contacts_pie_title': 'Top 10 Key Contacts by Number of Calls (Pie Chart)',
            'heatmap_title': 'Most Active Periods of Communication (Heatmap)',
            'line_chart_title': 'Total Calls per Day (Line Chart)',
            'country_donut_title': 'Calls by Country (Donut Chart)',
            'city_donut_title': 'Calls by City (Donut Chart)',
            'xaxis_calls': 'Number of Calls',
            'xaxis_date': 'Date',
            'yaxis_contacts': 'Contacts',
            'xaxis_time': 'Time of Day',
            'yaxis_duration': 'Average Duration (seconds)',
            'xaxis_apps': 'Apps',
            'xaxis_app': 'App',
            'xaxis_call_type': 'Call Type',
            'xaxis_calls_incoming': 'Incoming Calls',
            'xaxis_calls_outgoing': 'Outgoing Calls',
            'xaxis_calls_total': 'Total Calls',
            'index': 'index',
            'calls': 'Calls',
            'city': 'City',
            'country': 'Country',
        },
        'ru': {
            'bar_chart_title': 'Входящие и исходящие звонки (Гистограмма)',
            'pie_chart_title': 'Входящие и исходящие звонки (Круговая диаграмма)',
            'average_duration_title': 'Средняя длительность звонков',
            'stacked_bar_title': 'Использование приложений для звонков (Сложенная гистограмма)',
            'app_pie_chart_title': 'Использование приложений для звонков (Круговая диаграмма)',
            'key_contacts_bar_title': 'Топ-10 ключевых контактов по количеству звонков',
            'key_contacts_pie_title': 'Топ-10 ключевых контактов (Круговая диаграмма)',
            'heatmap_title': 'Активные периоды общения (Тепловая карта)',
            'line_chart_title': 'Общее количество звонков в день (Линейный график)',
            'country_donut_title': 'Звонки по странам (Круговая диаграмма)',
            'city_donut_title': 'Звонки по городам (Круговая диаграмма)',
            'xaxis_calls': 'Количество звонков',
            'xaxis_date': 'Дата',
            'yaxis_contacts': 'Контакты',
            'xaxis_time': 'Время суток',
            'yaxis_duration': 'Средняя длительность (секунды)',
            'xaxis_apps': 'Приложения',
            'xaxis_app': 'Приложение',
            'xaxis_call_type': 'Тип звонка',
            'xaxis_calls_incoming': 'Входящие звонки',
            'xaxis_calls_outgoing': 'Исходящие звонки',
            'xaxis_calls_total': 'Все звонки',
            'index': 'индекс',
            'calls': 'Звонки',
            'city': 'Город',
            'country': 'Страна',
        }
    }
    text = translations[language]
    figures = []
    titles = []

    # 1. Incoming vs Outgoing Calls (Bar Chart)
    data = {
        text['xaxis_call_type']: [text['xaxis_calls_incoming'], text['xaxis_calls_outgoing']],
        text['xaxis_calls']: [stats['incoming'], stats['outgoing']]
    }
    df = pd.DataFrame(data)
    fig1 = px.bar(df, x=text['xaxis_call_type'], y=text['xaxis_calls'], color=text['xaxis_call_type'],
                  color_discrete_sequence=['skyblue', 'salmon'])
    fig1.update_layout(
        xaxis_title=text['xaxis_call_type'],
        yaxis_title=text['xaxis_calls'],
        title_text='',
        xaxis_tickfont_size=16,
        yaxis_tickfont_size=16,
        xaxis_title_font_size=18,
        yaxis_title_font_size=18,
        showlegend=False
    )
    figures.append(fig1)
    titles.append(text['bar_chart_title'])

    # Pie chart
    fig2 = px.pie(df, values=text['xaxis_calls'], names=text['xaxis_call_type'],
                  color=text['xaxis_call_type'],
                  hole=.3,
                  color_discrete_sequence=['skyblue', 'salmon'])
    fig2.update_traces(textposition='inside',
                       texttemplate='%{percent:.1%}<br>(%{value})')
    fig2.update_layout(
        title_text='',
        legend_title_text=text['xaxis_call_type'],
    )
    figures.append(fig2)
    titles.append(text['pie_chart_title'])

    # 2. Average Call Duration Statistics (Bar Chart)
    call_durations = [
        stats['call_duration']['incoming_calls']['average_duration'],
        stats['call_duration']['outgoing_calls']['average_duration'],
        stats['call_duration']['total_calls']['average_duration']
    ]
    labels = [text['xaxis_calls_incoming'], text['xaxis_calls_outgoing'], text['xaxis_calls_total']]
    data = {
        text['xaxis_call_type']: labels,
        text['yaxis_duration']: call_durations
    }
    df = pd.DataFrame(data)
    fig3 = px.bar(df, x=text['xaxis_call_type'], y=text['yaxis_duration'], color=text['xaxis_call_type'],
                  color_discrete_sequence=['lightblue', 'lightblue', 'lightblue'])
    fig3.update_layout(
        xaxis_title=text['xaxis_call_type'],
        yaxis_title=text['yaxis_duration'],
        title_text='',
        xaxis_tickfont_size=16,
        yaxis_tickfont_size=16,
        xaxis_title_font_size=18,
        yaxis_title_font_size=18,
        showlegend=False
    )
    figures.append(fig3)
    titles.append(text['average_duration_title'])

    # 3. Call Apps Usage (Stacked Bar Chart)
    apps_data = stats['call_apps']
    apps = list(apps_data.keys())
    incoming_calls = [apps_data[app]['incoming'] for app in apps]
    outgoing_calls = [apps_data[app]['outgoing'] for app in apps]
    data = {
        text['xaxis_apps']: apps,
        text['xaxis_calls_incoming']: incoming_calls,
        text['xaxis_calls_outgoing']: outgoing_calls
    }
    df = pd.DataFrame(data)
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(name=text['xaxis_calls_incoming'], x=df[text['xaxis_apps']], y=df[text['xaxis_calls_incoming']], marker_color='skyblue'))
    fig4.add_trace(go.Bar(name=text['xaxis_calls_outgoing'], x=df[text['xaxis_apps']], y=df[text['xaxis_calls_outgoing']], marker_color='salmon'))
    fig4.update_layout(
        barmode='stack',
        xaxis_title=text['xaxis_apps'],
        yaxis_title=text['xaxis_calls'],
        title_text='',
        xaxis_tickfont_size=16,
        yaxis_tickfont_size=16,
        xaxis_title_font_size=18,
        yaxis_title_font_size=18,
        legend_title_text=text['xaxis_call_type'],
        legend_font_size=16,
        showlegend=True
    )
    figures.append(fig4)
    titles.append(text['stacked_bar_title'])

    # Pie chart for apps
    total_calls_per_app = {app: apps_data[app]['incoming'] + apps_data[app]['outgoing'] for app in apps}
    labels = list(total_calls_per_app.keys())
    sizes = list(total_calls_per_app.values())
    data = {
        text['xaxis_app']: labels,
        text['xaxis_calls_total']: sizes
    }
    df = pd.DataFrame(data)
    fig5 = px.pie(df, values=text['xaxis_calls_total'], names=text['xaxis_app'],
                  hole=.3,
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    fig5.update_traces(textposition='inside',
                       texttemplate='%{percent:.1%}<br>(%{value})')
    fig5.update_layout(
        title_text='',
        legend_title_text=text['xaxis_app'],
    )
    figures.append(fig5)
    titles.append(text['app_pie_chart_title'])

    # 4. Key Contacts (Horizontal Bar Chart)
    if len(stats['key_contacts']) != 0:
        contacts_data = stats['key_contacts']
        sorted_contacts = sorted(contacts_data.items(), key=lambda x: x[1], reverse=True)
        contacts, contact_counts = zip(*sorted_contacts)
        top_contacts = contacts[:10]
        top_counts = contact_counts[:10]
        data = {
            text['yaxis_contacts']: top_contacts,
            text['xaxis_calls']: top_counts
        }
        df = pd.DataFrame(data)
        fig6 = px.bar(df, x=text['xaxis_calls'], y=text['yaxis_contacts'], orientation='h', color=text['xaxis_calls'],
                      color_continuous_scale='Greens')
        fig6.update_layout(
            xaxis_title=text['xaxis_calls'],
            yaxis_title=text['yaxis_contacts'],
            title_text='',
            xaxis_tickfont_size=16,
            yaxis_tickfont_size=16,
            xaxis_title_font_size=18,
            yaxis_title_font_size=18,
            showlegend=False,
            coloraxis_showscale=False
        )
        fig6.update_yaxes(categoryorder='total descending')
        figures.append(fig6)
        titles.append(text['key_contacts_bar_title'])

        # Pie chart for contacts
        data = {
            text['yaxis_contacts']: top_contacts,
            text['xaxis_calls']: top_counts
        }
        df = pd.DataFrame(data)
        fig7 = px.pie(df, values=text['xaxis_calls'], names=text['yaxis_contacts'], hole=.3,
                      color_discrete_sequence=px.colors.qualitative.Pastel)
        fig7.update_traces(textposition='inside',
                           texttemplate='%{percent:.1%}<br>(%{value})')
        fig7.update_layout(
            title_text='',
            legend_title_text=text['yaxis_contacts'],
        )
        figures.append(fig7)
        titles.append(text['key_contacts_pie_title'])

    # 5. Most Active Periods of Communication (Heatmap)
    if len(stats['activity_periods']) != 0:
        activity_data = pd.DataFrame(stats['activity_periods']).T
        activity_data.index = pd.to_datetime(activity_data.index).date
        activity_data = activity_data.sort_index()
        line_data = activity_data[['total_calls']].copy()
        activity_data = activity_data.drop(columns='total_calls')
        activity_data.reset_index(inplace=True)
        activity_data_melt = activity_data.melt(id_vars='index', var_name=text['xaxis_time'], value_name=text['calls'])

        fig8 = px.density_heatmap(activity_data_melt, x=text['xaxis_time'], y='index', z=text['calls'],
                                  color_continuous_scale='Viridis')
        fig8.update_layout(
            xaxis_title=text['xaxis_time'],
            yaxis_title=text['xaxis_date'],
            title_text='',
            xaxis_tickfont_size=16,
            yaxis_tickfont_size=16,
            xaxis_title_font_size=18,
            yaxis_title_font_size=18,
            coloraxis_colorbar=dict(
                title=text['calls'],
                lenmode='fraction',
                len=1.0,
                yanchor='middle',
                y=0.5
            )
        )
        figures.append(fig8)
        titles.append(text['heatmap_title'])

        # 6. Total Calls per Day (Line Chart)
        line_data.reset_index(inplace=True)
        fig9 = px.line(line_data, x='index', y='total_calls')
        fig9.update_layout(
            xaxis_title=text['xaxis_date'],
            yaxis_title=text['xaxis_calls_total'],
            title_text='',
            xaxis_tickfont_size=12,
            yaxis_tickfont_size=12,
            xaxis_title_font_size=14,
            yaxis_title_font_size=14,
        )
        fig9.update_traces(mode='lines+markers', marker=dict(size=6, color='royalblue'), line=dict(color='royalblue'))
        fig9.update_xaxes(tickangle=45, tickformat='%Y-%m-%d')
        figures.append(fig9)
        titles.append(text['line_chart_title'])

    # 7. Country Activity (Donut Chart)
    if 'country_activity' in stats and len(stats['country_activity']) != 0:
        country_data = stats['country_activity']
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
            text['country']: countries,
            text['xaxis_calls']: counts
        }
        df = pd.DataFrame(data)
        fig10 = px.pie(df, values=text['xaxis_calls'], names=text['country'], hole=.3,
                       color_discrete_sequence=px.colors.qualitative.Pastel)
        fig10.update_traces(textposition='inside',
                            texttemplate='%{percent:.1%}<br>(%{value})')
        fig10.update_layout(
            title_text='',
            legend_title_text=text['country'],
        )
        figures.append(fig10)
        titles.append(text['country_donut_title'])

    # 8. City Activity (Donut Chart)
    if 'city_activity' in stats and len(stats['city_activity']) != 0:
        city_data = stats['city_activity']
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
            text['city']: cities,
            text['xaxis_calls']: counts
        }
        df = pd.DataFrame(data)
        fig11 = px.pie(df, values=text['xaxis_calls'], names=text['city'], hole=.3,
                       color_discrete_sequence=px.colors.qualitative.Pastel)
        fig11.update_traces(textposition='inside',
                            texttemplate='%{percent:.1%}<br>(%{value})')
        fig11.update_layout(
            title_text='',
            legend_title_text=text['city'],
        )
        figures.append(fig11)
        titles.append(text['city_donut_title'])

    # Save each figure as a PNG file
    for fig, title in zip(figures, titles):
        # Sanitize the title to create a filename
        filename = re.sub(r'[^\w\s-]', '', title)  # Remove special characters
        filename = filename.replace(' ', '_')       # Replace spaces with underscores
        filename = filename.lower()                 # Convert to lowercase
        filename = f"{filename}.png"
        # Save the figure as a PNG file
        fig.show()

