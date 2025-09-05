
# IPL Data Analysis Project

This project provides a command-line interactive program to analyze IPL (Indian Premier League) cricket data from 2008 to 2024.

## Features

- Player career summary: Runs, Wickets, Catches, Matches played.
- Player's best season analysis for runs and wickets.
- Venue-wise analysis: Top wicket-takers, average first innings scores, toss impact.
- Team-wise analysis: Head-to-head stats, matches per season, win percentage.
- Umpire analysis: Matches judged, frequent umpire pairings, win bias.
- Season statistics: Orange Cap (top run-scorers), Purple Cap (top wicket-takers), most economical bowlers, best strike rates.
- Match-level insights: Highest-scoring matches, partnerships, 4s, and 6s analysis.

## Data

The program uses multiple CSV files located in the `normalized csvs` folder:
- `delivery.csv`
- `dismissals.csv`
- `match.csv`
- `match_result.csv`
- `match_teams.csv`
- `player_of_the_match.csv`
- `players.csv`
- `teams.csv`
- `toss.csv`
- `umpire.csv`
- `umpire_match.csv`
- `venue.csv`

## How to Run

1. Install dependencies (Python 3.x and pandas required):
   ```bash
   pip install pandas
   ```

2. Place all CSV files in a folder named `normalized csvs` in the project directory.

3. Run the main code file:
   ```bash
   python main_code.py
   ```

4. Follow the on-screen instructions to select queries and view results.

## Project Structure

```
project/
│-- normalized csvs/
│   │-- delivery.csv
│   │-- dismissals.csv
│   │-- match.csv
│   │-- ...
│-- main_code.py
│-- README.md
```

## Future Improvements

- Add visualizations for key statistics.
- Web-based interface for easier interaction.
- Optimize performance for large datasets.

---

Developed as part of a data analysis project for IPL statistics.
