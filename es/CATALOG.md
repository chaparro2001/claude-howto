<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Catálogo de Funcionalidades de Claude Code

> Guía de referencia rápida de todas las funcionalidades de Claude Code: comandos, agentes, skills, plugins y hooks.

**Navegación**: [Comandos](#slash-commands) | [Modos de permiso](#modos-de-permiso) | [Subagentes](#subagentes) | [Skills](#skills) | [Plugins](#plugins) | [Servidores MCP](#servidores-mcp) | [Hooks](#hooks) | [Memory](#archivos-de-memory) | [Nuevas funcionalidades](#nuevas-funcionalidades-marzo-2026)

---

## Resumen

| Funcionalidad | Integradas | Ejemplos | Total | Referencia |
|---------|----------|----------|-------|-----------|
| **Slash Commands** | 55+ | 8 | 63+ | [01-slash-commands/](../01-slash-commands/) |
| **Subagentes** | 6 | 11 | 17 | [04-subagents/](../04-subagents/) |
| **Skills** | 5 incluidas | 4 | 9 | [03-skills/](../03-skills/) |
| **Plugins** | - | 3 | 3 | [07-plugins/](../07-plugins/) |
| **Servidores MCP** | 1 | 8 | 9 | [05-mcp/](../05-mcp/) |
| **Hooks** | 25 eventos | 8 | 8 | [06-hooks/](../06-hooks/) |
| **Memory** | 7 tipos | 3 | 3 | [02-memory/](../02-memory/) |
| **Total** | **99** | **45** | **119** | |

---

## Slash Commands

Los comandos son atajos invocados por el usuario que ejecutan acciones específicas.

### Comandos integrados

| Comando | Descripción | Cuándo usarlo |
|---------|-------------|-------------|
| `/help` | Mostrar información de ayuda | Empezar, aprender comandos |
| `/btw` | Pregunta lateral sin agregar al contexto | Preguntas rápidas de desvío |
| `/chrome` | Configurar integración con Chrome | Automatización del navegador |
| `/clear` | Limpiar el historial de conversación | Empezar de nuevo, reducir contexto |
| `/diff` | Visor interactivo de diferencias | Revisar cambios |
| `/config` | Ver/editar la configuración | Personalizar el comportamiento |
| `/status` | Mostrar el estado de la sesión | Ver el estado actual |
| `/agents` | Listar agentes disponibles | Ver opciones de delegación |
| `/skills` | Listar skills disponibles | Ver capacidades de invocación automática |
| `/hooks` | Listar hooks configurados | Depurar automatización |
| `/insights` | Analizar patrones de sesión | Optimización de sesión |
| `/install-slack-app` | Instalar la app Claude para Slack | Integración con Slack |
| `/keybindings` | Personalizar atajos de teclado | Personalización de teclas |
| `/mcp` | Listar servidores MCP | Verificar integraciones externas |
| `/memory` | Ver archivos de memory cargados | Depurar la carga de contexto |
| `/mobile` | Generar código QR para móvil | Acceso desde móvil |
| `/passes` | Ver pases de uso | Información de suscripción |
| `/plugin` | Administrar plugins | Instalar/eliminar extensiones |
| `/plan` | Entrar en modo de planificación | Implementaciones complejas |
| `/rewind` | Volver a un checkpoint | Deshacer cambios, explorar alternativas |
| `/checkpoint` | Administrar checkpoints | Guardar/restaurar estados |
| `/cost` | Mostrar costos de uso de tokens | Monitorear el gasto |
| `/context` | Mostrar el uso de la ventana de contexto | Administrar la longitud de la conversación |
| `/export` | Exportar la conversación | Guardar como referencia |
| `/extra-usage` | Configurar límites de uso adicional | Gestión de límites de velocidad |
| `/feedback` | Enviar feedback o reporte de bug | Reportar problemas |
| `/login` | Autenticarse con Anthropic | Acceder a funcionalidades |
| `/logout` | Cerrar sesión | Cambiar de cuenta |
| `/sandbox` | Activar/desactivar modo sandbox | Ejecución segura de comandos |
| `/vim` | Activar/desactivar modo vim | Edición estilo vim |
| `/doctor` | Ejecutar diagnósticos | Solucionar problemas |
| `/reload-plugins` | Recargar plugins instalados | Gestión de plugins |
| `/release-notes` | Mostrar notas de versión | Ver nuevas funcionalidades |
| `/remote-control` | Habilitar control remoto | Acceso remoto |
| `/permissions` | Administrar permisos | Controlar el acceso |
| `/session` | Administrar sesiones | Workflows multi-sesión |
| `/rename` | Renombrar la sesión actual | Organizar sesiones |
| `/resume` | Retomar sesión anterior | Continuar el trabajo |
| `/todo` | Ver/administrar lista de tareas | Hacer seguimiento de tareas |
| `/tasks` | Ver tareas en segundo plano | Monitorear operaciones asíncronas |
| `/copy` | Copiar la última respuesta al portapapeles | Compartir output rápidamente |
| `/teleport` | Transferir sesión a otra máquina | Continuar el trabajo de forma remota |
| `/desktop` | Abrir la app desktop de Claude | Cambiar a la interfaz desktop |
| `/theme` | Cambiar el tema de color | Personalizar la apariencia |
| `/usage` | Mostrar estadísticas de uso de API | Monitorear cuota y costos |
| `/fork` | Bifurcar la conversación actual | Explorar alternativas |
| `/stats` | Mostrar estadísticas de sesión | Revisar métricas de sesión |
| `/statusline` | Configurar la línea de estado | Personalizar la visualización de estado |
| `/stickers` | Ver stickers de sesión | Recompensas divertidas |
| `/fast` | Activar/desactivar modo de output rápido | Acelerar respuestas |
| `/terminal-setup` | Configurar integración de terminal | Configurar funcionalidades del terminal |
| `/upgrade` | Buscar actualizaciones | Gestión de versiones |

### Comandos personalizados (ejemplos)

| Comando | Descripción | Cuándo usarlo | Alcance | Instalación |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | Analizar código para optimización | Mejora de rendimiento | Proyecto | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | Preparar pull request | Antes de enviar PRs | Proyecto | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | Generar documentación de API | Documentar APIs | Proyecto | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | Crear git commit con contexto | Hacer commits de cambios | Usuario | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | Hacer stage, commit y push | Despliegue rápido | Usuario | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | Reestructurar documentación | Mejorar docs | Proyecto | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | Configurar pipeline CI/CD | Proyectos nuevos | Proyecto | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | Expandir cobertura de tests | Mejorar el testing | Proyecto | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **Alcance**: `Usuario` = workflows personales (`~/.claude/commands/`), `Proyecto` = compartido con el equipo (`.claude/commands/`)

**Referencia**: [01-slash-commands/](../01-slash-commands/) | [Documentación oficial](https://code.claude.com/docs/en/interactive-mode)

**Instalación rápida (todos los comandos personalizados)**:
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## Modos de permiso

Claude Code soporta 6 modos de permiso que controlan cómo se autoriza el uso de herramientas.

| Modo | Descripción | Cuándo usarlo |
|------|-------------|-------------|
| `default` | Solicitar permiso en cada llamada a herramienta | Uso interactivo estándar |
| `acceptEdits` | Aceptar automáticamente ediciones de archivos, solicitar para otros | Workflows de edición de confianza |
| `plan` | Solo herramientas de lectura, sin escrituras | Planificación y exploración |
| `auto` | Aceptar todas las herramientas sin solicitar permiso | Operación completamente autónoma (Research Preview) |
| `bypassPermissions` | Omitir todas las verificaciones de permisos | CI/CD, entornos headless |
| `dontAsk` | Omitir herramientas que requerirían permiso | Scripting no interactivo |

> **Nota**: el modo `auto` es una funcionalidad en Research Preview (marzo 2026). Usá `bypassPermissions` solo en entornos de confianza y con sandbox.

**Referencia**: [Documentación oficial](https://code.claude.com/docs/en/permissions)

---

## Subagentes

Asistentes de IA especializados con contextos aislados para tareas específicas.

### Subagentes integrados

| Agente | Descripción | Herramientas | Modelo | Cuándo usarlo |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | Tareas de múltiples pasos, investigación | Todas las herramientas | Hereda el modelo | Investigación compleja, tareas multi-archivo |
| **Plan** | Planificación de implementación | Read, Glob, Grep, Bash | Hereda el modelo | Diseño de arquitectura, planificación |
| **Explore** | Exploración del código base | Read, Glob, Grep | Haiku 4.5 | Búsquedas rápidas, entender código |
| **Bash** | Ejecución de comandos | Bash | Hereda el modelo | Operaciones git, tareas de terminal |
| **statusline-setup** | Configuración de línea de estado | Bash, Read, Write | Sonnet 4.6 | Configurar la visualización de la línea de estado |
| **Claude Code Guide** | Ayuda y documentación | Read, Glob, Grep | Haiku 4.5 | Obtener ayuda, aprender funcionalidades |

### Campos de configuración de subagentes

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `name` | string | Identificador del agente |
| `description` | string | Qué hace el agente |
| `model` | string | Modelo alternativo (ej. `haiku-4.5`) |
| `tools` | array | Lista de herramientas permitidas |
| `effort` | string | Nivel de esfuerzo de razonamiento (`low`, `medium`, `high`) |
| `initialPrompt` | string | System prompt inyectado al inicio del agente |
| `disallowedTools` | array | Herramientas explícitamente denegadas a este agente |

### Subagentes personalizados (ejemplos)

| Agente | Descripción | Cuándo usarlo | Alcance | Instalación |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | Calidad de código completa | Sesiones de revisión de código | Proyecto | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | Diseño de arquitectura de funcionalidades | Planificación de nuevas funcionalidades | Proyecto | `cp 04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | Análisis profundo del código base | Entender funcionalidades existentes | Proyecto | `cp 04-subagents/code-explorer.md .claude/agents/` |
| `clean-code-reviewer` | Revisión de principios Clean Code | Revisión de mantenibilidad | Proyecto | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | Estrategia y cobertura de tests | Planificación de tests | Proyecto | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | Documentación técnica | Docs de API, guías | Proyecto | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | Revisión enfocada en seguridad | Auditorías de seguridad | Proyecto | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | Implementación completa de funcionalidades | Desarrollo de funcionalidades | Proyecto | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | Análisis de causa raíz | Investigación de bugs | Usuario | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | Consultas SQL, análisis de datos | Tareas de datos | Usuario | `cp 04-subagents/data-scientist.md .claude/agents/` |
| `performance-optimizer` | Profiling y ajuste de rendimiento | Investigación de cuellos de botella | Proyecto | `cp 04-subagents/performance-optimizer.md .claude/agents/` |

> **Alcance**: `Usuario` = personal (`~/.claude/agents/`), `Proyecto` = compartido con el equipo (`.claude/agents/`)

**Referencia**: [04-subagents/](../04-subagents/) | [Documentación oficial](https://code.claude.com/docs/en/sub-agents)

**Instalación rápida (todos los agentes personalizados)**:
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## Skills

Capacidades con invocación automática que incluyen instrucciones, scripts y templates.

### Skills de ejemplo

| Skill | Descripción | Cuándo se invoca automáticamente | Alcance | Instalación |
|-------|-------------|-------------------|-------|--------------|
| `code-review` | Revisión de código completa | "Review this code", "Check quality" | Proyecto | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | Verificador de consistencia de marca | Redactar copy de marketing | Proyecto | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | Generador de documentación de API | "Generate docs", "Document API" | Proyecto | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | Refactoring sistemático de código (Martin Fowler) | "Refactor this", "Clean up code" | Usuario | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **Alcance**: `Usuario` = personal (`~/.claude/skills/`), `Proyecto` = compartido con el equipo (`.claude/skills/`)

### Estructura de un skill

```
~/.claude/skills/skill-name/
├── SKILL.md          # Definición e instrucciones del skill
├── scripts/          # Scripts auxiliares
└── templates/        # Templates de output
```

### Campos del frontmatter de un skill

Los skills soportan YAML frontmatter en `SKILL.md` para la configuración:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `name` | string | Nombre para mostrar del skill |
| `description` | string | Qué hace el skill |
| `autoInvoke` | array | Frases disparadoras para invocación automática |
| `effort` | string | Nivel de esfuerzo de razonamiento (`low`, `medium`, `high`) |
| `shell` | string | Shell a usar para los scripts (`bash`, `zsh`, `sh`) |

**Referencia**: [03-skills/](../03-skills/) | [Documentación oficial](https://code.claude.com/docs/en/skills)

**Instalación rápida (todos los skills)**:
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### Skills incluidas

| Skill | Descripción | Cuándo se invoca automáticamente |
|-------|-------------|-------------------|
| `/simplify` | Revisar código por calidad | Después de escribir código |
| `/batch` | Ejecutar prompts en múltiples archivos | Operaciones por lotes |
| `/debug` | Depurar tests/errores fallidos | Sesiones de depuración |
| `/loop` | Ejecutar prompts en intervalos | Tareas recurrentes |
| `/claude-api` | Construir apps con la Claude API | Desarrollo de API |

---

## Plugins

Colecciones empaquetadas de comandos, agentes, servidores MCP y hooks.

### Plugins de ejemplo

| Plugin | Descripción | Componentes | Cuándo usarlo | Alcance | Instalación |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | Workflow de revisión de PR | 3 comandos, 3 agentes, GitHub MCP | Revisiones de código | Proyecto | `/plugin install pr-review` |
| `devops-automation` | Despliegue y monitoreo | 4 comandos, 3 agentes, K8s MCP | Tareas DevOps | Proyecto | `/plugin install devops-automation` |
| `documentation` | Suite de generación de docs | 4 comandos, 3 agentes, templates | Documentación | Proyecto | `/plugin install documentation` |

> **Alcance**: `Proyecto` = compartido con el equipo, `Usuario` = workflows personales

### Estructura de un plugin

```
.claude-plugin/
├── plugin.json       # Archivo de manifiesto
├── commands/         # Slash commands
├── agents/           # Subagentes
├── skills/           # Skills
├── mcp/              # Configuraciones MCP
├── hooks/            # Scripts de hook
└── scripts/          # Scripts utilitarios
```

**Referencia**: [07-plugins/](../07-plugins/) | [Documentación oficial](https://code.claude.com/docs/en/plugins)

**Comandos de gestión de plugins**:
```bash
/plugin list              # Listar plugins instalados
/plugin install <name>    # Instalar plugin
/plugin remove <name>     # Eliminar plugin
/plugin update <name>     # Actualizar plugin
```

---

## Servidores MCP

Servidores del Model Context Protocol para acceso a herramientas y APIs externas.

### Servidores MCP comunes

| Servidor | Descripción | Cuándo usarlo | Alcance | Instalación |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | Gestión de PRs, issues, código | Workflows de GitHub | Proyecto | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | Consultas SQL, acceso a datos | Operaciones de base de datos | Proyecto | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | Operaciones avanzadas de archivos | Tareas complejas de archivos | Usuario | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | Comunicación del equipo | Notificaciones, actualizaciones | Proyecto | Configurar en settings |
| **Google Docs** | Acceso a documentos | Edición y revisión de docs | Proyecto | Configurar en settings |
| **Asana** | Gestión de proyectos | Seguimiento de tareas | Proyecto | Configurar en settings |
| **Stripe** | Datos de pagos | Análisis financiero | Proyecto | Configurar en settings |
| **Memory** | Memory persistente | Recuperación entre sesiones | Usuario | Configurar en settings |
| **Context7** | Documentación de librerías | Búsqueda de docs actualizada | Integrado | Integrado |

> **Alcance**: `Proyecto` = equipo (`.mcp.json`), `Usuario` = personal (`~/.claude.json`), `Integrado` = preinstalado

### Ejemplo de configuración MCP

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Referencia**: [05-mcp/](../05-mcp/) | [Documentación del Protocolo MCP](https://modelcontextprotocol.io)

**Instalación rápida (GitHub MCP)**:
```bash
export GITHUB_TOKEN="tu_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## Hooks

Automatización basada en eventos que ejecuta comandos shell en respuesta a eventos de Claude Code.

### Eventos de hook

| Evento | Descripción | Cuándo se dispara | Casos de uso |
|-------|-------------|----------------|-----------|
| `SessionStart` | La sesión comienza o se retoma | Inicialización de sesión | Tareas de configuración |
| `InstructionsLoaded` | Instrucciones cargadas | Archivo CLAUDE.md o de reglas cargado | Manejo de instrucciones personalizadas |
| `UserPromptSubmit` | Antes del procesamiento del prompt | El usuario envía un mensaje | Validación de entrada |
| `PreToolUse` | Antes de la ejecución de una herramienta | Antes de que corra cualquier herramienta | Validación, logging |
| `PermissionRequest` | Diálogo de permiso mostrado | Antes de acciones sensibles | Flujos de aprobación personalizados |
| `PostToolUse` | Después de que una herramienta tiene éxito | Después de que completa cualquier herramienta | Formateo, notificaciones |
| `PostToolUseFailure` | La ejecución de herramienta falla | Después de un error de herramienta | Manejo de errores, logging |
| `Notification` | Se envía una notificación | Claude envía una notificación | Alertas externas |
| `SubagentStart` | Subagente iniciado | La tarea del subagente comienza | Inicializar contexto del subagente |
| `SubagentStop` | Subagente termina | La tarea del subagente se completa | Encadenar acciones |
| `Stop` | Claude termina de responder | Respuesta completa | Limpieza, reportes |
| `StopFailure` | Un error de API termina el turno | Ocurre un error de API | Recuperación de errores, logging |
| `TeammateIdle` | Agente compañero inactivo | Coordinación del equipo de agentes | Distribuir trabajo |
| `TaskCompleted` | Tarea marcada como completa | Tarea finalizada | Procesamiento post-tarea |
| `TaskCreated` | Tarea creada via TaskCreate | Nueva tarea creada | Seguimiento de tareas, logging |
| `ConfigChange` | Configuración actualizada | Settings modificados | Reaccionar a cambios de config |
| `CwdChanged` | El directorio de trabajo cambia | Directorio cambiado | Configuración específica por directorio |
| `FileChanged` | Un archivo vigilado cambia | Archivo modificado | Monitoreo de archivos, rebuild |
| `PreCompact` | Antes de la operación de compact | Compresión de contexto | Preservación de estado |
| `PostCompact` | Después de que completa la compactación | Compactación finalizada | Acciones post-compact |
| `WorktreeCreate` | Worktree siendo creado | Git worktree creado | Configurar entorno de worktree |
| `WorktreeRemove` | Worktree siendo eliminado | Git worktree eliminado | Limpiar recursos del worktree |
| `Elicitation` | Servidor MCP solicita entrada | Elicitación MCP | Validación de entrada |
| `ElicitationResult` | El usuario responde a la elicitación | El usuario responde | Procesamiento de respuesta |
| `SessionEnd` | La sesión termina | Terminación de sesión | Limpieza, guardar estado |

### Hooks de ejemplo

| Hook | Descripción | Evento | Alcance | Instalación |
|------|-------------|-------|-------|--------------|
| `validate-bash.py` | Validación de comandos | PreToolUse:Bash | Proyecto | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | Escaneo de seguridad | PostToolUse:Write | Proyecto | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | Formateo automático | PostToolUse:Write | Usuario | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | Validación de prompt | UserPromptSubmit | Proyecto | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | Seguimiento de uso de tokens | Stop | Usuario | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | Validación pre-commit | PreToolUse:Bash | Proyecto | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | Logging de comandos | PostToolUse:Bash | Usuario | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |
| `dependency-check.sh` | Escaneo de vulnerabilidades en cambios de manifiesto | PostToolUse:Write | Proyecto | `cp 06-hooks/dependency-check.sh .claude/hooks/` |

> **Alcance**: `Proyecto` = equipo (`.claude/settings.json`), `Usuario` = personal (`~/.claude/settings.json`)

### Configuración de hooks

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "~/.claude/hooks/validate-bash.py"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "command": "~/.claude/hooks/format-code.sh"
      }
    ]
  }
}
```

**Referencia**: [06-hooks/](../06-hooks/) | [Documentación oficial](https://code.claude.com/docs/en/hooks)

**Instalación rápida (todos los hooks)**:
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## Archivos de Memory

Contexto persistente cargado automáticamente entre sesiones.

### Tipos de memory

| Tipo | Ubicación | Alcance | Cuándo usarlo |
|------|----------|-------|-------------|
| **Managed Policy** | Políticas gestionadas por la organización | Organización | Aplicar estándares de toda la org |
| **Project** | `./CLAUDE.md` | Proyecto (equipo) | Estándares del equipo, contexto del proyecto |
| **Project Rules** | `.claude/rules/` | Proyecto (equipo) | Reglas de proyecto modulares |
| **User** | `~/.claude/CLAUDE.md` | Usuario (personal) | Preferencias personales |
| **User Rules** | `~/.claude/rules/` | Usuario (personal) | Reglas personales modulares |
| **Local** | `./CLAUDE.local.md` | Local (ignorado por git) | Overrides específicos de máquina (no está en la documentación oficial a marzo 2026; puede ser legacy) |
| **Auto Memory** | Automático | Sesión | Insights y correcciones capturadas automáticamente |

> **Alcance**: `Organización` = gestionado por admins, `Proyecto` = compartido con el equipo via git, `Usuario` = preferencias personales, `Local` = sin commit, `Sesión` = gestionado automáticamente

**Referencia**: [02-memory/](../02-memory/) | [Documentación oficial](https://code.claude.com/docs/en/memory)

**Instalación rápida**:
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## Nuevas funcionalidades (marzo 2026)

| Funcionalidad | Descripción | Cómo usarla |
|---------|-------------|------------|
| **Remote Control** | Controlar sesiones de Claude Code remotamente via API | Usá la API de control remoto para enviar prompts y recibir respuestas programáticamente |
| **Web Sessions** | Ejecutar Claude Code en un entorno basado en navegador | Accedé via `claude web` o a través de la Consola de Anthropic |
| **Desktop App** | Aplicación desktop nativa para Claude Code | Usá `/desktop` o descargalo desde el sitio de Anthropic |
| **Agent Teams** | Coordinar múltiples agentes trabajando en tareas relacionadas | Configurá agentes compañeros que colaboran y comparten contexto |
| **Task List** | Gestión y monitoreo de tareas en segundo plano | Usá `/tasks` para ver y administrar operaciones en segundo plano |
| **Prompt Suggestions** | Sugerencias de comandos según el contexto | Las sugerencias aparecen automáticamente según el contexto actual |
| **Git Worktrees** | Git worktrees aislados para desarrollo paralelo | Usá comandos de worktree para trabajo paralelo seguro en ramas |
| **Sandboxing** | Entornos de ejecución aislados por seguridad | Usá `/sandbox` para activar/desactivar; ejecuta comandos en entornos restringidos |
| **MCP OAuth** | Autenticación OAuth para servidores MCP | Configurá credenciales OAuth en los settings del servidor MCP para acceso seguro |
| **MCP Tool Search** | Buscar y descubrir herramientas MCP dinámicamente | Usá la búsqueda de herramientas para encontrar herramientas MCP disponibles en los servidores conectados |
| **Scheduled Tasks** | Configurar tareas recurrentes con `/loop` y herramientas cron | Usá `/loop 5m /command` o la herramienta CronCreate |
| **Chrome Integration** | Automatización del navegador con Chromium headless | Usá el flag `--chrome` o el comando `/chrome` |
| **Keyboard Customization** | Personalizar keybindings incluyendo soporte de chords | Usá `/keybindings` o editá `~/.claude/keybindings.json` |
| **Auto Mode** | Operación completamente autónoma sin solicitudes de permiso (Research Preview) | Usá `--mode auto` o `/permissions auto`; marzo 2026 |
| **Channels** | Comunicación multi-canal (Telegram, Slack, etc.) (Research Preview) | Configurá plugins de canal; marzo 2026 |
| **Voice Dictation** | Entrada por voz para prompts | Usá el ícono de micrófono o el keybinding de voz |
| **Agent Hook Type** | Hooks que inician un subagente en lugar de ejecutar un comando shell | Configurá `"type": "agent"` en la configuración del hook |
| **Prompt Hook Type** | Hooks que inyectan texto de prompt en la conversación | Configurá `"type": "prompt"` en la configuración del hook |
| **MCP Elicitation** | Los servidores MCP pueden solicitar entrada del usuario durante la ejecución de herramientas | Manejo via los eventos de hook `Elicitation` y `ElicitationResult` |
| **WebSocket MCP Transport** | Transporte basado en WebSocket para conexiones de servidores MCP | Usá `"transport": "websocket"` en la config del servidor MCP |
| **Plugin LSP Support** | Integración del Language Server Protocol via plugins | Configurá servidores LSP en `plugin.json` para funcionalidades del editor |
| **Managed Drop-ins** | Configuraciones drop-in gestionadas por la organización (v2.1.83) | Configurado por admins via managed policies; aplicado automáticamente a todos los usuarios |

---

## Matriz de referencia rápida

### Guía de selección de funcionalidades

| Necesidad | Funcionalidad recomendada | Por qué |
|------|---------------------|-----|
| Atajo rápido | Slash Command | Manual, inmediato |
| Contexto persistente | Memory | Carga automática |
| Automatización compleja | Skill | Invocación automática |
| Tarea especializada | Subagente | Contexto aislado |
| Datos externos | Servidor MCP | Acceso en tiempo real |
| Automatización por eventos | Hook | Disparado por eventos |
| Solución completa | Plugin | Bundle todo-en-uno |

### Prioridad de instalación

| Prioridad | Funcionalidad | Comando |
|----------|---------|---------|
| 1. Esencial | Memory | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. Uso diario | Slash Commands | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. Calidad | Subagentes | `cp 04-subagents/*.md .claude/agents/` |
| 4. Automatización | Hooks | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. Externo | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. Avanzado | Skills | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. Completo | Plugins | `/plugin install pr-review` |

---

## Instalación completa en un solo comando

Instalá todos los ejemplos de este repositorio:

```bash
# Crear directorios
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# Instalar todas las funcionalidades
cp 01-slash-commands/*.md .claude/commands/ && \
cp 02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r 03-skills/* ~/.claude/skills/ && \
cp 04-subagents/*.md .claude/agents/ && \
cp 06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## Recursos adicionales

- [Documentación oficial de Claude Code](https://code.claude.com/docs/en/overview)
- [Especificación del Protocolo MCP](https://modelcontextprotocol.io)
- [Roadmap de Aprendizaje](LEARNING-ROADMAP.md)
- [README principal](ROOT-README.md)

---

**Ultima Actualizacion**: Abril 2026
**Versión de Claude Code**: 2.1+
