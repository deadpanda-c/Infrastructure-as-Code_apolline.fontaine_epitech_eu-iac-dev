terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
  required_version = ">= 1.2"

  backend "s3" {
    bucket = "terraform-infraascode-bucket"
    key    = "state/terraform.tfstate"
    region = "eu-west-1"
    # use_lockfile = true
  }
}
