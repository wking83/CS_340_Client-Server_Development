About the Project/Project Title
The interactive dashboard was developed for Grazioso Salvare to interact with animal shelter data. This data can be visualized and filtered. The program is built on Python and Dash framework. This framework interacts with a MongoDB database. The database can be queried, filtered, and provide information for visualization charts and maps. 

Motivation
Animals must be supported based on their needs. Water, Mountain, and Disaster dogs all need to be identified so that they receive specific care and placement. This tool enables the shelter to make appropriate decisions based on the animal’s background. 

Getting Started
•	Install the required software provided in the installation section
•	Start MongoDB with the given authentication
•	Import the data (aac_shelter_outcomes.csv) in MongoDB
•	Run the project in Jupyter Notebook


Installation

•	MongoDB 6.x: NoSQL database containing animal data must be imported (aac_shelter_outcomes.csv)
1.	Username: aacuser
2.	Password: SNHU1234
3.	Host: nv-desktop-services.apporto.com
4.	Port: 31813
5.	Database: AAC
6.	Collection: animals

•	Jupyter Notebooks 6.5.2: Front end interface the dashboard in a browser environment. Allows for manipulation of python code to change visual representations.
•	Python 3.9: Simple and compatible with MongoDB. The interface and language are readily available for use.
•	PyMongo 4.3.3: Communication between Python and MongoDB and manages CRUD operations.
•	Dash 2.8.1: Interaction with Python web in a lightweight server capacity.  Displays and management tool.
•	Pandas 1.5.3: Table Generation and data wrangling. Gives user manipulation ability.
•	CRUDMongoModule v1-This module provides CRUD operations and interfaces with the PyMongo client.

Usage
@app.callback(
    Output('datatable-id', 'data'),
    [Input('filter-type', 'value')]
)
def update_dashboard(filter_type):
    if filter_type == 'Disaster':
        query = {
            "$and": [
                {"breed": {"$regex": "Rottweiler", "$options": "i"}},
                {"sex_upon_outcome": "Intact Male"},
                {"age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300}}
            ]
        }
    else:
        query = {'animal_type': 'Dog'}
    
    df = pd.DataFrame.from_records(shelter.read(query))
    if '_id' in df.columns:
        df.drop(columns=['_id'], inplace=True)
    return df.to_dict('records')
