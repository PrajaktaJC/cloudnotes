variable "resource_group_name" {
  default = "rg-cloudnotes-tf-dev"
}

variable "location" {
  default = "Central India"
}
variable "sql_admin_login" {
  default = "sqladmin"
}

variable "sql_admin_password" {
  sensitive = true
}