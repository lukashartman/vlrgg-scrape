# vlrgg-scrape
This tool navigates vlr.gg and scrapes data from recent match results. It will (hopefully) scrape the following data to be used for machine learning purposes:

| Data                            | Type         | Description                                                                                                                  |
|---------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------|
| UUID                            | Alphanumeric | Unique identifier to data cleanup purposes                                                                                   |
| Loadout Value                   | Number       | Value of entire teams loadout for round                                                                                      |
| Previous Loadout Value          | Number       | Value of entire teams loadout for previous round                                                                             |
| Team                            | String       | Name of team/org                                                                                                             |
| Map                             | String       | Name of Map                                                                                                                  |
| Map Pick                        | Boolean      | True if team picked map, false if not                                                                                        |
| Side                            | Boolean      | True if defense, false if attack                                                                                             |
| Consecutive Round Wins          | Number       | Number of rounds team has currently won/lost in a row. <br/> Positive if consecutive wins, negative if consecutive losses    |
| Total Round Wins                | Number       | Number of rounds team has won during a matchup                                                                               |
| Total Round Losses              | Number       | Number of rounds team has lost during a matchup                                                                              |
| Opponent Consecutive Round Wins | Number       | Number of rounds opponent has currently won/lost in a row. <br/> Positive if consecutive wins, negative if consecutive losse |
| Opponent Total Round Wins       | Number       | Number of rounds opponent has won during a matchup                                                                                  |
| Opponent Total Round Losses     | Number       | Number of rounds opponent has lost during a matchup                                                                          |
| Round Type                      | String       | Determinate of how team has won/lost (i.e, elimination, time, defuse, etc)                                                   |
|                                 |              |                                                                                                                              |
