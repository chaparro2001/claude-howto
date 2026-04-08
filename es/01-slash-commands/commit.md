---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: Create a git commit with context
---

## Contexto

- Estado actual de git: !`git status`
- Diff actual de git: !`git diff HEAD`
- Branch actual: !`git branch --show-current`
- Commits recientes: !`git log --oneline -10`

## Tu tarea

Basandote en los cambios anteriores, crea un unico commit de git.

Si se proporciono un mensaje via argumentos, usalo: $ARGUMENTS

De lo contrario, analiza los cambios y crea un mensaje de commit apropiado siguiendo el formato de conventional commits:

- `feat:` para nuevas funcionalidades
- `fix:` para correcciones de bugs
- `docs:` para cambios en documentacion
- `refactor:` para refactorizacion de codigo
- `test:` para agregar tests
- `chore:` para tareas de mantenimiento

---

**Ultima Actualizacion**: Abril 2026
