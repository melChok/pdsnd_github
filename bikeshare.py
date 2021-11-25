import time
import datetime
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). \
    #HINT: Use a while loop to handle invalid input
    while True:
        try:
            city = input('\nWould you like to look at data for Chicago,'\
                        'New York City or Washington?:\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
            month = input('Which month? January, February, March,'\
                         'April, May, June or all\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = input('Which day? Monday,Tuesday, Wednesday, Thursday,'\
                       'Friday, Saturday, Sunday or all\n').lower()
            break
        except:
            pass

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_weekday = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]

    time_data = pd.Series(data=[popular_month,popular_weekday,popular_start_hour], \
                          index=['Most common month:', 'Most common day_of_week:', 'Most common hour:'])

    print(time_data)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + df['End Station']).mode()[0]

    travel_data = pd.Series(data=[popular_start_station, popular_end_station, popular_trip],\
                             index=['Most commonly used start station:','Most commonly used end station:','\
                             ''Most frequent trip:'])
    print(travel_data)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (str(datetime.timedelta(seconds=np.float(df['Trip Duration'].sum()))))

    # TO DO: display mean travel time
    mean_travel_time = (str(datetime.timedelta(seconds=np.float(df['Trip Duration'].mean()))))

    travel_stats = pd.Series(data=[total_travel_time, mean_travel_time],\
                             index=['Total travel time in 2017:', 'Average travel time per trip:'])
    print(travel_stats)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nUser Types:\n')
    user_types = df['User Type'].value_counts()
    print(pd.Series(user_types))

    # TO DO: Display counts of gender
    print('\nGender Information:\n')
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print(pd.Series(gender_types)) if 'Gender' in df.columns else \
        print('No Gender information to display')

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nBirth Year Information:\n')
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        age_data = pd.Series(data = [earliest_birth_year, recent_birth_year, common_birth_year],\
                              index=['Olderst birth year:', 'Youngest birth year:', 'Common birth year:'])
        print(age_data)
    else:
      print('No Birth Year information to display')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data_promt(df):
    """promts user if they want to see raw data and shows 5 rows of data at every 'yes' promt"""

    print('\nShowing Raw data...\n')

    User_promt_1 = input('\nWould you like to see raw data? Enter yes to see raw data\n').lower()

    i=0
    while User_promt_1 == 'yes':
        while i <= df.shape[0]:
            print(df[i:i+5])
            i+=5
            if i <=2000:
             break
        Stop_display = input('\nWould you like to see more raw data? Enter yes or no\n').lower()
        if  Stop_display.lower() == 'no':
              break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_promt(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
