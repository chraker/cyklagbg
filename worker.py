import json
import logging
import os

import psycopg2
import requests

import psycopg2.extras

from cyklagbg import settings

db_password = os.environ['DB_PASSWORD']
api_token=os.environ['API_TOKEN']

def fetch_data():

    # get the data from gbg open data
    url = "http://data.goteborg.se/SelfServiceBicycleService/v1.0/Stations/" + api_token + "?format=JSON"
    data_dict = requests.get(url).json()


    # store it to database directly, indipendantly if django session ~~
    try:
        if settings.LOCAL:
            connection = psycopg2.connect(
                dbname='d6idrsht1f8b0s',
                user='ivfstvjeuporge',
                host='ec2-23-23-225-158.compute-1.amazonaws.com',
                password=db_password)
        else :
            connection = psycopg2.connect(
                dbname='bikestations',
                user='postgres',
                host='localhost',
                password=db_password)
    except:
        logging.exception("cannot connect to database")
    else:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(
            """DELETE from webapp_bikestation"""
        )
        for item in data_dict:
            cursor.execute(
                """INSERT INTO webapp_bikestation(
                  name, available_bike_stands, available_bikes, lat, long, isopen
                )
                VALUES(%s, %s, %s, %s, %s, %s)""",
                (
                    item["Name"],
                    item['AvailableBikeStands'] if 'AvailableBikeStands' in item else 0,
                    item['AvailableBikes'] if 'AvailableBikes' in item else 0,
                    item['Long'],
                    item['Lat'],
                    item['IsOpen']
                )
            )
        connection.commit()
        cursor.close()
        connection.close()
        print("yay")


    #store it in db through models, if django loaded
    # for key in data_dict:
    #     bike_sation = BikeStation(
    #         name = data_dict[key]['Name'],
    #         available_bike_stands = data_dict[key]['AvailableBikeStands'],
    #         available_bikes = data_dict[key]['AvailableBikes'],
    #         lat = data_dict[key]['Long'],
    #         long = data_dict[key]['Lat'],
    #         isopen = data_dict[key]['IsOpen']
    #     )
    #     print(bike_sation)
    #     bike_sation.save()
    #
    # print(data)

fetch_data()