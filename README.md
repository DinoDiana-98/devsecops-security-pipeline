# 🔒 DevSecOps Security Pipeline

![Security Pipeline](https://img.shields.io/badge/DevSecOps-Automated-8a2be2?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?style=for-the-badge&logo=githubactions)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Security-2496ED?style=for-the-badge&logo=docker)

## 📋 Descripción

Pipeline DevSecOps que implementa **seguridad automatizada** en cada push al repositorio. Este proyecto demuestra la integración de herramientas de seguridad en el ciclo de desarrollo (Shift Left Security), una práctica esencial en entornos empresariales modernos.

## 🛠️ Herramientas de Seguridad Integradas

| Herramienta | Tipo | Función | Estado |
|:---|:---|:---|:---|
| **Gitleaks** | Secrets Detection | Detecta API keys, tokens y contraseñas en el código | ✅ Activo |
| **Bandit** | SAST | Análisis estático de vulnerabilidades en Python | ✅ Activo |
| **Safety** | SCA | Auditoría de dependencias con CVEs conocidos | ✅ Activo |
| **Trivy** | Container Security | Escaneo de vulnerabilidades en imágenes Docker | ✅ Activo |

## 🏗️ Arquitectura del Pipeline

```mermaid
graph TD
    A[Git Push] --> B[GitHub Actions Trigger]
    B --> C[Secrets Scan - Gitleaks]
    B --> D[SAST - Bandit & Safety]
    B --> E[Container Scan - Trivy]
    C --> F{¿Secretos?}
    D --> G{¿Vulnerabilidades?}
    E --> H{¿CVEs en Imagen?}
    F -->|Encontrado| I[❌ Bloquear]
    F -->|Limpio| J[✅ Continuar]
    G --> J
    H --> J
    J --> K[📊 Reporte SARIF]
