terraform {
  required_version = ">= 1.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "689ddfb9-90af-4e7d-ae81-aeac6f5d415c"
}
data "azurerm_client_config" "current" {}