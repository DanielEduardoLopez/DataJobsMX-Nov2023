### DATA JOBS IN MEXICO DASHBOARD

"""
By Daniel Eduardo López
Date: 14 January 2024
GitHub: https://github.com/DanielEduardoLopez
LinkedIn: https://www.linkedin.com/in/daniel-eduardo-lopez
"""

#!pip install dash

# Run this app with 'python 3_Dashboard.py' and
# visit http://127.0.0.1:8050/ in your web browser.

# Import required libraries
import numpy as np
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px
import plotly.graph_objects as go

# Read the Job data into a Pandas dataframe
df = pd.read_csv("https://raw.githubusercontent.com/DanielEduardoLopez/DataJobsMX-Nov2023/main/Dataset_processed.csv")\
     .rename(columns = {'Avg Salary': 'Salary'}).drop(columns=['Original Job Title', 'Min Salary',	'Max Salary'])

max_salary = df['Salary'].max()
min_salary = df['Salary'].min()


# Settings

category_order = ['ML Engineer',
                  'Data Architect', 
                  'Data Engineer', 
                  'Data Scientist', 
                  'Business Analyst', 
                  'BI Analyst',
                  'Data Analyst']


# Plotting functions

# Job Demand: Pie Chart
def plot_pie_chart(df):

    job_df = pd.DataFrame(df['Job'].value_counts().reset_index()).rename(columns = {'count': 'Count'})

    pie_colors = ['#154360','#539ecd','#89bedc',"#a9cce3", "#d4e6f1",'#dbe9f6', "#ebf5fb"]

    demand_job_plot = px.pie(job_df, 
                            values='Count', 
                            names='Job', 
                            color = 'Job', 
                            hole = 0.7,  
                            color_discrete_sequence=px.colors.sequential.Blues_r,
                            height=450,
                            title='Demand of Data Jobs Per Category'
                            )
    
    demand_job_plot.update_traces(hoverinfo='label+percent+name', 
                                  textinfo='percent',                                 
                                  texttemplate='%{percent:.1%}',
                                  textfont_size=16,
                                  direction ='clockwise',                                
                                  marker=dict(colors=pie_colors, line=dict(color="rgba(0,0,0,0)", width=4))
                                  )
    
    demand_job_plot.update_layout(transition_duration=400, 
                                  title_x=0.5, 
                                  paper_bgcolor="rgba(0,0,0,0)", 
                                  plot_bgcolor="rgba(0,0,0,0)",
                                  legend=dict(
                                      #yanchor="bottom",
                                      y=0.01,
                                      #xanchor="right",
                                      x=0.99,
                                      bgcolor='#f0f0f0',
                                      bordercolor='#cbcccd',
                                      borderwidth=1.5
                                      )
                                  )
    
    return demand_job_plot

# Sample size and Avg Salary: Card
def plot_card(df):

    sample_size = len(df)

    avg_salary = np.mean(df['Salary'])

    card = go.Figure()

    card.add_trace(go.Indicator(
        mode="number",
        value=avg_salary,
        title={
            "text": "Avg. Mth. Salary (MXN)",
            "font": {"size": 15}
        },
        number={"font": {"size": 30}},
        domain = {'row': 0, 'column': 1})
    )

    card.add_trace(go.Indicator(
        mode="number",
        value=sample_size,
        title={
            "text": "Number of Data Jobs",
            "font": {"size": 15}
            },
        number={"font": {"size": 30}},
        domain = {'row': 1, 'column': 1})
    )

    card.update_layout(paper_bgcolor = "#B3D5FA",
                        grid = {'rows': 2, 'columns': 1, 'pattern': "independent"},
                       width = 210,
                        height = 150,
                       margin = {'t': 25, 'r': 0, 'l': 0, 'b': 0}
                      )

    return card


# Company Demand: Treemap
def plot_treemap(df):

    top = 20

    company_df =  (df.groupby(by='Company', as_index=False)['Job'].count()
                  .sort_values(by = 'Job', ascending = False)
                  .rename(columns = {'Job': 'Vacancies'})[:top]
                  .assign(Company=lambda d:d['Company'].map(lambda x: x[:15]))
                )

    company_df = company_df[company_df['Vacancies'] > 0]

    demand_company_plot = px.treemap(company_df, path = [px.Constant("."), 'Company'], values='Vacancies', color = 'Vacancies', 
                                    color_continuous_scale=px.colors.sequential.Blues,
                                    title= f'Top {top} Companies Demanding Data Jobs'
                                    )
    demand_company_plot.update_layout(transition_duration=400, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
      
    return demand_company_plot

# Alternative: Company Demand: Bar Chart
def plot_barchart(df):

    top = 30

    company_df = (df.groupby(by = 'Company', as_index= False)['Job'].count()
                  .sort_values(by = 'Job', ascending = False)
                  .rename(columns = {'Job': 'Vacancies'})[:top]
                  .assign(Company= lambda d:d['Company'].map(lambda x: x[:25]))
                )
    company_df = company_df[company_df['Vacancies'] > 0]

    demand_company_plot = px.bar(company_df.sort_values(by = 'Vacancies'), 
                                x='Vacancies', 
                                y='Company',
                                #color = 'Vacancies', 
                                color_continuous_scale=px.colors.sequential.Blues,
                                #text="Vacancies",
                                height=720,
                                title= f'Top {top} Companies Demanding Data Jobs',
                                opacity = 0.7)

    demand_company_plot.update_traces(marker_color= px.colors.sequential.Blues[7], 
                                      marker_line_color='white', 
                                      textfont_size=11, 
                                      textangle=0,
                                      textposition="outside", 
                                      cliponaxis=False, 
                                      hovertemplate=None)

    demand_company_plot.update_layout(transition_duration=400, 
                                      title_x=0.5, 
                                      paper_bgcolor="rgba(0,0,0,0)", 
                                      plot_bgcolor="#e1e7ff")

    demand_company_plot.update_layout(hovermode="x unified")

    return demand_company_plot

# Location Demand: Choropleth Map
def plot_cloropleth(df):

    # States dictionary with corresponding ID
    location_dict = {'Aguascalientes': 'AS', 
                    'Baja California': 'BC', 
                    'Baja California Sur': 'BS', 
                    'Campeche': 'CC',
                    'Ciudad de México':'DF',
                    'Chiapas': 'CS',
                    'Chihuahua':'CH',
                    'Coahuila':'CL',
                    'Colima':'CM',
                    'Durango':'DG',
                    'Estado de México':'MC',
                    'Guanajuato':'GT',
                    'Guerrero':'GR',
                    'Hidalgo':'HG',
                    'Jalisco':'JC',
                    'Michoacán':'MN',
                    'Morelos':'MS',
                    'Nayarit':'NT',
                    'Nuevo León':'NL',
                    'Oaxaca':'OC',
                    'Puebla':'PL',
                    'Querétaro':'QT',
                    'Quintana Roo':'QR',
                    'San Luis Potosí':'SP',
                    'Sinaloa':'SL',
                    'Sonora':'SR',
                    'Tabasco':'TC',
                    'Tamaulipas':'TS',
                    'Tlaxcala':'TL',
                    'Veracruz':'VZ',
                    'Yucatán':'YN',
                    'Zacatecas':'ZS'}

    location_df = (pd.DataFrame.from_dict(location_dict, orient='index').reset_index()
                  .rename(columns={"index": "State", 0: "ID"}).set_index('State')
                    )

    demand = (pd.DataFrame(df['Location'].value_counts())
              .reset_index()
              .rename(columns={'count':'Count', 'Location':'State'})
              .assign(total= lambda d: sum(d.Count))
              .assign(Percentage= lambda d: (d['Count'] / d.total )*100)
              .drop(columns=['total'])
              )

    location_df = location_df.merge(demand, left_on='State', right_on='State', how = 'outer').fillna(0)

    demand_location_plot = px.choropleth(location_df, 
                                        geojson = 'https://raw.githubusercontent.com/isaacarroyov/data_visualization_practice/master/Python/visualizing_mexican_wildfires_tds/data/states_mx.json', 
                                        locations='ID', 
                                        color='Percentage',
                                        color_continuous_scale="Blues",
                                        scope="north america",
                                        #title='Demand of Data Jobs per Mexican State',
                                        labels={'Percentage':'National <br>Demand %'}
                                        )
    demand_location_plot.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, 
                                      transition_duration=300,
                                      paper_bgcolor="rgba(0,0,0,0)", 
                                      plot_bgcolor="rgba(0,0,0,0)", 
                                      geo_bgcolor = "rgba(0,0,0,0)")
    demand_location_plot.update_geos(fitbounds="locations", 
                                    visible=False)
    demand_location_plot.update_layout(transition_duration=400, 
                                      title_x=0.5)
 
    return demand_location_plot

# Salary Per Job: Boxplot
def plot_boxplot(df):

    salary_job_df = df.dropna(axis = 0, how='any', subset = ['Salary'])

    salary_job_plot = px.box(salary_job_df, 
                            x = "Job", 
                            y = "Salary", 
                            color = "Job", 
                            points="all", 
                            color_discrete_sequence=px.colors.sequential.Blues_r,
                            category_orders={"Job": ['ML Engineer',
                                                    'Data Architect', 
                                                    'Data Engineer', 
                                                    'Data Scientist', 
                                                    'Business Analyst', 
                                                    'BI Analyst',
                                                    'Data Analyst']},
                            labels={
                                    "Salary": "Average Monthly Salary (MXN)",
                                    "Job": "Data Job Category"},
                            title='Salary Per Data Job Category',
                            height=450
                            )
    salary_job_plot.update_traces(showlegend=False)
    salary_job_plot.update_layout(transition_duration=400, 
                                  title_x=0.5, 
                                  paper_bgcolor="rgba(0,0,0,0)", 
                                  plot_bgcolor='#e1e7ff')
    salary_job_plot.update_yaxes(tickformat = '$,~s')

    return salary_job_plot

# Salary Per Company: Heatmap

def plot_heatmap(df):

    top = 30

    salary_job_df = df.dropna(axis = 0, how='any', subset = ['Salary'])

    salary_company_df = (pd.pivot_table(salary_job_df, index = 'Company', columns = 'Job', values = 'Salary', aggfunc= 'mean')
                        .assign(Total_Average= lambda d: d.mean(axis=1, numeric_only= True))
                        .fillna(0).sort_values('Total_Average', ascending = False)[:top]
                        .sort_values('Company', ascending = False)
                        .drop(columns = 'Total_Average').reset_index()
                        .rename(index = {'Job': 'Index'})
                        )                  

    salary_company_df = pd.melt(salary_company_df, id_vars = 'Company', var_name = 'Job', value_name = 'Salary')

    salary_company_plot = px.density_heatmap(salary_company_df, 
                                            y='Company', 
                                            x = 'Job', 
                                            z = 'Salary',
                                            histfunc="avg", 
                                            color_continuous_scale="Blues",
                                            height=720,
                                            title='Salary Per Company And Data Job Category',
                                            labels={"Job": "Data Job Category"},                                         
                                            #text_auto=True
                                            )
    salary_company_plot.update_layout(transition_duration=400, 
                                      title_x=0.5, 
                                      coloraxis_colorbar=dict(title="Avg. Mth. <br>Salary (MXN)"),
                                      paper_bgcolor="rgba(0,0,0,0)", 
                                      plot_bgcolor="rgba(0,0,0,0)")

    salary_company_plot.update_coloraxes(colorbar_tickformat = '$,~s')
    #salary_company_plot.update_traces(texttemplate="$%{z:,.0f}")

    return salary_company_plot

# Salary Per Location: Contour plot
def plot_contour(df):

    # States dictionary with corresponding ID
    location_dict = {'Aguascalientes': 'AS', 
                'Baja California': 'BC', 
                'Baja California Sur': 'BS', 
                'Campeche': 'CC',
                'Ciudad de México':'DF',
                'Chiapas': 'CS',
                'Chihuahua':'CH',
                'Coahuila':'CL',
                'Colima':'CM',
                'Durango':'DG',
                'Estado de México':'MC',
                'Guanajuato':'GT',
                'Guerrero':'GR',
                'Hidalgo':'HG',
                'Jalisco':'JC',
                'Michoacán':'MN',
                'Morelos':'MS',
                'Nayarit':'NT',
                'Nuevo León':'NL',
                'Oaxaca':'OC',
                'Puebla':'PL',
                'Querétaro':'QT',
                'Quintana Roo':'QR',
                'San Luis Potosí':'SP',
                'Sinaloa':'SL',
                'Sonora':'SR',
                'Tabasco':'TC',
                'Tamaulipas':'TS',
                'Tlaxcala':'TL',
                'Veracruz':'VZ',
                'Yucatán':'YN',
                'Zacatecas':'ZS'}

    location_df = (pd.DataFrame.from_dict(location_dict, orient='index')
                  .reset_index().rename(columns={"index": "State", 0: "ID"})
                  .set_index('State')
                    )

    demand = (pd.DataFrame(df['Location'].value_counts())
              .reset_index()
              .rename(columns={'count':'Count', 'Location':'State'})
              .assign(total= lambda d: sum(d.Count))
              .assign(Percentage= lambda d: (d['Count'] / d.total )*100)
              .drop(columns=['total'])
              )

    location_df = location_df.merge(demand, left_on='State', right_on='State', how = 'outer').fillna(0)

    salary_job_df = df.dropna(axis = 0, how='any', subset = ['Salary'])

    salary_location_df = (pd.pivot_table(data = salary_job_df, index = 'Location', columns = 'Job', values = 'Salary', aggfunc= 'mean')
                          .reset_index().merge(location_df, left_on='Location', right_on='State', how = 'outer')
                          .set_index('State').drop(columns =['ID', 'Count', 'Percentage', 'Location']).fillna(0)
                          .sort_values('State', ascending = False).reset_index()
                        )

    salary_location_df = pd.melt(salary_location_df, id_vars= 'State', var_name = 'Job', value_name = 'Salary')

    salary_location_plot = px.density_contour(salary_location_df, 
                                              y='State', 
                                              x='Job', 
                                              z='Salary',
                                              histfunc="avg", 
                                              color_discrete_sequence=px.colors.sequential.Blues_r,
                                              height=720,
                                              title='Salary Per Location And Data Job Category',
                                              labels={
                                                        "State": "Location",
                                                        'Job': 'Data Job Category'
                                                        }
                                                )

    salary_location_plot.update_traces(contours_coloring="fill", 
                                      contours_showlabels = True, 
                                      colorscale = 'Blues', 
                                      colorbar_tickformat='$,~s',
                                      colorbar_title_text='Avg. Mth. <br>Salary (MXN)')

    salary_location_plot.update_layout(transition_duration=400, 
                                      title_x=0.5, 
                                      coloraxis_colorbar=dict(title="Vacancies"),
                                      paper_bgcolor="rgba(0,0,0,0)", 
                                      plot_bgcolor="rgba(0,0,0,0)")

    return salary_location_plot


# Helper function for dropdowns
def create_dropdown_options(series):
    options = [{'label': i, 'value': i} for i in series.sort_values().unique()]
    options.insert(0, {'label': 'All', 'value': 'All'})
    return options

# Dash application
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div(children=[
                                # First section
                                # Adding Title
                                html.Div(children=[ html.H1('Data Jobs in Mexico Dashboard',
                                        style={'textAlign': 'center', 'color': 'white',
                                               'font-size': 40, 'font-family': 'Tahoma'})], 
                                               style={'margin-top': '0',
                                                      'width': '100%', 
                                                      'height': '60px', 
                                                      'background-color': 'navy', 
                                                      'float': 'center', 
                                                      'margin': '0'}  
                                        ),
                                
                                # Adding Author
                                html.P("By Daniel Eduardo López",
                                        style={'textAlign': 'center', 'color': 'navy',
                                               'font-size': 16, 'font-family': 'Tahoma'}),
                                dcc.Link(html.A('GitHub'), href="https://github.com/DanielEduardoLopez",
                                        style={'textAlign': 'center', 'color': 'navy',
                                               'font-size': 12, 'font-family': 'Tahoma',
                                               'margin': 'auto',
                                               'display': 'block'}),
                                
                                dcc.Link(html.A('LinkedIn'), href="https://www.linkedin.com/in/daniel-eduardo-lopez",
                                        style={'textAlign': 'center', 'color': 'navy',
                                               'font-size': 12, 'font-family': 'Tahoma',
                                               'margin': 'auto',
                                               'display': 'block'}),
                                # html.Br(),
                                
                                # Adding a very brief Introduction to the Dashboard
                                html.P("This Dashboard shows the Data Jobs demand and salaries in Mexico in February 2023.",
                                        style={'textAlign': 'center', 'color': 'black',
                                               'font-size': 14, 'font-family': 'Tahoma'}),
                                
                                html.P("- Data was collected on February 7, 2023 from the OCC website. -",
                                        style={'textAlign': 'center', 'color': 'navy',
                                               'font-size': 14, 'font-family': 'Tahoma'}),
                                html.Br(),
                                
                                # Second section: Dropdowns & Slider
                                html.Div(children=[
                                
                                      # Dropdown list to enable Data Job selection
                                      html.Br(),
                                      #html.Br(),

                                    html.Div(children=[
                                            html.Label("Data Job Selection:", className='dropdown-labels',
                                                    style={'textAlign': 'left', 'color': 'navy',
                                                      'font-size': 15, 'font-family': 'Tahoma'}
                                                    ),
                                            dcc.Dropdown(id='job_dropdown',
                                                      options=create_dropdown_options(df['Job']),
                                                      value='All',
                                                      placeholder="Select Data Job",
                                                      multi=True,
                                                      searchable=True,
                                                      style={'textAlign': 'left', 'color': '#2e2d2d',
                                                      'font-size': 14, 'font-family': 'Tahoma'}
                                                      ),
                                            ], id='first-selector',
                                            style={'margin-top': '0px',
                                                    'margin-left': '10px',
                                                    'margin-right': '0px',
                                                    'width': '25%',
                                                   'height': '80px',
                                                   'background-color': '#B3D5FA',
                                                   'float': 'center',
                                                   }
                                    ),

                                    # Dropdown list to enable Location selection
                                    html.Div(children=[
                                              html.Label("Location Selection:", className='dropdown-labels',
                                                        style={'textAlign': 'left', 'color': 'navy',
                                                          'font-size': 15, 'font-family': 'Tahoma'}
                                                        ),
                                              dcc.Dropdown(id='location_dropdown',
                                                          options=create_dropdown_options(df['Location']),
                                                          value='All',
                                                          placeholder="Select Location",
                                                          multi=True,
                                                          searchable=True,
                                                          style={'textAlign': 'left', 'color': '#2e2d2d',
                                                          'font-size': 14, 'font-family': 'Tahoma'}
                                                          ),
                                            ], id='second-selector',
                                            style={'margin-top': '-80px',
                                                    'margin-left': '28%',
                                                    'margin-right': '0px',
                                                    'width': '25%',
                                                   'height': '80px',
                                                   'background-color': '#B3D5FA',
                                                   'float': 'center',
                                                   }
                                    ),


                                      # Dropdown list to enable Company selection
                                    html.Div(children=[
                                              html.Label("Company Selection:", className='dropdown-labels',
                                                          style={'textAlign': 'left', 'color': 'navy',
                                                          'font-size': 15, 'font-family': 'Tahoma'}
                                                          ),
                                              dcc.Dropdown(id='company_dropdown',
                                                          options=create_dropdown_options(df['Company']),
                                                          value='All',
                                                          placeholder="Select Company",
                                                          multi=True,
                                                          searchable=True,
                                                          style={'textAlign': 'left', 'color': '#2e2d2d',
                                                          'font-size': 14, 'font-family': 'Tahoma'}
                                                          ),
                                    ], id='third-selector',
                                            style={'margin-top': '-80px',
                                                    'margin-left': '55%',
                                                    'margin-right': '0px',
                                                    'width': '25%',
                                                   'height': '80px',
                                                   'background-color': '#B3D5FA',
                                                   'float': 'center',
                                                   }
                                    ),
                                      # Checkbox for selecting only positions with disclosed salary 

                                    html.Div(children=[
                                              #html.Br(),
                                              dcc.Checklist(id='salary_filter',
                                                              options=['Enable Salary Range Selection'],
                                                              inline=True,
                                                              style={'textAlign': 'left', 'color': 'navy',
                                                              'font-size': 15, 'font-family': 'Tahoma'}
                                                              ),
                                              html.Label("(Displays Only Positions With Disclosed Salary)",
                                                        style={'textAlign': 'center', 'color': 'navy',
                                                          'font-size': 12, 'font-family': 'Tahoma'}
                                                        ),
                                    ], id='fourth-selector',
                                            style={'margin-top': '-60px',
                                                    'margin-left': '82%',
                                                    'margin-right': '10px',
                                                    'width': '18%',
                                                   'height': '80px',
                                                   'background-color': '#B3D5FA',
                                                   'float': 'center',
                                                   }
                                    ),
                                      
                                      # Range Slider for Salary selection

                                      html.Br(),

                                    html.Div(children=[
                                              html.Label("Salary Range Selection (MXN):",
                                                        style={'textAlign': 'left', 'color': 'navy',
                                                          'font-size': 15, 'font-family': 'Tahoma'}
                                                        ),
                                              dcc.RangeSlider(id='salary_slider',
                                                              min=0, max=140000, step=1000,
                                                              marks={0:  {'label': '$0', 'style': {'font-size': 16, 'font-family': 'Tahoma'}},
                                                                     20000: {'label': '$20,000', 'style': {'font-size': 16, 'font-family': 'Tahoma'}},
                                                                     40000: {'label': '$40,000', 'style': {'font-size': 16, 'font-family': 'Tahoma'}},
                                                                     60000: {'label': '$60,000', 'style': {'font-size': 16, 'font-family': 'Tahoma'}},
                                                                     80000: {'label': '$80,000', 'style': {'font-size': 16, 'font-family': 'Tahoma'}},
                                                                     100000: {'label': '$100,000', 'style': {'font-size': 16, 'font-family': 'Tahoma'}},
                                                                     120000: {'label': '$120,000', 'style': {'font-size': 16, 'font-family': 'Tahoma'}},
                                                                     140000: {'label': '$140,000', 'style': {'font-size': 16, 'font-family': 'Tahoma'}}
                                                                     },
                                                              value=[min_salary, max_salary]
                                                              ),
                                    ], id='fifth-selector',
                                            style={'margin-top': '-50px',
                                                    'margin-left': '0.5%',
                                                    'margin-right': '0.5%',
                                                    'width': '98%',
                                                   'height': '50px',
                                                   'background-color': '#B3D5FA',
                                                   'float': 'center',
                                                   }
                                    ),
                                                                                           

                                ], id='top-container',
                                style={'margin-top': '0px',
                                        'margin-left': '10px',
                                        'margin-right': '10px',
                                        'width': '99%',
                                       'height': '150px',
                                       'background-color': '#B3D5FA', 
                                       'float': 'center', 
                                       }
                                ),

                                # Third section: First Plot Section
                                html.Div(children=[

                                      # First Plot
                                      html.Div(children=[

                                            # Job Demand Plot: Donnut chart
                                            dcc.Graph(id='demand_job_plot'),                                   
                                    
                                            ], id='Donut_chart',
                                              style={'margin-top': '0px',
                                                      'margin-left': '-6%',
                                                      'width': '40%',
                                                      'height': '400px',                                                                                                            
                                                      }                                                
                                            ),

                                    # Card with Data Jobs Info
                                    html.Div(children=[

                                        # Card
                                        dcc.Graph(id='card'),

                                    ], id='card-container',
                                        style={'margin-top': '-320px',
                                               'margin-left': '22%',
                                               #'width': '300px',
                                               #'height': '300px',
                                               }
                                    ),

                                      # Second plot
                                      html.Div(children=[
                                      
                                            # Job-Salary Plot: Boxplot
                                                  dcc.Graph(id='salary_job_plot'),
                                          
                                          ], id='Boxplot',
                                            style={'margin-top': '-230px',
                                                    'margin-left': '35.5%',
                                                    'width': '33%',
                                                    'height': '400px',                                                                                                            
                                                    }                                                
                                          ),

                                      # Third plot
                                      html.Div(children=[

                                            # Location Demand Plot: Map
                                            dcc.Graph(id='demand_location_plot'),
                                            ], id='Map',
                                            style={'margin-top': '-400px',
                                                    'margin-left': '60.5%',
                                                    'width': '40%',
                                                    'height': '400px',
                                                    }
                                            ),
                                ], id='middle-container',
                                style={'margin-top': '10px',
                                        'margin-left': '5px',
                                        'margin-right': '5px',
                                        'width': '99%',
                                       'height': '485px',
                                       'float': 'center',
                                       }
                                ),
                                      
                              # Fourth section: Second Plot Section
                              html.Div(children=[

                                            # Fourth Plot
                                            html.Div(children=[

                                            # Company Demand Plot: Barchart
                                            dcc.Graph(id='demand_company_plot'),

                                            ], id='Barchart',
                                            style={'margin-top': '0px',
                                                    'margin-left': '1%',
                                                    'width': '34%',
                                                    'height': '720px',
                                                    }                                                
                                            ),                                 

                                            # Fifth Plot
                                            html.Div(children=[

                                                # Company-Salary Plot: Heatmap
                                                dcc.Graph(id='salary_company_plot'),

                                                ], id='Heatmap',
                                                style={'margin-top': '-720px',
                                                        'margin-left': '31%',
                                                        'width': '36%',
                                                        'height': '720px',
                                                        }
                                                ),

                                          #Sixth Plot
                                          html.Div(children=[

                                                # Location-Salary Plot: Contourmap
                                                dcc.Graph(id='salary_location_plot'),

                                                ], id='Contourmap',
                                                style={'margin-top': '-720px',
                                                        'margin-left': '65%',
                                                        'width': '36%',
                                                        'height': '720px',
                                                        }
                                                ),


                                      
                                      ], id='bottom-container',
                                         style={'margin-top': '-30px',
                                                  'width': '100%',
                                                  'height': '720px'
                                                  }
                                      ),




                        ], id='entire-dashboard',
                           style={'width': '100%',
                                  'overflow': 'hidden',
                                  'background-color': 'aliceblue', #f2ffe3 soft green
                                 }
                        )




                             

# Callback Functions

# Callback function for 'job_dropdown' as input and 'demand_job_plot' as output
@app.callback([Output(component_id='demand_job_plot', component_property='figure'),
               Output(component_id='demand_company_plot', component_property='figure'),
               Output(component_id='demand_location_plot', component_property='figure'),
               Output(component_id='salary_job_plot', component_property='figure'),
               Output(component_id='salary_company_plot', component_property='figure'),
               Output(component_id='salary_location_plot', component_property='figure'),
               Output(component_id='card', component_property='figure')],
              [Input(component_id='job_dropdown', component_property='value'),
               Input(component_id='location_dropdown', component_property='value'),
               Input(component_id='company_dropdown', component_property='value'),
               Input(component_id='salary_slider', component_property='value'),
               Input(component_id='salary_filter', component_property='value')]
              )
def update_output(job, location, company, salary, salary_filter):
  """
  This function updates the output plots based on the parameters of:
  - job
  - location
  - company
  - salary
  """
  dff = df.copy()
  low, high = salary

  if salary_filter == ['Enable Salary Range Selection']:
    mask = (dff['Salary'] >= low) & (dff['Salary'] <= high)
    dff = dff[mask]

  if (job or company or location or salary) == None:
        raise PreventUpdate 
  
  if 'All' in job and 'All' in location and 'All' in company:
    
    demand_job_plot = plot_pie_chart(dff)
    demand_company_plot = plot_barchart(dff)
    demand_location_plot = plot_cloropleth(dff)
    salary_job_plot = plot_boxplot(dff)
    salary_company_plot = plot_heatmap(dff)
    salary_location_plot = plot_contour(dff)
    card = plot_card(dff)

  else:

        if ('All' in (company and location)) and ('All' not in job):
          dff = dff[dff.Job.isin(job)]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_barchart(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card = plot_card(dff)
        
        elif ('All' in (job and location)) and ('All' not in company):
          dff = dff[dff.Company.isin(company)]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_barchart(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card = plot_card(dff)
        
        elif ('All' in (company and job)) and ('All' not in location):
          dff = dff[dff.Location.isin(location)]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_barchart(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card = plot_card(dff)
        
        elif ('All' in job) and ('All' not in (company and location)):
          dff = dff[(dff.Company.isin(company)) & (dff.Location.isin(location))]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_barchart(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card = plot_card(dff)

        elif ('All' in location) and ('All' not in (company and job)):
          dff = dff[(dff.Company.isin(company)) & (dff.Job.isin(job))]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_barchart(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card = plot_card(dff)

        elif ('All' in company) and ('All' not in (location and job)):
          dff = dff[(dff.Location.isin(location)) & (dff.Job.isin(job))]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_barchart(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card = plot_card(dff)

        elif 'All' not in (company and location and job):
          dff = dff[(dff.Job.isin(job)) & (dff.Location.isin(location)) & (dff.Company.isin(company))]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_barchart(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card = plot_card(dff)
        
        else:
          raise PreventUpdate 

  return demand_job_plot, demand_company_plot, demand_location_plot, salary_job_plot, salary_company_plot, salary_location_plot, card

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
