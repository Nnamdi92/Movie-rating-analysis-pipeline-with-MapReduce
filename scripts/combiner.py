#!/usr/bin/env python3

import sys
from collections import defaultdict
from decimal import Decimal



# Initialize variables to keep track of the total rating and count of votes for each movie in each year
total_rating = defaultdict(Decimal)
rating_count = defaultdict(int)

# Process the input line by line
for line in sys.stdin:
    # Parse the input line
    year, title, rating, count = line.strip().split('\t')
    rating = Decimal(rating)
    count = int(count)
    
    # Accumulate ratings and count of votes for each movie in each year
    total_rating[(title, year)] += rating
    rating_count[(title, year)] += 1

# Output the aggregated results for each movie in each year
for (title, year), count in rating_count.items():
    # Check if the movie has enough votes to be considered
    if count >= min_votes:
        # Output the result
        print("%s\t%s\t%s\t%s" % (year, title, total_rating[(title, year)], count))
