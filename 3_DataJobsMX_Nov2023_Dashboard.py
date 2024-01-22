### DATA JOBS IN MEXICO DASHBOARD

"""
By Daniel Eduardo López
Date: 14 January 2024
LinkedIn: https://www.linkedin.com/in/daniel-eduardo-lopez
GitHub: https://github.com/DanielEduardoLopez
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

# Images

image_path = 'assets/icon.png'

# Settings

category_order = ['ML Engineer',
                  'Data Architect', 
                  'Data Engineer', 
                  'Data Scientist', 
                  'Business Analyst', 
                  'BI Analyst',
                  'Data Analyst']

# Color settings
light_bg_color= '#ececec'#'#f0f0f0' # platinum
shadow_color='#adadad'
dash_theme=px.colors.sequential.Blues#px.colors.sequential.PuBu
dash_theme_r=px.colors.sequential.Blues_r#px.colors.sequential.PuBu_r
dark_bg_color= dash_theme_r[0]

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
                            color_discrete_sequence=dash_theme_r,
                            height=280,
                            title='<b>Demand of Data Jobs Per Category</b>'
                            )
    
    demand_job_plot.update_traces(hoverinfo='label+percent+name', 
                                  textinfo='percent',                                 
                                  texttemplate='%{percent:.0%}',
                                  textfont_size=16,
                                  direction ='clockwise',                                
                                  marker=dict(colors=dash_theme_r, line=dict(color="rgba(0,0,0,0)", width=4))
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
                                      #bgcolor='#d6eaf8',
                                      bordercolor="rgba(0,0,0,0)"#'#2471a3',#blue
                                      #borderwidth=1.5
                                      ),
                                  margin={"r":0,"t":80,"l":0,"b":0}
                                  )
    
    return demand_job_plot

# Sample size and Avg Salary: Card
def plot_card_salary(df):
  
    avg_salary = np.mean(df['Salary'])

    card_salary = go.Figure()

    card_salary.add_trace(go.Indicator(
        mode="number",
        value=avg_salary,
        # title={
        #     "text": "<b>Mean Monthly Salary (MXN)</b>",
        #     "font": {"size": 15,'color': dark_bg_color},          
        # },
        number={"font": {"size": 30}},
        domain = {'row': 0, 'column': 1})
    )

    card_salary.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                        grid = {'rows': 1, 'columns': 1, 'pattern': "independent"},
                       width = 200,
                        height = 55,                        
                       margin = {'t': 5, 'r': 0, 'l': 0, 'b': 0}
                      )

    return card_salary


def plot_card_demand(df):

    sample_size = len(df)   

    card_demand = go.Figure()

    card_demand.add_trace(go.Indicator(
        mode="number",
        value=sample_size,
        # title={
        #     "text": "<b>Number of Data Jobs</b>",
        #     "font": {"size": 15, 'color': 'dark_bg_color'}
        #     },
        number={"font": {"size": 30}},
        domain = {'row': 1, 'column': 1}),
        
    )
 

    card_demand.update_layout(paper_bgcolor = "rgba(0,0,0,0)",
                        grid = {'rows': 1, 'columns': 1, 'pattern': "independent"},
                       width = 200,
                        height = 55,
                       margin = {'t': 5, 'r': 0, 'l': 0, 'b': 0}
                      )

    return card_demand

# Company Demand: Treemap
def plot_treemap(df):

    top = 10

    company_df =  (df.loc[lambda d: d['Company'] != 'Confidential']
                  .groupby(by='Company', as_index=False)['Job'].count()
                  .sort_values(by = 'Job', ascending = False)
                  .rename(columns = {'Job': 'Vacancies'})[:top]
                  .assign(Company=lambda d:d['Company'].map(lambda x: x[:15]))
                )

    company_df = company_df[company_df['Vacancies'] > 0]

    demand_company_plot = px.treemap(company_df, 
                                     path = [px.Constant("."), 'Company'], 
                                     values='Vacancies', 
                                     color = 'Vacancies', 
                                     color_continuous_scale=dash_theme,
                                     title= f'<b>Top {top} Companies Demanding Data Jobs</b>',
                                     height= 380,
                                     #width = 450,

                                    )
    
    demand_company_plot.update_layout(transition_duration=400, 
                                      paper_bgcolor="rgba(0,0,0,0)", 
                                      plot_bgcolor="rgba(0,0,0,0)",
                                      margin={"r":0,"t":80,"l":20,"b":20}
                                      )
      
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
                                        color_continuous_scale=dash_theme,
                                        scope="north america",
                                        height= 370,
                                        #title='Demand of Data Jobs per Mexican State',
                                        labels={'Percentage':'National <br>Demand %'}
                                        )
     
    demand_location_plot.update_geos(fitbounds="locations", 
                                    visible=False)
    
    demand_location_plot.update_layout(margin={"r":0,"t":40,"l":0,"b":15}, 
                                      transition_duration=400,
                                      paper_bgcolor="rgba(0,0,0,0)", 
                                      plot_bgcolor="rgba(0,0,0,0)", 
                                      geo_bgcolor = "rgba(0,0,0,0)",                                      
                                      title_x=0.5)   
    
    demand_location_plot.add_annotation(
                                        xanchor="center",
                                        yanchor='top',
                                        yshift=180,
                                        xshift=40,
                                        font={'size':17},
                                        text="<b>Demand of Data Jobs by Location</b>", # text
                                        showarrow=False,
                                        align="center",
                                        bgcolor="rgba(0, 0, 0, 0)",

)
 
    return demand_location_plot

# Salary Per Job: Boxplot
def plot_boxplot(df):

    salary_job_df = df.dropna(axis = 0, how='any', subset = ['Salary'])

    salary_job_plot = px.box(salary_job_df, 
                            x = "Job", 
                            y = "Salary", 
                            color = "Job", 
                            points="all", 
                            color_discrete_sequence=dash_theme_r,
                            category_orders={"Job": ['ML Engineer',
                                                    'Data Architect', 
                                                    'Data Engineer', 
                                                    'Data Scientist', 
                                                    'Business Analyst', 
                                                    'BI Analyst',
                                                    'Data Analyst']},
                            labels={
                                    "Salary": "Mean Monthly Salary (MXN)",
                                    "Job": "Data Job Category"},
                            title='<b>Salary Per Data Job Category</b>',
                            height=400
                            )
    salary_job_plot.update_traces(showlegend=False)
    salary_job_plot.update_layout(transition_duration=400, 
                                  title_x=0.5, 
                                  paper_bgcolor="rgba(0,0,0,0)", 
                                  plot_bgcolor='#e1e7ff',
                                  margin={"r":0,"t":50,"l":40,"b":0})
    salary_job_plot.update_yaxes(tickformat = '$,~s')

    return salary_job_plot

# Salary Per Company: Heatmap

def plot_heatmap(df):

    top = 15

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
                                            color_continuous_scale=dash_theme,
                                            height=440,
                                            title='<b>Salary Per Company And Data Job Category</b>',
                                            labels={"Job": ""},                                         
                                            #text_auto=True
                                            )
    salary_company_plot.update_layout(transition_duration=400, 
                                      title_x=0.5, 
                                      coloraxis_colorbar=dict(title="Avg. Mth. <br>Salary (MXN)"),
                                      paper_bgcolor="rgba(0,0,0,0)", 
                                      plot_bgcolor="rgba(0,0,0,0)",
                                      margin={"r":20,"t":50,"l":20,"b":40}
                                      )

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
                                              color_discrete_sequence=dash_theme_r,
                                              height=440,
                                              title='<b>Salary Per Location And Data Job Category</b>',
                                              labels={
                                                        "State": "Location",
                                                        'Job': ''
                                                        }
                                                )

    salary_location_plot.update_traces(contours_coloring="fill", 
                                      contours_showlabels = True, 
                                      colorscale = dash_theme, 
                                      colorbar_tickformat='$,~s',
                                      colorbar_title_text='Avg. Mth. <br>Salary (MXN)')

    salary_location_plot.update_layout(transition_duration=400, 
                                      title_x=0.5, 
                                      coloraxis_colorbar=dict(title="Vacancies"),
                                      paper_bgcolor="rgba(0,0,0,0)", 
                                      plot_bgcolor="rgba(0,0,0,0)",
                                      margin={"r":20,"t":50,"l":20,"b":40}
                                      )

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
                                html.Div(children=[ 
                                                   html.Br(),
                                                   html.Img(src=image_path,
                                                             style={
                                                            'margin-top': '15px',
                                                            'margin-left': '70%',
                                                            'width': '70px', 
                                                            'height': '70px', 
                                                            'float': 'center',
                                                        }),
                                                   html.H1("Dashboard of Data Jobs in Mexico",
                                                  style={'textAlign': 'center', 'color': '#002c5b', #'#3a3a3a', #'#0025a1',
                                                        'font-size': 40, 'font-family': 'Tahoma',
                                                        #'text-shadow': '0 0 3px #848484',
                                                        'margin-top': '-65px'
                                                        }),                                               
                                                    
                                               ], 
                                               style={'margin-top': '-25px',
                                                      'width': '100%', 
                                                      'height': '110px', 
                                                      #'background-color': '#B3D5FA', #'#C0C0C0', 
                                                      'float': 'center', 
                                                      }                                               
                                        ),
                                
                                html.Div(children=[ html.P('.',
                                        style={'textAlign': 'center', 'color': 'navy',
                                               'font-size': 5, 'font-family': 'Tahoma'})], 
                                               style={'margin-top': '-5px',
                                                      'width': '100%', 
                                                      'height': '10px', 
                                                      'background-color': dark_bg_color, 
                                                      'textAlign': 'center',
                                                      'float': 'center', 
                                                      'border-style': 'solid',
                                                      'border-color': 'White',
                                                      'border-width': '1px',
                                                      'border-radius': '10px',
                                                      'box-shadow': '3px 3px 3px '+shadow_color,
                                                      }  
                                              
                                        ),
                                
                                html.Br(),
                                html.Br(),
                                
                                # Second section: Dropdowns & Slider
                                html.Div(children=[
                                
                                      # Dropdown list to enable Data Job selection
                                      html.Br(),
                                      #html.Br(),

                                    html.Div(children=[
                                            html.P("Sliders:", 
                                                   className='dropdown-labels',
                                                    style={'textAlign': 'left', 'color': 'white', 'font-weight': 'bold',
                                                      'font-size': 20, 'font-family': 'Tahoma', 'text-shadow': '0 0 2px #fff'}
                                                    ),
                                            html.Br(),
                                            html.Div(
                                                html.Label("Data Job:", className='dropdown-labels',
                                                        style={'textAlign': 'left', 'color': 'white', 'font-weight': 'bold', 'text-shadow': '0 0 2px #fff',
                                                          'font-size': 17, 'font-family': 'Tahoma', }
                                                        ),  style={'background-color': dark_bg_color,}
                                            ),                                            
                                            dcc.Dropdown(id='job_dropdown',
                                                      options=create_dropdown_options(df['Job']),
                                                      value='All',
                                                      placeholder="Select Data Job",
                                                      multi=True,
                                                      searchable=True,
                                                      style={'textAlign': 'left', 'color': '#2e2d2d',
                                                      'font-size': 15, 'font-family': 'Tahoma'}
                                                      ),
                                            ], id='first-selector',
                                            style={'margin-top': '15px',
                                                    'margin-left': '10px',
                                                    'margin-right': '0px',
                                                    'width': '90%',
                                                   'height': '80px',
                                                   #'background-color': dark_bg_color,
                                                   'float': 'center',
                                                   }
                                    ),

                                    # Dropdown list to enable Location selection
                                    html.Div(children=[
                                              html.Div(
                                                  html.Label("Location:", className='dropdown-labels',
                                                            style={'textAlign': 'left', 'color': 'white','font-weight': 'bold', 'text-shadow': '0 0 2px #fff',
                                                              'font-size': 17, 'font-family': 'Tahoma'}
                                                            ), style={'background-color': dark_bg_color,}

                                              ),                                              
                                              dcc.Dropdown(id='location_dropdown',
                                                          options=create_dropdown_options(df['Location']),
                                                          value='All',
                                                          placeholder="Select Location",
                                                          multi=True,
                                                          searchable=True,
                                                          style={'textAlign': 'left', 'color': '#2e2d2d',
                                                          'font-size': 15, 'font-family': 'Tahoma'}
                                                          ),
                                            ], id='second-selector',
                                            style={'margin-top': '60px',
                                                    'margin-left': '10px',
                                                    'margin-right': '0px',
                                                    'width': '90%',
                                                   'height': '80px',
                                                   #'background-color': dark_bg_color,
                                                   'float': 'center',
                                                   }
                                    ),


                                      # Dropdown list to enable Company selection
                                    html.Div(children=[
                                               html.Div(
                                                  html.Label("Company:", className='dropdown-labels',
                                                              style={'textAlign': 'left', 'color': 'white','font-weight': 'bold', 'text-shadow': '0 0 2px #fff',
                                                              'font-size': 17, 'font-family': 'Tahoma'}
                                                              ), style={'background-color': dark_bg_color,}
                                               ),                                              
                                              dcc.Dropdown(id='company_dropdown',
                                                          options=create_dropdown_options(df['Company']),
                                                          value='All',
                                                          placeholder="Select Company",
                                                          multi=True,
                                                          searchable=True,
                                                          style={'textAlign': 'left', 'color': '#2e2d2d',
                                                          'font-size': 15, 'font-family': 'Tahoma'}
                                                          ),
                                    ], id='third-selector',
                                            style={'margin-top': '0px',
                                                    'margin-left': '10px',
                                                    'margin-right': '0px',
                                                    'width': '90%',
                                                   'height': '80px',
                                                   #'background-color': dark_bg_color,
                                                   'float': 'center',
                                                   }
                                    ),
                                      # Checkbox for selecting only positions with disclosed salary 

                                    html.Div(children=[
                                              
                                              dcc.Checklist(id='salary_filter',
                                                              options=['Enable Salary Range Selection'],
                                                              inline=True,
                                                              style={'textAlign': 'left', 'color': 'white', 'font-weight': 'bold',
                                                              'font-size': 17, 'font-family': 'Tahoma'}
                                                              ),
                                              html.Br(),
                                              html.Label("(Displays only positions with disclosed salary)",
                                                        style={'textAlign': 'center', 'color': 'white',
                                                          'font-size': 15, 'font-family': 'Tahoma'}
                                                        ),
                                    ], id='fourth-selector',
                                            style={'margin-top': '10px',
                                                    'margin-left': '10px',
                                                    'margin-right': '10px',
                                                    'width': '90%',
                                                   'height': '80px',
                                                   #'background-color': dark_bg_color,
                                                   'float': 'center',
                                                   }
                                    ),
                                      
                                      # Range Slider for Salary selection


                                    html.Div(children=[
                                              html.Div(
                                              html.Label("Salary Range (MXN):",
                                                        style={'textAlign': 'left', 'color': 'white', 'font-weight': 'bold', 'text-shadow': '0 0 2px #fff',
                                                          'font-size': 17, 'font-family': 'Tahoma'}
                                                        ), style={'background-color': dark_bg_color,}
                                              ),
                                              
                                              html.Div(
                                              dcc.RangeSlider(id='salary_slider',
                                                              min=0, max=100000, step=2000,
                                                              marks={0:  {'label': '$0', 'style': {'font-size': 17, 'font-family': 'Tahoma'}},                                                                     
                                                                     30000: {'label': '$30k', 'style': {'font-size': 17, 'font-family': 'Tahoma'}},
                                                                     60000: {'label': '$60k', 'style': {'font-size': 17, 'font-family': 'Tahoma'}},
                                                                     90000: {'label': '$90k', 'style': {'font-size': 17, 'font-family': 'Tahoma'}},                                                                     
                                                                     },
                                                              value=[min_salary, max_salary]
                                                              ), style={'background-color': 'white',}
                                              ),
                                    ], id='fifth-selector',
                                            style={'margin-top': '50px',
                                                    'margin-left': '10px',
                                                    'margin-right': '0',
                                                    'width': '90%',
                                                   'height': '80px',
                                                   #'background-color': dark_bg_color,
                                                   'float': 'center',
                                                   }
                                    ),
                                  
                                  html.Div(children=[
                                        # html.P("This Dashboard shows the Data Jobs demand and salaries in Mexico in November 2023.",
                                        #                                           style={'textAlign': 'center', 'color': 'black',
                                        #                                                 'font-size': 14, 'font-family': 'Tahoma'}),
                                      #html.Br(),
                                      html.P("Data Source:",
                                              style={'textAlign': 'center', 'color': 'white', 'font-weight': 'bold',
                                                     'font-size': 17, 'font-family': 'Tahoma'}),
                                      html.P("Data collected from OCC.com.mx on 26 November 2023.",
                                              style={'textAlign': 'center', 'color': 'white',
                                                     'font-size': 13, 'font-family': 'Tahoma'}),
                                        ], style={'margin-top': '30px','margin-right': '5%'}
                                  ),    
                                  
                                  html.Div(children=[
                                                                     # Adding Author
                                        html.P("© Daniel Eduardo López",
                                                style={'textAlign': 'center', 'color': dash_theme_r[0],
                                                      'font-size': 16, 'font-family': 'Tahoma'}),

                                        dcc.Link(html.A('LinkedIn'), href="https://www.linkedin.com/in/daniel-eduardo-lopez",
                                                 target="_blank",
                                                style={'textAlign': 'center', 'color': dash_theme_r[0],
                                                      'font-size': 12, 'font-family': 'Tahoma',
                                                      'margin-top': '-5px',
                                                      'display': 'block'
                                                      }),
                                        dcc.Link(html.A('GitHub'), href="https://github.com/DanielEduardoLopez/DataJobsMX-Nov2023",
                                                 target="_blank",
                                                style={'textAlign': 'center', 'color': dash_theme_r[0],
                                                      'font-size': 12, 'font-family': 'Tahoma',
                                                      'margin': 'auto',
                                                      'display': 'block'}),

                                          ], style={'margin-top': '60px','margin-right': '5%'}
                                           
                                           
                                           ),                              

                                ], id='left-container',
                                style={'margin-top': '0px',
                                        'margin-left': '5px',
                                        'margin-right': '10px',
                                        'width': '14%',
                                       'height': '700px',
                                       'background-color': dark_bg_color, 
                                       'float': 'center', 
                                       'border-top-right-radius': '70px',
                                       'border-bottom-right-radius': '70px',                                                                              
                                        'box-shadow': '5px 5px 5px '+shadow_color,
                                        
                                       }
                                ),

                                # Third section: Plots Section
                                html.Div(children=[
                                    html.Div(children=[

                                          # First Plot
                                          html.Div(children=[
                                             

                                          html.Div(
                                             html.Label("Mean Monthly Salary",
                                                              style={'textAlign': 'center', 'color': 'white','font-weight': 'bold', #'text-shadow': '0 0 2px #fff',
                                                              'font-size': 17, 'font-family': 'Tahoma', 'margin-left': '5%'}
                                                              ), style={'background-color': dark_bg_color, 
                                                                        'width': '200px',
                                                                        'border-top-right-radius': '10px',
                                                                        'border-top-left-radius': '10px',
                                                                        }
                                          ),
                                            # Card
                                            dcc.Graph(id='card_salary'),

                                            

                                        ], id='card-container-1',
                                            style={'margin-top': '20px',
                                                  'margin-left': '1%',
                                                  'background-color': 'white',
                                                  'border-width': '2px',
                                                  'box-shadow': '1px 1px 1px '+shadow_color,
                                                  'width': '200px',
                                                  #'height': '100px',
                                                  'border-radius': '10px',
                                                  }
                                          
                                                ),
                                        html.Div([
                                          html.Div(
                                             html.Label("Number of Data Jobs",
                                                              style={'textAlign': 'center', 'color': 'white','font-weight': 'bold', #'text-shadow': '0 0 2px #fff',
                                                              'font-size': 17, 'font-family': 'Tahoma', 'margin-left': '5%'}
                                                              ), style={'background-color': dark_bg_color, 'width': '200px',
                                                                        'border-top-right-radius': '10px',
                                                                        'border-top-left-radius': '10px',
                                                                        }
                                          ),
                                            # Card
                                            dcc.Graph(id='card_demand'),

                                            

                                        ], id='card-container-2',
                                            style={'margin-top': '-76px',
                                                  'margin-left': '17%',
                                                  'background-color': 'white',
                                                  'border-width': '2px',
                                                  'box-shadow': '1px 1px 1px '+shadow_color,
                                                  'width': '200px',                                                  
                                                  #'height': '100px',
                                                  'border-radius': '10px',
                                                  }
                                          
                                                ),

                                        # Card with Data Jobs Info
                                        html.Div(children=[
                                                # Job Demand Plot: Donnut chart
                                                dcc.Graph(id='demand_job_plot'),                                   
                                        
                                                ], id='Donut_chart',
                                                  style={'margin-top': '10px',
                                                          'margin-left': '0px',
                                                          'width': '32%',
                                                          'height': '290px',
                                                          'box-shadow': '1px 1px 1px '+shadow_color,
                                                          'border-radius': '20px',    
                                                          'background-color': 'White',
                                                          }      
                                        ),

                                          # Second plot
                                          html.Div(children=[
                                          
                                                # Job-Salary Plot: Treemap
                                                      dcc.Graph(id='demand_company_plot'),
                                              
                                              ], id='Boxplot',
                                                style={'margin-top': '-370px',
                                                        'margin-left': '32.5%',
                                                        'width': '33%',
                                                        'height': '370px',
                                                        'box-shadow': '1px 1px 1px '+shadow_color,
                                                        'border-radius': '20px',    
                                                        'background-color': 'White',                                                                                                            
                                                        }                                                
                                              ),

                                          # Third plot
                                          html.Div(children=[

                                                # Location Demand Plot: Map
                                                dcc.Graph(id='demand_location_plot'),
                                                ], id='Map',
                                                style={'margin-top': '-370px',
                                                        'margin-left': '66%',
                                                        'width': '34%',
                                                        'height': '370px',
                                                         'box-shadow': '1px 1px 1px '+shadow_color,
                                                        'border-radius': '20px',    
                                                        'background-color': 'White',          
                                                        }
                                                ),
                                    ], id='middle-container',
                                    style={'margin-top': '10px',
                                            'margin-left': '5px',
                                            'margin-right': '5px',
                                            'width': '99%',
                                          'height': '500px',
                                          'float': 'center',
                                          }
                                    ),
                                          
                                  # Fourth section: Second Plot Section
                                  html.Div(children=[

                                                # Fourth Plot
                                                html.Div(children=[

                                                # Company Demand Plot: Boxplot
                                                dcc.Graph(id='salary_job_plot'),

                                                ], id='Treemap',
                                                style={'margin-top': '80px',
                                                        'margin-left': '0.5%',
                                                        'width': '31.5%',
                                                        'height': '410px',
                                                        'box-shadow': '1px 1px 1px '+shadow_color,
                                                        'border-radius': '20px',    
                                                        'background-color': 'White',         
                                                        }                                                
                                                ),                                 

                                                # Fifth Plot
                                                html.Div(children=[

                                                    # Company-Salary Plot: Heatmap
                                                    dcc.Graph(id='salary_company_plot'),

                                                    ], id='Heatmap',
                                                    style={'margin-top': '-410px',
                                                            'margin-left': '32.5%',
                                                            'width': '32.7%',
                                                            'height': '410px',
                                                            'box-shadow': '1px 1px 1px '+shadow_color,
                                                            'border-radius': '20px',    
                                                            'background-color': 'White',      
                                                            }
                                                    ),

                                              #Sixth Plot
                                              html.Div(children=[

                                                    # Location-Salary Plot: Contourmap
                                                    dcc.Graph(id='salary_location_plot'),

                                                    ], id='Contourmap',
                                                    style={'margin-top': '-410px',
                                                            'margin-left': '65.7%',
                                                            'width': '33.7%',
                                                            'height': '410px',
                                                            'box-shadow': '1px 1px 1px '+shadow_color,
                                                            'border-radius': '20px',    
                                                            'background-color': 'White',      
                                                            }
                                                    ),


                                          
                                          ], id='bottom-container',
                                            style={'margin-top': '-200px',
                                                      'width': '100%',
                                                      'height': '600px'
                                                      }
                                          ),
                                ], id='right-container',
                                style={'margin-top': '-730px',
                                        'margin-left': '15%',
                                        'margin-right': '1px',
                                        'width': '85%',
                                       'height': '800px',
                                       
                                       }
                                ),



                        ], id='entire-dashboard',
                           style={'width': '100%',
                                  'height': '100%',
                                  'overflow': 'hidden',
                                  'background-color': light_bg_color, 
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
               Output(component_id='card_salary', component_property='figure'),
               Output(component_id='card_demand', component_property='figure')],
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
    demand_company_plot = plot_treemap(dff)
    demand_location_plot = plot_cloropleth(dff)
    salary_job_plot = plot_boxplot(dff)
    salary_company_plot = plot_heatmap(dff)
    salary_location_plot = plot_contour(dff)
    card_demand = plot_card_demand(dff)
    card_salary = plot_card_salary(dff)

  else:

        if ('All' in (company and location)) and ('All' not in job):
          dff = dff[dff.Job.isin(job)]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_treemap(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card_demand = plot_card_demand(dff)
          card_salary = plot_card_salary(dff)
        
        elif ('All' in (job and location)) and ('All' not in company):
          dff = dff[dff.Company.isin(company)]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_treemap(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card_demand = plot_card_demand(dff)
          card_salary = plot_card_salary(dff)
        
        elif ('All' in (company and job)) and ('All' not in location):
          dff = dff[dff.Location.isin(location)]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_treemap(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card_demand = plot_card_demand(dff)
          card_salary = plot_card_salary(dff)
        
        elif ('All' in job) and ('All' not in (company and location)):
          dff = dff[(dff.Company.isin(company)) & (dff.Location.isin(location))]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_treemap(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card_demand = plot_card_demand(dff)
          card_salary = plot_card_salary(dff)

        elif ('All' in location) and ('All' not in (company and job)):
          dff = dff[(dff.Company.isin(company)) & (dff.Job.isin(job))]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_treemap(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card_demand = plot_card_demand(dff)
          card_salary = plot_card_salary(dff)

        elif ('All' in company) and ('All' not in (location and job)):
          dff = dff[(dff.Location.isin(location)) & (dff.Job.isin(job))]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_treemap(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card_demand = plot_card_demand(dff)
          card_salary = plot_card_salary(dff)

        elif 'All' not in (company and location and job):
          dff = dff[(dff.Job.isin(job)) & (dff.Location.isin(location)) & (dff.Company.isin(company))]

          demand_job_plot = plot_pie_chart(dff)
          demand_company_plot = plot_treemap(dff)
          demand_location_plot = plot_cloropleth(dff)
          salary_job_plot = plot_boxplot(dff)
          salary_company_plot = plot_heatmap(dff)
          salary_location_plot = plot_contour(dff)
          card_demand = plot_card_demand(dff)
          card_salary = plot_card_salary(dff)
        
        else:
          raise PreventUpdate 

  return demand_job_plot, demand_company_plot, demand_location_plot, salary_job_plot, salary_company_plot, salary_location_plot, card_salary, card_demand

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
