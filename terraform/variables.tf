variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-1"
}

variable "vpc_name" {
    description = "Name of the VPC"
    type        = string
    default     = "infraascode-vpc"
}
