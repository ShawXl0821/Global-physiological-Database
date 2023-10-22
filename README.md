# Global-physiological-Database
The aim of this project is to address the challenge of inaccessible physiological data collected from various laboratory studies. These studies have generated valuable data on participants' physiological responses under diverse environmental conditions, activity levels, and clothing settings. However, due to the lack of data publication, the potential for reusing this data to answer new research questions remains untapped. To overcome this limitation, we collaborate on defining the best database architecture to store and organize these physiological datasets.

<br>

This is a guidance for general users to deploy the MongoDB database locally and manipulate the database to manage the large dataset.

<br>

## Table of contents
-   [Getting Started](#getting-started)
    -   [Data Cleaning](#data-cleaning)
    -   [Installation of MongoDB](#installation-of-mongodb)
    -   [Manuscript and Presentation](#manuscript-and-presentation)
-   [Prerequisites](#prerequisites)
    -   [Latex](#latex)
-   [Author](#authors)


## Getting started  

### Data Cleaning  
Before storing data into the database, you need to clean the dataset to a certain format. We have provided a sample data cleaning script and an explanation at https://github.com/ShawXl0821/Global-physiological-Database/tree/main/Data. The result of the data cleaning must contain timestamp, Participant_ID, Trial_ID and paramameters of the experiment data. A sample cleaned dataset should be like this:  

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/result.png>

Then, you are good to go with the database.  

### Installation of MongoDB  
1. For this project, we selected MongoDB Community Server to store and manage the database on local environment. You should download the installer on https://www.mongodb.com/try/download/community

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/install1.png>

2. Execute the installer, you should choose the complete installation option and install the MongoDB Compass (which will be used in the next phase) as well.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/install2.png>
   
3. Install Mongod as a service and custom your direcory setting (recommend using the default direcory to avoid errors)

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/install3.png>

4. Install and open the MongoDB Compass

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/newCompass1.png>

5. Click 'New connection' on the left and the interface will automatically generate a connection string for you. Click 'Connect' to connect to your localhost. You can also click 'Save & Connect' to save your connection information.

<img src=https://github.com/ShawXl0821/Global-physiological-Database/blob/main/Asset/newCompass2.png>

<br>


