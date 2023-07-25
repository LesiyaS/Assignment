import requests

def get_weather_data(location):
    url=f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response=requests.get(url)
    data=response.json()
    return data
def print_weather_forecast(data):
    for forecast in data["list"]:
        print(f"Time:{forecast['dt_txt']},Weather:{forecast['weather'][0]['description']}")

def print_wind_speed(data):
    for forecast in data["list"]:
        print(f"Time:{forecast['dt_txt']},Wind speed:{forecast['wind']['speed']} m/s")

def print_pressure(data):
    for forecast in data["list"]:
        print(f"Time: {forecast['dt_txt']}, Pressure: {forecast['main']['pressure']} hPa")

def main():
    location=input("Enter the location(e.g.,London,us):")
    data=get_weather_data(location)

    while True:
        print("\nOptions:")
        print("1.Get weather")
        print("2.Get wind speed")
        print("3.Get pressure")
        print("0.Exit")
        option=input("Enter your choice(0-3):")

        if option =="1":
            print_weather_forecast(data)
        elif option=="2":
            print_wind_speed(data)
        elif option == "3":
            print_pressure(data)
        elif option == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


