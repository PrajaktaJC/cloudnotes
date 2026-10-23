CloudNotes is a cloud-native CRUD application built on Microsoft Azure using Python Flask.
The application allows users to create, read, update, and delete notes while leveraging Azure-native services for hosting, database storage, secure secret management, identity, and monitoring.

Features:
Create Notes
Read Notes
Update Notes
Delete Notes
Secure secret management with Azure Key Vault
Passwordless authentication using Managed Identity
Application monitoring using Application Insights
Azure SQL Database integration

Architecture:
                       Users
                         │
                         ▼
                    Azure App Service
                         │
                         ├── Application Insights
                         │
                         ├── Managed Identity
                         │
                         ├── Azure Key Vault
                         │
                         ▼
                    Azure SQL Database

Technology Stack:
                  Python
                  Flask
                  SQLAlchemy
                  Azure SQL Database
                  Azure Key Vault
                  Managed Identity
                  Application Insights
                  Git
                  GitHub

Security Implementation
    The project follows Azure security best practices:
  Implemented
    ✅ Azure Key Vault for secret storage
    ✅ Managed Identity for secure access
    ✅ No passwords stored in source code
    ✅ No passwords stored in GitHub
    ✅ Azure RBAC permissions

Monitoring
    Application telemetry is collected through Application Insights.
    Monitoring includes:
                Request Tracking
                Response Time Monitoring
                Failure Tracking
                Log Analytics Queries
                Application Diagnostics
                
KQL query: 
                requests
              | order by timestamp desc
              | take 10

Challenges and Solutions
    Challenge 1
            GitHub Actions ZIP deployment failed.
    Resolution
            Investigated deployment logs and successfully deployed using App Service Local Git deployment.


   Challenge 2
          Azure SQL authentication failures.
    Resolution
        Verified credentials, firewall configuration, and SQL connectivity using SQLAlchemy and pyodbc.

   
  Challenge 3
        Secure password management.
  Resolution
        Removed hardcoded credentials and implemented Azure Key Vault with Managed Identity access.    


   
