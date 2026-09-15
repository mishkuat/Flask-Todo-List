variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
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
  default     = "203.0.113.10/32"
}