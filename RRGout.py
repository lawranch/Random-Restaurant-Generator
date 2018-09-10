import RRGin
import yelpAPI



def UI():
    print("Welcome to Lawrance's Random Restaurant Generator!\n" +
          "This application will choose a restaurant for you if",
          "you don't know what you want.\n" +
          "To use this application, you will need to enter your",
          "location, the distance you're\nwilling to travel, and",
          "how much you're willing to spend.\n")

    parameters = []

    parameters.append(('term', 'restaurants'))
    RRGin.obtain_location(parameters)
    RRGin.obtain_radius(parameters)
    RRGin.obtain_price(parameters)
    parameters.append(('open_now', 'true'))

    restaurant_list = yelpAPI.obtain_search_link_info(yelpAPI.build_search_link(parameters))

    while (1):
        restaurant = yelpAPI.select_random_restaurant(restaurant_list)
        response = yelpAPI.obtain_restaurant_details(yelpAPI.build_details_link(restaurant))

        print('Name: {}'.format(response['name']))
        print('Address: {}, {}, {} {}'.format(response['location']['address1'], response['location']['city'], response['location']['state'], response['location']['zip_code']))
        print('Phone: {}'.format(response['phone']))

        answer = RRGin.randomize_again()

        if (answer == 'n'):
            return
