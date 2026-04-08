---
name: Setup CI/CD Pipeline
description: Implement pre-commit hooks and GitHub Actions for quality assurance
tags: ci-cd, devops, automation
---

# Configuracion de Pipeline CI/CD

Implementar gates de calidad DevOps completos adaptados al tipo de proyecto:

1. **Analizar proyecto**: Detectar lenguaje(s), framework, sistema de build y herramientas existentes
2. **Configurar pre-commit hooks** con herramientas especificas del lenguaje:
   - Formateo: Prettier/Black/gofmt/rustfmt/etc.
   - Linting: ESLint/Ruff/golangci-lint/Clippy/etc.
   - Seguridad: Bandit/gosec/cargo-audit/npm audit/etc.
   - Verificacion de tipos: TypeScript/mypy/flow (si aplica)
   - Tests: Ejecutar suites de tests relevantes
3. **Crear workflows de GitHub Actions** (.github/workflows/):
   - Replicar checks de pre-commit en push/PR
   - Matrix multi-version/plataforma (si aplica)
   - Verificacion de build y tests
   - Pasos de deployment (si se necesita)
4. **Verificar pipeline**: Testear localmente, crear PR de prueba, confirmar que todos los checks pasen

Usar herramientas gratuitas/open-source. Respetar configs existentes. Mantener ejecucion rapida.

---

**Ultima Actualizacion**: Abril 2026
