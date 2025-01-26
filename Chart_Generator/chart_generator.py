import os
import subprocess

def write_to_file(file_path, content, file_name, generate_img=False):
    with open(file_path, "w") as file:
        file.write(content)
        print()
        print(f'File written to: {file_path}')

    if generate_img:
        subprocess.run('cd Team_Charts', shell=True)

        png_file_path = file_path.replace(".md", ".svg")

        command = f"mmdc -i {file_path} -o {png_file_path}"
        print(f'Command: {command}')

        subprocess.run(command, shell=True)
        # print(f'PNG file generated at: {png_file_path}')

# Get the Full_Chart from a markdown file
path = os.getcwd()
path = os.path.join(path, 'Notes')
path = os.path.join(path, 'scl_notes.md')

with open(path, "r") as file:
    file_contents = file.read()
    # Find the start and end of the first chart in the markdown file
    start_index = file_contents.index("```mermaid")
    # print(f'Start index: {start_index}')
    rest_of_file = file_contents[start_index:]
    # print(rest_of_file)
    end_index = start_index + rest_of_file.index("\n```") + 3
    # print(f'End index: {end_index}')
    full_chart = file_contents[start_index:end_index]
    # print()
    # print(f'Full_Chart: {full_chart}')

# Extract teams from the Full_Chart
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
path = os.path.join(path, 'Chart_Generator')
path = os.path.join(path, 'Team_Charts')

# print(path)

styles = {
    "Residential(Residential)": "\n    style Residential fill:#33a9ac, stroke:black, color:#fff",
    "Industrial(Industrial)": "\n    style Industrial fill:#ffa646, stroke:black",
    "Structure(Structure)": "\n    style Structure fill:#f86041, stroke:black, color:#fff",
    "Facade(Facade)": "\n    style Facade fill:#982062, stroke:black, color:#fff",
    "Service(Service)": "\n    style Service fill:#343779, stroke:black, color:#fff"
}

# Create markdown files for each team
for team in teams:
    team_chart = f"""```mermaid\n    graph LR\n"""
    # print(team)
    for line in full_chart.splitlines():
        if "--" in line:
            if team in line:
                team_chart += line + '\n'
    for team_name, style in styles.items():
        if team_name in team_chart:
            team_chart += style
    team_chart += "\n```"
    file_name = f"{team}.md"
    team_path = os.path.join(path, file_name)
    # print(team_path)

    # Write to markdown file
    write_to_file(team_path, team_chart, file_name, generate_img=True)

# Create markdown file for each pair of teams
for team_0 in teams:
    for team_1 in teams:
        if team_0 != team_1:
            team_chart = f"""```mermaid\n    graph LR\n"""
            # print(team_0, team_1)
            for line in full_chart.splitlines():
                if "--" in line:
                    if team_0 in line and team_1 in line:
                        team_chart += line + '\n'
            for team_name, style in styles.items():
                if team_name in team_chart:
                    team_chart += style
            team_chart += "\n```"

            file_name = f"{team_0}-{team_1}.md"
            team_path = os.path.join(path, file_name)
            # print(f'Team 0: {team_0}, Team 1: {team_1} Path: {team_path}')

            # Write to markdown file
            write_to_file(team_path, team_chart, file_name, generate_img=True)

# Generate the Full_Chart
path = os.getcwd()
path = os.path.join(path, 'Chart_Generator')
path = os.path.join(path, 'Team_Charts')
full_chart_path = os.path.join(path, "Full_Chart.md")

full_chart_str = f"""```mermaid\n    graph LR\n"""
for line in full_chart.splitlines():
    if "--" in line:
        full_chart_str += line + '\n'
for team_name, style in styles.items():
    if team_name in full_chart_str:
        full_chart_str += style
full_chart_str += "\n```"

write_to_file(full_chart_path, full_chart_str, file_name="Full_Chart.md", generate_img=True)
