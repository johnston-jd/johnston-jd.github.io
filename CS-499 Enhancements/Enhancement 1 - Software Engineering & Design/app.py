#Jaymie Johnston
#CS499 Capstone
#Enhancement 1 - Software Engineering and Design
#Enhancement 3 - Databases
# Configure the necessary Python module imports for dashboard components
import dash_leaflet as dl
import mariadb
from dash import dcc
from dash import html
from dash import Dash
import plotly.express as px
from dash import dash_table
from dash.dependencies import Input, Output
import base64
import sys

# Configure the plotting routines
import pandas as pd
from pygments.lexers import go

from animal_shelter import animalshelter

###########################
# Data Manipulation / Model
###########################

#MariaDB database information
user = 'root'
password = 'L3w!sZ03Sally'
host = '127.0.0.1'
port = 49670
db = 'animalshelter'

# Connect to database
shelter = animalshelter('root', 'L3w!sZ03Sally', capacity=10000)

#Returns all records from mariadb
try:
    connection = mariadb.connect(user='root', password='L3w!sZ03Sally', host='127.0.0.1', port=49670, database = 'animalshelter')
    cursor = connection.cursor()

    #select all from table
    table_name = 'aac_shelter_outcomes'
    query = f' SELECT * FROM animalshelter.{table_name}'

    cursor.execute(query)

    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=[i[0] for i in cursor.description])

    print(df)

except mariadb.Error as e:
    print(f"Error: {e}")
    sys.exit(1)


connection.close()

for row in rows:
    print(row)

#Drops the 'id' column so data_table does not crash
df.drop(columns=['id'],inplace=True)

print(len(df.to_dict(orient='records')))


#########################
# Dashboard Layout / View
#########################
app = Dash(__name__)

#Logo
image_filename = 'Grazioso Salvare Logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#Dashboard layout
app.layout = html.Div([
    html.Div(id='hidden-div', style={'display':'none'}),
    html.Center(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))),
    html.Center(html.B(html.H1('Austin Animal Center'))),
    html.Hr(),
    html.Div([
#Enhancement 1 - changed from Radio Buttons to Dropdown to allow for more than 1 parameter to be selected
# Added additional filter options
        dcc.Dropdown(
            id = 'Dropdown',
            options=[
                {'label': 'Water Rescue', 'value': 'Water Rescue'},
                {'label': 'Mountain or Wilderness Rescue', 'value': 'Mountain'},
                {'label': 'Disaster Rescue & Individual Tracking', 'value': 'Disaster'},
                {'label': 'Dog Breeds', 'value': 'All Dogs'}, #new option
                {'label': 'Cat Breeds', 'value': 'All Cats'}, #new option
                {'label': 'Dog Male', 'value': 'Male Dogs'}, #new option
                {'label': 'Dog Female', 'value': 'Female Dogs'}, #new option
                {'label': 'Cat Male', 'value': 'Male Cats'}, #new option
                {'label': 'Cat Female', 'value': 'Female Cats'}, #new option
                {'label': 'Reset', 'value': 'Reset'}

        ],
        multi=True, #can select more than one option
        placeholder='Select an option',
        value=[],
        #labelStyle={'display':'inline-block'}
        )

    ]),


    html.Hr(),
    dash_table.DataTable(id='datatable-id',
                         columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns],
                         data=df.to_dict('records'),
#interactive datatable features
#Enhancement 1 - updated sorting and selectable rows. Updated table layout size
        editable = False,
        filter_action = 'native',
        sort_action = 'native', #sort through animals
        sort_mode = 'multi', #can sort by multiple parameters
        row_selectable = 'multi', #changed from 'single'
        row_deletable = False,
        selected_columns = [],
        selected_rows = [],
        page_action = 'native',
        page_current = 0,
        page_size = 10,
        #Updated table layout
        style_table = {'overflowX': 'auto'},
        style_cell = {'height': 'auto', 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px', 'whiteSpace': 'normal'},

                        ),
    html.Br(),
    html.Hr(),
#Makes chart and geolocation side by side
    html.Div(className='row',
         style={'display' : 'flex'},
             children=[
        html.Div(
            id='graph-id',
            className='col s12 m6',

            ),
        html.Div(
            id='map-id',
            className='col s12 m6',
            )
        ])
])

#############################################
# Interaction Between Components / Controller
#############################################

#Enhancement 1 - Added additional filtering options
@app.callback(Output('datatable-id',"data"),
              Output('datatable-id',"columns"),
              Output('datatable-id',"selected_rows"),
              [Input('Dropdown',"value")])
def update_dashboard(filter_type):

        if filter_type == 'Reset':
            df = pd.DataFrame.from_records(shelter.get({}))
        #Water Rescue Type Filter
        elif filter_type == 'Water':
            df = pd.DataFrame.from_records(shelter.get({ 'sex_upon_outcome' : 'Intact Female',
                'breed' : {'$in' : ['Labrador Retriever Mix', 'Chesapeake Bay Retriever'
                'Newfoundland']},
                'age_upon_outcome_in_weeks' : {'$gte' : 26.0},
                'age_upon_outcome_in_weeks' : {'$lte' : 156.0}
                    }))
        #Mountain Rescue Type Filter
        elif filter_type == 'Mountain':
            df = pd.DataFrame.from_records(shelter.get( {'sex_upon_outcome' : 'Intact Male',
                'breed' : {'$in' : ['German Shepard', 'Alaskan Malamute', 'Old English Sheepdog', 'Siberian Husky', 'Rottweiler']},
                'age_upon_outcome_in_weeks' : {'$gte' : 26.0},
                'age_upon_outcome_in_weeks' : {'$lte' : 156.0}
                      }))
        #Disaster Rescue Type Filter
        elif filter_type == 'Disaster':
            df = pd.DataFrame.from_records(shelter.get( {'sex_upon_outcome' : 'Intact Male',
                'breed' : {'$in' : ['Doberman Pinscher', 'German Shepard', 'Golden Retriever', 'Bloodhound', 'Rottweiler']},
                'age_upon_outcome_in_weeks' : {'$gte' : 20.0},
                'age_upon_outcome_in_weeks' : {'$lte' : 300.0}
                     }))
        #Enhancement 1 - Start of new filtering options
        #Dog Breeds Type Filter
        elif filter_type == 'All Dogs':
            df = pd.DataFrame.from_records(shelter.get( {'animal_type' : 'Dog'}))

        #Cat Breeds Type Filter
        elif filter_type == 'All Cats':
            df = pd.DataFrame.from_records(shelter.get( {'animal_type' : 'Cat'}))

        #Male Dog Filter Type
        elif filter_type == 'Male Dogs':
            df = pd.DataFrame.from_records(shelter.get( {'animal_type' : 'Dog', 'sex_upon_outcome' : {'$in' : ['Intact Male', 'Neutered Male']}}))
        #Female Dog Filter Type
        elif filter_type == 'Female Dogs':
            df = pd.DataFrame.from_records(shelter.get( {'animal_type' : 'Dog', 'sex_upon_outcome' : {'$in' : ['Intact Female', 'Neutered Female']}}))
        #Male Cat Filter Type
        elif filter_type == 'Male Cats':
            df = pd.DataFrame.from_records(shelter.get( {'animal_type' : 'Cat', 'sex_upon_outcome' : {'$in' : ['Intact Male', 'Neutered Male']}}))
        #Female Cat Filter Type
        elif filter_type == 'Female Cats':
            df = pd.DataFrame.from_records(shelter.get( {'animal_type' : 'Cat', 'sex_upon_outcome' : {'$in' : ['Intact Female', 'Neutered Female']}}))

        else:
            df = pd.DataFrame.from_records(shelter.get({}))

        data = df.to_dict('records')
        columns = [{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns]
        selected_rows = [0]  # reset the selected row to first row when filter setting changes

        return data, columns, selected_rows


# Display the breeds of animal based on quantity represented in
# the data table
@app.callback(
    Output('graph-id', "children"),
    [Input('datatable-id', "derived_virtual_data")])
def update_graphs(viewData):
#Pie chart
    dff = pd.DataFrame.from_records(viewData)
    figure = px.pie(df, names='animal_type', title='Preferred Animals', color_discrete_sequence=px.colors.sequential.RdBu)
    figure.update_traces(textinfo='percent', textposition='inside')
    return [
        dcc.Graph(
        figure = figure
                          )
       ]


#This callback will highlight a cell on the data table when the user selects it
@app.callback(
    Output('datatable-id', 'style_data_conditional'),
    [Input('datatable-id', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]


#This callback will update the geolocation chart for the selected data entry
#derived_virtual_selected_rows will be the selected row(s) in the table in the form of
#a list.
@app.callback(
    Output('map-id', "children"),
     [Input('datatable-id', "derived_virtual_selected_rows")])
def update_map(virtualRows):
    #austin Texas is [30.75, -97.48]

    #create the views
    if not virtualRows:
        marker_array = (30.75, -97.48)  #default marker at Austin Animal Shelter
        tool_tip = "Austin Animal Center"
        pop_up_heading = "Austin Animal Center"
        pop_up_paragraph = "Shelter Home Location"

    else:  #build views based on the selection
        dff = pd.DataFrame(df.iloc[virtualRows])
        lat = float(dff['location_lat'].to_string().split()[1])
        long = float(dff['location_long'].to_string().split()[1])
        marker_array = (lat, long)  #build the array based on selection

        tool_tip = dff['animal_id']
        pop_up_heading = "Animal ID"
        pop_up_paragraph = dff['animal_id']

    #return the map with marker
    #map moves with location marker
    return [dl.Map(style={'width': '1000px', 'height': '500px'}, center=marker_array,
                   zoom=10, children=[dl.TileLayer(id="base-layer-id"),
                                      dl.Marker(position=marker_array, children=[
                                          dl.Tooltip(tool_tip),
                                          dl.Popup([
                                              html.H1(pop_up_heading),
                                              html.P(pop_up_paragraph)
                                          ])
                                      ])
                                      ])
            ]

if __name__ == "__main__":
    app.run(debug=True)