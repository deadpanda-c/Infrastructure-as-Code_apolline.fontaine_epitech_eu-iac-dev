data "github_repository" "permission" {
  name = "Infrastructure-as-Code_apolline.fontaine_epitech_eu-iac-dev"
}

resource "github_team_repository" "permission" {
  for_each = {
    for team in local.repo_teams_files["permission"] :
    team.team_name => {
      team_id    = github_team.all[team.team_name].id
      permission = team.permission
    } if lookup(github_team.all, team.team_name, false) != false
  }

  team_id    = each.value.team_id
  repository = data.github_repository.permission.id
  permission = each.value.permission
}