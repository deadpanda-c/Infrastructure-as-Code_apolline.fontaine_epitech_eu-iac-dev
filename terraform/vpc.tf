resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  region     = var.region
  tags = merge(var.tags, {
    Name = "${var.vpc_name}-subnet"
  })
}

resource "aws_subnet" "subnet1" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
  tags = merge(var.tags, {
    Name = "${var.vpc_name}"
  })
}
