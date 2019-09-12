# Explore-US-Bikeshare-Data
Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, I used data provided by Udacity, which was shared with them by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.

### Datasets
Randomly selected data for the first six months of 2017 was provided for all three cities. All three of the data files contain the same core six (6) columns:

1. Start Time (e.g., 2017-01-01 00:07:57)
2. End Time (e.g., 2017-01-01 00:20:53)
3. Trip Duration (in seconds - e.g., 776)
4. Start Station (e.g., Broadway & Barry Ave)
5. End Station (e.g., Sedgwick St & North Ave)
6. User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
Gender
Birth Year

### Evaluate
For the project, a variety of descriptive statistics were computed to provide following information:

##### 1 Popular times of travel (i.e., occurs most often in the start time)
- most common month
- most common day of week
- most common hour of day

##### 2 Popular stations and trip
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

##### 3 Trip duration
- total travel time
- average travel time

##### 4 User info
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

An interative experience was created in the terminal to answer the above questions. To conduct data analysis and answer the above questions, a user can filter the data by asking questions like:

1. Would you like to see data for Chicago, New York, or Washington?
2. Would you like to filter the data by month, day, or not at all?
3. Which month - January, February, March, April, May, or June?
4. Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The script had to anticipate raw input errors like using improper upper or lower case, typos, or users misunderstanding what you are expecting.
