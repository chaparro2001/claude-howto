<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks

Los hooks son scripts automatizados que se ejecutan en respuesta a eventos especificos durante las sesiones de Claude Code. Permiten automatizacion, validacion, gestion de permisos y workflows personalizados.

## Descripcion general

Los hooks son acciones automatizadas (comandos de shell, webhooks HTTP, prompts de LLM o evaluaciones de subagente) que se ejecutan automaticamente cuando ocurren eventos especificos en Claude Code. Reciben entrada en JSON y comunican resultados mediante codigos de salida y salida JSON.

**Caracteristicas clave:**
- Automatizacion basada en eventos
- Entrada/salida basada en JSON
- Soporte para hooks de tipo command, prompt, HTTP y agent
- Coincidencia de patrones para hooks especificos de herramientas

## Configuracion

Los hooks se configuran en archivos de settings con una estructura especifica:

- `~/.claude/settings.json` - Configuracion del usuario (todos los proyectos)
- `.claude/settings.json` - Configuracion del proyecto (compartible, se hace commit)
- `.claude/settings.local.json` - Configuracion local del proyecto (no se hace commit)
- Managed policy - Configuracion a nivel de organizacion
- Plugin `hooks/hooks.json` - Hooks con ambito de plugin
- Frontmatter de Skill/Agent - Hooks de lifetime del componente

### Estructura basica de configuracion

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**Campos clave:**

| Campo | Descripcion | Ejemplo |
|-------|-------------|---------|
| `matcher` | Patron para coincidir con nombres de herramientas (distingue mayusculas) | `"Write"`, `"Edit\|Write"`, `"*"` |
| `hooks` | Array de definiciones de hook | `[{ "type": "command", ... }]` |
| `type` | Tipo de hook: `"command"` (bash), `"prompt"` (LLM), `"http"` (webhook), o `"agent"` (subagente) | `"command"` |
| `command` | Comando de shell a ejecutar | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | Timeout opcional en segundos (defecto 60) | `30` |
| `once` | Si es `true`, ejecuta el hook solo una vez por sesion | `true` |

### Patrones de matcher

| Patron | Descripcion | Ejemplo |
|---------|-------------|---------|
| Cadena exacta | Coincide con una herramienta especifica | `"Write"` |
| Patron regex | Coincide con multiples herramientas | `"Edit\|Write"` |
| Comodin | Coincide con todas las herramientas | `"*"` o `""` |
| Herramientas MCP | Patron de server y herramienta | `"mcp__memory__.*"` |

**Valores de matcher para InstructionsLoaded:**

| Valor del matcher | Descripcion |
|---------------|-------------|
| `session_start` | Instrucciones cargadas al inicio de la sesion |
| `nested_traversal` | Instrucciones cargadas durante recorrido de directorios anidados |
| `path_glob_match` | Instrucciones cargadas mediante coincidencia de patron glob de ruta |

## Tipos de hook

Claude Code soporta cuatro tipos de hook:

### Command Hooks

El tipo de hook por defecto. Ejecuta un comando de shell y se comunica mediante JSON en stdin/stdout y codigos de salida.

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

### HTTP Hooks

> Agregado en v2.1.63.

Endpoints de webhook remotos que reciben la misma entrada JSON que los command hooks. Los HTTP hooks envian JSON al URL mediante POST y reciben una respuesta JSON. Los HTTP hooks se enrutan a traves del sandbox cuando el sandboxing esta habilitado. La interpolacion de variables de entorno en URLs requiere una lista explicita `allowedEnvVars` por seguridad.

```json
{
  "hooks": {
    "PostToolUse": [{
      "type": "http",
      "url": "https://my-webhook.example.com/hook",
      "matcher": "Write"
    }]
  }
}
```

**Propiedades clave:**
- `"type": "http"` -- identifica esto como un HTTP hook
- `"url"` -- la URL del endpoint del webhook
- Se enruta a traves del sandbox cuando el sandbox esta habilitado
- Requiere una lista explicita `allowedEnvVars` para cualquier interpolacion de variables de entorno en la URL

### Prompt Hooks

Prompts evaluados por LLM donde el contenido del hook es un prompt que Claude evalua. Se usan principalmente con los eventos `Stop` y `SubagentStop` para verificacion inteligente de completitud de tareas.

```json
{
  "type": "prompt",
  "prompt": "Evaluate if Claude completed all requested tasks.",
  "timeout": 30
}
```

El LLM evalua el prompt y devuelve una decision estructurada (ver [Hooks basados en prompt](#hooks-basados-en-prompt) para mas detalles).

### Agent Hooks

Hooks de verificacion basados en subagentes que generan un agente dedicado para evaluar condiciones o realizar verificaciones complejas. A diferencia de los prompt hooks (evaluacion de LLM en un solo turno), los agent hooks pueden usar herramientas y realizar razonamiento en multiples pasos.

```json
{
  "type": "agent",
  "prompt": "Verify the code changes follow our architecture guidelines. Check the relevant design docs and compare.",
  "timeout": 120
}
```

**Propiedades clave:**
- `"type": "agent"` -- identifica esto como un agent hook
- `"prompt"` -- la descripcion de la tarea para el subagente
- El agente puede usar herramientas (Read, Grep, Bash, etc.) para realizar su evaluacion
- Devuelve una decision estructurada similar a los prompt hooks

## Eventos de hook

Claude Code soporta **26 eventos de hook**:

| Evento | Cuando se activa | Entrada del matcher | Puede bloquear | Uso comun |
|-------|---------------|---------------|-----------|------------|
| **SessionStart** | La sesion comienza/se reanuda/clear/compact | startup/resume/clear/compact | No | Configuracion del entorno |
| **InstructionsLoaded** | Despues de cargar CLAUDE.md o archivo de reglas | (ninguno) | No | Modificar/filtrar instrucciones |
| **UserPromptSubmit** | El usuario envia un prompt | (ninguno) | Si | Validar prompts |
| **PreToolUse** | Antes de la ejecucion de una herramienta | Nombre de herramienta | Si (allow/deny/ask) | Validar, modificar entradas |
| **PermissionRequest** | Se muestra el dialogo de permisos | Nombre de herramienta | Si | Auto-aprobar/denegar |
| **PermissionDenied** | El usuario deniega un prompt de permiso | Nombre de herramienta | No | Registro, analitica, aplicacion de politicas |
| **PostToolUse** | Despues de que la herramienta tiene exito | Nombre de herramienta | No | Agregar contexto, feedback |
| **PostToolUseFailure** | La ejecucion de la herramienta falla | Nombre de herramienta | No | Manejo de errores, registro |
| **Notification** | Se envia una notificacion | Tipo de notificacion | No | Notificaciones personalizadas |
| **SubagentStart** | Se genera un subagente | Nombre del tipo de agente | No | Configuracion del subagente |
| **SubagentStop** | El subagente termina | Nombre del tipo de agente | Si | Validacion del subagente |
| **Stop** | Claude termina de responder | (ninguno) | Si | Verificacion de completitud de tarea |
| **StopFailure** | Un error de API termina el turno | (ninguno) | No | Recuperacion de errores, registro |
| **TeammateIdle** | Un companero del equipo de agentes esta inactivo | (ninguno) | Si | Coordinacion de companeros |
| **TaskCompleted** | La tarea se marca como completa | (ninguno) | Si | Acciones post-tarea |
| **TaskCreated** | La tarea se crea via TaskCreate | (ninguno) | No | Seguimiento de tareas, registro |
| **ConfigChange** | Los archivos de configuracion cambian | (ninguno) | Si (excepto policy) | Reaccionar a actualizaciones de config |
| **CwdChanged** | El directorio de trabajo cambia | (ninguno) | No | Configuracion especifica por directorio |
| **FileChanged** | Un archivo vigilado cambia | (ninguno) | No | Monitoreo de archivos, reconstruccion |
| **PreCompact** | Antes de la compactacion del contexto | manual/auto | No | Acciones previas a compactacion |
| **PostCompact** | Despues de que la compactacion termina | (ninguno) | No | Acciones posteriores a compactacion |
| **WorktreeCreate** | Se esta creando un worktree | (ninguno) | Si (retorno de ruta) | Inicializacion del worktree |
| **WorktreeRemove** | Se esta eliminando un worktree | (ninguno) | No | Limpieza del worktree |
| **Elicitation** | El servidor MCP solicita entrada del usuario | (ninguno) | Si | Validacion de entrada |
| **ElicitationResult** | El usuario responde a la elicitacion | (ninguno) | Si | Procesamiento de respuesta |
| **SessionEnd** | La sesion termina | (ninguno) | No | Limpieza, registro final |

### PreToolUse

Se ejecuta despues de que Claude crea los parametros de la herramienta y antes del procesamiento. Usalo para validar o modificar las entradas de la herramienta.

**Configuracion:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py"
          }
        ]
      }
    ]
  }
}
```

**Matchers comunes:** `Task`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**Control de salida:**
- `permissionDecision`: `"allow"`, `"deny"`, o `"ask"`
- `permissionDecisionReason`: Explicacion de la decision
- `updatedInput`: Parametros de entrada de la herramienta modificados

### PostToolUse

Se ejecuta inmediatamente despues de que la herramienta se completa. Usalo para verificacion, registro o para proporcionar contexto de vuelta a Claude.

**Configuracion:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py"
          }
        ]
      }
    ]
  }
}
```

**Control de salida:**
- La decision `"block"` proporciona feedback a Claude
- `additionalContext`: Contexto agregado para Claude

### UserPromptSubmit

Se ejecuta cuando el usuario envia un prompt, antes de que Claude lo procese.

**Configuracion:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py"
          }
        ]
      }
    ]
  }
}
```

**Control de salida:**
- `decision`: `"block"` para prevenir el procesamiento
- `reason`: Explicacion si se bloqueo
- `additionalContext`: Contexto agregado al prompt

### Stop y SubagentStop

Se ejecutan cuando Claude termina de responder (Stop) o cuando un subagente se completa (SubagentStop). Soportan evaluacion basada en prompt para verificacion inteligente de completitud de tareas.

**Campo de entrada adicional:** Tanto los hooks `Stop` como `SubagentStop` reciben un campo `last_assistant_message` en su entrada JSON, que contiene el mensaje final de Claude o del subagente antes de detenerse. Esto es util para evaluar la completitud de la tarea.

**Configuracion:**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Evaluate if Claude completed all requested tasks.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### SubagentStart

Se ejecuta cuando un subagente comienza su ejecucion. La entrada del matcher es el nombre del tipo de agente, lo que permite que los hooks apunten a tipos especificos de subagente.

**Configuracion:**
```json
{
  "hooks": {
    "SubagentStart": [
      {
        "matcher": "code-review",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/subagent-init.sh"
          }
        ]
      }
    ]
  }
}
```

### SessionStart

Se ejecuta cuando la sesion comienza o se reanuda. Puede persistir variables de entorno.

**Matchers:** `startup`, `resume`, `clear`, `compact`

**Funcion especial:** Usa `CLAUDE_ENV_FILE` para persistir variables de entorno (tambien disponible en los hooks `CwdChanged` y `FileChanged`):

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### SessionEnd

Se ejecuta cuando la sesion termina para realizar limpieza o registro final. No puede bloquear la terminacion.

**Valores del campo reason:**
- `clear` - El usuario limpio la sesion
- `logout` - El usuario cerro sesion
- `prompt_input_exit` - El usuario salio mediante la entrada de prompt
- `other` - Otro motivo

**Configuracion:**
```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-cleanup.sh\""
          }
        ]
      }
    ]
  }
}
```

### Evento Notification

Matchers actualizados para eventos de notificacion:
- `permission_prompt` - Notificacion de solicitud de permiso
- `idle_prompt` - Notificacion de estado inactivo
- `auth_success` - Exito de autenticacion
- `elicitation_dialog` - Dialogo mostrado al usuario

## Hooks con ambito de componente

Los hooks pueden adjuntarse a componentes especificos (skills, agentes, commands) en su frontmatter:

**En SKILL.md, agent.md, o command.md:**

```yaml
---
name: secure-operations
description: Perform operations with security checks
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/check.sh"
          once: true  # Only run once per session
---
```

**Eventos soportados para hooks de componente:** `PreToolUse`, `PostToolUse`, `Stop`

Esto permite definir hooks directamente en el componente que los usa, manteniendo el codigo relacionado junto.

### Hooks en frontmatter de subagente

Cuando un hook `Stop` esta definido en el frontmatter de un subagente, se convierte automaticamente en un hook `SubagentStop` con alcance a ese subagente. Esto asegura que el hook de stop solo se active cuando ese subagente especifico se complete, en lugar de cuando la sesion principal se detenga.

```yaml
---
name: code-review-agent
description: Automated code review subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verify the code review is thorough and complete."
  # The above Stop hook auto-converts to SubagentStop for this subagent
---
```

## Evento PermissionRequest

Maneja solicitudes de permisos con formato de salida personalizado:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow|deny",
      "updatedInput": {},
      "message": "Custom message",
      "interrupt": false
    }
  }
}
```

## Entrada y salida de hooks

### Entrada JSON (via stdin)

Todos los hooks reciben entrada JSON via stdin:

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.js",
    "content": "..."
  },
  "tool_use_id": "toolu_01ABC123...",
  "agent_id": "agent-abc123",
  "agent_type": "main",
  "worktree": "/path/to/worktree"
}
```

**Campos comunes:**

| Campo | Descripcion |
|-------|-------------|
| `session_id` | Identificador unico de la sesion |
| `transcript_path` | Ruta al archivo de transcripcion de la conversacion |
| `cwd` | Directorio de trabajo actual |
| `hook_event_name` | Nombre del evento que activo el hook |
| `agent_id` | Identificador del agente que ejecuta este hook |
| `agent_type` | Tipo de agente (`"main"`, nombre del tipo de subagente, etc.) |
| `worktree` | Ruta al worktree de git, si el agente esta ejecutandose en uno |

### Codigos de salida

| Codigo de salida | Significado | Comportamiento |
|-----------|---------|----------|
| **0** | Exito | Continuar, analizar JSON en stdout |
| **2** | Error bloqueante | Bloquear la operacion, stderr se muestra como error |
| **Otro** | Error no bloqueante | Continuar, stderr se muestra en modo verbose |

### Salida JSON (stdout, codigo de salida 0)

```json
{
  "continue": true,
  "stopReason": "Optional message if stopping",
  "suppressOutput": false,
  "systemMessage": "Optional warning message",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "File is in allowed directory",
    "updatedInput": {
      "file_path": "/modified/path.js"
    }
  }
}
```

## Variables de entorno

| Variable | Disponibilidad | Descripcion |
|----------|-------------|-------------|
| `CLAUDE_PROJECT_DIR` | Todos los hooks | Ruta absoluta a la raiz del proyecto |
| `CLAUDE_ENV_FILE` | SessionStart, CwdChanged, FileChanged | Ruta de archivo para persistir variables de entorno |
| `CLAUDE_CODE_REMOTE` | Todos los hooks | `"true"` si se ejecuta en entornos remotos |
| `${CLAUDE_PLUGIN_ROOT}` | Hooks de plugin | Ruta al directorio del plugin |
| `${CLAUDE_PLUGIN_DATA}` | Hooks de plugin | Ruta al directorio de datos del plugin |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | Hooks de SessionEnd | Timeout configurable en milisegundos para hooks de SessionEnd (reemplaza el valor por defecto) |

## Hooks basados en prompt

Para los eventos `Stop` y `SubagentStop`, puedes usar evaluacion basada en LLM:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if all tasks are complete. Return your decision.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**Schema de respuesta del LLM:**
```json
{
  "decision": "approve",
  "reason": "All tasks completed successfully",
  "continue": false,
  "stopReason": "Task complete"
}
```

## Ejemplos

### Ejemplo 1: Validador de comandos Bash (PreToolUse)

**Archivo:** `.claude/hooks/validate-bash.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"\brm\s+-rf\s+/", "Blocking dangerous rm -rf / command"),
    (r"\bsudo\s+rm", "Blocking sudo rm command"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name != "Bash":
        sys.exit(0)

    command = input_data.get("tool_input", {}).get("command", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, command):
            print(message, file=sys.stderr)
            sys.exit(2)  # Exit 2 = blocking error

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**Configuracion:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\""
          }
        ]
      }
    ]
  }
}
```

### Ejemplo 2: Escaner de seguridad (PostToolUse)

**Archivo:** `.claude/hooks/security-scan.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

SECRET_PATTERNS = [
    (r"password\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded password"),
    (r"api[_-]?key\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded API key"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})
    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    file_path = tool_input.get("file_path", "")

    warnings = []
    for pattern, message in SECRET_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            warnings.append(message)

    if warnings:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"Security warnings for {file_path}: " + "; ".join(warnings)
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### Ejemplo 3: Auto-formateo de codigo (PostToolUse)

**Archivo:** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# Read JSON from stdin
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# Format based on file extension
case "$FILE_PATH" in
    *.js|*.jsx|*.ts|*.tsx|*.json)
        command -v prettier &>/dev/null && prettier --write "$FILE_PATH" 2>/dev/null
        ;;
    *.py)
        command -v black &>/dev/null && black "$FILE_PATH" 2>/dev/null
        ;;
    *.go)
        command -v gofmt &>/dev/null && gofmt -w "$FILE_PATH" 2>/dev/null
        ;;
esac

exit 0
```

### Ejemplo 4: Validador de prompts (UserPromptSubmit)

**Archivo:** `.claude/hooks/validate-prompt.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"delete\s+(all\s+)?database", "Dangerous: database deletion"),
    (r"rm\s+-rf\s+/", "Dangerous: root deletion"),
]

def main():
    input_data = json.load(sys.stdin)
    prompt = input_data.get("user_prompt", "") or input_data.get("prompt", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            output = {
                "decision": "block",
                "reason": f"Blocked: {message}"
            }
            print(json.dumps(output))
            sys.exit(0)

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### Ejemplo 5: Hook de stop inteligente (basado en prompt)

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if Claude completed all requested tasks. Check: 1) Were all files created/modified? 2) Were there unresolved errors? If incomplete, explain what's missing.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### Ejemplo 6: Rastreador de uso de contexto (pares de hooks)

Rastrea el consumo de tokens por solicitud usando los hooks `UserPromptSubmit` (pre-mensaje) y `Stop` (post-respuesta) juntos.

**Archivo:** `.claude/hooks/context-tracker.py`

```python
#!/usr/bin/env python3
"""
Context Usage Tracker - Tracks token consumption per request.

Uses UserPromptSubmit as "pre-message" hook and Stop as "post-response" hook
to calculate the delta in token usage for each request.

Token Counting Methods:
1. Character estimation (default): ~4 chars per token, no dependencies
2. tiktoken (optional): More accurate (~90-95%), requires: pip install tiktoken
"""
import json
import os
import sys
import tempfile

# Configuration
CONTEXT_LIMIT = 128000  # Claude's context window (adjust for your model)
USE_TIKTOKEN = False    # Set True if tiktoken is installed for better accuracy


def get_state_file(session_id: str) -> str:
    """Get temp file path for storing pre-message token count, isolated by session."""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    Count tokens in text.

    Uses tiktoken with p50k_base encoding if available (~90-95% accuracy),
    otherwise falls back to character estimation (~80-90% accuracy).
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # Fall back to estimation

    # Character-based estimation: ~4 characters per token for English
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """Read and concatenate all content from transcript file."""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # Extract text content from various message formats
                if "message" in entry:
                    msg = entry["message"]
                    if isinstance(msg.get("content"), str):
                        content.append(msg["content"])
                    elif isinstance(msg.get("content"), list):
                        for block in msg["content"]:
                            if isinstance(block, dict) and block.get("type") == "text":
                                content.append(block.get("text", ""))
            except json.JSONDecodeError:
                continue

    return "\n".join(content)


def handle_user_prompt_submit(data: dict) -> None:
    """Pre-message hook: Save current token count before request."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # Save to temp file for later comparison
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """Post-response hook: Calculate and report token delta."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # Load pre-message count
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # Calculate delta
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # Report usage
    method = "tiktoken" if USE_TIKTOKEN else "estimated"
    print(f"Context ({method}): ~{current_tokens:,} tokens ({percentage:.1f}% used, ~{remaining:,} remaining)", file=sys.stderr)
    if delta_tokens > 0:
        print(f"This request: ~{delta_tokens:,} tokens", file=sys.stderr)


def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name", "")

    if event == "UserPromptSubmit":
        handle_user_prompt_submit(data)
    elif event == "Stop":
        handle_stop(data)

    sys.exit(0)


if __name__ == "__main__":
    main()
```

**Configuracion:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ]
  }
}
```

**Como funciona:**
1. `UserPromptSubmit` se activa antes de que tu prompt sea procesado: guarda el conteo de tokens actual
2. `Stop` se activa despues de que Claude responde: calcula el delta e informa el uso
3. Cada sesion esta aislada via `session_id` en el nombre del archivo temporal

**Metodos de conteo de tokens:**

| Metodo | Precision | Dependencias | Velocidad |
|--------|----------|--------------|-------|
| Estimacion por caracteres | ~80-90% | Ninguna | <1ms |
| tiktoken (p50k_base) | ~90-95% | `pip install tiktoken` | <10ms |

> **Nota:** Anthropic no ha lanzado un tokenizador offline oficial. Ambos metodos son aproximaciones. La transcripcion incluye prompts del usuario, respuestas de Claude y salidas de herramientas, pero NO prompts de sistema ni contexto interno.

### Ejemplo 7: Script de configuracion de permisos en modo auto (ejecucion unica)

Un script de configuracion de una sola vez que inicializa `~/.claude/settings.json` con ~67 reglas de permisos seguras equivalentes al modo auto de Claude Code, sin ningun hook, sin recordar opciones futuras. Ejecutalo una vez; es seguro volver a ejecutarlo (omite reglas ya presentes).

**Archivo:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Preview what would be added
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Apply
python3 09-advanced-features/setup-auto-mode-permissions.py
```

**Que se agrega:**

| Categoria | Ejemplos |
|----------|---------|
| Herramientas integradas | `Read(*)`, `Edit(*)`, `Write(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)` |
| Git solo lectura | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)` |
| Git escritura (local) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Gestores de paquetes | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| Build y tests | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Shell comun | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

**Que esta intencionalmente excluido** (nunca lo agrega este script):
- `rm -rf`, `sudo`, force push, `git reset --hard`
- `DROP TABLE`, `kubectl delete`, `terraform destroy`
- `npm publish`, `curl | bash`, despliegues a produccion

## Hooks de plugin

Los plugins pueden incluir hooks en su archivo `hooks/hooks.json`:

**Archivo:** `plugins/hooks/hooks.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh"
          }
        ]
      }
    ]
  }
}
```

**Variables de entorno en hooks de plugin:**
- `${CLAUDE_PLUGIN_ROOT}` - Ruta al directorio del plugin
- `${CLAUDE_PLUGIN_DATA}` - Ruta al directorio de datos del plugin

Esto permite que los plugins incluyan validacion personalizada y hooks de automatizacion.

## Hooks de herramientas MCP

Las herramientas MCP siguen el patron `mcp__<server>__<tool>`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"systemMessage\": \"Memory operation logged\"}'"
          }
        ]
      }
    ]
  }
}
```

## Consideraciones de seguridad

### Aviso

**USAR BAJO TU PROPIA RESPONSABILIDAD**: Los hooks ejecutan comandos de shell arbitrarios. Eres el unico responsable de:
- Los comandos que configures
- Los permisos de acceso/modificacion de archivos
- La posible perdida de datos o daños al sistema
- Probar los hooks en entornos seguros antes de usarlos en produccion

### Notas de seguridad

- **Se requiere confianza en el espacio de trabajo:** Los comandos de salida de hook `statusLine` y `fileSuggestion` ahora requieren la aceptacion de confianza en el espacio de trabajo antes de que surtan efecto.
- **Hooks HTTP y variables de entorno:** Los HTTP hooks requieren una lista explicita `allowedEnvVars` para usar la interpolacion de variables de entorno en las URLs. Esto previene la filtracion accidental de variables de entorno sensibles a endpoints remotos.
- **Jerarquia de settings administrados:** La configuracion `disableAllHooks` ahora respeta la jerarquia de settings administrados, lo que significa que los settings a nivel de organizacion pueden forzar la deshabilitacion de hooks que los usuarios individuales no pueden anular.

### Buenas practicas

| Hacer | No hacer |
|-----|-------|
| Validar y sanitizar todas las entradas | Confiar ciegamente en los datos de entrada |
| Entrecomillar variables de shell: `"$VAR"` | Usar sin comillas: `$VAR` |
| Bloquear recorrido de rutas (`..`) | Permitir rutas arbitrarias |
| Usar rutas absolutas con `$CLAUDE_PROJECT_DIR` | Usar rutas hardcodeadas |
| Omitir archivos sensibles (`.env`, `.git/`, keys) | Procesar todos los archivos |
| Probar hooks de forma aislada primero | Desplegar hooks sin probar |
| Usar `allowedEnvVars` explicito para HTTP hooks | Exponer todas las variables de entorno a webhooks |

## Depuracion

### Habilitar modo debug

Ejecuta Claude con el flag de debug para logs detallados de hooks:

```bash
claude --debug
```

### Modo verbose

Usa `Ctrl+O` en Claude Code para habilitar el modo verbose y ver el progreso de ejecucion de los hooks.

### Probar hooks de forma independiente

```bash
# Test with sample JSON input
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# Check exit code
echo $?
```

## Ejemplo de configuracion completo

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/format-code.sh\"",
            "timeout": 30
          },
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py\""
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-init.sh\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Verify all tasks are complete before stopping.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Detalles de ejecucion de hooks

| Aspecto | Comportamiento |
|--------|----------|
| **Timeout** | 60 segundos por defecto, configurable por comando |
| **Paralelizacion** | Todos los hooks que coincidan se ejecutan en paralelo |
| **Deduplicacion** | Los comandos de hook identicos se deduplicam |
| **Entorno** | Se ejecuta en el directorio actual con el entorno de Claude Code |

## Solucion de problemas

### El hook no se ejecuta
- Verificar que la sintaxis de la configuracion JSON sea correcta
- Comprobar que el patron del matcher coincide con el nombre de la herramienta
- Asegurarse de que el script exista y sea ejecutable: `chmod +x script.sh`
- Ejecutar `claude --debug` para ver los logs de ejecucion del hook
- Verificar que el hook lee JSON desde stdin (no como argumentos del comando)

### El hook bloquea inesperadamente
- Probar el hook con JSON de muestra: `echo '{"tool_name": "Write", ...}' | ./hook.py`
- Comprobar el codigo de salida: debe ser 0 para permitir, 2 para bloquear
- Revisar la salida stderr (se muestra con el codigo de salida 2)

### Errores de analisis JSON
- Siempre leer desde stdin, no desde argumentos del comando
- Usar analisis JSON adecuado (no manipulacion de cadenas)
- Manejar campos faltantes de forma elegante

## Instalacion

### Paso 1: Crear el directorio de hooks
```bash
mkdir -p ~/.claude/hooks
```

### Paso 2: Copiar los hooks de ejemplo
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### Paso 3: Configurar en settings

Edita `~/.claude/settings.json` o `.claude/settings.json` con la configuracion de hooks mostrada arriba.

## Conceptos relacionados

- **[Checkpoints y Rewind](../08-checkpoints/)** - Guardar y restaurar el estado de la conversacion
- **[Slash Commands](../01-slash-commands/)** - Crear slash commands personalizados
- **[Skills](../03-skills/)** - Capacidades autonomas reutilizables
- **[Subagents](../04-subagents/)** - Ejecucion delegada de tareas
- **[Plugins](../07-plugins/)** - Paquetes de extension integrados
- **[Advanced Features](../09-advanced-features/)** - Explorar capacidades avanzadas de Claude Code

## Recursos adicionales

- **[Documentacion oficial de Hooks](https://code.claude.com/docs/en/hooks)** - Referencia completa de hooks
- **[Referencia del CLI](https://code.claude.com/docs/en/cli-reference)** - Documentacion de la interfaz de linea de comandos
- **[Guia de Memory](../02-memory/)** - Configuracion de contexto persistente

---
**Ultima Actualizacion**: Abril 2026
**Version de Claude Code**: 2.1+
**Modelos compatibles**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
