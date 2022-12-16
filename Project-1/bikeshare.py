import time
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle    invalid inputs
    while True:
        city = input('Please enter city (chicago, new york city, washington): ').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('Invalid City.')
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Please enter month (all, january, february, ... , june): ").lower()
        if month in months:
           break
        else:
            print('Invalid Month.')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while True:
        day = input("Please enter day of week (all, monday, tuesday, ... sunday): ").lower()
        if day in days:
            break
        else:
            print('Invalid Day.')
            
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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time(dtype= string) column to datetime(dtype =datetime) 
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    print(f"The most common month: {df['month'].mode()[0]}")

    # TO DO: display the most common day of week
    
    print(f"The most common day of week: {df['day_of_week'].mode()[0]}")

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['Start hour'] = df['Start Time'].dt.hour

    print(f"The most common start hour: {df['Start hour'].mode()[0]}")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f"The most commonly used start station:  {df['Start Station'].mode()[0]}")

    # TO DO: display most commonly used end station
    print(f"The most commonly used end station:  {df['End Station'].mode()[0]}")

    # TO DO: display most frequent combination of start station and end station trip
    # Conct Start Station colomn and End Station colomn
    df['Trip'] = df['Start Station'] +', '+ df['End Station']
    print(f"The most frequent trip:  {df['Trip'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    print(f"total travel time: {int(df['Trip Duration'].sum())} ")
    
    # TO DO: display mean travel time
    print(f"mean travel time: {int(df['Trip Duration'].mean())} ")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"Counts of user types: \n{df['User Type'].value_counts()}")
    print()
    if city !='washington':
        # TO DO: Display counts of gender
        print(f"Counts of gender: \n{df['Gender'].value_counts()}")
        print()
        # TO DO: Display earliest, most recent, and most common year of birth
        print(f"The earliest year of birth: {int(df['Birth Year'].min())}")
        print(f"The most recent year of birth: {int(df['Birth Year'].max())}")
        print(f"The most common year of birth: {int(df['Birth Year'].mode()[0])}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    # TO DO: Show dataset to user 
    index = 0 
    user_answer = input("Do you want to show the first five rows of data? type(yes or no): ").lower()
    while user_answer != 'no':     
        if user_answer == 'yes':    
            print(df[index:index+5])
            index +=5
            user_answer = input("Do you want to show another five rows of data? type(yes or no): ").lower() 
        elif user_answer not in ['yes','no']:
            print("Invalid choice.")
            user_answer = input("Do you want to show another five rows of data? type(yes or no): ").lower()
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
