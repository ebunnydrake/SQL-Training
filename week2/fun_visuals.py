import pandas as pd
import plotly.express as px

# Load CSV with state, vehicle_maker, total_orders columns
file_path = "/Users/elliedrake/SQL-Training/week2/top-maker-by-state.csv"
df = pd.read_csv(file_path)

# Ensure 'state' column uses full state names
# If your CSV uses abbreviations (like 'CA'), set locationmode="USA-states"
# If it uses full names (like 'California'), use locationmode="USA-states" + mapping if needed

# Mapping from state names to abbreviations
state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
    'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
    'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}

# Convert state names to abbreviations if needed
if df['state'].iloc[0] not in state_abbrev.values():
    df['state'] = df['state'].map(state_abbrev)

# Group to get total orders per state (if needed)
state_totals = df.groupby("state", as_index=False)["total_orders"].sum()

# Plot the map
fig = px.choropleth(
    state_totals,
    locations="state",
    locationmode="USA-states",  # For state abbreviations like 'CA', 'TX'
    color="total_orders",
    color_continuous_scale="Blues",
    scope="usa",
    title="Top Vehicle Maker Order Count by State"
)

fig.show()
