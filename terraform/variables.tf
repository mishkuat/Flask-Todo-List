variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "branch_name" {
  description = "Git branch name used to name the EC2 instance"
  type        = string
  default     = "dev"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "The EC2 key pair name"
  type        = string
  default     = "flask-todo-key"
}

variable "public_key_path" {
  description = "Path to your public SSH key"
  type        = string
  default     = "~/.ssh/flask-todo-key.pub"
}

variable "allowed_ssh_cidr" {
  description = "Your public IP in CIDR format"
  type        = string
  default     = "188.148.231.134/32"
}

