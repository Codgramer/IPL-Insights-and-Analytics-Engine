import pandas as pd
import numpy as np
import time
from collections import defaultdict

def display_projection(df, column_name, label):
    start_time = time.time()

    print("This is a projection type of query")
    print(f"This query uses the {label}.csv and performs a projection on the attribute {column_name}")

    values = df[column_name].tolist()
    print(f"List of all {label}s in IPL:")
    for i, val in enumerate(values, 1):
        print(f"{i}. {val}")
    print(f"Total number of {label}s in IPL: {len(values)}")

    print(f" Time taken: {time.time() - start_time:.4f} seconds\n")


def find_col(df, candidates):
    """Return the first column name from candidates that exists in df, else None."""
    for c in candidates:
        if c in df.columns:
            return c
    return None

def get_player_id_by_name(name):
    """Case-insensitive lookup; returns player_id or None. If multiple matches, returns first."""
    if name is None or name.strip()=="":
        return None
    s = name.strip().lower()
    if 'player' in players.columns:
        hits = players[players['player'].str.lower().str.contains(s, na=False)]
        if hits.empty:
            return None
        return hits.iloc[0]['player_id']
    return None

def get_team_id_by_name(name):
    s = str(name).strip().lower()
    if 'team' in teams.columns:
        hits = teams[teams['team'].str.lower() == s]
        if hits.empty:
            # try partial match
            hits = teams[teams['team'].str.lower().str.contains(s, na=False)]
            if hits.empty:
                return None
        return hits.iloc[0]['team_id']
    return None

def get_umpire_match_df():
    # handle possible variable name differences
    if 'umpire_match' in globals():
        return globals()['umpire_match']
    if 'umpir_match' in globals():
        return globals()['umpir_match']
    if 'umpire_match_df' in globals():
        return globals()['umpire_match_df']
    return None


def season_mask_from_input(series, season_input):
    s = str(season_input).strip()
    if s == "":
        return pd.Series([True] * len(series), index=series.index)
    # if user enters a simple year like '2017', match any season containing that substring
    if s.isdigit():
        return series.astype(str).str.contains(s)
    # otherwise expect an exact match like '2017/18'
    return series.astype(str) == s

if __name__ == "__main__":
    # Create a DataFrame with random data
    delivery=pd.read_csv('normalized csvs/delivery.csv')
    # delivery['delivery_time'] = pd.to_datetime(delivery['delivery_time'])
    dismissals=pd.read_csv('normalized csvs/dismissals.csv')
    match_result=pd.read_csv('normalized csvs/match_result.csv')
    match_teams=pd.read_csv('normalized csvs/match_teams.csv')
    match=pd.read_csv('normalized csvs/match.csv')
    player_of_the_match=pd.read_csv('normalized csvs/player_of_the_match.csv')
    players=pd.read_csv('normalized csvs/players.csv')
    teams=pd.read_csv('normalized csvs/teams.csv')
    toss=pd.read_csv('normalized csvs/toss.csv')
    umpire=pd.read_csv('normalized csvs/umpire.csv')
    umpire_match=pd.read_csv('normalized csvs/umpire_match.csv')
    venue=pd.read_csv('normalized csvs/venue.csv')

    print("Welcome to the IPL Data Analysis Program!")
    time.sleep(1)
    print("This program consists of the data of all IPL matches from 2008 to 2024")
    time.sleep(1)

    while(True):
        print("\n")
        print("------------------------------------------------------")
        print("Please select any one of the below query")
        print("1 - List of all teams in IPL")
        print("2 - List of all players played in IPL")
        print("3 - List of all umpires in IPL")
        print("4 - List of all venues in IPL")
        print("5 - List of all matches played in IPL and all information about them")
        print("6 - Particular player stats in IPL")
        print("7 - How many times has a particular player became the man of match and in which matches")
        print("8 - Head to Head stats of any 2 teams")
        print("9 - Player team history (player played from which team in which season)")
        print("10 - For a given stadium, winning while batting first and winning while batting second")
        print("11 - For a given stadium, average first innings score")
        print("12 - Total number of 4s or 6s per season")
        print("13 - Average powerplay score of a team for each season")
        print("14 - Average wickets taken in powerplay of a team for each season")
        print("15 - Particular season stats - purple cap, orange cap, most 4s, most 6s, most number of dot balls, winner, runner up")
        print("16 - Number of matches judged by a particular umpire")
        print("17 - Most hundreds and fifties per season")
        print("18 - Most 5 wicket takers in a match per season")
        print("19 - Bowler vs Batter comparison")
        print("20 - Update team name")
        print("21 - Update venue name")
        print("22 - Matches per season for a team")
        print("23 - Top run-scorers in a season")
        print("24 - Most economical bowlers in a season")
        print("25 - Best strike rates for a team in a season")
        print("26 - Player's best season (highest runs/wickets)")
        print("27 - Player strike rate & average per season")
        print("28 - Highest partnerships per season")
        print("29 - Most frequent umpire pairings")
        print("30 - Umpire win bias (team win % under specific umpire)")
        print("31 - Top 10 highest scoring matches in a season")
        print("32 - Teams with most playoff appearances")
        print("33 - Finals winners by season")
        print("34 - Player of the Match in playoff games")
        print("35 - Exit the program")

        print("\n")

        choice=int(input("Enter your choice: "))
        if choice==1:
            display_projection(teams, 'team', 'team')
        elif choice==2:
            display_projection(players, 'player', 'player')
        elif choice==3:
            display_projection(umpire, 'umpire', 'umpire')
        elif choice==4:
            display_projection(venue, 'venue', 'venue')
        elif choice==5:
            start_time = time.time()
            print("This query uses the following csvs:")
            print("1. match.csv -> match_id, season, date, venue_id")
            print("2. match_teams.csv -> match_id, team_id1, team_id2")
            print("3. teams.csv -> team_id, team_name")
            print("4. venue.csv -> venue_id, venue_name")
            print("5. umpire_match.csv -> match_id, umpire_id1, umpire_id2")
            print("6. umpire.csv -> umpire_id, umpire_name")
            print("7. match_result.csv -> match_id, winner_id")
            print("8. player_of_the_match.csv -> match_id, player_of_the_match_id")
            print("9. players.csv -> player_id, player")
            print("10. toss.csv -> match_id, team_id, toss_winner")
            print("\nThe below is the information about the matches:")
            print("Match ID | Season | Date | Venue | Team 1 | Team 2 | Umpire 1 | Umpire 2 | Winner | Player of the Match")

            merged = match.merge(venue, on='venue_id', how='left') \
                  .merge(match_teams, on='match_id', how='left') \
                  .merge(teams.rename(columns={'team_id': 'team_id1', 'team': 'team1_name'}), on='team_id1', how='left') \
                  .merge(teams.rename(columns={'team_id': 'team_id2', 'team': 'team2_name'}), on='team_id2', how='left') \
                  .merge(umpire_match, on='match_id', how='left') \
                  .merge(umpire.rename(columns={'umpire_id': 'umpire_id1', 'umpire': 'umpire1_name'}), on='umpire_id1', how='left') \
                  .merge(umpire.rename(columns={'umpire_id': 'umpire_id2', 'umpire': 'umpire2_name'}), on='umpire_id2', how='left') \
                  .merge(match_result, on='match_id', how='left') \
                  .merge(teams.rename(columns={'team_id': 'winner_id', 'team': 'winner_name'}), on='winner_id', how='left') \
                  .merge(player_of_the_match, on='match_id', how='left') \
                  .merge(players.rename(columns={'player_id': 'player_of_the_match_id', 'player': 'pom_name'}), on='player_of_the_match_id', how='left')
            for i, row in merged.iterrows():
                print(f"{row['match_id']} | {row['season']} | {row['date']} | {row['venue']} | "
                    f"{row['team1_name']} | {row['team2_name']} | {row['umpire1_name']} | {row['umpire2_name']} | "
                    f"{row['winner_name']} | {row['pom_name']}")
            print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")
        elif choice==6:
            
            player_name = input("Enter the name of the player: ")
            start_time = time.time()
            try:
                player_id = players[players['player'] == player_name]['player_id'].values[0]
                batter_deliveries = delivery[delivery['batter_id'] == player_id]
                runs_scored = batter_deliveries['batsman_runs'].sum()
                matches_batted = batter_deliveries['match_id'].unique()
                dismissals_merged = dismissals.merge(
                    delivery,
                    on=['match_id', 'inning', 'over', 'ball'],
                    how='inner'
                )
                bowler_dismissals = dismissals_merged[dismissals_merged['bowler_id'] == player_id]

                # bowler_deliveries = delivery[(delivery['bowler_id'] == player_id) & (dismissals['is_wicket'] == 1)]
                wickets_taken = len(bowler_dismissals)
                matches_bowled = set(bowler_dismissals['match_id'].unique())
                catches = dismissals[(dismissals['dismissal_kind'] == 'caught') & (dismissals['fielder_id'] == player_id)]
                catches_taken = len(catches)
                matches_fielded = catches['match_id'].unique()
                all_matches = set(matches_batted) | set(matches_bowled) | set(matches_fielded)
                print(f"Player Name: {player_name}")
                print(f"Runs Scored: {runs_scored}")
                print(f"Wickets Taken: {wickets_taken}")
                print(f"Catches Taken: {catches_taken}")
                print("Total number of matches played by the player:", len(all_matches))
                print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")
            except IndexError:
                 print("Player not found. Please check the name.")
            
        elif choice==7:
            
            player_name = input("Enter the name of the player: ")
            start_time= time.time()
            try:
                player_id = players[players['player'] == player_name]['player_id'].values[0]
                potm_matches = player_of_the_match[player_of_the_match['player_of_the_match_id'] == player_id]
                if potm_matches.empty:
                    print(f"{player_name} has never been Player of the Match.")
                else:
                    merged_df = potm_matches.merge(match, on='match_id').merge(venue, on='venue_id')
                    print(f"Player Name: {player_name}")
                    print("Total number of matches in which the player was Player of the Match:", len(merged_df))
                    print("Player of the Match in the following matches:")
                    for idx, row in merged_df.iterrows():
                        print(f"{idx+1} | {player_name} | {row['date']} | {row['venue']}")
                print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")
            except IndexError:
                print("Player not found. Please check the name.")
        elif choice==8:

            
            team1_name=input("Enter the name of the first team: ")
            team2_name=input("Enter the name of the second team: ")
            start_time= time.time()
            team_id_map = dict(zip(teams['team'], teams['team_id']))
            team1_id = team_id_map.get(team1_name)
            team2_id = team_id_map.get(team2_name)
            if team1_id is None or team2_id is None:
                print("One or both team names are invalid.")
            else:
                mask = (
                    ((match_teams['team_id1'] == team1_id) & (match_teams['team_id2'] == team2_id)) |
                    ((match_teams['team_id1'] == team2_id) & (match_teams['team_id2'] == team1_id))
                )
                relevant_matches = match_teams[mask]
                match_ids = relevant_matches['match_id'].unique()
                matches_played = len(match_ids)
                relevant_results = match_result[match_result['match_id'].isin(match_ids)]
                team1_wins = (relevant_results['winner_id'] == team1_id).sum()
                team2_wins = (relevant_results['winner_id'] == team2_id).sum()
                relevant_tosses = toss[toss['match_id'].isin(match_ids)]
                team1_toss_winds = (relevant_tosses['toss_winner'] == team1_id).sum()
                team2_toss_winds = (relevant_tosses['toss_winner'] == team2_id).sum()
                print(f"Head to head stats between {team1_name} and {team2_name}:")
                print(f"Total matches played: {matches_played}")
                print(f"{team1_name} wins: {team1_wins}")
                print(f"{team2_name} wins: {team2_wins}")
                print(f"{team1_name} toss wins: {team1_toss_winds}")
                print(f"{team2_name} toss wins: {team2_toss_winds}")
            end_time = time.time()
            print(f"Execution time: {end_time - start_time:.4f} seconds")
            
        elif choice==9:
            
            player_name = input("Enter the name of the player: ")
            start_time = time.time()
            player_row = players[players['player'] == player_name]
            if player_row.empty:
                print("Invalid player name.")
            else:
                player_id = player_row['player_id'].values[0]
                delivery_season = delivery.merge(match[['match_id', 'season']], on='match_id', how='left')
                dismissals_with_season = dismissals.merge(
                    delivery_season,
                    on=['match_id', 'inning', 'over', 'ball'],
                    how='left'
                )
                caught_fielding_rows = dismissals_with_season[
                    (dismissals_with_season['dismissal_kind'] == 'caught') &
                    (dismissals_with_season['fielder_id'] == player_id)
                ]
                is_batter = delivery_season['batter_id'] == player_id
                is_bowler = delivery_season['bowler_id'] == player_id
                
                batter_rows = delivery_season[is_batter][['season', 'batting_team_id']].drop_duplicates('season')
                bowler_rows = delivery_season[is_bowler][['season', 'bowling_team_id']].drop_duplicates('season')
                fielder_rows = caught_fielding_rows[['season', 'bowling_team_id']].drop_duplicates('season')
                team_history = {}
                for _, row in batter_rows.iterrows():
                    team_history[row['season']] = row['batting_team_id']
                for _, row in bowler_rows.iterrows():
                    team_history.setdefault(row['season'], row['bowling_team_id'])
                for _, row in fielder_rows.iterrows():
                    team_history.setdefault(row['season'], row['bowling_team_id'])
                print(f"Player Name: {player_name}")
                print("Team history:")
                for season in sorted(team_history.keys()):
                    team_id = team_history[season]
                    team_name_row = teams[teams['team_id'] == team_id]['team']
                    team_name = team_name_row.values[0] if not team_name_row.empty else "Not Played"
                    print(f"Season {season}: {team_name}")
                end_time = time.time()
                print(f"Execution time: {end_time - start_time:.4f} seconds")
            
        elif choice==10:
            
            venue_name=input("Enter the name of the venue: ")
            start_time = time.time()
            venue_row = venue[venue['venue'] == venue_name]
            if venue_row.empty:
                print("Invalid venue name.")
            else:
                venue_id = venue_row['venue_id'].values[0]
                venue_matches = match[match['venue_id'] == venue_id]
                if venue_matches.empty:
                    print("No matches played at this venue.")
                else:
                    venue_match_results = venue_matches.merge(match_result, on='match_id', how='left')
                    venue_match_results = venue_match_results.merge(toss, on='match_id', how='left')
                    # venue_match_results = venue_match_results[venue_match_results['winner_id']]
                    matches_played = len(venue_match_results)
                    first_bat_wins=0
                    second_bat_wins=0
                    matches_abandoned=0
                    for _, row in venue_match_results.iterrows():
                        
                        winner = row['winner_id']
                        toss_winner = row['toss_winner']
                        toss_decision = row['toss_decision']
                        if pd.isna(winner):
                            matches_abandoned += 1
                            continue
                        if toss_decision == 'bat':
                            if winner == toss_winner:
                                first_bat_wins += 1
                            else:
                                second_bat_wins += 1
                        elif toss_decision == 'field':
                            if winner == toss_winner:
                                second_bat_wins += 1
                            else:
                                first_bat_wins += 1
                    print(f"Venue Name: {venue_name}")
                    print("Stats:")
                    print(f"Total matches played: {matches_played}")
                    print(f"Matches won while batting first: {first_bat_wins}")
                    print(f"Matches won while batting second: {second_bat_wins}")
                    print(f"Matches abandoned: {matches_abandoned}")

            end_time = time.time()
            print(f"Execution time: {end_time - start_time:.4f} seconds")
                        
        elif choice==11:
            
            venue1=input("Enter the name of the venue: ")
            start_time = time.time()
            venue_row = venue[venue['venue'] == venue1]
            if venue_row.empty:
                print("Invalid venue name.")
            else:
                venue_id = venue_row['venue_id'].values[0]
                venue_matches = match[match['venue_id'] == venue_id]
                if venue_matches.empty:
                    print("No matches played in this venue.")
                else:
                    first_innings = delivery[
                        (delivery['match_id'].isin(venue_matches['match_id'])) &
                        (delivery['inning'] == 1)
                    ]
                    total_runs = first_innings['total_runs'].sum()
                    matches_played = venue_matches.shape[0]
                    average_runs = total_runs / matches_played if matches_played > 0 else 0
                    print(f"Venue Name: {venue1}")
                    print("Stats:")
                    print(f"Total matches played: {matches_played}")
                    print(f"Average first innings score: {average_runs:.2f}")
                end_time = time.time()
                print(f"Execution time: {end_time - start_time:.4f} seconds")
        elif choice==12:
            start_time = time.time()
            delivery_season = delivery.merge(match[['match_id', 'season']], on='match_id', how='left')
            delivery_season['four'] = (delivery_season['batsman_runs'] == 4).astype(int)
            delivery_season['six'] = (delivery_season['batsman_runs'] == 6).astype(int)
            season_totals = delivery_season.groupby('season')[['four', 'six']].sum().reset_index()
            print("Total number of 4s and 6s per season:")
            for _, row in season_totals.iterrows():
                print(f"Season {(row['season'])}: 4s = {row['four']}, 6s = {row['six']}")
            end_time = time.time()
            print(f"\nExecution time: {end_time - start_time:.4f} seconds")
        elif choice==13:
            
            team_name = input("Enter the name of the team: ")
            start_time = time.time()
            team_id = teams[teams['team'] == team_name]['team_id'].values[0]
            delivery_season = delivery.merge(match[['match_id', 'season']], on='match_id', how='left')
            powerplay = delivery_season[(delivery_season['batting_team_id'] == team_id) & (delivery_season['over'] < 6)]
            runs_by_season = powerplay.groupby('season')['total_runs'].sum().reset_index()
            matches_by_season = powerplay[['season', 'match_id']].drop_duplicates().groupby('season').size().reset_index(name='matches')
            stats = runs_by_season.merge(matches_by_season, on='season')
            stats['avg_powerplay'] = stats['total_runs'] / stats['matches']
            print("Average powerplay score for each season:")
            for _, row in stats.iterrows():
                 print(f"Season {(row['season'])}: Average powerplay score = {row['avg_powerplay']:.2f}")
            end_time = time.time()
            print(f"\nExecution time: {end_time - start_time:.4f} seconds")
        elif choice==14:
            
            team_name = input("Enter the name of the team: ")
            start_time = time.time()
            team_row = teams[teams['team'] == team_name]
            if team_row.empty:
                print("Invalid team name")
            else:
                team_id = team_row['team_id'].values[0]
                delivery_season = delivery.merge(match[['match_id', 'season']], on='match_id', how='left')
                dismissals_season = dismissals.merge(
                    delivery_season[['match_id', 'inning', 'over', 'ball', 'season', 'bowling_team_id']],
                    on=['match_id', 'inning', 'over', 'ball'],
                    how='left'
                )
                powerplay = dismissals_season[
                    (dismissals_season['bowling_team_id'] == team_id) &
                    (dismissals_season['over'] < 6)
                ]
            
                wickets_by_season = powerplay.groupby('season').size().reset_index(name='wickets')
                matches_by_season = powerplay[['season', 'match_id']].drop_duplicates().groupby('season').size().reset_index(name='matches')
                stats = wickets_by_season.merge(matches_by_season, on='season')
                stats['avg_powerplay'] = stats['wickets'] / stats['matches']
                print("Average wickets taken in powerplay for each season:")
                for _, row in stats.iterrows():
                    print(f"Season {(row['season'])}: Average wickets taken = {row['avg_powerplay']:.2f}")
                end_time = time.time()
                print(f"\nExecution time: {end_time - start_time:.4f} seconds")
        elif choice == 15:
            start_time = time.time()
            player_stats = defaultdict(lambda: defaultdict(lambda: {
                'sixes': 0, 'fours': 0, 'dot_balls': 0, 'wickets': 0, 'runs': 0
            }))
            winner_ipl = {}
            runner_up_ipl = {}

            match_season = dict(zip(match['match_id'], match['season']))
            match_type = dict(zip(match['match_id'], match['match_type']))
            match_result_dict = dict(zip(match_result['match_id'], match_result['winner_id']))
            match_teams_dict = match_teams.set_index('match_id')[['team_id1', 'team_id2']].to_dict(orient='index')
            team_names = teams.set_index('team_id')['team'].to_dict()

            merged_df = pd.merge(delivery, dismissals,
                                on=['match_id', 'inning', 'over', 'ball'],
                                how='left')

            for idx, row in merged_df.iterrows():
                match_id = row['match_id']
                season = match_season.get(match_id)
                type = match_type.get(match_id)
                batter_id = row['batter_id']
                bowler_id = row['bowler_id']
                runs = row['batsman_runs']
                total_runs = row['total_runs']

                if type and "Final" in str(type) and season not in winner_ipl:
                    winner_id = match_result_dict.get(match_id)
                    team1_id = match_teams_dict.get(match_id, {}).get('team_id1')
                    team2_id = match_teams_dict.get(match_id, {}).get('team_id2')
                    if winner_id:
                        winner_ipl[season] = team_names.get(winner_id, "Unknown")
                        runner_up_id = team2_id if winner_id == team1_id else team1_id
                        runner_up_ipl[season] = team_names.get(runner_up_id, "Unknown")

                stats = player_stats[batter_id][season]
                stats['runs'] += runs
                if runs == 4:
                    stats['fours'] += 1
                elif runs == 6:
                    stats['sixes'] += 1

                # bowling stats
                stats = player_stats[bowler_id][season]
                if pd.notna(row.get('dismissal_kind')):
                    stats['wickets'] += 1
                elif total_runs == 0:
                    stats['dot_balls'] += 1

            orange_cap = defaultdict(lambda: (None, 0))
            purple_cap = defaultdict(lambda: (None, 0))
            most_sixes = defaultdict(lambda: (None, 0))
            most_fours = defaultdict(lambda: (None, 0))

            for player_id, seasons in player_stats.items():
                for season, stats in seasons.items():
                    if stats['runs'] > orange_cap[season][1]:
                        orange_cap[season] = (player_id, stats['runs'])
                    if stats['wickets'] > purple_cap[season][1]:
                        purple_cap[season] = (player_id, stats['wickets'])
                    if stats['sixes'] > most_sixes[season][1]:
                        most_sixes[season] = (player_id, stats['sixes'])
                    if stats['fours'] > most_fours[season][1]:
                        most_fours[season] = (player_id, stats['fours'])

            season_in = input("Enter season or press Enter for ALL: ").strip()

            print("Season Awards:")
            if season_in:
                if season_in in orange_cap:
                    seasons_to_print = [season_in]
                else:
                    print(f"No data found for season {season_in}.")
                    seasons_to_print = []
            else:
                seasons_to_print = sorted(orange_cap.keys())

            for season in seasons_to_print:
                orange_player = players[players['player_id'] == orange_cap[season][0]]['player'].values[0]
                purple_player = players[players['player_id'] == purple_cap[season][0]]['player'].values[0]
                sixes_player = players[players['player_id'] == most_sixes[season][0]]['player'].values[0]
                fours_player = players[players['player_id'] == most_fours[season][0]]['player'].values[0]
                print(f"\n Season {season}:")
                print(f" Orange Cap: {orange_player} ({orange_cap[season][1]} runs)")
                print(f" Purple Cap: {purple_player} ({purple_cap[season][1]} wickets)")
                print(f" Most Sixes: {sixes_player} ({most_sixes[season][1]} sixes)")
                print(f" Most Fours: {fours_player} ({most_fours[season][1]} fours)")
                print(f" Winner: {winner_ipl.get(season,'Unknown')}")
                print(f" Runner Up: {runner_up_ipl.get(season,'Unknown')}")

            end_time = time.time()
            print(f"\nExecution time: {end_time - start_time:.4f} seconds")

        elif choice==16:
            
            umpire_name = input("Enter the name of the umpire: ").strip()
            start_time= time.time()
            umpire_row = umpire[umpire['umpire'].str.lower() == umpire_name.lower()]
            if umpire_row.empty:
                print(f"Umpire '{umpire_name}' not found.")
            else:
                umpire_id = umpire_row['umpire_id'].values[0]
                matches_judged = (umpire_match['umpire_id1'] == umpire_id).sum()
                matches_judged+=(umpire_match['umpire_id2'] == umpire_id).sum()
                print(f"Umpire Name: {umpire_name}")
                print("Total number of matches judged by the umpire:", matches_judged)
                print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")
        elif choice==17:
            start_time= time.time()
            print("Calculating most 50s and 100s per season...")
            delivery_with_season = delivery.merge(match[['match_id', 'season']], on='match_id')
            match_runs = delivery_with_season.groupby(['batter_id', 'season', 'match_id'])['batsman_runs'].sum().reset_index()
            match_runs['fifty'] = match_runs['batsman_runs'].between(50, 99)
            match_runs['hundred'] = match_runs['batsman_runs'] >= 100
            fifties_count = match_runs.groupby(['batter_id', 'season'])['fifty'].sum().reset_index()
            hundreds_count = match_runs.groupby(['batter_id', 'season'])['hundred'].sum().reset_index()
            stats = fifties_count.merge(hundreds_count, on=['batter_id', 'season'])
            most_fifties = stats.loc[stats.groupby('season')['fifty'].idxmax()]
            most_hundreds = stats.loc[stats.groupby('season')['hundred'].idxmax()]
            print("Most Fifties and Hundreds per season:")
            for season in sorted(stats['season'].unique()):
                fifties_row = most_fifties[most_fifties['season'] == season]
                hundreds_row = most_hundreds[most_hundreds['season'] == season]
                fifties_player = players[players['player_id'] == fifties_row['batter_id'].values[0]]['player'].values[0]
                hundreds_player = players[players['player_id'] == hundreds_row['batter_id'].values[0]]['player'].values[0]
                print(f"\n Season {season}:")
                print(f" Most Fifties: {fifties_player} ({fifties_row['fifty'].values[0]} fifties)")
                print(f" Most Hundreds: {hundreds_player} ({hundreds_row['hundred'].values[0]} hundreds)")
            print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")
                                
        elif choice==18:
            start_time=time.time()
            delivery_with_season = delivery.merge(match[['match_id', 'season']], on='match_id')
            merged = delivery_with_season.merge(
                dismissals[['match_id', 'inning', 'over', 'ball']],
                on=['match_id', 'inning', 'over', 'ball'],
                how='left',
                indicator=True
            )
            merged['is_wicket'] = merged['_merge'] == 'both'
            wickets_per_match = merged[merged['is_wicket']] \
                .groupby(['bowler_id', 'season', 'match_id']).size().reset_index(name='wicket_count')
            wickets_per_match = wickets_per_match[wickets_per_match['wicket_count'] >= 5]
            five_wicket_hauls = wickets_per_match.groupby(['bowler_id', 'season']).size().reset_index(name='five_wicket_hauls')
            most_five_wickets = five_wicket_hauls.loc[five_wicket_hauls.groupby('season')['five_wicket_hauls'].idxmax()]
            print("Most 5-Wicket Takers per Season:")
            for _, row in most_five_wickets.iterrows():
                player_name = players[players['player_id'] == row['bowler_id']]['player'].values[0]
                print(f"\n Season {row['season']}:")
                print(f" Most 5-Wicket Taker: {player_name} ({row['five_wicket_hauls']} times)") 
            print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")       
        elif choice==19:
            
            print("Bowler vs Batter Comparison")
            bowler_name = input("Enter the name of the bowler: ").strip()
            batter_name = input("Enter the name of the batter: ").strip()
            start_time=time.time()
            bowler_row = players[players['player'].str.lower() == bowler_name.lower()]
            batter_row = players[players['player'].str.lower() == batter_name.lower()]
            if bowler_row.empty or batter_row.empty:
                print(" Invalid bowler or batter name.")
            else:
                bowler_id = bowler_row['player_id'].values[0]
                batter_id = batter_row['player_id'].values[0]
                vs_df = delivery[(delivery['bowler_id'] == bowler_id) & (delivery['batter_id'] == batter_id)]
                if vs_df.empty:
                    print(" No deliveries found between this bowler and batter.")
                else:
                    vs_df = vs_df.copy()
                    vs_df = vs_df.merge(
                        dismissals[['match_id', 'inning', 'over', 'ball']],
                        on=['match_id', 'inning', 'over', 'ball'],
                        how='left',
                        indicator=True
                    )
                    vs_df['is_wicket'] = vs_df['_merge'] == 'both'
                    # vs_df['is_wicket'] = dismissals.loc[vs_df.index, 'is_wicket']
                    total_balls = len(vs_df)
                    total_runs = vs_df['batsman_runs'].sum()
                    dot_balls = (vs_df['total_runs'] == 0).sum()
                    wickets = vs_df['is_wicket'].sum()
                    print(f"\n Head-to-Head: {bowler_name} vs {batter_name}")
                    print(f" Balls Bowled: {total_balls}")
                    print(f" Runs Scored: {total_runs}")
                    print(f" Wickets Taken: {wickets}")
                    print(f" Dot Balls: {dot_balls}")
                    print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")                       
        elif choice==20:
            
            old_team_name = input("Enter the old name of the team: ").strip()
            new_team_name = input("Enter the new name of the team: ").strip()
            start_time= time.time()

            # Check if input is empty
            if not old_team_name or not new_team_name:
                print("Team names cannot be empty.")
            else:
                team_id = teams[teams['team'].str.lower() == old_team_name.lower()]['team_id'].values

                if len(team_id) == 0:
                    print(f"Team '{old_team_name}' not found.")
                else:
                    team_id = team_id[0]
                    teams.loc[teams['team_id'] == team_id, 'team'] = new_team_name
                    teams.to_csv('normalized csvs/teams.csv', index=False)
                    print(f"Team name updated successfully from '{old_team_name}' to '{new_team_name}'.")
                    print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")

        elif choice==21:
            old_venue_name = input("Enter the old name of the venue: ").strip()
            new_venue_name = input("Enter the new name of the venue: ").strip()
            start_time= time.time()

            # Check if input is empty
            if not old_venue_name or not new_venue_name:
                print("Venue names cannot be empty.")
            else:
                venue_id = venue[venue['venue'].str.lower() == old_venue_name.lower()]['venue_id'].values

                if len(venue_id) == 0:
                    print(f"Venue '{old_venue_name}' not found.")
                else:
                    venue_id = venue_id[0]
                    venue.loc[venue['venue_id'] == venue_id, 'venue'] = new_venue_name
                    venue.to_csv('normalized csvs/venue.csv', index=False)
                    print(f"Venue name updated successfully from '{old_venue_name}' to '{new_venue_name}'.")
                    print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")
       
        elif choice==22:
            team_name = input("Enter team name: ").strip()
            season_in = input("Enter season or press Enter for all seasons: ").strip()
            start_time = time.time()
            trow = teams[teams['team'].str.lower() == team_name.lower()]
            if trow.empty:
                print("Invalid team name.")
            else:
                team_id = trow['team_id'].values[0]
                mt = match_teams.merge(match[['match_id','season']], on='match_id', how='left')
                # select rows where either team1 or team2 is the team
                sel = mt[(mt['team_id1']==team_id) | (mt['team_id2']==team_id)].copy()
                sel = sel[ season_mask_from_input(sel['season'], season_in) ]
                if sel.empty:
                    print("No matches found for given inputs.")
                else:
                    out = sel.groupby('season').size().reset_index(name='matches_played').sort_values('season')
                    print(f"Matches for {team_name}:")
                    for _, r in out.iterrows():
                        print(f"Season {r['season']}: {int(r['matches_played'])}")
            print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")

        elif choice==23:
            season_in = input("Enter season (e.g., 2017 or 2017/18): ").strip()
            start_time = time.time()
            d = delivery.merge(match[['match_id','season']], on='match_id', how='left')
            mask = season_mask_from_input(d['season'], season_in)
            dsel = d[mask]
            if dsel.empty:
                print("No data for that season.")
            else:
                runs = dsel.groupby('batter_id')['batsman_runs'].sum().reset_index()
                runs = runs.merge(players[['player_id','player']], left_on='batter_id', right_on='player_id', how='left')
                runs = runs.sort_values('batsman_runs', ascending=False).head(10)
                print(f"Top run-scorers in season {season_in if season_in else 'ALL'} (top 10):")
                for _, r in runs.iterrows():
                    name = r['player'] if pd.notna(r['player']) else f"id:{int(r['batter_id'])}"
                    print(f"{name}: {int(r['batsman_runs'])} runs")
            print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")

        elif choice==24:
            season_in = input("Enter season: ").strip()
            min_balls_in = input("Enter minimum balls threshold (press Enter for 100): ").strip()
            try:
                min_balls = int(min_balls_in) if min_balls_in else 100
            except:
                min_balls = 100
            start_time = time.time()
            d = delivery.merge(match[['match_id','season']], on='match_id', how='left')
            dsel = d[ season_mask_from_input(d['season'], season_in) ]
            if dsel.empty:
                print("No data for that season.")
            else:
                grp = dsel[dsel['bowler_id']>0].groupby('bowler_id').agg(balls=('bowler_id','size'),
                                                                          runs_conceded=('total_runs','sum')).reset_index()
                grp = grp[grp['balls'] >= min_balls].copy()
                if grp.empty:
                    print(f"No bowlers with at least {min_balls} balls in given season.")
                else:
                    grp['economy'] = (grp['runs_conceded'] / grp['balls']) * 6.0
                    grp = grp.merge(players[['player_id','player']], left_on='bowler_id', right_on='player_id', how='left')
                    grp = grp.sort_values('economy').head(10)
                    print(f"Top economical bowlers in season {season_in if season_in else 'ALL'} (min {min_balls} balls):")
                    for _, r in grp.iterrows():
                        name = r['player'] if pd.notna(r['player']) else f"id:{int(r['bowler_id'])}"
                        print(f"{name}: economy {r['economy']:.2f} (Balls {int(r['balls'])}, Runs {int(r['runs_conceded'])})")
            print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")


        elif choice==25:
            team_name = input("Enter team name: ").strip()
            season_in = input("Enter season or press Enter for all: ").strip()
            min_balls_in = input("Enter minimum balls threshold (default 60): ").strip()
            try:
                min_balls = int(min_balls_in) if min_balls_in else 60
            except:
                min_balls = 60
            start_time = time.time()
            trow = teams[teams['team'].str.lower() == team_name.lower()]
            if trow.empty:
                print("Invalid team name.")
            else:
                team_id = trow['team_id'].values[0]
                d = delivery.merge(match[['match_id','season']], on='match_id', how='left')
                sel = d[(d['batting_team_id']==team_id)]
                sel = sel[ season_mask_from_input(sel['season'], season_in) ]
                if sel.empty:
                    print("No data for that team/season.")
                else:
                    grp = sel.groupby('batter_id').agg(balls=('batter_id','size'),
                                                       runs=('batsman_runs','sum')).reset_index()
                    grp = grp[grp['balls'] >= min_balls].copy()
                    if grp.empty:
                        print(f"No batters with at least {min_balls} balls.")
                    else:
                        grp['strike_rate'] = (grp['runs'] / grp['balls']) * 100.0
                        grp = grp.merge(players[['player_id','player']], left_on='batter_id', right_on='player_id', how='left')
                        grp = grp.sort_values('strike_rate', ascending=False).head(10)
                        print(f"Top strike rates for {team_name} in {season_in if season_in else 'ALL'} (min {min_balls} balls):")
                        for _, r in grp.iterrows():
                            name = r['player'] if pd.notna(r['player']) else f"id:{int(r['batter_id'])}"
                            print(f"{name}: SR {r['strike_rate']:.2f} (Runs {int(r['runs'])}, Balls {int(r['balls'])})")
            print(f"\n Time taken: {time.time() - start_time:.4f} seconds\n")


        elif choice == 26:
            pname = input("Enter player name: ").strip()
            pid = get_player_id_by_name(pname)
            if pid is None:
                print("Player not found.")
            else:
                start_time = time.time()
                run_col = find_col(delivery, ['batsman_runs','batsman_id','runs','batsman_run','batter_runs'])
                if run_col is None or 'match_id' not in delivery.columns:
                    print("Required delivery columns missing to compute runs per season.")
                else:
                    d = delivery.merge(match[['match_id','season']], on='match_id', how='left')
                    runs_season = d.loc[d['batter_id'] == pid].groupby('season')[run_col].sum().reset_index().sort_values(run_col, ascending=False)
                    if {'match_id','inning','over','ball'}.issubset(dismissals.columns) and {'match_id','inning','over','ball','bowler_id'}.issubset(delivery.columns):
                        merged = dismissals.merge(delivery[['match_id','inning','over','ball','bowler_id']], on=['match_id','inning','over','ball'], how='left')
                        merged = merged.merge(match[['match_id','season']], on='match_id', how='left')
                        wkts_season = merged.loc[merged['bowler_id'] == pid].groupby('season').size().reset_index(name='wickets').sort_values('wickets', ascending=False)
                    else:
                        wkts_season = pd.DataFrame(columns=['season','wickets'])
                    if not runs_season.empty:
                        top_run = runs_season.iloc[0]
                        print(f"Best batting season: {top_run['season']} with {int(top_run[run_col])} runs")
                    else:
                        print("No batting records found.")
                    if not wkts_season.empty:
                        top_wkt = wkts_season.iloc[0]
                        print(f"Best bowling season: {top_wkt['season']} with {int(top_wkt['wickets'])} wickets")
                    else:
                        print("No bowling records found.")
                print(f"\nTime taken: {time.time() - start_time:.4f} s\n")

        elif choice == 27:
            pname = input("Enter player name: ").strip()
            pid = get_player_id_by_name(pname)
            if pid is None:
                print("Player not found.")
            else:
                start_time = time.time()
                run_col = find_col(delivery, ['batsman_runs','batsman_id','runs','batsman_run','batter_runs'])
                if run_col is None:
                    print("Batsman run column not found.")
                else:
                    d = delivery.merge(match[['match_id','season']], on='match_id', how='left')
                    if {'match_id','inning','over','ball'}.issubset(dismissals.columns):
                        merged = d.merge(dismissals[['match_id','inning','over','ball','dismissal_kind','fielder_id']],
                                        on=['match_id','inning','over','ball'], how='left')
                    else:
                        merged = d.copy()
                        merged['dismissal_kind'] = None
                    player_rows = merged.loc[merged['batter_id'] == pid]
                    if player_rows.empty:
                        print("No batting records for this player.")
                    else:
                        stats = player_rows.groupby('season').agg(balls=('batter_id','count'),
                                                                runs=(run_col,'sum'),
                                                                outs=('dismissal_kind', lambda x: x.notna().sum())).reset_index()
                        print(f"Season-wise SR & Avg for {pname}:")
                        for _, r in stats.iterrows():
                            balls = int(r['balls']); runs = int(r['runs']); outs = int(r['outs'])
                            sr = (runs/balls)*100.0 if balls>0 else 0.0
                            avg = (runs/outs) if outs>0 else float('nan')
                            avg_str = f"{avg:.2f}" if outs>0 else "NA"
                            print(f"{r['season']}: SR={sr:.2f}, Avg={avg_str} (Runs {runs}, Balls {balls}, Outs {outs})")
                print(f"\nTime taken: {time.time() - start_time:.4f} s\n")


        elif choice == 28:
            season_in = input("Enter season or press Enter for ALL: ").strip()
            start_time = time.time()
            run_col = find_col(delivery, ['batsman_runs','batsman_id','runs','batsman_run','batter_runs'])
            if run_col is None or 'non_striker_id' not in delivery.columns:
                print("Partnership query requires 'non_striker_id' and a batsman-run column in delivery.")
            else:
                d = delivery.merge(match[['match_id','season']], on='match_id', how='left')
                d = d[ season_mask_from_input(d['season'], season_in) ]
                if d.empty:
                    print("No deliveries for the specified season.")
                else:
                    d['p1'] = d[['batter_id','non_striker_id']].apply(lambda x: int(min(x['batter_id'], x['non_striker_id'])), axis=1)
                    d['p2'] = d[['batter_id','non_striker_id']].apply(lambda x: int(max(x['batter_id'], x['non_striker_id'])), axis=1)
                    agg = d.groupby(['season','match_id','inning','p1','p2'])[run_col].sum().reset_index(name='partnership_runs')
                    top_per_season = agg.sort_values(['season','partnership_runs'], ascending=[True,False]).groupby('season').first().reset_index()
                    top_per_season = top_per_season.merge(players[['player_id','player']], left_on='p1', right_on='player_id', how='left') \
                                                .merge(players[['player_id','player']], left_on='p2', right_on='player_id', how='left', suffixes=('_p1','_p2'))
                    print(f"Top partnership (approx) per season for '{season_in if season_in else 'ALL'}':")
                    for _, r in top_per_season.iterrows():
                        p1 = r['player_p1'] if pd.notna(r['player_p1']) else f"id:{int(r['p1'])}"
                        p2 = r['player_p2'] if pd.notna(r['player_p2']) else f"id:{int(r['p2'])}"
                        print(f"Season {r['season']}: {p1} & {p2} -> {int(r['partnership_runs'])} runs ")
            print(f"\nTime taken: {time.time() - start_time:.4f} s\n")

        elif choice == 29:
            start_time = time.time()
            um_df = get_umpire_match_df()
            if um_df is None or um_df.empty:
                print("Umpire-match data not available (expected 'umpire_match' or 'umpir_match').")
            else:
                um = um_df.copy()
                um['u1'] = um[['umpire_id1','umpire_id2']].min(axis=1)
                um['u2'] = um[['umpire_id1','umpire_id2']].max(axis=1)
                top = um.groupby(['u1','u2']).size().reset_index(name='count').sort_values('count', ascending=False).head(10)
                top = top.merge(umpire[['umpire_id','umpire']], left_on='u1', right_on='umpire_id', how='left') \
                        .merge(umpire[['umpire_id','umpire']], left_on='u2', right_on='umpire_id', how='left', suffixes=('_u1','_u2'))
                print("Most frequent umpire pairings:")
                for _, r in top.iterrows():
                    n1 = r['umpire_u1'] if pd.notna(r['umpire_u1']) else f"id:{int(r['u1'])}"
                    n2 = r['umpire_u2'] if pd.notna(r['umpire_u2']) else f"id:{int(r['u2'])}"
                    print(f"{n1} & {n2}: {int(r['count'])} matches")
            print(f"\nTime taken: {time.time() - start_time:.4f} s\n")

        elif choice == 30:
            uname = input("Enter umpire name: ").strip()
            start_time = time.time()
            if 'umpire' not in globals() or 'umpire_id' not in umpire.columns:
                print("Umpire table not present or missing columns.")
            else:
                urows = umpire[umpire['umpire'].str.lower().str.contains(uname.lower(), na=False)]
                if urows.empty:
                    print("Umpire not found.")
                else:
                    uid = int(urows.iloc[0]['umpire_id'])
                    umdf = get_umpire_match_df()
                    if umdf is None:
                        print("Umpire-match table not available.")
                    else:
                        mids = umdf.loc[(umdf['umpire_id1'] == uid) | (umdf['umpire_id2'] == uid), 'match_id'].unique().tolist()
                        if len(mids) == 0:
                            print("No matches found for this umpire.")
                        else:
                            winners = match_result[match_result['match_id'].isin(mids)]
                            win_counts = winners.groupby('winner_id').size().reset_index(name='wins')
                            matches_played = match_teams[match_teams['match_id'].isin(mids)]
                            mp = pd.melt(matches_played, id_vars=['match_id'], value_vars=['team_id1','team_id2'], value_name='team_id')[['match_id','team_id']]
                            mp_counts = mp.groupby('team_id')['match_id'].nunique().reset_index(name='matches')
                            info = mp_counts.merge(win_counts, left_on='team_id', right_on='winner_id', how='left').fillna(0)
                            info = info.merge(teams[['team_id','team']], left_on='team_id', right_on='team_id', how='left')
                            info['win_pct'] = info['wins'] / info['matches'] * 100.0
                            info = info.sort_values('win_pct', ascending=False).head(15)
                            print(f"Win % for teams in matches officiated by {urows.iloc[0]['umpire']}:")
                            for _, r in info.iterrows():
                                print(f"{r['team']}: {r['win_pct']:.2f}% ({int(r['wins'])}/{int(r['matches'])})")
            print(f"\nTime taken: {time.time() - start_time:.4f} s\n")

        elif choice == 31:
            season_in = input("Enter season or press Enter for ALL: ").strip()
            start_time = time.time()
            if 'total_runs' not in delivery.columns:
                print("Column 'total_runs' not found in delivery.")
            else:
                d = delivery.merge(match[['match_id','season','date']], on='match_id', how='left')
                dsel = d[ season_mask_from_input(d['season'], season_in) ]
                if dsel.empty:
                    print("No deliveries for that season.")
                else:
                    totals = dsel.groupby('match_id')['total_runs'].sum().reset_index(name='total_runs').sort_values('total_runs', ascending=False).head(10)
                    info = totals.merge(match[['match_id','season','date']], on='match_id', how='left') \
                                .merge(match_teams, on='match_id', how='left') \
                                .merge(teams.rename(columns={'team_id':'team_id1','team':'team1'}), on='team_id1', how='left') \
                                .merge(teams.rename(columns={'team_id':'team_id2','team':'team2'}), on='team_id2', how='left')
                    print(f"Top 10 highest-scoring matches in season {season_in if season_in else 'ALL'}:")
                    for _, r in info.iterrows():
                        print(f"{r['season']} | {r.get('date','')}: {r.get('team1','Unknown')} vs {r.get('team2','Unknown')} -> Total runs {int(r['total_runs'])}")
            print(f"\nTime taken: {time.time() - start_time:.4f} s\n")

        elif choice == 32:
            start_time = time.time()
            pmask = match['match_type'].astype(str).str.contains('Qualifier|Eliminator|Final', case=False, na=False)
            playoffs = match.loc[pmask, 'match_id'].unique().tolist()
            if len(playoffs) == 0:
                print("No playoff matches found in 'match.match_type'.")
            else:
                mt = match_teams[match_teams['match_id'].isin(playoffs)]
                counts = pd.concat([mt['team_id1'], mt['team_id2']]).value_counts().reset_index()
                counts.columns = ['team_id','appearances']
                counts = counts.merge(teams, left_on='team_id', right_on='team_id', how='left')
                print("Top teams by playoff matches appearance:")
                for _, r in counts.head(10).iterrows():
                    print(f"{r['team']}: {int(r['appearances'])} playoff matches appearance")
            print(f"\nTime taken: {time.time() - start_time:.4f} s\n")

        elif choice == 33:
            start_time = time.time()

            finals_mask = match['match_type'].astype(str).str.contains('final', case=False, na=False)
            finals_df = match.loc[finals_mask, ['match_id', 'season', 'date', 'match_type']].copy()

            if finals_df.empty:
                print("No Finals found (check match_type values).")
            else:
                finals_df['date_parsed'] = pd.to_datetime(finals_df['date'], errors='coerce')

                def pick_one_final(g):
                    if g['date_parsed'].notna().any():
                        return g.loc[g['date_parsed'].idxmax()]
                    else:
                        return g.loc[g['match_id'].idxmax()]

                finals_picked = finals_df.groupby('season', as_index=False).apply(pick_one_final).reset_index(drop=True)

                finals_with_winner = finals_picked.merge(match_result[['match_id', 'winner_id']], on='match_id', how='left')

                finals_with_winner = finals_with_winner.merge(teams[['team_id', 'team']], left_on='winner_id', right_on='team_id', how='left')

                finals_with_winner = finals_with_winner.sort_values(by=['date_parsed', 'season'], ascending=[True, True])

                print("Finals winners by season:")
                for _, r in finals_with_winner.iterrows():
                    season_str = str(r['season'])
                    winner_name = r['team'] if pd.notna(r['team']) else 'Unknown'
                    print(f"{season_str}: {winner_name}")

            print(f"\nTime taken: {time.time() - start_time:.4f} s\n")



        elif choice == 34:
            start_time = time.time()
            # Pick only playoff matches (Qualifier, Eliminator, Semi Final, Final)
            pmask = match['match_type'].astype(str).str.contains('Qualifier|Eliminator|Final|Semi', case=False, na=False)
            playoffs = match.loc[pmask, ['match_id', 'season', 'date', 'match_type']].copy()

            if playoffs.empty:
                print("No playoff matches found.")
            else:
                pom = player_of_the_match.merge(playoffs, on='match_id', how='inner')
                pom = pom.merge(players, left_on='player_of_the_match_id', right_on='player_id', how='left')

                if pom.empty:
                    print("No Player-of-the-Match data for playoff matches.")
                else:
                    print("Player of the Match in playoff matches:")
                    for _, r in pom.iterrows():
                        mdate = r['date']
                        pname = r['player'] if pd.notna(r['player']) else "Unknown Player"
                        mtype = r['match_type'] if pd.notna(r['match_type']) else "Playoff Match"
                        print(f"{mdate}: {pname} ({mtype})")

            print(f"\nTime taken: {time.time() - start_time:.4f} s\n")




        
        elif choice==35:
            print("Exiting the program...")
            time.sleep(1)
            print("Thank you for using the IPL Data Analysis Program!")
            time.sleep(1)
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
            time.sleep(1)
            



                

        
        
        



            
        time.sleep(1)
        
        # break