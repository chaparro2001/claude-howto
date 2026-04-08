<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code — Índice completo de ejemplos

Este documento proporciona un índice completo de todos los archivos de ejemplo organizados por tipo de funcionalidad.

## Estadísticas de resumen

- **Total de archivos**: más de 100 archivos
- **Categorías**: 10 categorías de funcionalidades
- **Plugins**: 3 plugins completos
- **Skills**: 6 skills completos
- **Hooks**: 8 hooks de ejemplo
- **Listos para usar**: Todos los ejemplos

---

## 01. Slash Commands (10 archivos)

Atajos invocados por el usuario para workflows comunes.

| Archivo | Descripción | Caso de uso |
|------|-------------|----------|
| `optimize.md` | Analizador de optimización de código | Encontrar problemas de rendimiento |
| `pr.md` | Preparación de pull request | Automatización del workflow de PR |
| `generate-api-docs.md` | Generador de documentación de API | Generar docs de API |
| `commit.md` | Asistente de mensaje de commit | Commits estandarizados |
| `setup-ci-cd.md` | Configuración de pipeline CI/CD | Automatización DevOps |
| `push-all.md` | Hacer push de todos los cambios | Workflow de push rápido |
| `unit-test-expand.md` | Expandir cobertura de tests unitarios | Automatización de tests |
| `doc-refactor.md` | Refactoring de documentación | Mejoras de docs |
| `pr-slash-command.png` | Ejemplo de captura de pantalla | Referencia visual |
| `README.md` | Documentación | Guía de configuración y uso |

**Ruta de instalación**: `.claude/commands/`

**Uso**: `/optimize`, `/pr`, `/generate-api-docs`, `/commit`, `/setup-ci-cd`, `/push-all`, `/unit-test-expand`, `/doc-refactor`

---

## 02. Memory (6 archivos)

Contexto persistente y estándares del proyecto.

| Archivo | Descripción | Alcance | Ubicación |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | Estándares del proyecto para el equipo | Todo el proyecto | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | Reglas específicas para la API | Directorio | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | Preferencias personales | Usuario | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | Captura de pantalla: memory guardada | - | Referencia visual |
| `memory-ask-claude.png` | Captura de pantalla: preguntar a Claude | - | Referencia visual |
| `README.md` | Documentación | - | Referencia |

**Instalación**: Copiar a la ubicación correspondiente

**Uso**: Cargado automáticamente por Claude

---

## 03. Skills (28 archivos)

Capacidades con invocación automática que incluyen scripts y templates.

### Skill de revisión de código (5 archivos)
```
code-review/
├── SKILL.md                          # Definición del skill
├── scripts/
│   ├── analyze-metrics.py            # Analizador de métricas de código
│   └── compare-complexity.py         # Comparación de complejidad
└── templates/
    ├── review-checklist.md           # Checklist de revisión
    └── finding-template.md           # Documentación de hallazgos
```

**Propósito**: Revisión de código completa con análisis de seguridad, rendimiento y calidad

**Invocación automática**: Al revisar código

---

### Skill de voz de marca (4 archivos)
```
brand-voice/
├── SKILL.md                          # Definición del skill
├── templates/
│   ├── email-template.txt            # Formato de email
│   └── social-post-template.txt      # Formato de redes sociales
└── tone-examples.md                  # Mensajes de ejemplo
```

**Propósito**: Asegurar voz de marca consistente en las comunicaciones

**Invocación automática**: Al crear copy de marketing

---

### Skill generador de documentación (2 archivos)
```
doc-generator/
├── SKILL.md                          # Definición del skill
└── generate-docs.py                  # Extractor de docs en Python
```

**Propósito**: Generar documentación de API completa a partir del código fuente

**Invocación automática**: Al crear o actualizar documentación de API

---

### Skill de refactoring (5 archivos)
```
refactor/
├── SKILL.md                          # Definición del skill
├── scripts/
│   ├── analyze-complexity.py         # Analizador de complejidad
│   └── detect-smells.py              # Detector de code smells
├── references/
│   ├── code-smells.md                # Catálogo de code smells
│   └── refactoring-catalog.md        # Patrones de refactoring
└── templates/
    └── refactoring-plan.md           # Template de plan de refactoring
```

**Propósito**: Refactoring sistemático de código con análisis de complejidad

**Invocación automática**: Al refactorizar código

---

### Skill Claude MD (1 archivo)
```
claude-md/
└── SKILL.md                          # Definición del skill
```

**Propósito**: Administrar y optimizar archivos CLAUDE.md

---

### Skill de borrador de blog (3 archivos)
```
blog-draft/
├── SKILL.md                          # Definición del skill
└── templates/
    ├── draft-template.md             # Template de borrador de blog
    └── outline-template.md           # Template de esquema de blog
```

**Propósito**: Redactar entradas de blog con estructura consistente

**Más**: `README.md` - Guía general de skills y uso

**Ruta de instalación**: `~/.claude/skills/` o `.claude/skills/`

---

## 04. Subagentes (9 archivos)

Asistentes de IA especializados con capacidades personalizadas.

| Archivo | Descripción | Herramientas | Caso de uso |
|------|-------------|-------|----------|
| `code-reviewer.md` | Análisis de calidad de código | read, grep, diff, lint_runner | Revisiones completas |
| `test-engineer.md` | Análisis de cobertura de tests | read, write, bash, grep | Automatización de tests |
| `documentation-writer.md` | Creación de documentación | read, write, grep | Generación de docs |
| `secure-reviewer.md` | Revisión de seguridad (solo lectura) | read, grep | Auditorías de seguridad |
| `implementation-agent.md` | Implementación completa | read, write, bash, grep, edit, glob | Desarrollo de funcionalidades |
| `debugger.md` | Especialista en depuración | read, bash, grep | Investigación de bugs |
| `data-scientist.md` | Especialista en análisis de datos | read, write, bash | Workflows de datos |
| `clean-code-reviewer.md` | Estándares de código limpio | read, grep | Calidad de código |
| `README.md` | Documentación | - | Guía de configuración y uso |

**Ruta de instalación**: `.claude/agents/`

**Uso**: Delegado automáticamente por el agente principal

---

## 05. Protocolo MCP (5 archivos)

Integraciones con herramientas y APIs externas.

| Archivo | Descripción | Se integra con | Caso de uso |
|------|-------------|-----------------|----------|
| `github-mcp.json` | Integración con GitHub | GitHub API | Gestión de PRs/issues |
| `database-mcp.json` | Consultas a base de datos | PostgreSQL/MySQL | Consultas de datos en vivo |
| `filesystem-mcp.json` | Operaciones de archivos | Sistema de archivos local | Gestión de archivos |
| `multi-mcp.json` | Múltiples servidores | GitHub + DB + Slack | Integración completa |
| `README.md` | Documentación | - | Guía de configuración y uso |

**Ruta de instalación**: `.mcp.json` (alcance de proyecto) o `~/.claude.json` (alcance de usuario)

**Uso**: `/mcp__github__list_prs`, etc.

---

## 06. Hooks (9 archivos)

Scripts de automatización basada en eventos que se ejecutan automáticamente.

| Archivo | Descripción | Evento | Caso de uso |
|------|-------------|-------|----------|
| `format-code.sh` | Formatea el código automáticamente | PreToolUse:Write | Formateo de código |
| `pre-commit.sh` | Ejecuta tests antes del commit | PreToolUse:Bash | Automatización de tests |
| `security-scan.sh` | Escaneo de seguridad | PostToolUse:Write | Verificaciones de seguridad |
| `log-bash.sh` | Registra comandos bash | PostToolUse:Bash | Logging de comandos |
| `validate-prompt.sh` | Valida prompts | PreToolUse | Validación de entrada |
| `notify-team.sh` | Envía notificaciones | Notification | Notificaciones al equipo |
| `context-tracker.py` | Hace seguimiento del uso de la ventana de contexto | PostToolUse | Monitoreo de contexto |
| `context-tracker-tiktoken.py` | Seguimiento de contexto basado en tokens | PostToolUse | Conteo preciso de tokens |
| `README.md` | Documentación | - | Guía de configuración y uso |

**Ruta de instalación**: Configurar en `~/.claude/settings.json`

**Uso**: Configurado en settings, se ejecuta automáticamente

**Tipos de hook** (4 tipos, 25 eventos):
- Tool Hooks: PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest
- Session Hooks: SessionStart, SessionEnd, Stop, StopFailure, SubagentStart, SubagentStop
- Task Hooks: UserPromptSubmit, TaskCompleted, TaskCreated, TeammateIdle
- Lifecycle Hooks: ConfigChange, CwdChanged, FileChanged, PreCompact, PostCompact, WorktreeCreate, WorktreeRemove, Notification, InstructionsLoaded, Elicitation, ElicitationResult

---

## 07. Plugins (3 plugins completos, 40 archivos)

Colecciones empaquetadas de funcionalidades.

### Plugin PR Review (10 archivos)
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # Manifiesto del plugin
├── commands/
│   ├── review-pr.md                  # Revisión completa
│   ├── check-security.md             # Verificación de seguridad
│   └── check-tests.md                # Verificación de cobertura de tests
├── agents/
│   ├── security-reviewer.md          # Especialista en seguridad
│   ├── test-checker.md               # Especialista en tests
│   └── performance-analyzer.md       # Especialista en rendimiento
├── mcp/
│   └── github-config.json            # Integración con GitHub
├── hooks/
│   └── pre-review.js                 # Validación pre-revisión
└── README.md                         # Documentación del plugin
```

**Funcionalidades**: Análisis de seguridad, cobertura de tests, impacto en rendimiento

**Comandos**: `/review-pr`, `/check-security`, `/check-tests`

**Instalación**: `/plugin install pr-review`

---

### Plugin DevOps Automation (15 archivos)
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # Manifiesto del plugin
├── commands/
│   ├── deploy.md                     # Despliegue
│   ├── rollback.md                   # Rollback
│   ├── status.md                     # Estado del sistema
│   └── incident.md                   # Respuesta a incidentes
├── agents/
│   ├── deployment-specialist.md      # Experto en despliegues
│   ├── incident-commander.md         # Coordinador de incidentes
│   └── alert-analyzer.md             # Analizador de alertas
├── mcp/
│   └── kubernetes-config.json        # Integración con Kubernetes
├── hooks/
│   ├── pre-deploy.js                 # Verificaciones pre-despliegue
│   └── post-deploy.js                # Tareas post-despliegue
├── scripts/
│   ├── deploy.sh                     # Automatización de despliegue
│   ├── rollback.sh                   # Automatización de rollback
│   └── health-check.sh               # Health checks
└── README.md                         # Documentación del plugin
```

**Funcionalidades**: Despliegue Kubernetes, rollback, monitoreo, respuesta a incidentes

**Comandos**: `/deploy`, `/rollback`, `/status`, `/incident`

**Instalación**: `/plugin install devops-automation`

---

### Plugin Documentation (14 archivos)
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # Manifiesto del plugin
├── commands/
│   ├── generate-api-docs.md          # Generación de docs de API
│   ├── generate-readme.md            # Creación de README
│   ├── sync-docs.md                  # Sincronización de docs
│   └── validate-docs.md              # Validación de docs
├── agents/
│   ├── api-documenter.md             # Especialista en docs de API
│   ├── code-commentator.md           # Especialista en comentarios de código
│   └── example-generator.md          # Creador de ejemplos
├── mcp/
│   └── github-docs-config.json       # Integración con GitHub
├── templates/
│   ├── api-endpoint.md               # Template de endpoint de API
│   ├── function-docs.md              # Template de docs de función
│   └── adr-template.md               # Template de ADR
└── README.md                         # Documentación del plugin
```

**Funcionalidades**: Docs de API, generación de README, sincronización de docs, validación

**Comandos**: `/generate-api-docs`, `/generate-readme`, `/sync-docs`, `/validate-docs`

**Instalación**: `/plugin install documentation`

**Más**: `README.md` - Guía general de plugins y uso

---

## 08. Checkpoints y Rewind (2 archivos)

Guardar el estado de la conversación y explorar enfoques alternativos.

| Archivo | Descripción | Contenido |
|------|-------------|---------|
| `README.md` | Documentación | Guía completa de checkpoints |
| `checkpoint-examples.md` | Ejemplos del mundo real | Migración de base de datos, optimización de rendimiento, iteración de UI, depuración |
| | | |

**Conceptos clave**:
- **Checkpoint**: Snapshot del estado de la conversación
- **Rewind**: Volver a un checkpoint anterior
- **Branch Point**: Explorar múltiples enfoques

**Uso**:
```
# Los checkpoints se crean automáticamente con cada prompt del usuario
# Para hacer rewind, presiona Esc dos veces o usa:
/rewind
# Luego elige: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, o Never mind
```

**Casos de uso**:
- Probar diferentes implementaciones
- Recuperarse de errores
- Experimentación segura
- Comparar soluciones
- A/B testing

---

## 09. Funcionalidades Avanzadas (3 archivos)

Capacidades avanzadas para workflows complejos.

| Archivo | Descripción | Funcionalidades |
|------|-------------|----------|
| `README.md` | Guía completa | Documentación de todas las funcionalidades avanzadas |
| `config-examples.json` | Ejemplos de configuración | Más de 10 configuraciones para casos de uso específicos |
| `planning-mode-examples.md` | Ejemplos de planificación | REST API, migración de base de datos, refactoring |
| Scheduled Tasks | Tareas recurrentes con `/loop` y herramientas cron | Workflows recurrentes automatizados |
| Chrome Integration | Automatización del navegador via Chromium headless | Testing y scraping web |
| Remote Control (expandido) | Métodos de conexión, seguridad, tabla comparativa | Gestión de sesiones remotas |
| Keyboard Customization | Keybindings personalizados, soporte de chords, contextos | Atajos personalizados |
| Desktop App (expandido) | Conectores, launch.json, funcionalidades enterprise | Integración desktop |
| | | |

**Funcionalidades avanzadas cubiertas**:

### Planning Mode
- Crear planes de implementación detallados
- Estimaciones de tiempo y evaluación de riesgos
- Desglose sistemático de tareas

### Extended Thinking
- Razonamiento profundo para problemas complejos
- Análisis de decisiones de arquitectura
- Evaluación de compromisos

### Background Tasks
- Operaciones de larga duración sin bloquear
- Workflows de desarrollo paralelo
- Gestión y monitoreo de tareas

### Modos de permiso
- **default**: Pedir aprobación en acciones riesgosas
- **acceptEdits**: Aceptar automáticamente ediciones de archivos, preguntar para las demás
- **plan**: Análisis de solo lectura, sin modificaciones
- **auto**: Aprobar automáticamente acciones seguras, solicitar para las riesgosas
- **dontAsk**: Aceptar todas las acciones excepto las riesgosas
- **bypassPermissions**: Aceptar todas (requiere `--dangerously-skip-permissions`)

### Headless Mode (`claude -p`)
- Integración con CI/CD
- Ejecución automatizada de tareas
- Procesamiento por lotes

### Gestión de sesiones
- Múltiples sesiones de trabajo
- Cambio y guardado de sesiones
- Persistencia de sesiones

### Funcionalidades interactivas
- Atajos de teclado
- Historial de comandos
- Completado por Tab
- Entrada multilínea

### Configuración
- Gestión completa de settings
- Configuraciones específicas por entorno
- Personalización por proyecto

### Scheduled Tasks
- Tareas recurrentes con el comando `/loop`
- Herramientas cron: CronCreate, CronList, CronDelete
- Workflows recurrentes automatizados

### Chrome Integration
- Automatización del navegador via Chromium headless
- Capacidades de testing y scraping web
- Interacción con páginas y extracción de datos

### Remote Control (expandido)
- Métodos y protocolos de conexión
- Consideraciones de seguridad y buenas prácticas
- Tabla comparativa de opciones de acceso remoto

### Keyboard Customization
- Configuración de keybindings personalizados
- Soporte de chords para atajos de múltiples teclas
- Activación de keybindings según el contexto

### Desktop App (expandido)
- Conectores para integración con IDE
- Configuración de launch.json
- Funcionalidades enterprise y despliegue

---

## 10. Uso del CLI (1 archivo)

Patrones de uso y referencia de la interfaz de línea de comandos.

| Archivo | Descripción | Contenido |
|------|-------------|---------|
| `README.md` | Documentación del CLI | Flags, opciones y patrones de uso |

**Funcionalidades clave del CLI**:
- `claude` - Iniciar sesión interactiva
- `claude -p "prompt"` - Modo headless/no interactivo
- `claude web` - Iniciar sesión web
- `claude --model` - Seleccionar modelo (Sonnet 4.6, Opus 4.6)
- `claude --permission-mode` - Establecer el modo de permiso
- `claude --remote` - Habilitar control remoto via WebSocket

---

## Archivos de documentación (13 archivos)

| Archivo | Ubicación | Descripción |
|------|----------|-------------|
| `README.md` | `/` | Descripción general de los ejemplos |
| `INDEX.md` | `/` | Este índice completo |
| `QUICK_REFERENCE.md` | `/` | Tarjeta de referencia rápida |
| `README.md` | `/01-slash-commands/` | Guía de slash commands |
| `README.md` | `/02-memory/` | Guía de memory |
| `README.md` | `/03-skills/` | Guía de skills |
| `README.md` | `/04-subagents/` | Guía de subagentes |
| `README.md` | `/05-mcp/` | Guía de MCP |
| `README.md` | `/06-hooks/` | Guía de hooks |
| `README.md` | `/07-plugins/` | Guía de plugins |
| `README.md` | `/08-checkpoints/` | Guía de checkpoints |
| `README.md` | `/09-advanced-features/` | Guía de funcionalidades avanzadas |
| `README.md` | `/10-cli/` | Guía del CLI |

---

## Árbol completo de archivos

```
claude-howto/
├── README.md                                    # Descripción general principal
├── INDEX.md                                     # Este archivo
├── QUICK_REFERENCE.md                           # Tarjeta de referencia rápida
├── claude_concepts_guide.md                     # Guía original de conceptos
│
├── 01-slash-commands/                           # Slash Commands
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # Memory
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # Skills
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # Subagentes
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # Protocolo MCP
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # Hooks
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # Plugins
│   ├── pr-review/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── review-pr.md
│   │   │   ├── check-security.md
│   │   │   └── check-tests.md
│   │   ├── agents/
│   │   │   ├── security-reviewer.md
│   │   │   ├── test-checker.md
│   │   │   └── performance-analyzer.md
│   │   ├── mcp/
│   │   │   └── github-config.json
│   │   ├── hooks/
│   │   │   └── pre-review.js
│   │   └── README.md
│   ├── devops-automation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── deploy.md
│   │   │   ├── rollback.md
│   │   │   ├── status.md
│   │   │   └── incident.md
│   │   ├── agents/
│   │   │   ├── deployment-specialist.md
│   │   │   ├── incident-commander.md
│   │   │   └── alert-analyzer.md
│   │   ├── mcp/
│   │   │   └── kubernetes-config.json
│   │   ├── hooks/
│   │   │   ├── pre-deploy.js
│   │   │   └── post-deploy.js
│   │   ├── scripts/
│   │   │   ├── deploy.sh
│   │   │   ├── rollback.sh
│   │   │   └── health-check.sh
│   │   └── README.md
│   ├── documentation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── generate-api-docs.md
│   │   │   ├── generate-readme.md
│   │   │   ├── sync-docs.md
│   │   │   └── validate-docs.md
│   │   ├── agents/
│   │   │   ├── api-documenter.md
│   │   │   ├── code-commentator.md
│   │   │   └── example-generator.md
│   │   ├── mcp/
│   │   │   └── github-docs-config.json
│   │   ├── templates/
│   │   │   ├── api-endpoint.md
│   │   │   ├── function-docs.md
│   │   │   └── adr-template.md
│   │   └── README.md
│   └── README.md
│
├── 08-checkpoints/                              # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # Funcionalidades Avanzadas
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # Uso del CLI
    └── README.md
```

---

## Inicio rápido por caso de uso

### Calidad de código y revisiones
```bash
# Instalar slash command
cp 01-slash-commands/optimize.md .claude/commands/

# Instalar subagente
cp 04-subagents/code-reviewer.md .claude/agents/

# Instalar skill
cp -r 03-skills/code-review ~/.claude/skills/

# O instalar el plugin completo
/plugin install pr-review
```

### DevOps y despliegue
```bash
# Instalar plugin (incluye todo)
/plugin install devops-automation
```

### Documentación
```bash
# Instalar slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Instalar subagente
cp 04-subagents/documentation-writer.md .claude/agents/

# Instalar skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# O instalar el plugin completo
/plugin install documentation
```

### Estándares del equipo
```bash
# Configurar project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Editalo para que coincida con los estándares de tu equipo
```

### Integraciones externas
```bash
# Configurar variables de entorno
export GITHUB_TOKEN="tu_token"
export DATABASE_URL="postgresql://..."

# Instalar config MCP (alcance de proyecto)
cp 05-mcp/multi-mcp.json .mcp.json
```

### Automatización y validación
```bash
# Instalar hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Configurar hooks en settings (~/.claude/settings.json)
# Ver 06-hooks/README.md
```

### Experimentación segura
```bash
# Los checkpoints se crean automáticamente con cada prompt del usuario
# Para hacer rewind: presiona Esc+Esc o usa /rewind
# Luego elige qué restaurar desde el menú de rewind

# Ver 08-checkpoints/README.md para ejemplos
```

### Workflows avanzados
```bash
# Configurar funcionalidades avanzadas
# Ver 09-advanced-features/config-examples.json

# Usar planning mode
/plan Implement feature X

# Usar modos de permiso
claude --permission-mode plan          # Para revisión de código (solo lectura)
claude --permission-mode acceptEdits   # Aceptar ediciones automáticamente
claude --permission-mode auto          # Aprobar automáticamente acciones seguras

# Ejecutar en modo headless para CI/CD
claude -p "Run tests and report results"

# Ejecutar tareas en segundo plano
Run tests in background

# Ver 09-advanced-features/README.md para la guía completa
```

---

## Matriz de cobertura de funcionalidades

| Categoría | Comandos | Agentes | MCP | Hooks | Scripts | Templates | Docs | Imágenes | Total |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **01 Slash Commands** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 Memory** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 Skills** | - | - | - | - | 5 | 9 | 1 | - | **28** |
| **04 Subagentes** | - | 8 | - | - | - | - | 1 | - | **9** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 Hooks** | - | - | - | 8 | - | - | 1 | - | **9** |
| **07 Plugins** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **40** |
| **08 Checkpoints** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 Advanced** | - | - | - | - | - | - | 1 | 2 | **3** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## Camino de aprendizaje

### Principiante (Semana 1)
1. ✅ Leer `README.md`
2. ✅ Instalar 1-2 slash commands
3. ✅ Crear el archivo de project memory
4. ✅ Probar los comandos básicos

### Intermedio (Semanas 2-3)
1. ✅ Configurar GitHub MCP
2. ✅ Instalar un subagente
3. ✅ Intentar delegar tareas
4. ✅ Instalar un skill

### Avanzado (Semana 4+)
1. ✅ Instalar un plugin completo
2. ✅ Crear slash commands personalizados
3. ✅ Crear un subagente personalizado
4. ✅ Crear un skill personalizado
5. ✅ Construir tu propio plugin

### Experto (Semana 5+)
1. ✅ Configurar hooks para automatización
2. ✅ Usar checkpoints para experimentación
3. ✅ Configurar planning mode
4. ✅ Usar modos de permiso de forma efectiva
5. ✅ Configurar headless mode para CI/CD
6. ✅ Dominar la gestión de sesiones

---

## Búsqueda por palabra clave

### Rendimiento
- `01-slash-commands/optimize.md` - Análisis de rendimiento
- `04-subagents/code-reviewer.md` - Revisión de rendimiento
- `03-skills/code-review/` - Métricas de rendimiento
- `07-plugins/pr-review/agents/performance-analyzer.md` - Especialista en rendimiento

### Seguridad
- `04-subagents/secure-reviewer.md` - Revisión de seguridad
- `03-skills/code-review/` - Análisis de seguridad
- `07-plugins/pr-review/` - Verificaciones de seguridad

### Testing
- `04-subagents/test-engineer.md` - Ingeniero de tests
- `07-plugins/pr-review/commands/check-tests.md` - Cobertura de tests

### Documentación
- `01-slash-commands/generate-api-docs.md` - Comando de docs de API
- `04-subagents/documentation-writer.md` - Agente escritor de docs
- `03-skills/doc-generator/` - Skill generador de docs
- `07-plugins/documentation/` - Plugin completo de documentación

### Despliegue
- `07-plugins/devops-automation/` - Solución DevOps completa

### Automatización
- `06-hooks/` - Automatización basada en eventos
- `06-hooks/pre-commit.sh` - Automatización pre-commit
- `06-hooks/format-code.sh` - Formateo automático
- `09-advanced-features/` - Headless mode para CI/CD

### Validación
- `06-hooks/security-scan.sh` - Validación de seguridad
- `06-hooks/validate-prompt.sh` - Validación de prompts

### Experimentación
- `08-checkpoints/` - Experimentación segura con rewind
- `08-checkpoints/checkpoint-examples.md` - Ejemplos del mundo real

### Planificación
- `09-advanced-features/planning-mode-examples.md` - Ejemplos de planning mode
- `09-advanced-features/README.md` - Extended thinking

### Configuración
- `09-advanced-features/config-examples.json` - Ejemplos de configuración

---

## Notas

- Todos los ejemplos están listos para usar
- Modificalos para adaptarlos a tus necesidades específicas
- Los ejemplos siguen las buenas prácticas de Claude Code
- Cada categoría tiene su propio README con instrucciones detalladas
- Los scripts incluyen manejo adecuado de errores
- Los templates son personalizables

---

## Contribuciones

¿Quieres agregar más ejemplos? Sigue esta estructura:
1. Crea el subdirectorio correspondiente
2. Incluye un README.md con las instrucciones de uso
3. Sigue las convenciones de nombres
4. Pruébalo exhaustivamente
5. Actualiza este índice

---

**Ultima Actualizacion**: Abril 2026
**Versión de Claude Code**: 2.1+
**Total de ejemplos**: más de 100 archivos
**Categorías**: 10 funcionalidades
**Hooks**: 8 scripts de automatización
**Ejemplos de configuración**: más de 10 escenarios
**Listos para usar**: Todos los ejemplos
