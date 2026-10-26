output "resource_group_name" {
  value = azurerm_resource_group.cloudnotes.name
}

output "web_app_name" {
  value = azurerm_linux_web_app.cloudnotes.name
}

output "key_vault_name" {
  value = azurerm_key_vault.cloudnotes.name
}

output "sql_server_name" {
  value = azurerm_mssql_server.cloudnotes.name
}

output "sql_database_name" {
  value = azurerm_mssql_database.cloudnotes.name
}