<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code Examples - Tarjeta de Referencia Rapida

## 🚀 Comandos de Instalacion Rapida

### Slash Commands
```bash
# Instalar todos
cp 01-slash-commands/*.md .claude/commands/

# Instalar uno especifico
cp 01-slash-commands/optimize.md .claude/commands/
```

### Memory
```bash
# Memoria del proyecto
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Memoria personal
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills
```bash
# Skills personales
cp -r 03-skills/code-review ~/.claude/skills/

# Skills del proyecto
cp -r 03-skills/code-review .claude/skills/
```

### Subagents
```bash
# Instalar todos
cp 04-subagents/*.md .claude/agents/

# Instalar uno especifico
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# Configurar credenciales
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Instalar config (alcance de proyecto)
cp 05-mcp/github-mcp.json .mcp.json

# O alcance de usuario: agregar a ~/.claude.json
```

### Hooks
```bash
# Instalar hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Configurar en settings (~/.claude/settings.json)
```

### Plugins
```bash
# Instalar desde ejemplos (si estan publicados)
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints
```bash
# Los checkpoints se crean automaticamente con cada prompt del usuario
# Para volver atras, presiona Esc dos veces o usa:
/rewind

# Luego elige: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, o Never mind
```

### Advanced Features
```bash
# Configurar en settings (.claude/settings.json)
# Ver 09-advanced-features/config-examples.json

# Modo de planificacion
/plan Task description

# Modos de permisos (usar el flag --permission-mode)
# default        - Pedir aprobacion en acciones riesgosas
# acceptEdits    - Auto-aceptar ediciones de archivos, pedir para otras
# plan           - Analisis de solo lectura, sin modificaciones
# dontAsk        - Aceptar todas las acciones excepto las riesgosas
# auto           - El clasificador de fondo decide los permisos automaticamente
# bypassPermissions - Aceptar todas las acciones (requiere --dangerously-skip-permissions)

# Gestion de sesiones
/resume                # Retomar una conversacion anterior
/rename "name"         # Nombrar la sesion actual
/fork                  # Bifurcar la sesion actual
claude -c              # Continuar la conversacion mas reciente
claude -r "session"    # Retomar sesion por nombre/ID
```

---

## 📋 Hoja de Referencia de Funcionalidades

| Funcionalidad | Ruta de Instalacion | Uso |
|---------|-------------|-------|
| **Slash Commands (55+)** | `.claude/commands/*.md` | `/command-name` |
| **Memory** | `./CLAUDE.md` | Se carga automaticamente |
| **Skills** | `.claude/skills/*/SKILL.md` | Se invoca automaticamente |
| **Subagents** | `.claude/agents/*.md` | Se delega automaticamente |
| **MCP** | `.mcp.json` (proyecto) o `~/.claude.json` (usuario) | `/mcp__server__action` |
| **Hooks (25 eventos)** | `~/.claude/hooks/*.sh` | Disparado por evento (4 tipos) |
| **Plugins** | Via `/plugin install` | Agrupa todo |
| **Checkpoints** | Integrado | `Esc+Esc` o `/rewind` |
| **Planning Mode** | Integrado | `/plan <task>` |
| **Modos de Permisos (6)** | Integrado | `--allowedTools`, `--permission-mode` |
| **Sessions** | Integrado | `/session <command>` |
| **Background Tasks** | Integrado | Ejecutar en segundo plano |
| **Remote Control** | Integrado | WebSocket API |
| **Web Sessions** | Integrado | `claude web` |
| **Git Worktrees** | Integrado | `/worktree` |
| **Auto Memory** | Integrado | Guarda automaticamente en CLAUDE.md |
| **Task List** | Integrado | `/task list` |
| **Bundled Skills (5)** | Integrado | `/simplify`, `/loop`, `/claude-api`, `/voice`, `/browse` |

---

## 🎯 Casos de Uso Frecuentes

### Revision de Codigo
```bash
# Metodo 1: Slash command
cp 01-slash-commands/optimize.md .claude/commands/
# Uso: /optimize

# Metodo 2: Subagent
cp 04-subagents/code-reviewer.md .claude/agents/
# Uso: Se delega automaticamente

# Metodo 3: Skill
cp -r 03-skills/code-review ~/.claude/skills/
# Uso: Se invoca automaticamente

# Metodo 4: Plugin (mejor opcion)
/plugin install pr-review
# Uso: /review-pr
```

### Documentacion
```bash
# Slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# Skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Plugin (solucion completa)
/plugin install documentation
```

### DevOps
```bash
# Plugin completo
/plugin install devops-automation

# Comandos: /deploy, /rollback, /status, /incident
```

### Estandares de Equipo
```bash
# Memoria del proyecto
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Editar para tu equipo
vim CLAUDE.md
```

### Automatizacion y Hooks
```bash
# Instalar hooks (25 eventos, 4 tipos: command, http, prompt, agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Ejemplos:
# - Tests pre-commit: pre-commit.sh
# - Auto-formato de codigo: format-code.sh
# - Escaneo de seguridad: security-scan.sh

# Auto Mode para workflows completamente autonomos
claude --enable-auto-mode -p "Refactor and test the auth module"
# O cambiar modos interactivamente con Shift+Tab
```

### Refactorizacion Segura
```bash
# Los checkpoints se crean automaticamente antes de cada prompt
# Intentar refactorizacion
# Si funciona: continuar
# Si falla: presionar Esc+Esc o usar /rewind para volver atras
```

### Implementacion Compleja
```bash
# Usar planning mode
/plan Implement user authentication system

# Claude crea un plan detallado
# Revisar y aprobar
# Claude implementa de forma sistematica
```

### Integracion CI/CD
```bash
# Ejecutar en modo headless (no interactivo)
claude -p "Run all tests and generate report"

# Con permission mode para CI
claude -p "Run tests" --permission-mode dontAsk

# Con Auto Mode para tareas de CI completamente autonomas
claude --enable-auto-mode -p "Run tests and fix failures"

# Con hooks para automatizacion
# Ver 09-advanced-features/README.md
```

### Aprendizaje y Experimentacion
```bash
# Usar plan mode para analisis seguro
claude --permission-mode plan

# Experimentar con seguridad - los checkpoints se crean automaticamente
# Si necesitas volver atras: presionar Esc+Esc o usar /rewind
```

### Agent Teams
```bash
# Habilitar agent teams
export CLAUDE_AGENT_TEAMS=1

# O en settings.json
{ "agentTeams": { "enabled": true } }

# Comenzar con: "Implement feature X using a team approach"
```

### Tareas Programadas
```bash
# Ejecutar un comando cada 5 minutos
/loop 5m /check-status

# Recordatorio unico
/loop 30m "remind me to check the deploy"
```

---

## 📁 Referencia de Ubicaciones de Archivos

```
Tu Proyecto/
├── .claude/
│   ├── commands/              # Los slash commands van aqui
│   ├── agents/                # Los subagents van aqui
│   ├── skills/                # Los skills del proyecto van aqui
│   └── settings.json          # Configuracion del proyecto (hooks, etc.)
├── .mcp.json                  # Configuracion MCP (alcance de proyecto)
├── CLAUDE.md                  # Memoria del proyecto
└── src/
    └── api/
        └── CLAUDE.md          # Memoria especifica del directorio

Directorio del Usuario/
├── .claude/
│   ├── commands/              # Comandos personales
│   ├── agents/                # Agents personales
│   ├── skills/                # Skills personales
│   ├── hooks/                 # Scripts de hooks
│   ├── settings.json          # Configuracion del usuario
│   ├── managed-settings.d/    # Configuracion gestionada (enterprise/org)
│   └── CLAUDE.md              # Memoria personal
└── .claude.json               # Config MCP personal (alcance de usuario)
```

---

## 🔍 Encontrar Ejemplos

### Por Categoria
- **Slash Commands**: `01-slash-commands/`
- **Memory**: `02-memory/`
- **Skills**: `03-skills/`
- **Subagents**: `04-subagents/`
- **MCP**: `05-mcp/`
- **Hooks**: `06-hooks/`
- **Plugins**: `07-plugins/`
- **Checkpoints**: `08-checkpoints/`
- **Advanced Features**: `09-advanced-features/`
- **CLI**: `10-cli/`

### Por Caso de Uso
- **Performance**: `01-slash-commands/optimize.md`
- **Seguridad**: `04-subagents/secure-reviewer.md`
- **Testing**: `04-subagents/test-engineer.md`
- **Documentacion**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### Por Complejidad
- **Simple**: Slash commands
- **Medio**: Subagents, Memory
- **Avanzado**: Skills, Hooks
- **Completo**: Plugins

---

## 🎓 Ruta de Aprendizaje

### Dia 1
```bash
# Leer el resumen
cat README.md

# Instalar un comando
cp 01-slash-commands/optimize.md .claude/commands/

# Probarlo
/optimize
```

### Dias 2-3
```bash
# Configurar memoria
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# Instalar subagent
cp 04-subagents/code-reviewer.md .claude/agents/
```

### Dias 4-5
```bash
# Configurar MCP
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# Probar comandos MCP
/mcp__github__list_prs
```

### Semana 2
```bash
# Instalar skill
cp -r 03-skills/code-review ~/.claude/skills/

# Dejar que se invoque automaticamente
# Solo escribe: "Review this code for issues"
```

### Semana 3+
```bash
# Instalar plugin completo
/plugin install pr-review

# Usar funcionalidades agrupadas
/review-pr
/check-security
/check-tests
```

---

## Novedades (Marzo 2026)

| Funcionalidad | Descripcion | Uso |
|---------|-------------|-------|
| **Auto Mode** | Operacion completamente autonoma con clasificador de fondo | Flag `--enable-auto-mode`, `Shift+Tab` para cambiar modos |
| **Channels** | Integracion con Discord y Telegram | Flag `--channels`, bots de Discord/Telegram |
| **Voice Dictation** | Dictar comandos y contexto a Claude por voz | Comando `/voice` |
| **Hooks (25 eventos)** | Sistema de hooks ampliado con 4 tipos | Tipos command, http, prompt, agent |
| **MCP Elicitation** | Los servidores MCP pueden solicitar entrada del usuario en tiempo de ejecucion | Se solicita automaticamente cuando el servidor necesita aclaracion |
| **WebSocket MCP** | Transporte WebSocket para conexiones MCP | Configurar en `.mcp.json` con URLs `ws://` |
| **Plugin LSP** | Soporte del Language Server Protocol para plugins | `userConfig`, variable `${CLAUDE_PLUGIN_DATA}` |
| **Remote Control** | Controlar Claude Code via WebSocket API | `claude --remote` para integraciones externas |
| **Web Sessions** | Interfaz de Claude Code basada en navegador | `claude web` para lanzar |
| **Desktop App** | Aplicacion de escritorio nativa | Descargar desde claude.ai/download |
| **Task List** | Gestionar tareas en segundo plano | `/task list`, `/task status <id>` |
| **Auto Memory** | Guardado automatico de memoria desde conversaciones | Claude guarda automaticamente el contexto clave en CLAUDE.md |
| **Git Worktrees** | Espacios de trabajo aislados para desarrollo en paralelo | `/worktree` para crear espacio de trabajo aislado |
| **Model Selection** | Cambiar entre Sonnet 4.6 y Opus 4.6 | `/model` o flag `--model` |
| **Agent Teams** | Coordinar multiples agents en tareas | Habilitar con la variable de entorno `CLAUDE_AGENT_TEAMS=1` |
| **Scheduled Tasks** | Tareas recurrentes con `/loop` | `/loop 5m /command` o herramienta CronCreate |
| **Chrome Integration** | Automatizacion del navegador | Flag `--chrome` o comando `/chrome` |
| **Keyboard Customization** | Atajos de teclado personalizados | Comando `/keybindings` |

---

## Consejos y Trucos

### Personalizacion
- Comenzar con los ejemplos tal como estan
- Modificar para adaptarlos a tus necesidades
- Probar antes de compartir con el equipo
- Versionar tus configuraciones en git

### Buenas Practicas
- Usar memory para los estandares del equipo
- Usar plugins para workflows completos
- Usar subagents para tareas complejas
- Usar slash commands para tareas rapidas

### Solucion de Problemas
```bash
# Verificar ubicacion de archivos
ls -la .claude/commands/
ls -la .claude/agents/

# Verificar sintaxis YAML
head -20 .claude/agents/code-reviewer.md

# Probar conexion MCP
echo $GITHUB_TOKEN
```

---

## 📊 Matriz de Funcionalidades

| Necesidad | Usar Esto | Ejemplo |
|------|----------|---------|
| Atajo rapido | Slash Command (55+) | `01-slash-commands/optimize.md` |
| Estandares de equipo | Memory | `02-memory/project-CLAUDE.md` |
| Workflow automatico | Skill | `03-skills/code-review/` |
| Tarea especializada | Subagent | `04-subagents/code-reviewer.md` |
| Datos externos | MCP (+ Elicitation, WebSocket) | `05-mcp/github-mcp.json` |
| Automatizacion por evento | Hook (25 eventos, 4 tipos) | `06-hooks/pre-commit.sh` |
| Solucion completa | Plugin (+ soporte LSP) | `07-plugins/pr-review/` |
| Experimento seguro | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| Completamente autonomo | Auto Mode | `--enable-auto-mode` o `Shift+Tab` |
| Integraciones de chat | Channels | `--channels` (Discord, Telegram) |
| Pipeline CI/CD | CLI | `10-cli/README.md` |

---

## 🔗 Accesos Rapidos

- **Guia Principal**: `README.md`
- **Indice Completo**: `INDEX.md`
- **Resumen**: `EXAMPLES_SUMMARY.md`
- **Guia Original**: `claude_concepts_guide.md`

---

## 📞 Preguntas Frecuentes

**P: ¿Cual debo usar?**
R: Empeza con slash commands y agrega funcionalidades segun las necesites.

**P: ¿Puedo combinar funcionalidades?**
R: ¡Si! Funcionan juntas. Memory + Commands + MCP = poderoso.

**P: ¿Como comparto con el equipo?**
R: Haz commit del directorio `.claude/` en git.

**P: ¿Y los secretos?**
R: Usa variables de entorno, nunca los hardcodees.

**P: ¿Puedo modificar los ejemplos?**
R: ¡Absolutamente! Son templates para personalizar.

---

## ✅ Checklist

Checklist para comenzar:

- [ ] Leer `README.md`
- [ ] Instalar 1 slash command
- [ ] Probar el comando
- [ ] Crear el `CLAUDE.md` del proyecto
- [ ] Instalar 1 subagent
- [ ] Configurar 1 integracion MCP
- [ ] Instalar 1 skill
- [ ] Probar un plugin completo
- [ ] Personalizar para tus necesidades
- [ ] Compartir con el equipo

---

**Inicio Rapido**: `cat README.md`

**Indice Completo**: `cat INDEX.md`

**Esta Tarjeta**: ¡Tenela a mano para referencia rapida!

---
**Ultima Actualizacion**: Abril 2026
**Claude Code Version**: 2.1+
