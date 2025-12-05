# Infra as code

## Terraform commands

terraform init -backend-config=dev.config
terraform plan -var-file=dev.tfvars
terraform apply -var-file=dev.tfvars -auto-approve
terraform destroy -var-file=dev.tfvars -auto-approve
