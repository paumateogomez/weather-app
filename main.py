from src.weather_service import get_weather


def show_menu():
    print("\n=== WEATHER APP ===")
    print("1. Search weather")
    print("2. Exit")


def main():

    while True:

        show_menu()

        option = input("\nSelect an option: ")

        if option == "1":

            city = input("Enter city: ")
            get_weather(city)

        elif option == "2":

            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()