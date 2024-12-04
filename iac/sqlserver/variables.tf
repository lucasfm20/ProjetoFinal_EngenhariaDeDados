variable "resource_group_name" {
  description = "Nome do Resource Group do Databricks"
  type        = string
}

variable "location" {
  description = "Localização do Databricks"
  type        = string
  default     = "East US"
}

variable "subscription_id" {
  description = "ID da Subscription na Azure"
  type        = string
}

variable "usuario_admin" {
  description = "Usuário Admin do SQL Server"
  type        = string
}

variable "password" {
  description = "Senha do SQL Server"
  type        = string
}