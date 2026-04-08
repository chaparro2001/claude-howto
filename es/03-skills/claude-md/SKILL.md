---
name: claude-md
description: Create or update CLAUDE.md files following best practices for optimal AI agent onboarding
---

## Entrada del usuario

```text
$ARGUMENTS
```

**DEBES** considerar la entrada del usuario antes de continuar (si no está vacía). El usuario puede especificar:
- `create` - Crear un nuevo CLAUDE.md desde cero
- `update` - Mejorar un CLAUDE.md existente
- `audit` - Analizar y reportar sobre la calidad del CLAUDE.md actual
- Una ruta específica para crear/actualizar (ej.: `src/api/CLAUDE.md` para instrucciones de un directorio específico)

## Principios fundamentales

**Los LLMs son sin estado**: CLAUDE.md es el único archivo que se incluye automáticamente en cada conversación. Es el documento principal de incorporación para los agentes de IA en tu codebase.

### Las reglas de oro

1. **Menos es más**: Los LLMs de frontera pueden seguir ~150-200 instrucciones. El system prompt de Claude Code ya usa ~50. Mantén tu CLAUDE.md enfocado y conciso.

2. **Aplicabilidad universal**: Solo incluye información relevante para TODAS las sesiones. Las instrucciones específicas de tareas pertenecen a archivos separados.

3. **No uses Claude como linter**: Las guías de estilo saturan el contexto y degradan el seguimiento de instrucciones. Usa herramientas deterministas (prettier, eslint, etc.) en su lugar.

4. **Nunca lo generes automáticamente**: CLAUDE.md es el punto de mayor apalancamiento del harness de IA. Crealo manualmente con cuidado y reflexión.

## Flujo de ejecución

### 1. Análisis del proyecto

Primero, analiza el estado actual del proyecto:

1. Verifica si existen archivos CLAUDE.md:
   - Nivel raíz: `./CLAUDE.md` o `.claude/CLAUDE.md`
   - Específicos de directorio: `**/CLAUDE.md`
   - Configuración global del usuario: `~/.claude/CLAUDE.md`

2. Identificá la estructura del proyecto:
   - Stack tecnológico (lenguajes, frameworks)
   - Tipo de proyecto (monorepo, aplicación única, librería)
   - Herramientas de desarrollo (gestor de paquetes, sistema de build, test runner)

3. Revisá la documentación existente:
   - README.md
   - CONTRIBUTING.md
   - package.json, pyproject.toml, Cargo.toml, etc.

### 2. Estrategia de contenido (QUÉ, POR QUÉ, CÓMO)

Estructurá el CLAUDE.md en torno a tres dimensiones:

#### QUÉ - Tecnología y estructura
- Resumen del stack tecnológico
- Organización del proyecto (especialmente importante para monorepos)
- Directorios clave y sus propósitos

#### POR QUÉ - Propósito y contexto
- Qué hace el proyecto
- Por qué se tomaron ciertas decisiones arquitectónicas
- De qué es responsable cada componente principal

#### CÓMO - Flujo de trabajo y convenciones
- Flujo de desarrollo (bun vs node, pip vs uv, etc.)
- Procedimientos y comandos de testing
- Métodos de verificación y build
- "Gotchas" críticos o requisitos no obvios

### 3. Estrategia de divulgación progresiva

Para proyectos más grandes, recomendá crear una carpeta `agent_docs/`:

```
agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- architecture_decisions.md
```

En CLAUDE.md, haz referencia a estos archivos con instrucciones como:
```markdown
For detailed build instructions, refer to `agent_docs/building_the_project.md`
```

**Importante**: Usa referencias `archivo:línea` en lugar de fragmentos de código para evitar contexto desactualizado.

### 4. Restricciones de calidad

Al crear o actualizar CLAUDE.md:

1. **Extensión objetivo**: Menos de 300 líneas (idealmente menos de 100)
2. **Sin reglas de estilo**: Eliminá cualquier instrucción de linting/formato
3. **Sin instrucciones específicas de tareas**: Movalas a archivos separados
4. **Sin fragmentos de código**: Usa referencias a archivos en su lugar
5. **Sin información redundante**: No repitas lo que ya está en package.json o README

### 5. Secciones esenciales

Un CLAUDE.md bien estructurado debe incluir:

```markdown
# Project Name

Brief one-line description.

## Tech Stack
- Primary language and version
- Key frameworks/libraries
- Database/storage (if any)

## Project Structure
[Only for monorepos or complex structures]
- `apps/` - Application entry points
- `packages/` - Shared libraries

## Development Commands
- Install: `command`
- Test: `command`
- Build: `command`

## Critical Conventions
[Only non-obvious, high-impact conventions]
- Convention 1 with brief explanation
- Convention 2 with brief explanation

## Known Issues / Gotchas
[Things that consistently trip up developers]
- Issue 1
- Issue 2
```

### 6. Anti-patrones a evitar

**NO incluyas:**
- Guías de estilo de código (usa linters)
- Documentación sobre cómo usar Claude
- Explicaciones largas de patrones obvios
- Ejemplos de código copiados y pegados
- Buenas prácticas genéricas ("escribe código limpio")
- Instrucciones para tareas específicas
- Contenido generado automáticamente
- Listas de TODOs extensas

### 7. Lista de verificación de calidad

Antes de finalizar, verifica:

- [ ] Menos de 300 líneas (preferiblemente menos de 100)
- [ ] Cada línea aplica a TODAS las sesiones
- [ ] Sin reglas de estilo/formato
- [ ] Sin fragmentos de código (usa referencias a archivos)
- [ ] Los comandos están verificados y funcionan
- [ ] Se usa divulgación progresiva para proyectos complejos
- [ ] Los gotchas críticos están documentados
- [ ] Sin redundancia con README.md

## Formato de salida

### Para `create` o por defecto:

1. Analizá el proyecto
2. Redactá un CLAUDE.md siguiendo la estructura anterior
3. Presentá el borrador para revisión
4. Escribí en la ubicación apropiada después de la aprobación

### Para `update`:

1. Lee el CLAUDE.md existente
2. Audita contra las mejores prácticas
3. Identificá:
   - Contenido a eliminar (reglas de estilo, fragmentos de código, específico de tareas)
   - Contenido a condensar
   - Información esencial faltante
4. Presenta los cambios para revisión
5. Aplica los cambios después de la aprobación

### Para `audit`:

1. Lee el CLAUDE.md existente
2. Genera un informe con:
   - Recuento de líneas actual vs objetivo
   - Porcentaje de contenido universalmente aplicable
   - Lista de anti-patrones encontrados
   - Recomendaciones de mejora
3. NO modifiques el archivo, solo reporta

## Manejo de AGENTS.md

Si el usuario solicita la creación/actualización de AGENTS.md:

AGENTS.md se usa para definir comportamientos especializados de agentes. A diferencia de CLAUDE.md (que es para contexto del proyecto), AGENTS.md define:
- Roles y capacidades de agentes personalizados
- Instrucciones y restricciones específicas del agente
- Definiciones de workflow para escenarios multi-agente

Aplica principios similares:
- Mantenerlo enfocado y conciso
- Usa divulgación progresiva
- Referencia documentos externos en lugar de incrustar contenido

## Notas

- Siempre verifica que los comandos funcionen antes de incluirlos
- Ante la duda, dejalo afuera: menos es más
- El system reminder le dice a Claude que CLAUDE.md "puede o no ser relevante" — cuanto más ruido, más se ignora
- Los monorepos se benefician más de una estructura clara de QUÉ/POR QUÉ/CÓMO
- Los archivos CLAUDE.md específicos de directorio deben ser aún más enfocados
