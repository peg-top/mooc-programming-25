# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    with open(filename) as station_file:

        stations = {}

        for station_line in station_file:
            station_info = station_line.split(";")
            if station_info[0] != "Longitude":
                stations[station_info[3]] = (float(station_info[0]), float(station_info[1]))

        return stations
    
def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):

    greates_stations = ("", "", 0)

    for station1 in stations:
        for station2 in stations:
            if station1 != station2:
                d = distance(stations, station1, station2)
                if d > greates_stations[2]:
                    greates_stations = (station1, station2, d)
    return greates_stations


# stations = get_station_data('stations1.csv')
# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
# d = distance(stations, "Viiskulma", "Kaivopuisto")
# print(d)

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)