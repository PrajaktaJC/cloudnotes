terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tfstate-dev"
    storage_account_name = "tfstatepraju01"
    container_name       = "tfstate"
    key                  = "cloudnotes.tfstate"
  }
}