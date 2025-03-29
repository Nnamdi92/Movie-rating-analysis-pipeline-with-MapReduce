#!/usr/bin/env python3

import sys
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP

# Set the minimum number of votes
min_votes = 10
print('min_votes = %s' % min_votes, file=sys.stderr)

# Initialize variables to keep track of the total rating and count of votes for each movie in each year
total_rating = defaultdict(Decimal)
rating_count = defaultdict(int)
highest_movies = defaultdict(list)
highest_average_rating = defaultdict(Decimal)

# Process the input line by line
for line in sys.stdin:
    # Parse the input line
    year, title, rating, count = line.strip().split('\t')
    rating = Decimal(rating)
    count = int(count)
    
    # Accumulate ratings and count of votes for each movie in each year
    total_rating[(title, year)] += rating
    rating_count[(title, year)] += count

# Calculate the average rating for each movie in each year
for (title, year), count in rating_count.items():
    # Check if the movie has enough votes to be considered
    if count >= min_votes:
        # Calculate the average rating
        average_rating = total_rating[(title, year)] / count
        # Update the highest average rating and corresponding movies for the year
        average_rating = average_rating.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        if average_rating > highest_average_rating[year]:
            highest_average_rating[year] = average_rating
            highest_movies[year] = [(title, average_rating)]
        elif average_rating == highest_average_rating[year]:
            highest_movies[year].append((title, average_rating))
# Output the result for each year
for year, movies in highest_movies.items():
    for movie, average_rating in movies:
        print("%s\t%s\t%s" % (year, movie, average_rating))