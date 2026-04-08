<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Funcionalidades Avanzadas

Guía completa de las capacidades avanzadas de Claude Code, incluyendo planning mode, extended thinking, auto mode, background tasks, permission modes, print mode (no interactivo), gestión de sesiones, funcionalidades interactivas, channels, dictado por voz, remote control, web sessions, desktop app, lista de tareas, sugerencias de prompt, git worktrees, sandboxing, managed settings y configuración.

## Tabla de Contenidos

1. [Descripción General](#descripción-general)
2. [Planning Mode](#planning-mode)
3. [Extended Thinking](#extended-thinking)
4. [Auto Mode](#auto-mode)
5. [Background Tasks](#background-tasks)
6. [Tareas Programadas](#tareas-programadas)
7. [Permission Modes](#permission-modes)
8. [Headless Mode](#headless-mode)
9. [Gestión de Sesiones](#gestión-de-sesiones)
10. [Funcionalidades Interactivas](#funcionalidades-interactivas)
11. [Dictado por Voz](#dictado-por-voz)
12. [Channels](#channels)
13. [Integración con Chrome](#integración-con-chrome)
14. [Remote Control](#remote-control)
15. [Web Sessions](#web-sessions)
16. [Desktop App](#desktop-app)
17. [Lista de Tareas](#lista-de-tareas)
18. [Sugerencias de Prompt](#sugerencias-de-prompt)
19. [Git Worktrees](#git-worktrees)
20. [Sandboxing](#sandboxing)
21. [Managed Settings (Enterprise)](#managed-settings-enterprise)
22. [Configuración y Ajustes](#configuración-y-ajustes)
23. [Agent Teams](#agent-teams)
24. [Buenas Prácticas](#buenas-prácticas)
25. [Recursos Adicionales](#recursos-adicionales)

---

## Descripción General

Las funcionalidades avanzadas de Claude Code extienden las capacidades base con planificación, razonamiento, automatización y mecanismos de control. Estas características habilitan flujos de trabajo sofisticados para tareas de desarrollo complejas, revisión de código, automatización y gestión de múltiples sesiones.

**Las principales funcionalidades avanzadas incluyen:**
- **Planning Mode**: Crear planes de implementación detallados antes de codificar
- **Extended Thinking**: Razonamiento profundo para problemas complejos
- **Auto Mode**: Un clasificador de seguridad en segundo plano revisa cada acción antes de ejecutarla (Research Preview)
- **Background Tasks**: Ejecutar operaciones largas sin bloquear la conversación
- **Permission Modes**: Controlar lo que Claude puede hacer (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`)
- **Print Mode**: Ejecutar Claude Code de forma no interactiva para automatización y CI/CD (`claude -p`)
- **Gestión de Sesiones**: Administrar múltiples sesiones de trabajo
- **Funcionalidades Interactivas**: Atajos de teclado, entrada multilínea e historial de comandos
- **Dictado por Voz**: Entrada de voz push-to-talk con soporte STT para 20 idiomas
- **Channels**: Los servidores MCP envían mensajes a sesiones activas (Research Preview)
- **Remote Control**: Controlar Claude Code desde Claude.ai o la app de Claude
- **Web Sessions**: Ejecutar Claude Code en el navegador en claude.ai/code
- **Desktop App**: Aplicación independiente para revisión visual de diffs y múltiples sesiones
- **Lista de Tareas**: Seguimiento persistente de tareas a través de compactaciones de contexto
- **Sugerencias de Prompt**: Sugerencias de comandos inteligentes basadas en el contexto
- **Git Worktrees**: Ramas de worktree aisladas para trabajo en paralelo
- **Sandboxing**: Aislamiento de sistema de archivos y red a nivel de OS
- **Managed Settings**: Despliegue empresarial mediante plist, Registry o archivos administrados
- **Configuración**: Personalizar el comportamiento con archivos de configuración JSON

---

## Planning Mode

El planning mode permite que Claude analice tareas complejas antes de implementarlas, creando un plan detallado que puedes revisar y aprobar.

### ¿Qué es el Planning Mode?

El planning mode es un enfoque en dos fases:
1. **Fase de planificación**: Claude analiza la tarea y crea un plan de implementación detallado
2. **Fase de implementación**: Una vez aprobado, Claude ejecuta el plan

### Cuándo Usar Planning Mode

✅ Usa planning mode para:
- Refactorización compleja de múltiples archivos
- Implementaciones de nuevas funcionalidades
- Cambios de arquitectura
- Migraciones de bases de datos
- Rediseños importantes de API

❌ No lo uses para:
- Correcciones de bugs simples
- Cambios de formato
- Ediciones de un solo archivo
- Consultas rápidas

### Activar Planning Mode

**Slash command**:
```bash
/plan Implement user authentication system
```

**Flag de CLI**:
```bash
claude --permission-mode plan
```

**Establecer como predeterminado**:
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**Atajo de teclado**:
- `Shift + Tab` - Alternar entre permission modes (incluye plan)
- `Alt + M` - Alternar permission modes (Windows/Linux)

### Beneficios del Planning Mode

- **Enfoque de implementación estructurado**: Desglose detallado de los pasos de implementación
- **Revisión y aprobación**: Aprueba o ajusta el plan antes de la ejecución
- **Identificación de riesgos**: Detectá posibles problemas antes de implementar
- **Fases claras**: Fases e hitos de implementación organizados

### Ejemplo: Implementación de Funcionalidad

```
User: /plan Add a real-time notification system

Claude: I'll create a plan for implementing real-time notifications.

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Install WebSocket libraries (socket.io)
2. Set up WebSocket server
3. Configure connection management

### Phase 2: Backend Implementation
4. Create notification service
5. Implement notification queue
6. Add database schema for notifications
7. Create API endpoints

### Phase 3: Frontend Integration
8. Set up WebSocket client
9. Create notification UI components
10. Implement notification state management
11. Add notification permissions

### Phase 4: Testing & Deployment
12. Write unit tests
13. Write integration tests
14. Update documentation
15. Deploy to staging

Estimated time: 3-4 hours
Files to modify: 12
New files to create: 8

Ready to proceed? (yes/no/modify plan)

User: yes

Claude: [Begins implementation following the plan]
```

### Modificaciones del Plan

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: Updated plan:
[Shows modified plan with queue removed]

User: Looks good, proceed

Claude: [Implements modified plan]
```

### Configuración del Planning Mode

El planning mode se activa mediante el flag de CLI o el slash command:

```bash
# Activate plan mode via CLI
claude --permission-mode plan

# Or use the /plan slash command inside the REPL
/plan Implement user authentication system
```

**Alias de modelo para planificación**: Usa `opusplan` como alias de modelo para usar Opus en la planificación y Sonnet en la ejecución:

```bash
claude --model opusplan "design and implement the new API"
```

**Editar el plan externamente**: Presioná `Ctrl+G` para abrir el plan actual en tu editor externo y hacer modificaciones detalladas.

### Ultraplan

Usa `/ultraplan <prompt>` para un flujo de trabajo de planificación de extremo a extremo: Claude elabora un plan detallado, lo abre en el navegador para revisión y luego lo ejecuta de forma remota o lo envía de vuelta a tu terminal para ejecución local.

---

## Extended Thinking

El extended thinking permite que Claude dedique más tiempo a razonar sobre problemas complejos antes de proporcionar una solución.

### ¿Qué es el Extended Thinking?

El extended thinking es un proceso de razonamiento deliberado, paso a paso, donde Claude:
- Descompone problemas complejos
- Considera múltiples enfoques
- Evalúa los trade-offs
- Razona a través de casos extremos

### Activar Extended Thinking

**Atajo de teclado**:
- `Option + T` (macOS) / `Alt + T` (Windows/Linux) - Activar/desactivar extended thinking

**Activación automática**:
- Habilitado por defecto para todos los modelos (Opus 4.6, Sonnet 4.6, Haiku 4.5)
- Opus 4.6: Razonamiento adaptativo con niveles de esfuerzo: `low` (○), `medium` (◐), `high` (●), `max` (solo Opus 4.6)
- Otros modelos: Presupuesto fijo de hasta 31.999 tokens

**Métodos de configuración**:
- Alternar: `Alt+T` / `Option+T`, o mediante `/config`
- Ver razonamiento: `Ctrl+O` (modo verbose)
- Establecer esfuerzo: comando `/effort` o flag `--effort`

**Presupuesto personalizado**:
```bash
export MAX_THINKING_TOKENS=1024
```

**Nivel de esfuerzo** (solo Opus 4.6):
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○), medium (◐), high (●), or max (Opus 4.6 only)
```

**Flag de CLI**:
```bash
claude --effort high "complex architectural review"
```

**Slash command**:
```
/effort high
```

> **Nota:** La palabra clave "ultrathink" en los prompts activa el modo de razonamiento profundo. Los niveles de esfuerzo `low`, `medium`, `high` y `max` (solo Opus 4.6) controlan cuánto razonamiento realiza Claude.

### Beneficios del Extended Thinking

- **Razonamiento profundo**: Dedicar más tiempo a pensar en problemas complejos
- **Mejores decisiones arquitectónicas**: Tomar decisiones informadas con evaluación exhaustiva
- **Consideración de casos extremos**: Analizar posibles problemas y escenarios
- **Análisis exhaustivo**: Enfoque estructurado para resolver problemas complejos

### Ejemplo: Decisión Arquitectónica

```
User: /think Should we use microservices or a monolith for our e-commerce platform?

Claude: Let me think through this architectural decision carefully...

<extended_thinking>
## Context Analysis
- Team size: 5 developers
- Expected traffic: 10k daily users initially
- Need to scale to 100k+ users
- Limited DevOps resources
- 6-month timeline to MVP

## Approach 1: Microservices
Pros:
+ Independent scaling
+ Technology flexibility
+ Team independence
+ Fault isolation

Cons:
- Operational complexity
- Network overhead
- Distributed tracing needed
- Requires DevOps expertise
- Slower initial development

## Approach 2: Monolith
Pros:
+ Simpler deployment
+ Faster initial development
+ Easier debugging
+ Lower operational overhead
+ Single codebase

Cons:
- Scaling challenges later
- All-or-nothing deployments
- Technology lock-in
- Potential for tight coupling

## Decision Factors
1. Team size (5 devs) → Favors monolith
2. DevOps resources (limited) → Favors monolith
3. Timeline (6 months) → Favors monolith
4. Future scale (100k users) → Achievable with monolith + caching
5. Complexity budget → Limited

## Recommendation
Start with a **modular monolith**:
- Single deployment unit
- Clear module boundaries
- Clean interfaces between modules
- Prepare for future extraction to microservices if needed

This gives you:
✓ Fast initial development
✓ Low operational complexity
✓ Option to extract services later
✓ Clear architecture

Migration path: When you reach 50k+ users or specific modules need independent scaling, extract those modules into microservices.
</extended_thinking>

**Recommendation**: Implement a modular monolith with clean module boundaries.

This approach balances your current constraints (team size, timeline, DevOps resources) with future scalability needs. You can migrate specific modules to microservices later when there's a clear business need.
```

### Configuración del Extended Thinking

El extended thinking se controla mediante variables de entorno, atajos de teclado y flags de CLI:

```bash
# Set thinking token budget
export MAX_THINKING_TOKENS=16000

# Set effort level (Opus 4.6 only): low (○), medium (◐), high (●), or max (Opus 4.6 only)
export CLAUDE_CODE_EFFORT_LEVEL=high
```

Altérnalo durante una sesión con `Alt+T` / `Option+T`, establece el esfuerzo con `/effort` o configúralo mediante `/config`.

---

## Auto Mode

El Auto Mode es un permission mode en Research Preview (marzo 2026) que usa un clasificador de seguridad en segundo plano para revisar cada acción antes de ejecutarla. Permite que Claude trabaje de forma autónoma mientras bloquea operaciones peligrosas.

### Requisitos

- **Plan**: Team, Enterprise o API (no disponible en planes Pro o Max)
- **Modelo**: Claude Sonnet 4.6 u Opus 4.6
- **Proveedor**: Solo Anthropic API (no compatible con Bedrock, Vertex ni Foundry)
- **Clasificador**: Se ejecuta en Claude Sonnet 4.6 (agrega costo adicional de tokens)

### Habilitar Auto Mode

```bash
# Unlock auto mode with CLI flag
claude --enable-auto-mode

# Then cycle to it with Shift+Tab in the REPL
```

O establecerlo como el permission mode predeterminado:

```bash
claude --permission-mode auto
```

Configuración mediante archivo de ajustes:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Cómo Funciona el Clasificador

El clasificador en segundo plano evalúa cada acción siguiendo este orden de decisión:

1. **Reglas de allow/deny** -- Primero se verifican las reglas de permisos explícitas
2. **Solo lectura/ediciones aprobadas automáticamente** -- Las lecturas y ediciones de archivos pasan automáticamente
3. **Clasificador** -- El clasificador en segundo plano revisa la acción
4. **Fallback** -- Vuelve a preguntar al usuario después de 3 bloqueos consecutivos o 20 bloqueos totales

### Acciones Bloqueadas por Defecto

El auto mode bloquea las siguientes acciones por defecto:

| Acción Bloqueada | Ejemplo |
|----------------|---------|
| Instalaciones pipe-to-shell | `curl \| bash` |
| Envío de datos sensibles externamente | API keys, credenciales por la red |
| Despliegues a producción | Comandos de deploy apuntando a producción |
| Eliminación masiva | `rm -rf` en directorios grandes |
| Cambios de IAM | Modificaciones de permisos y roles |
| Force push a main | `git push --force origin main` |

### Acciones Permitidas por Defecto

| Acción Permitida | Ejemplo |
|----------------|---------|
| Operaciones de archivos locales | Leer, escribir, editar archivos del proyecto |
| Instalación de dependencias declaradas | `npm install`, `pip install` desde el manifiesto |
| HTTP de solo lectura | `curl` para obtener documentación |
| Push a la rama actual | `git push origin feature-branch` |

### Configurar Auto Mode

**Imprimir reglas por defecto como JSON**:
```bash
claude auto-mode defaults
```

**Configurar infraestructura de confianza** mediante la configuración administrada `autoMode.environment` para despliegues empresariales. Esto permite a los administradores definir entornos CI/CD de confianza, targets de despliegue y patrones de infraestructura.

### Comportamiento de Fallback

Cuando el clasificador no está seguro, el auto mode vuelve a preguntar al usuario:
- Después de **3 bloqueos consecutivos** del clasificador
- Después de **20 bloqueos totales** en una sesión

Esto garantiza que el usuario siempre mantenga el control cuando el clasificador no puede aprobar una acción con confianza.

### Establecer Permisos Equivalentes a Auto Mode Sin Plan Team

Si no tienes un plan Team o prefieres un enfoque más simple sin el clasificador en segundo plano, puedes configurar tu `~/.claude/settings.json` con una línea base conservadora de reglas de permisos seguras. El script comienza con reglas de solo lectura e inspección local, y luego te permite activar ediciones, pruebas, escrituras git locales, instalaciones de paquetes y acciones de escritura de GitHub CLI solo cuando las necesitas.

**Archivo:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Preview what would be added (no changes written)
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Apply the conservative baseline
python3 09-advanced-features/setup-auto-mode-permissions.py

# Add more capability only when you need it
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

El script agrega reglas en estas categorías:

| Categoría | Ejemplos |
|----------|---------|
| Herramientas de solo lectura principales | `Read(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)`, `WebFetch(*)` |
| Inspección local | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)`, `Bash(cat:*)` |
| Ediciones opcionales | `Edit(*)`, `Write(*)`, `NotebookEdit(*)` |
| Test/build opcional | `Bash(pytest:*)`, `Bash(python3 -m pytest:*)`, `Bash(cargo test:*)` |
| Escrituras git opcionales | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git stash:*)` |
| Git (escritura local) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Gestores de paquetes | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| Build y test | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Shell común | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

Las operaciones peligrosas (`rm -rf`, `sudo`, force push, `DROP TABLE`, `terraform destroy`, etc.) están excluidas intencionalmente. El script es idempotente: ejecutarlo dos veces no duplica las reglas.

---

## Background Tasks

Las background tasks permiten que operaciones de larga duración se ejecuten sin bloquear tu conversación.

### ¿Qué Son las Background Tasks?

Las background tasks se ejecutan de forma asíncrona mientras sigues trabajando:
- Suites de pruebas largas
- Procesos de build
- Migraciones de bases de datos
- Scripts de despliegue
- Herramientas de análisis

**Uso básico:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Show all tasks
/task status bg-1234 # Check progress
/task show bg-1234   # View output
/task cancel bg-1234 # Cancel task
```

### Iniciar Background Tasks

```
User: Run the full test suite in the background

Claude: Starting tests in background (task-id: bg-1234)
You can continue working while tests run.

[You can continue the conversation]

User: Meanwhile, let's refactor the auth module

Claude: [Works on auth module while tests run in background]

[Later, when tests complete]

Claude: 📢 Background task bg-1234 completed:
✅ 245 tests passed
❌ 3 tests failed
View results: /task show bg-1234
```

### Gestionar Background Tasks

**Listar tareas activas**:
```
User: /task list

Active background tasks:
1. [bg-1234] Running tests (50% complete, 2min remaining)
2. [bg-1235] Building Docker image (25% complete, 8min remaining)
3. [bg-1236] Deploying to staging (90% complete, 30sec remaining)
```

**Verificar el estado de una tarea**:
```
User: /task status bg-1234

Task bg-1234: Running tests
Status: In progress
Progress: 120/245 tests (49%)
Started: 2025-11-08 10:30:15
Estimated completion: 2025-11-08 10:34:22
```

**Ver el output de una tarea**:
```
User: /task show bg-1234

[Shows live output from the test run]
```

**Cancelar una tarea**:
```
User: /task cancel bg-1234

Cancelled background task bg-1234
```

### Ejemplo: Desarrollo en Paralelo

```
User: Run the build in the background

Claude: Starting build... (task-id: bg-5001)

User: Also run the linter in background

Claude: Starting linter... (task-id: bg-5002)

User: While those run, let's implement the new API endpoint

Claude: [Implements API endpoint while build and linter run]

[10 minutes later]

Claude: 📢 Build completed successfully (bg-5001)
📢 Linter found 12 issues (bg-5002)

User: Show me the linter issues

Claude: [Shows linter output from bg-5002]
```

### Configuración

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

## Tareas Programadas

Las tareas programadas te permiten ejecutar prompts automáticamente en un horario recurrente o como recordatorios de una sola vez. Las tareas tienen alcance de sesión — se ejecutan mientras Claude Code está activo y se borran cuando la sesión termina. Disponible desde v2.1.72+.

### El comando `/loop`

```bash
# Explicit interval
/loop 5m check if the deployment finished

# Natural language
/loop check build status every 30 minutes
```

También se admiten expresiones cron estándar de 5 campos para programación precisa.

### Recordatorios de Una Sola Vez

Establece recordatorios que se disparan una sola vez a una hora específica:

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### Gestionar Tareas Programadas

| Herramienta | Descripción |
|------|-------------|
| `CronCreate` | Crear una nueva tarea programada |
| `CronList` | Listar todas las tareas programadas activas |
| `CronDelete` | Eliminar una tarea programada |

**Límites y comportamiento**:
- Hasta **50 tareas programadas** por sesión
- Alcance de sesión — se borran cuando la sesión termina
- Las tareas recurrentes expiran automáticamente después de **3 días**
- Las tareas solo se disparan mientras Claude Code está en ejecución — no hay recuperación de disparos perdidos

### Detalles de Comportamiento

| Aspecto | Detalle |
|--------|--------|
| **Jitter recurrente** | Hasta el 10% del intervalo (máximo 15 minutos) |
| **Jitter de una sola vez** | Hasta 90 segundos en los límites :00/:30 |
| **Disparos perdidos** | Sin recuperación — se omiten si Claude Code no estaba en ejecución |
| **Persistencia** | No persisten entre reinicios |

### Tareas Programadas en la Nube

Usa `/schedule` para crear tareas programadas en la nube que se ejecutan en la infraestructura de Anthropic:

```
/schedule daily at 9am run the test suite and report failures
```

Las tareas programadas en la nube persisten entre reinicios y no requieren que Claude Code esté ejecutándose localmente.

### Deshabilitar Tareas Programadas

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

### Ejemplo: Monitoreo de un Despliegue

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **Consejo**: Las tareas programadas tienen alcance de sesión. Para automatización persistente que sobreviva reinicios, usa pipelines de CI/CD, GitHub Actions o tareas programadas de la Desktop App.

---

## Permission Modes

Los permission modes controlan qué acciones puede tomar Claude sin aprobación explícita.

### Permission Modes Disponibles

| Modo | Comportamiento |
|---|---|
| `default` | Solo lectura de archivos; solicita confirmación para todas las demás acciones |
| `acceptEdits` | Lee y edita archivos; solicita confirmación para comandos |
| `plan` | Solo lectura de archivos (modo de investigación, sin ediciones) |
| `auto` | Todas las acciones con verificaciones del clasificador de seguridad en segundo plano (Research Preview) |
| `bypassPermissions` | Todas las acciones, sin verificaciones de permisos (peligroso) |
| `dontAsk` | Solo se ejecutan las herramientas preaprobadas; todas las demás se deniegan |

Alterna entre modos con `Shift+Tab` en el CLI. Establece un valor predeterminado con el flag `--permission-mode` o el ajuste `permissions.defaultMode`.

### Métodos de Activación

**Atajo de teclado**:
```bash
Shift + Tab  # Cycle through all 6 modes
```

**Slash command**:
```bash
/plan                  # Enter plan mode
```

**Flag de CLI**:
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**Configuración**:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Ejemplos de Permission Modes

#### Modo Default
Claude solicita confirmación para acciones significativas:

```
User: Fix the bug in auth.ts

Claude: I need to modify src/auth.ts to fix the bug.
The change will update the password validation logic.

Approve this change? (yes/no/show)
```

#### Plan Mode
Revisa el plan de implementación antes de la ejecución:

```
User: /plan Implement user authentication system

Claude: I'll create a plan for implementing authentication.

## Implementation Plan
[Detailed plan with phases and steps]

Ready to proceed? (yes/no/modify)
```

#### Accept Edits Mode
Aceptar automáticamente las modificaciones de archivos:

```
User: acceptEdits
User: Fix the bug in auth.ts

Claude: [Makes changes without asking]
```

### Casos de Uso

**Revisión de Código**:
```
User: claude --permission-mode plan
User: Review this PR and suggest improvements

Claude: [Reads code, provides feedback, but cannot modify]
```

**Programación en Pareja**:
```
User: claude --permission-mode default
User: Let's implement the feature together

Claude: [Asks for approval before each change]
```

**Tareas Automatizadas**:
```
User: claude --permission-mode acceptEdits
User: Fix all linting issues in the codebase

Claude: [Auto-accepts file edits without asking]
```

---

## Headless Mode

El print mode (`claude -p`) permite que Claude Code se ejecute sin entrada interactiva, ideal para automatización y CI/CD. Este es el modo no interactivo, que reemplaza el flag `--headless` anterior.

### ¿Qué es el Print Mode?

El print mode habilita:
- Ejecución automatizada de scripts
- Integración con CI/CD
- Procesamiento por lotes
- Tareas programadas

### Ejecutar en Print Mode (No Interactivo)

```bash
# Run specific task
claude -p "Run all tests"

# Process piped content
cat error.log | claude -p "Analyze these errors"

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### Ejemplos Adicionales de Uso de Print Mode

```bash
# Run a specific task with output capture
claude -p "Run all tests and generate coverage report"

# With structured output
claude -p --output-format json "Analyze code quality"

# With input from stdin
echo "Analyze code quality" | claude -p "explain this"
```

### Ejemplo: Integración con CI/CD

**GitHub Actions**:
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for:
            - Code quality issues
            - Security vulnerabilities
            - Performance concerns
            - Test coverage
            Output results as JSON" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: JSON.stringify(review, null, 2)
            });
```

### Configuración del Print Mode

El print mode (`claude -p`) admite varios flags para automatización:

```bash
# Limit autonomous turns
claude -p --max-turns 5 "refactor this module"

# Structured JSON output
claude -p --output-format json "analyze this codebase"

# With schema validation
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# Disable session persistence
claude -p --no-session-persistence "one-off analysis"
```

---

## Gestión de Sesiones

Administrá múltiples sesiones de Claude Code de forma efectiva.

### Comandos de Gestión de Sesiones

| Comando | Descripción |
|---------|-------------|
| `/resume` | Reanudar una conversación por ID o nombre |
| `/rename` | Nombrar la sesión actual |
| `/fork` | Hacer fork de la sesión actual en una nueva rama |
| `claude -c` | Continuar la conversación más reciente |
| `claude -r "session"` | Reanudar una sesión por nombre o ID |

### Reanudar Sesiones

**Continuar la última conversación**:
```bash
claude -c
```

**Reanudar una sesión con nombre**:
```bash
claude -r "auth-refactor" "finish this PR"
```

**Renombrar la sesión actual** (dentro del REPL):
```
/rename auth-refactor
```

### Hacer Fork de Sesiones

Haz fork de una sesión para probar un enfoque alternativo sin perder el original:

```
/fork
```

O desde el CLI:
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### Persistencia de Sesiones

Las sesiones se guardan automáticamente y se pueden reanudar:

```bash
# Continue last conversation
claude -c

# Resume specific session by name or ID
claude -r "auth-refactor"

# Resume and fork for experimentation
claude --resume auth-refactor --fork-session "alternative approach"
```

---

## Funcionalidades Interactivas

### Atajos de Teclado

Claude Code admite atajos de teclado para mayor eficiencia. Aquí está la referencia completa de la documentación oficial:

| Atajo | Descripción |
|----------|-------------|
| `Ctrl+C` | Cancelar la entrada/generación actual |
| `Ctrl+D` | Salir de Claude Code |
| `Ctrl+G` | Editar el plan en un editor externo |
| `Ctrl+L` | Limpiar la pantalla del terminal |
| `Ctrl+O` | Alternar salida verbose (ver razonamiento) |
| `Ctrl+R` | Búsqueda inversa en el historial |
| `Ctrl+T` | Alternar vista de lista de tareas |
| `Ctrl+B` | Tareas ejecutándose en segundo plano |
| `Esc+Esc` | Revertir código/conversación |
| `Shift+Tab` / `Alt+M` | Alternar permission modes |
| `Option+P` / `Alt+P` | Cambiar modelo |
| `Option+T` / `Alt+T` | Alternar extended thinking |

**Edición de Línea (atajos readline estándar):**

| Atajo | Acción |
|----------|--------|
| `Ctrl + A` | Ir al inicio de la línea |
| `Ctrl + E` | Ir al final de la línea |
| `Ctrl + K` | Cortar hasta el final de la línea |
| `Ctrl + U` | Cortar hasta el inicio de la línea |
| `Ctrl + W` | Eliminar palabra hacia atrás |
| `Ctrl + Y` | Pegar (yank) |
| `Tab` | Autocompletar |
| `↑ / ↓` | Historial de comandos |

### Personalizar los Keybindings

Creá atajos de teclado personalizados ejecutando `/keybindings`, que abre `~/.claude/keybindings.json` para edición (v2.1.18+).

**Formato de configuración**:

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    },
    {
      "context": "Confirmation",
      "bindings": {
        "ctrl+a": "confirmation:yes"
      }
    }
  ]
}
```

Establece un binding en `null` para desvincularlo de su atajo predeterminado.

### Contextos Disponibles

Los keybindings tienen alcance a contextos específicos de la UI:

| Contexto | Acciones de Teclas |
|---------|-------------|
| **Chat** | `submit`, `cancel`, `cycleMode`, `modelPicker`, `thinkingToggle`, `undo`, `externalEditor`, `stash`, `imagePaste` |
| **Confirmation** | `yes`, `no`, `previous`, `next`, `nextField`, `cycleMode`, `toggleExplanation` |
| **Global** | `interrupt`, `exit`, `toggleTodos`, `toggleTranscript` |
| **Autocomplete** | `accept`, `dismiss`, `next`, `previous` |
| **HistorySearch** | `search`, `previous`, `next` |
| **Settings** | Navegación de ajustes específica al contexto |
| **Tabs** | Gestión y cambio de pestañas |
| **Help** | Navegación del panel de ayuda |

En total hay 18 contextos, incluyendo `Transcript`, `Task`, `ThemePicker`, `Attachments`, `Footer`, `MessageSelector`, `DiffDialog`, `ModelPicker` y `Select`.

### Soporte para Chords

Los keybindings admiten secuencias chord (combinaciones de múltiples teclas):

```
"ctrl+k ctrl+s"   → Two-key sequence: press ctrl+k, then ctrl+s
"ctrl+shift+p"    → Simultaneous modifier keys
```

**Sintaxis de teclas**:
- **Modificadores**: `ctrl`, `alt` (o `opt`), `shift`, `meta` (o `cmd`)
- **Mayúscula implica Shift**: `K` es equivalente a `shift+k`
- **Teclas especiales**: `escape`, `enter`, `return`, `tab`, `space`, `backspace`, `delete`, teclas de flecha

### Teclas Reservadas y en Conflicto

| Tecla | Estado | Notas |
|-----|--------|-------|
| `Ctrl+C` | Reservada | No se puede reasignar (interrupción) |
| `Ctrl+D` | Reservada | No se puede reasignar (salir) |
| `Ctrl+B` | Conflicto de terminal | Tecla prefijo de tmux |
| `Ctrl+A` | Conflicto de terminal | Tecla prefijo de GNU Screen |
| `Ctrl+Z` | Conflicto de terminal | Suspender proceso |

> **Consejo**: Si un atajo no funciona, verifica conflictos con tu emulador de terminal o multiplexor.

### Completado por Tab

Claude Code proporciona completado por Tab inteligente:

```
User: /rew<TAB>
→ /rewind

User: /plu<TAB>
→ /plugin

User: /plugin <TAB>
→ /plugin install
→ /plugin enable
→ /plugin disable
```

### Historial de Comandos

Accedé a comandos anteriores:

```
User: <↑>  # Previous command
User: <↓>  # Next command
User: Ctrl+R  # Search history

(reverse-i-search)`test': run all tests
```

### Entrada Multilínea

Para consultas complejas, usa el modo multilínea:

```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

**Ejemplo:**

```
User: \
> Implement a user authentication system
> with the following requirements:
> - JWT tokens
> - Email verification
> - Password reset
> - 2FA support
> \end

Claude: [Processes the multi-line request]
```

### Edición en Línea

Editá comandos antes de enviarlos:

```
User: Deploy to prodcution<Backspace><Backspace>uction

[Edit in-place before sending]
```

### Modo Vim

Habilitá los keybindings de Vi/Vim para edición de texto:

**Activación**:
- Usa el comando `/vim` o `/config` para habilitar
- Cambio de modo con `Esc` para NORMAL, `i/a/o` para INSERT

**Teclas de navegación**:
- `h` / `l` - Mover izquierda/derecha
- `j` / `k` - Mover abajo/arriba
- `w` / `b` / `e` - Mover por palabra
- `0` / `$` - Ir al inicio/final de la línea
- `gg` / `G` - Saltar al inicio/final del texto

**Objetos de texto**:
- `iw` / `aw` - Dentro de/alrededor de la palabra
- `i"` / `a"` - Dentro de/alrededor de cadena entre comillas
- `i(` / `a(` - Dentro de/alrededor de paréntesis

### Modo Bash

Ejecutá comandos de shell directamente con el prefijo `!`:

```bash
! npm test
! git status
! cat src/index.js
```

Úsalo para ejecutar comandos rápidamente sin cambiar de contexto.

---

## Dictado por Voz

El Dictado por Voz proporciona entrada de voz push-to-talk para Claude Code, permitiéndote hablar tus prompts en lugar de escribirlos.

### Activar el Dictado por Voz

```
/voice
```

### Características

| Característica | Descripción |
|---------|-------------|
| **Push-to-talk** | Mantén presionada una tecla para grabar, suelta para enviar |
| **20 idiomas** | Speech-to-text admite 20 idiomas |
| **Keybinding personalizado** | Configura la tecla push-to-talk mediante `/keybindings` |
| **Requisito de cuenta** | Requiere una cuenta Claude.ai para el procesamiento STT |

### Configuración

Personalizá el keybinding push-to-talk en tu archivo de keybindings (`/keybindings`). El dictado por voz usa tu cuenta Claude.ai para el procesamiento speech-to-text.

---

## Channels

Channels es una funcionalidad en Research Preview que envía eventos de servicios externos a una sesión activa de Claude Code mediante servidores MCP. Las fuentes incluyen Telegram, Discord, iMessage y webhooks arbitrarios, lo que permite que Claude reaccione a notificaciones en tiempo real sin necesidad de polling.

### Suscribirse a Channels

```bash
# Subscribe to channel plugins at startup
claude --channels discord,telegram

# Subscribe to multiple sources
claude --channels discord,telegram,imessage,webhooks
```

### Integraciones Compatibles

| Integración | Descripción |
|-------------|-------------|
| **Discord** | Recibir y responder mensajes de Discord en tu sesión |
| **Telegram** | Recibir y responder mensajes de Telegram en tu sesión |
| **iMessage** | Recibir notificaciones de iMessage en tu sesión |
| **Webhooks** | Recibir eventos de fuentes de webhook arbitrarias |

### Configuración

Configura los channels con el flag `--channels` al inicio. Para despliegues empresariales, usa la configuración administrada para controlar qué plugins de channel están permitidos:

```json
{
  "allowedChannelPlugins": ["discord", "telegram"]
}
```

El ajuste administrado `allowedChannelPlugins` controla qué plugins de channel están permitidos en toda la organización.

### Cómo Funciona

1. Los servidores MCP actúan como plugins de channel que se conectan a servicios externos
2. Los mensajes y eventos entrantes se envían a la sesión activa de Claude Code
3. Claude puede leer y responder mensajes dentro del contexto de la sesión
4. Los plugins de channel deben ser aprobados mediante el ajuste administrado `allowedChannelPlugins`
5. No se requiere polling — los eventos se envían en tiempo real

---

## Integración con Chrome

La Integración con Chrome conecta Claude Code a tu navegador Chrome o Microsoft Edge para automatización web en tiempo real y debugging. Es una funcionalidad beta disponible desde v2.0.73+ (soporte para Edge agregado en v1.0.36+).

### Habilitar la Integración con Chrome

**Al iniciar**:

```bash
claude --chrome      # Enable Chrome connection
claude --no-chrome   # Disable Chrome connection
```

**Dentro de una sesión**:

```
/chrome
```

Seleccioná "Enabled by default" para activar la Integración con Chrome en todas las sesiones futuras. Claude Code comparte el estado de inicio de sesión de tu navegador, por lo que puede interactuar con aplicaciones web autenticadas.

### Capacidades

| Capacidad | Descripción |
|------------|-------------|
| **Debugging en tiempo real** | Leer logs de consola, inspeccionar elementos del DOM, depurar JavaScript en tiempo real |
| **Verificación de diseño** | Comparar páginas renderizadas con maquetas de diseño |
| **Validación de formularios** | Probar envíos de formularios, validación de entradas y manejo de errores |
| **Testing de apps web** | Interactuar con apps autenticadas (Gmail, Google Docs, Notion, etc.) |
| **Extracción de datos** | Scrapear y procesar contenido de páginas web |
| **Grabación de sesión** | Grabar interacciones del navegador como archivos GIF |

### Permisos a Nivel de Sitio

La extensión de Chrome gestiona el acceso por sitio. Otorgá o revocá el acceso a sitios específicos en cualquier momento a través del popup de la extensión. Claude Code solo interactúa con los sitios que hayas permitido explícitamente.

### Cómo Funciona

Claude Code controla el navegador en una ventana visible — puedes ver las acciones en tiempo real. Cuando el navegador encuentra una página de inicio de sesión o un CAPTCHA, Claude hace una pausa y espera a que lo resuelvas manualmente antes de continuar.

### Limitaciones Conocidas

- **Soporte de navegadores**: Solo Chrome y Edge — Brave, Arc y otros navegadores basados en Chromium no son compatibles
- **WSL**: No disponible en Windows Subsystem for Linux
- **Proveedores de terceros**: No compatible con los proveedores de API Bedrock, Vertex ni Foundry
- **Service worker inactivo**: El service worker de la extensión de Chrome puede quedar inactivo durante sesiones prolongadas

> **Consejo**: La Integración con Chrome es una funcionalidad beta. El soporte de navegadores puede ampliarse en versiones futuras.

---

## Remote Control

El Remote Control te permite continuar una sesión de Claude Code que se está ejecutando localmente desde tu teléfono, tablet o cualquier navegador. Tu sesión local sigue ejecutándose en tu máquina — nada se mueve a la nube. Disponible en los planes Pro, Max, Team y Enterprise (v2.1.51+).

### Iniciar Remote Control

**Desde el CLI**:

```bash
# Start with default session name
claude remote-control

# Start with a custom name
claude remote-control --name "Auth Refactor"
```

**Desde dentro de una sesión**:

```
/remote-control
/remote-control "Auth Refactor"
```

**Flags disponibles**:

| Flag | Descripción |
|------|-------------|
| `--name "title"` | Título de sesión personalizado para fácil identificación |
| `--verbose` | Mostrar logs de conexión detallados |
| `--sandbox` | Habilitar aislamiento de sistema de archivos y red |
| `--no-sandbox` | Deshabilitar sandboxing (predeterminado) |

### Conectarse a una Sesión

Tres formas de conectarse desde otro dispositivo:

1. **URL de sesión** — Se imprime en el terminal cuando la sesión comienza; abrila en cualquier navegador
2. **Código QR** — Presioná `espacio` después de iniciar para mostrar un código QR escaneable
3. **Buscar por nombre** — Navegá tus sesiones en claude.ai/code o en la app móvil de Claude (iOS/Android)

### Seguridad

- **Sin puertos entrantes** abiertos en tu máquina
- **Solo HTTPS saliente** mediante TLS
- **Credenciales con alcance limitado** — múltiples tokens de corta duración con alcance restringido
- **Aislamiento de sesión** — cada sesión remota es independiente

### Remote Control vs Claude Code en la Web

| Aspecto | Remote Control | Claude Code en la Web |
|--------|---------------|-------------------|
| **Ejecución** | Se ejecuta en tu máquina | Se ejecuta en la nube de Anthropic |
| **Herramientas locales** | Acceso completo a servidores MCP locales, archivos y CLI | Sin dependencias locales |
| **Caso de uso** | Continuar trabajo local desde otro dispositivo | Empezar desde cualquier navegador |

### Limitaciones

- Una sesión remota por instancia de Claude Code
- El terminal debe permanecer abierto en la máquina host
- La sesión expira después de aproximadamente 10 minutos si la red no está disponible

### Casos de Uso

- Controlar Claude Code desde un dispositivo móvil o tablet cuando no estás en tu escritorio
- Usar la interfaz más rica de claude.ai manteniendo la ejecución local de herramientas
- Revisiones rápidas de código mientras te mueves con tu entorno de desarrollo local completo

---

## Web Sessions

Las Web Sessions te permiten ejecutar Claude Code directamente en el navegador en claude.ai/code, o crear sesiones web desde el CLI.

### Crear una Web Session

```bash
# Create a new web session from the CLI
claude --remote "implement the new API endpoints"
```

Esto inicia una sesión de Claude Code en claude.ai a la que puedes acceder desde cualquier navegador.

### Reanudar Web Sessions Localmente

Si iniciaste una sesión en la web y quieres continuarla localmente:

```bash
# Resume a web session in the local terminal
claude --teleport
```

O desde dentro de un REPL interactivo:
```
/teleport
```

### Casos de Uso

- Empezar trabajo en una máquina y continuarlo en otra
- Compartir una URL de sesión con miembros del equipo
- Usar la interfaz web para revisión visual de diffs y luego cambiar al terminal para ejecución

---

## Desktop App

La Desktop App de Claude Code proporciona una aplicación independiente con revisión visual de diffs, sesiones en paralelo y conectores integrados. Disponible para macOS y Windows (planes Pro, Max, Team y Enterprise).

### Instalación

Descargá desde [claude.ai](https://claude.ai) para tu plataforma:
- **macOS**: Build universal (Apple Silicon e Intel)
- **Windows**: Instaladores x64 y ARM64 disponibles

Consultá el [Desktop Quickstart](https://code.claude.com/docs/en/desktop-quickstart) para instrucciones de configuración.

### Transferir desde el CLI

Transferí tu sesión actual del CLI a la Desktop App:

```
/desktop
```

### Funcionalidades Principales

| Funcionalidad | Descripción |
|---------|-------------|
| **Vista de diff** | Revisión visual archivo por archivo con comentarios en línea; Claude lee los comentarios y revisa |
| **Vista previa de app** | Inicia automáticamente servidores de desarrollo con un navegador integrado para verificación en tiempo real |
| **Monitoreo de PR** | Integración con GitHub CLI con auto-fix de fallos de CI y auto-merge cuando pasan las verificaciones |
| **Sesiones en paralelo** | Múltiples sesiones en la barra lateral con aislamiento automático mediante Git worktree |
| **Tareas programadas** | Tareas recurrentes (por hora, diario, días de semana, semanal) que se ejecutan mientras la app está abierta |
| **Renderizado rico** | Renderizado de código, markdown y diagramas con resaltado de sintaxis |

### Configuración de la Vista Previa de App

Configura el comportamiento del servidor de desarrollo en `.claude/launch.json`:

```json
{
  "command": "npm run dev",
  "port": 3000,
  "readyPattern": "ready on",
  "persistCookies": true
}
```

### Conectores

Conectá servicios externos para un contexto más rico:

| Conector | Capacidad |
|-----------|------------|
| **GitHub** | Monitoreo de PR, seguimiento de issues, revisión de código |
| **Slack** | Notificaciones, contexto de canales |
| **Linear** | Seguimiento de issues, gestión de sprints |
| **Notion** | Documentación, acceso a base de conocimiento |
| **Asana** | Gestión de tareas, seguimiento de proyectos |
| **Calendar** | Conciencia de horarios, contexto de reuniones |

> **Nota**: Los conectores no están disponibles para sesiones remotas (en la nube).

### Sesiones Remotas y SSH

- **Sesiones remotas**: Se ejecutan en la infraestructura de la nube de Anthropic; continúan incluso cuando la app está cerrada. Accesibles desde claude.ai/code o la app móvil de Claude
- **Sesiones SSH**: Se conectan a máquinas remotas mediante SSH con acceso completo al sistema de archivos y herramientas remotas. Claude Code debe estar instalado en la máquina remota

### Permission Modes en Desktop

La Desktop App admite los mismos 4 permission modes que el CLI:

| Modo | Comportamiento |
|------|----------|
| **Ask permissions** (predeterminado) | Revisar y aprobar cada edición y comando |
| **Auto accept edits** | Las ediciones de archivos se aprueban automáticamente; los comandos requieren aprobación manual |
| **Plan mode** | Revisar el enfoque antes de realizar cualquier cambio |
| **Bypass permissions** | Ejecución automática (solo en sandbox, controlado por el administrador) |

### Funcionalidades Enterprise

- **Consola de administración**: Controlar el acceso a la pestaña Code y los ajustes de permisos para la organización
- **Despliegue MDM**: Desplegar mediante MDM en macOS o MSIX en Windows
- **Integración SSO**: Requerir inicio de sesión único para los miembros de la organización
- **Managed settings**: Gestionar centralmente la configuración del equipo y la disponibilidad de modelos

---

## Lista de Tareas

La funcionalidad de Lista de Tareas proporciona seguimiento persistente de tareas que sobrevive a las compactaciones de contexto (cuando el historial de conversación se recorta para ajustarse a la context window).

### Alternar la Lista de Tareas

Presioná `Ctrl+T` para activar o desactivar la vista de la lista de tareas durante una sesión.

### Tareas Persistentes

Las tareas persisten a través de compactaciones de contexto, asegurando que los elementos de trabajo de larga duración no se pierdan cuando el contexto de la conversación se recorta. Esto es particularmente útil para implementaciones complejas de múltiples pasos.

### Directorios de Tareas con Nombre

Usa la variable de entorno `CLAUDE_CODE_TASK_LIST_ID` para crear directorios de tareas con nombre compartidos entre sesiones:

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

Esto permite que múltiples sesiones compartan la misma lista de tareas, lo que resulta útil para flujos de trabajo en equipo o proyectos con múltiples sesiones.

---

## Sugerencias de Prompt

Las Sugerencias de Prompt muestran comandos de ejemplo en gris basados en tu historial de git y el contexto de la conversación actual.

### Cómo Funciona

- Las sugerencias aparecen como texto en gris debajo de tu prompt de entrada
- Presioná `Tab` para aceptar la sugerencia
- Presioná `Enter` para aceptar y enviar inmediatamente
- Las sugerencias son conscientes del contexto, basándose en el historial de git y el estado de la conversación

### Deshabilitar Sugerencias de Prompt

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git Worktrees

Los Git Worktrees te permiten iniciar Claude Code en un worktree aislado, habilitando el trabajo en paralelo en diferentes ramas sin necesidad de hacer stash o cambiar de rama.

### Iniciar en un Worktree

```bash
# Start Claude Code in an isolated worktree
claude --worktree
# or
claude -w
```

### Ubicación del Worktree

Los worktrees se crean en:
```
<repo>/.claude/worktrees/<name>
```

### Sparse Checkout para Monorepos

Usa el ajuste `worktree.sparsePaths` para realizar sparse-checkout en monorepos, reduciendo el uso de disco y el tiempo de clonación:

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### Herramientas y Hooks de Worktree

| Elemento | Descripción |
|------|-------------|
| `ExitWorktree` | Herramienta para salir y limpiar el worktree actual |
| `WorktreeCreate` | Evento de hook que se dispara cuando se crea un worktree |
| `WorktreeRemove` | Evento de hook que se dispara cuando se elimina un worktree |

### Limpieza Automática

Si no se realizan cambios en el worktree, se limpia automáticamente cuando la sesión termina.

### Casos de Uso

- Trabajar en una rama de funcionalidad manteniendo la rama main intacta
- Ejecutar pruebas de forma aislada sin afectar el directorio de trabajo
- Probar cambios experimentales en un entorno descartable
- Sparse-checkout de paquetes específicos en monorepos para un inicio más rápido

---

## Sandboxing

El Sandboxing proporciona aislamiento de sistema de archivos y red a nivel de OS para los comandos Bash ejecutados por Claude Code. Es complementario a las reglas de permisos y proporciona una capa adicional de seguridad.

### Habilitar Sandboxing

**Slash command**:
```
/sandbox
```

**Flags de CLI**:
```bash
claude --sandbox       # Enable sandboxing
claude --no-sandbox    # Disable sandboxing
```

### Ajustes de Configuración

| Ajuste | Descripción |
|---------|-------------|
| `sandbox.enabled` | Habilitar o deshabilitar sandboxing |
| `sandbox.failIfUnavailable` | Fallar si no se puede activar el sandboxing |
| `sandbox.filesystem.allowWrite` | Rutas permitidas para acceso de escritura |
| `sandbox.filesystem.allowRead` | Rutas permitidas para acceso de lectura |
| `sandbox.filesystem.denyRead` | Rutas denegadas para acceso de lectura |
| `sandbox.enableWeakerNetworkIsolation` | Habilitar aislamiento de red más débil en macOS |

### Ejemplo de Configuración

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    },
    "enableWeakerNetworkIsolation": true
  }
}
```

### Cómo Funciona

- Los comandos Bash se ejecutan en un entorno con sandbox con acceso restringido al sistema de archivos
- El acceso a la red puede aislarse para prevenir conexiones externas no deseadas
- Funciona junto con las reglas de permisos para una defensa en profundidad
- En macOS, usa `sandbox.enableWeakerNetworkIsolation` para restricciones de red (el aislamiento completo de red no está disponible en macOS)

### Casos de Uso

- Ejecutar código no confiable o generado de forma segura
- Prevenir modificaciones accidentales de archivos fuera del proyecto
- Restringir el acceso a la red durante tareas automatizadas

---

## Managed Settings (Enterprise)

Los Managed Settings permiten que los administradores empresariales desplieguen la configuración de Claude Code en toda una organización usando herramientas de gestión nativas de cada plataforma.

### Métodos de Despliegue

| Plataforma | Método | Desde |
|----------|--------|-------|
| macOS | Archivos plist administrados (MDM) | v2.1.51+ |
| Windows | Registro de Windows | v2.1.51+ |
| Multiplataforma | Archivos de configuración administrados | v2.1.51+ |
| Multiplataforma | Drop-ins administrados (directorio `managed-settings.d/`) | v2.1.83+ |

### Drop-ins Administrados

Desde v2.1.83, los administradores pueden desplegar múltiples archivos de managed settings en un directorio `managed-settings.d/`. Los archivos se fusionan en orden alfabético, permitiendo configuración modular entre equipos:

```
~/.claude/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### Managed Settings Disponibles

| Ajuste | Descripción |
|---------|-------------|
| `disableBypassPermissionsMode` | Impedir que los usuarios habiliten bypass permissions |
| `availableModels` | Restringir qué modelos pueden seleccionar los usuarios |
| `allowedChannelPlugins` | Controlar qué plugins de channel están permitidos |
| `autoMode.environment` | Configurar infraestructura de confianza para auto mode |
| Políticas personalizadas | Políticas de permisos y herramientas específicas de la organización |

### Ejemplo: Plist de macOS

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>disableBypassPermissionsMode</key>
  <true/>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

## Configuración y Ajustes

### Ubicaciones de los Archivos de Configuración

1. **Config global**: `~/.claude/config.json`
2. **Config de proyecto**: `./.claude/config.json`
3. **Config de usuario**: `~/.config/claude-code/settings.json`

### Ejemplo de Configuración Completa

**Configuración principal de funcionalidades avanzadas:**

```json
{
  "permissions": {
    "mode": "default"
  },
  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh"
  },
  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"]
      }
    }
  }
}
```

**Ejemplo de configuración extendida:**

```json
{
  "permissions": {
    "mode": "default",
    "allowedTools": ["Bash(git log:*)", "Read"],
    "disallowedTools": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": ["eslint --fix ${file_path}"] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": ["~/.claude/hooks/security-scan.sh"] }],
    "Stop": [{ "hooks": ["~/.claude/hooks/notify.sh"] }]
  },

  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

### Variables de Entorno

Sobreescribe la configuración con variables de entorno:

```bash
# Model selection
export ANTHROPIC_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# API configuration
export ANTHROPIC_API_KEY=sk-ant-...

# Thinking configuration
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high

# Feature toggles
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=true
export CLAUDE_CODE_SIMPLE=true              # Set by --bare flag

# MCP configuration
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# Task management
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Agent teams (experimental)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Subagent and plugin configuration
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=1

# Subprocess and streaming
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000
```

### Comandos de Gestión de Configuración

```
User: /config
[Opens interactive configuration menu]
```

El comando `/config` proporciona un menú interactivo para alternar ajustes como:
- Extended thinking activado/desactivado
- Salida verbose
- Permission mode
- Selección de modelo

### Configuración por Proyecto

Creá `.claude/config.json` en tu proyecto:

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": ["npm test && npm run lint"] }]
  },
  "permissions": {
    "mode": "default"
  },
  "mcp": {
    "servers": {
      "project-db": {
        "command": "mcp-postgres",
        "env": {
          "DATABASE_URL": "${PROJECT_DB_URL}"
        }
      }
    }
  }
}
```

---

## Agent Teams

Agent Teams es una funcionalidad experimental que permite que múltiples instancias de Claude Code colaboren en una tarea. Está deshabilitada por defecto.

### Habilitar Agent Teams

Habilitalo mediante variable de entorno o configuración:

```bash
# Environment variable
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

O agregalo a tu JSON de ajustes:

```json
{
  "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
}
```

### Cómo Funcionan los Agent Teams

- Un **team lead** coordina la tarea general y delega subtareas a los compañeros de equipo
- Los **teammates** trabajan de forma independiente, cada uno con su propia context window
- Una **lista de tareas compartida** habilita la auto-coordinación entre los miembros del equipo
- Usa definiciones de subagente (`.claude/agents/` o el flag `--agents`) para definir los roles y especializaciones de los teammates

### Modos de Visualización

Los Agent Teams admiten dos modos de visualización, configurados con el flag `--teammate-mode`:

| Modo | Descripción |
|------|-------------|
| `in-process` (predeterminado) | Los teammates se ejecutan dentro del mismo proceso de terminal |
| `tmux` | Cada teammate obtiene un panel dividido dedicado (requiere tmux o iTerm2) |
| `auto` | Selecciona automáticamente el mejor modo de visualización |

```bash
# Use tmux split panes for teammate display
claude --teammate-mode tmux

# Explicitly use in-process mode
claude --teammate-mode in-process
```

### Casos de Uso

- Tareas de refactorización grandes donde diferentes teammates manejan diferentes módulos
- Revisión de código e implementación en paralelo
- Cambios coordinados en múltiples archivos a lo largo de una base de código

> **Nota**: Agent Teams es experimental y puede cambiar en versiones futuras. Consultá [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) para la referencia completa.

---

## Buenas Prácticas

### Planning Mode
- ✅ Úsalo para tareas complejas de múltiples pasos
- ✅ Revisa los planes antes de aprobarlos
- ✅ Modifica los planes cuando sea necesario
- ❌ No lo uses para tareas simples

### Extended Thinking
- ✅ Úsalo para decisiones arquitectónicas
- ✅ Úsalo para resolución de problemas complejos
- ✅ Revisa el proceso de razonamiento
- ❌ No lo uses para consultas simples

### Background Tasks
- ✅ Úsalo para operaciones de larga duración
- ✅ Monitorea el progreso de las tareas
- ✅ Maneja los fallos de tareas con elegancia
- ❌ No inicies demasiadas tareas concurrentes

### Permisos
- ✅ Usa `plan` para revisión de código (solo lectura)
- ✅ Usa `default` para desarrollo interactivo
- ✅ Usa `acceptEdits` para flujos de trabajo de automatización
- ✅ Usa `auto` para trabajo autónomo con controles de seguridad
- ❌ No uses `bypassPermissions` a menos que sea absolutamente necesario

### Sesiones
- ✅ Usa sesiones separadas para tareas diferentes
- ✅ Guarda los estados de sesión importantes
- ✅ Limpia las sesiones antiguas
- ❌ No mezcles trabajo no relacionado en una sola sesión

---

## Recursos Adicionales

Para más información sobre Claude Code y funcionalidades relacionadas:

- [Documentación Oficial de Modo Interactivo](https://code.claude.com/docs/en/interactive-mode)
- [Documentación Oficial de Headless Mode](https://code.claude.com/docs/en/headless)
- [Referencia de CLI](https://code.claude.com/docs/en/cli-reference)
- [Guía de Checkpoints](../08-checkpoints/) - Gestión de sesiones y retroceso
- [Slash Commands](../01-slash-commands/) - Referencia de comandos
- [Guía de Memory](../02-memory/) - Contexto persistente
- [Guía de Skills](../03-skills/) - Capacidades autónomas
- [Guía de Subagentes](../04-subagents/) - Ejecución delegada de tareas
- [Guía de MCP](../05-mcp/) - Acceso a datos externos
- [Guía de Hooks](../06-hooks/) - Automatización basada en eventos
- [Guía de Plugins](../07-plugins/) - Extensiones incluidas
- [Documentación Oficial de Tareas Programadas](https://code.claude.com/docs/en/scheduled-tasks)
- [Documentación Oficial de Integración con Chrome](https://code.claude.com/docs/en/chrome)
- [Documentación Oficial de Remote Control](https://code.claude.com/docs/en/remote-control)
- [Documentación Oficial de Keybindings](https://code.claude.com/docs/en/keybindings)
- [Documentación Oficial de Desktop App](https://code.claude.com/docs/en/desktop)
- [Documentación Oficial de Agent Teams](https://code.claude.com/docs/en/agent-teams)

---
**Ultima Actualizacion**: Abril 2026
**Versión de Claude Code**: 2.1+
**Modelos Compatibles**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
