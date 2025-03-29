#!/usr/bin/env python3
import sys



# Read included years
with open('years.txt', 'r') as f:
    included_years = f.read().split()
    # Print debug/info message to stderr
    print('included_years = %s' % included_years, file=sys.stderr)

# If years.txt is empty, include all years
if not included_years:
    included_years = []

# Process the input line by line
for line in sys.stdin:
    # Parse the input line
    uid, title, genres, year, rating = line.strip().split('\t')
    
    # If included_years is not empty and the year is not in included_years, skip this line
    if included_years and year not in included_years:
        continue
    
    # Split genres if there are multiple
    movie_genres = genres.split('|')
    
    # Output rating for each genre separately
    for genre in movie_genres:
        # Output format: year, title, rating, count
        print('%s\t%s\t%s\t%s' % (year, title, rating, 1))