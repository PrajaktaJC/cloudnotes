

resource "azurerm_resource_group" "cloudnotes" {
  name     = var.resource_group_name
  location = var.location
}
resource "azurerm_service_plan" "cloudnotes" {
  name                = "asp-cloudnotes-tf-dev"
  resource_group_name = azurerm_resource_group.cloudnotes.name
  location            = azurerm_resource_group.cloudnotes.location

  os_type  = "Linux"
  sku_name = "B1"
}
resource "azurerm_linux_web_app" "cloudnotes" {
  name                = "cloudnotes-tf-praju"
  location            = azurerm_resource_group.cloudnotes.location
  resource_group_name = azurerm_resource_group.cloudnotes.name
  service_plan_id     = azurerm_service_plan.cloudnotes.id

  site_config {
    application_stack {
      python_version = "3.13"
    }
  }

  https_only = true
}
resource "azurerm_application_insights" "cloudnotes" {
  name                = "appi-cloudnotes-tf-dev"
  location            = azurerm_resource_group.cloudnotes.location
  resource_group_name = azurerm_resource_group.cloudnotes.name
  application_type    = "web"
}
resource "azurerm_key_vault" "cloudnotes" {
  name                = "kv-cloudnotes-tf-praju"
  location            = azurerm_resource_group.cloudnotes.location
  resource_group_name = azurerm_resource_group.cloudnotes.name
  tenant_id           = data.azurerm_client_config.current.tenant_id

  sku_name = "standard"

  purge_protection_enabled   = false
  soft_delete_retention_days = 7
}
resource "azurerm_mssql_server" "cloudnotes" {
  name                = "sql-cloudnotes-tf-praju"
  resource_group_name = azurerm_resource_group.cloudnotes.name
  location            = azurerm_resource_group.cloudnotes.location

  version = "12.0"

  administrator_login          = var.sql_admin_login
  administrator_login_password = var.sql_admin_password
}

resource "azurerm_mssql_database" "cloudnotes" {
  name      = "cloudnotesdb"
  server_id = azurerm_mssql_server.cloudnotes.id

  sku_name = "Basic"
}