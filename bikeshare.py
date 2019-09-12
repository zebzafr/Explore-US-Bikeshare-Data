import time
import pandas as pd
import numpy as np
import csv 

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["washington", "new york city", "chicago"]
    while True:
        
        city = input('\nEnter the city name you are interested in: ').lower()
        if city not in cities:
            print('Wrong city. Try again.')
            continue
        print('Thank you for the input!')
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    while True:
        month = input('Enter the month: ').lower()
        if month not in months:
            print('Try agian.\n')
            
        elif month == 'all':
            print('\nNo filter applied.\n')
            break
        else:
            print('Thank you for the input.')
            break                 
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while True:
        day = input('\nEnter the day: ').lower()
        if day not in days:
            print('\nWrong input.Please enter the day.\n')
        elif day == 'all':
            print('\nNo filter appied for day.\n')
            break
        else:
            print('Thank you for the input')
            break
      
        
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
    #load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])
    #print(df.head())
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d')
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    
#     if df['month'].empty:
#         print('Dataframe is empty.')
    
    if month != 'all':
                months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
                
                month = months.index(month)
                df = df[df['month'] == month]
            
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if day != 'all':
                df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    popular_month = ''
    popular_day = ''
    popular_hour = None

    try:
    # TO DO: display the most common month
        popular_month = df['month'].value_counts().idxmax()
        #popular_month = months.index(popular_month)
        print('Most popular month is: ', popular_month)
    
    # TO DO: display the most common day of week   
        popular_day = df['day_of_week'].value_counts().idxmax()
        print('Most popular day of the week is: ', popular_day) 
  
    # TO DO: display the most common start hour
        popular_hour = df['hour'].value_counts().idxmax()
        print('Most Frequent Start Hour:', popular_hour)
    
    except (ValueError, KeyError):
        print('No data.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return popular_day, popular_month, popular_hour




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    start_station = ''
    end_station = ''
    start_end_station = ''

    try:
    # TO DO: display most commonly used start station
        start_station = df['Start Station'].value_counts().argmax()
        print('Most commonly used start station is : ', start_station)
                      
    # TO DO: display most commonly used end station
        end_station = df['Start Station'].value_counts().argmax()
        print('Most common end station is : ', end_station)
    # TO DO: display most frequent combination of start station and end station trip
        start_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
        print('Most frequent combination of start and end station trip is : ', start_end_station)
        
    except (KeyError, ValueError):
        return None
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return start_station, end_station, start_end_station



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
   
    total_trip_time = None
    average_trip_time = None
    
    try:
    # TO DO: display total travel time
        total_trip_time = df['Trip Duration'].sum()
        print('The total travel time for the city is: {} seconds'.format(total_trip_time))
   
    # TO DO: display mean travel time
        average_trip_time = df['Trip Duration'].mean()
        print('The mean travel time for the city is: {} seconds'.format(average_trip_time))
    
    except(ValueError, KeyError):
        print('No data.')

        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return total_trip_time, average_trip_time



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    gender_types = None
    user_types = None
    
    try:
    # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print('User breakdown:\n', user_types)
  
    # TO DO: Display counts of gender
        gender_types = df['Gender'].value_counts()
        print('\nGender Breakdown:\n',gender_types)
    
    except (ValueError, KeyError):
        print('\nNo data.\n')
    

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year_common = None
    most_recent_birth_year = None
    earliest_birth_year = None
    try:
        birth_year_common = df['Birth Year'].value_counts().idxmax()
        print('\nThe most common year of birth is: ',(birth_year_common))
    
        most_recent_birth_year = df['Birth Year'].iloc[-1]
        print('\nThe year of birth of the recent bike user is: ',(most_recent_birth_year))
    
        earliest_birth_year = df['Birth Year'].iloc[0]
        print('\nThe year of birth of the first bike user is: ',(earliest_birth_year))
    
    except (KeyError, ValueError):
        print('\nNo information on "Birth Year".\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    
    print('-'*40)
    return user_types, gender_types, birth_year_common, most_recent_birth_year, earliest_birth_year




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)        
        trip_duration_stats(df)
        user_stats(df)
        
    # Display raw data based on user request  
        count = 0
        data = df.to_dict('records')
        for k in data:
            print(k)
            count = count + 1
            if count % 5 == 0:
                keystroke = input('\nType "yes" for more data.\n')
                if keystroke.lower() != 'yes':
                    break
                 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
