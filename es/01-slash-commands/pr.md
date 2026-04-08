---
description: Clean up code, stage changes, and prepare a pull request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# Checklist de Preparacion de Pull Request

Antes de crear un PR, ejecutar estos pasos:

1. Ejecutar linting: `prettier --write .`
2. Ejecutar tests: `npm test`
3. Revisar git diff: `git diff HEAD`
4. Agregar cambios al stage: `git add .`
5. Crear mensaje de commit siguiendo conventional commits:
   - `fix:` para correcciones de bugs
   - `feat:` para nuevas funcionalidades
   - `docs:` para documentacion
   - `refactor:` para reestructuracion de codigo
   - `test:` para agregar tests
   - `chore:` para mantenimiento

6. Generar resumen del PR incluyendo:
   - Que cambio
   - Por que cambio
   - Testing realizado
   - Impactos potenciales

---

**Ultima Actualizacion**: Abril 2026
