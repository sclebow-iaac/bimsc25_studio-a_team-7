import os

# Get the full chart from a markdown file
path = os.getcwd()
path = os.path.join(path, 'Notes')
path = os.path.join(path, 'scl_notes.md')

with open(path, "r") as file:
    file_contents = file.read()
    # Find the start and end of the chart in the markdown file
    start_index = file_contents.index("```mermaid")
    print(f'Start index: {start_index}')
    rest_of_file = file_contents[start_index:]
    print(rest_of_file)
    end_index = start_index + rest_of_file.index("```") + 3
    print(f'End index: {end_index}')
    full_chart = rest_of_file[:end_index]

# Extract teams from the full chart
teams = set()
for line in full_chart.splitlines():
    if '-->' in line:
        index_0 = line.index('--')
        index_1 = line.index('-->')

        team_0 = line[:index_0].strip()
        team_1 = line[index_1 + 3:].strip()

        teams.add(team_0)
        teams.add(team_1)

path = os.getcwd()
path = os.path.join(path, 'Chart Generator')
path = os.path.join(path, 'Team Charts')

# print(path)

# Create markdown files for each team
for team in teams:
    team_chart = f"""```mermaid\n    graph LR\n"""
    print(team)
    for line in full_chart.splitlines():
        if "--" in line:
            if team in line:
                team_chart += line + '\n'
    team_chart += "```"

    team_path = os.path.join(path, f"{team}.md")
    # print(team_path)

    # Write to markdown file
    with open(team_path, "w") as file:
        file.write(team_chart)

# Create markdown file for each pair of teams
for team_0 in teams:
    for team_1 in teams:
        if team_0 != team_1:
            team_chart = f"""```mermaid\n    graph LR\n"""
            print(team_0, team_1)
            for line in full_chart.splitlines():
                if "--" in line:
                    if team_0 in line and team_1 in line:
                        team_chart += line + '\n'
            team_chart += "```"

            team_path = os.path.join(path, f"{team_0} - {team_1}.md")
            # print(team_path)

            # Write to markdown file
            with open(team_path, "w") as file:
                file.write(team_chart)