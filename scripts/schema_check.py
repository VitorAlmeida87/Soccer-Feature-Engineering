import pandas as pd, json
from pathlib import Path

mf = sorted(Path("data/matches").iterdir())[0]
mid = mf.name

with open(mf / f"{mid}_match.json") as f:
    mj = json.load(f)
print("HOME TEAM KEYS:", list(mj["home_team"].keys()))
print("home_team_id:", mj["home_team"]["id"])
print("away_team_id:", mj["away_team"]["id"])

de = pd.read_csv(mf / f"{mid}_dynamic_events.csv", low_memory=False)
print("\nevent_type uniques:", sorted(de["event_type"].dropna().unique().tolist()))
obr = de.loc[de["event_type"] == "off_ball_run", "event_subtype"].dropna().unique().tolist()
print("off_ball_run subtypes:", sorted(obr))

cols = [
    "pressing_chain_index","pressing_chain_length","last_line_break",
    "first_line_break","second_last_line_break","dangerous","lead_to_shot",
    "lead_to_goal","pass_direction","player_targeted_penalty_area_reception",
    "channel_start","third_start","n_opponents_bypassed","pass_distance","team_id"
]
for c in cols:
    if c in de.columns:
        print(f"{c}: dtype={de[c].dtype}, sample={de[c].dropna().unique()[:4].tolist()}")
    else:
        print(f"{c}: MISSING")

pop = pd.read_csv(mf / f"{mid}_phases_of_play.csv")
print("\nteam_in_possession_phase_type:", sorted(pop["team_in_possession_phase_type"].dropna().unique().tolist()))
print("team_out_of_possession_phase_type:", sorted(pop["team_out_of_possession_phase_type"].dropna().unique().tolist()))
print("team_in_possession_id sample:", pop["team_in_possession_id"].dropna().unique()[:4].tolist())
print("pop columns:", pop.columns.tolist())
