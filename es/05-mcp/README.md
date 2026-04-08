<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (Model Context Protocol)

Esta carpeta contiene documentación completa y ejemplos de configuraciones y uso de servidores MCP con Claude Code.

## Descripcion general

MCP (Model Context Protocol) es una forma estandarizada de que Claude acceda a herramientas externas, APIs y fuentes de datos en tiempo real. A diferencia de Memory, MCP proporciona acceso en vivo a datos que cambian.

Caracteristicas clave:
- Acceso en tiempo real a servicios externos
- Sincronizacion de datos en vivo
- Arquitectura extensible
- Autenticacion segura
- Interacciones basadas en herramientas

## Arquitectura MCP

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
```

## Ecosistema MCP

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["Local Files"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Slack Workspace"]
    F -->|Docs| K["Google Drive"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#f3e5f5,stroke:#333,color:#333
    style G fill:#e8f5e9,stroke:#333,color:#333
    style H fill:#e8f5e9,stroke:#333,color:#333
    style I fill:#e8f5e9,stroke:#333,color:#333
    style J fill:#e8f5e9,stroke:#333,color:#333
    style K fill:#e8f5e9,stroke:#333,color:#333
```

## Metodos de instalacion MCP

Claude Code soporta multiples protocolos de transporte para las conexiones de servidor MCP:

### Transporte HTTP (Recomendado)

```bash
# Conexion HTTP basica
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP con header de autenticacion
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Transporte Stdio (Local)

Para servidores MCP que se ejecutan localmente:

```bash
# Servidor Node.js local
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# Con variables de entorno
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

### Transporte SSE (Deprecado)

El transporte Server-Sent Events esta deprecado en favor de `http` pero sigue siendo compatible:

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### Transporte WebSocket

Transporte WebSocket para conexiones bidireccionales persistentes:

```bash
claude mcp add --transport ws realtime-server wss://example.com/mcp
```

### Nota especifica para Windows

En Windows nativo (no WSL), usa `cmd /c` para los comandos npx:

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### Autenticacion OAuth 2.0

Claude Code soporta OAuth 2.0 para servidores MCP que lo requieran. Al conectarse a un server con OAuth habilitado, Claude Code maneja todo el flujo de autenticacion:

```bash
# Conectar a un servidor MCP con OAuth habilitado (flujo interactivo)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# Preconfigurar credenciales OAuth para configuracion no interactiva
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| Caracteristica | Descripcion |
|---------|-------------|
| **OAuth interactivo** | Usa `/mcp` para iniciar el flujo OAuth basado en navegador |
| **Clientes OAuth preconfigurados** | Clientes OAuth integrados para servicios comunes como Notion, Stripe y otros (v2.1.30+) |
| **Credenciales preconfiguradas** | Flags `--client-id`, `--client-secret`, `--callback-port` para configuracion automatizada |
| **Almacenamiento de tokens** | Los tokens se guardan de forma segura en el keychain del sistema |
| **Step-up auth** | Soporta autenticacion escalonada para operaciones privilegiadas |
| **Caching de descubrimiento** | Los metadatos de descubrimiento OAuth se almacenan en cache para reconexiones mas rapidas |
| **Override de metadatos** | `oauth.authServerMetadataUrl` en `.mcp.json` para reemplazar el descubrimiento de metadatos OAuth por defecto |

#### Reemplazar el descubrimiento de metadatos OAuth

Si tu servidor MCP devuelve errores en el endpoint estandar de metadatos OAuth (`/.well-known/oauth-authorization-server`) pero expone un endpoint OIDC funcional, puedes indicarle a Claude Code que obtenga los metadatos OAuth desde una URL especifica. Configura `authServerMetadataUrl` en el objeto `oauth` de la configuracion del server:

```json
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "authServerMetadataUrl": "https://auth.example.com/.well-known/openid-configuration"
      }
    }
  }
}
```

La URL debe usar `https://`. Esta opcion requiere Claude Code v2.1.64 o posterior.

### Conectores MCP de Claude.ai

Los servidores MCP configurados en tu cuenta de Claude.ai estan disponibles automaticamente en Claude Code. Esto significa que cualquier conexion MCP que configures a traves de la interfaz web de Claude.ai sera accesible sin configuracion adicional.

Los conectores MCP de Claude.ai tambien estan disponibles en modo `--print` (v2.1.83+), habilitando el uso no interactivo y con scripts.

Para deshabilitar los servidores MCP de Claude.ai en Claude Code, establece la variable de entorno `ENABLE_CLAUDEAI_MCP_SERVERS` en `false`:

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **Nota:** Esta funcion solo esta disponible para usuarios que hayan iniciado sesion con cuentas Claude.ai.

## Proceso de configuracion MCP

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as External Service

    User->>Claude: Type /mcp
    Claude->>Claude: List available MCP servers
    Claude->>User: Show options
    User->>Claude: Select GitHub MCP
    Claude->>Config: Update configuration
    Config->>Claude: Activate connection
    Claude->>Service: Test connection
    Service-->>Claude: Authentication successful
    Claude->>User: ✅ MCP connected!
```

## Busqueda de herramientas MCP

Cuando las descripciones de herramientas MCP superan el 10% de la ventana de contexto, Claude Code habilita automaticamente la busqueda de herramientas para seleccionar las correctas de forma eficiente sin sobrecargar el contexto del modelo.

| Configuracion | Valor | Descripcion |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | `auto` (defecto) | Se habilita automaticamente cuando las descripciones de herramientas superan el 10% del contexto |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | Se habilita automaticamente con un umbral personalizado de `N` herramientas |
| `ENABLE_TOOL_SEARCH` | `true` | Siempre habilitado independientemente del numero de herramientas |
| `ENABLE_TOOL_SEARCH` | `false` | Deshabilitado; todas las descripciones de herramientas se envian completas |

> **Nota:** La busqueda de herramientas requiere Sonnet 4 o posterior, u Opus 4 o posterior. Los modelos Haiku no son compatibles con la busqueda de herramientas.

## Actualizaciones dinamicas de herramientas

Claude Code soporta notificaciones `list_changed` de MCP. Cuando un servidor MCP agrega, elimina o modifica dinamicamente sus herramientas disponibles, Claude Code recibe la actualizacion y ajusta su lista de herramientas automaticamente, sin necesidad de reconexion ni reinicio.

## MCP Apps

MCP Apps es la primera extension oficial de MCP, que permite que las llamadas a herramientas MCP devuelvan componentes de interfaz interactivos que se renderizan directamente en la interfaz de chat. En lugar de respuestas en texto plano, los servidores MCP pueden entregar dashboards enriquecidos, formularios, visualizaciones de datos y workflows de varios pasos, todo mostrado en linea sin salir de la conversacion.

## Elicitacion MCP

Los servidores MCP pueden solicitar entradas estructuradas del usuario mediante dialogos interactivos (v2.1.49+). Esto permite que un servidor MCP pida informacion adicional durante un workflow, por ejemplo solicitar una confirmacion, seleccionar entre una lista de opciones o completar campos requeridos, agregando interactividad a las interacciones con servidores MCP.

## Limite de descripciones de herramientas e instrucciones

A partir de la v2.1.84, Claude Code aplica un **limite de 2 KB** en las descripciones de herramientas e instrucciones por servidor MCP. Esto evita que servidores individuales consuman contexto excesivo con definiciones de herramientas demasiado verbosas, reduciendo el ruido en el contexto y manteniendo las interacciones eficientes.

## Prompts MCP como slash commands

Los servidores MCP pueden exponer prompts que aparecen como slash commands en Claude Code. Los prompts son accesibles usando la convencion de nombres:

```
/mcp__<server>__<prompt>
```

Por ejemplo, si un server llamado `github` expone un prompt llamado `review`, puedes invocarlo como `/mcp__github__review`.

## Deduplicacion de servidores

Cuando el mismo servidor MCP esta definido en multiples ambitos (local, proyecto, usuario), la configuracion local tiene precedencia. Esto te permite reemplazar configuraciones MCP a nivel de proyecto o usuario con personalizaciones locales sin conflictos.

## Recursos MCP mediante menciones @

Puedes referenciar recursos MCP directamente en tus prompts usando la sintaxis de mencion `@`:

```
@server-name:protocol://resource/path
```

Por ejemplo, para referenciar un recurso de base de datos especifico:

```
@database:postgres://mydb/users
```

Esto permite que Claude obtenga e incluya el contenido del recurso MCP en linea como parte del contexto de la conversacion.

## Ambitos MCP

Las configuraciones MCP pueden almacenarse en diferentes ambitos con distintos niveles de comparticion:

| Ambito | Ubicacion | Descripcion | Compartido con | Requiere aprobacion |
|-------|----------|-------------|-------------|------------------|
| **Local** (defecto) | `~/.claude.json` (bajo la ruta del proyecto) | Privado al usuario actual, solo para el proyecto actual (se llamaba `project` en versiones anteriores) | Solo vos | No |
| **Project** | `.mcp.json` | Incorporado al repositorio git | Miembros del equipo | Si (primer uso) |
| **User** | `~/.claude.json` | Disponible en todos los proyectos (se llamaba `global` en versiones anteriores) | Solo vos | No |

### Usar el ambito Project

Guarda las configuraciones MCP especificas del proyecto en `.mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.github.com/mcp"
    }
  }
}
```

Los miembros del equipo veran un prompt de aprobacion la primera vez que usen los MCP del proyecto.

## Gestion de configuracion MCP

### Agregar servidores MCP

```bash
# Agregar servidor basado en HTTP
claude mcp add --transport http github https://api.github.com/mcp

# Agregar servidor stdio local
claude mcp add --transport stdio database -- npx @company/db-server

# Listar todos los servidores MCP
claude mcp list

# Obtener detalles de un servidor especifico
claude mcp get github

# Eliminar un servidor MCP
claude mcp remove github

# Resetear las opciones de aprobacion especificas del proyecto
claude mcp reset-project-choices

# Importar desde Claude Desktop
claude mcp add-from-claude-desktop
```

## Tabla de servidores MCP disponibles

| Servidor MCP | Proposito | Herramientas comunes | Auth | Tiempo real |
|------------|---------|--------------|------|-----------|
| **Filesystem** | Operaciones de archivos | read, write, delete | Permisos del SO | ✅ Si |
| **GitHub** | Gestion de repositorios | list_prs, create_issue, push | OAuth | ✅ Si |
| **Slack** | Comunicacion de equipo | send_message, list_channels | Token | ✅ Si |
| **Database** | Consultas SQL | query, insert, update | Credenciales | ✅ Si |
| **Google Docs** | Acceso a documentos | read, write, share | OAuth | ✅ Si |
| **Asana** | Gestion de proyectos | create_task, update_status | API Key | ✅ Si |
| **Stripe** | Datos de pagos | list_charges, create_invoice | API Key | ✅ Si |
| **Memory** | Memoria persistente | store, retrieve, delete | Local | ❌ No |

## Ejemplos practicos

### Ejemplo 1: Configuracion de GitHub MCP

**Archivo:** `.mcp.json` (raiz del proyecto)

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Herramientas disponibles en GitHub MCP:**

#### Gestion de Pull Requests
- `list_prs` - Lista todos los PRs en el repositorio
- `get_pr` - Obtiene detalles del PR incluyendo el diff
- `create_pr` - Crea un nuevo PR
- `update_pr` - Actualiza la descripcion/titulo del PR
- `merge_pr` - Fusiona el PR a la rama principal
- `review_pr` - Agrega comentarios de revision

**Ejemplo de solicitud:**
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### Gestion de Issues
- `list_issues` - Lista todos los issues
- `get_issue` - Obtiene detalles de un issue
- `create_issue` - Crea un nuevo issue
- `close_issue` - Cierra un issue
- `add_comment` - Agrega un comentario a un issue

#### Informacion del repositorio
- `get_repo_info` - Detalles del repositorio
- `list_files` - Estructura del arbol de archivos
- `get_file_content` - Lee el contenido de un archivo
- `search_code` - Busca en todo el codigo

#### Operaciones de commit
- `list_commits` - Historial de commits
- `get_commit` - Detalles de un commit especifico
- `create_commit` - Crea un nuevo commit

**Configuracion**:
```bash
export GITHUB_TOKEN="your_github_token"
# O usa el CLI para agregar directamente:
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

### Expansion de variables de entorno en la configuracion

Las configuraciones MCP soportan expansion de variables de entorno con valores por defecto de respaldo. La sintaxis `${VAR}` y `${VAR:-default}` funciona en los siguientes campos: `command`, `args`, `env`, `url` y `headers`.

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}",
        "X-Custom-Header": "${CUSTOM_HEADER:-default-value}"
      }
    },
    "local-server": {
      "command": "${MCP_BIN_PATH:-npx}",
      "args": ["${MCP_PACKAGE:-@company/mcp-server}"],
      "env": {
        "DB_URL": "${DATABASE_URL:-postgresql://localhost/dev}"
      }
    }
  }
}
```

Las variables se expanden en tiempo de ejecucion:
- `${VAR}` - Usa la variable de entorno, error si no esta definida
- `${VAR:-default}` - Usa la variable de entorno, cae al valor por defecto si no esta definida

### Ejemplo 2: Configuracion de base de datos MCP

**Configuracion:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-database"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

**Ejemplo de uso:**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# Using MCP database tool:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Results:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

**Configuracion**:
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# O usa el CLI para agregar directamente:
claude mcp add --transport stdio database -- npx @modelcontextprotocol/server-database
```

### Ejemplo 3: Workflow con multiples MCPs

**Escenario: Generacion de reporte diario**

```markdown
# Daily Report Workflow using Multiple MCPs

## Setup
1. GitHub MCP - fetch PR metrics
2. Database MCP - query sales data
3. Slack MCP - post report
4. Filesystem MCP - save report

## Workflow

### Step 1: Fetch GitHub Data
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Step 2: Query Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Step 3: Generate Report
Combine data into HTML report

### Step 4: Save to Filesystem
Write report.html to /reports/

### Step 5: Post to Slack
Send summary to #daily-reports channel

Final Output:
✅ Report generated and posted
📊 47 PRs merged this week
💰 $12,450 in daily sales
```

**Configuracion**:
```bash
export GITHUB_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="your_slack_token"
# Add each MCP server via the CLI or configure them in .mcp.json
```

### Ejemplo 4: Operaciones con Filesystem MCP

**Configuracion:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    }
  }
}
```

**Operaciones disponibles:**

| Operacion | Comando | Proposito |
|-----------|---------|---------|
| Listar archivos | `ls ~/projects` | Mostrar contenido del directorio |
| Leer archivo | `cat src/main.ts` | Leer contenido de un archivo |
| Escribir archivo | `create docs/api.md` | Crear nuevo archivo |
| Editar archivo | `edit src/app.ts` | Modificar archivo |
| Buscar | `grep "async function"` | Buscar en archivos |
| Eliminar | `rm old-file.js` | Eliminar archivo |

**Configuracion**:
```bash
# Usa el CLI para agregar directamente:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## MCP vs Memory: Matriz de decision

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

## Patron de solicitud/respuesta

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
    App->>App: Process result
    App->>App: Continue task

    Note over MCP,DB: Real-time access<br/>No caching
```

## Variables de entorno

Almacena las credenciales sensibles en variables de entorno:

```bash
# ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

Luego referenciadas en la config MCP:

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## Claude como servidor MCP (`claude mcp serve`)

Claude Code puede actuar como servidor MCP para otras aplicaciones. Esto permite que herramientas externas, editores y sistemas de automatizacion aprovechen las capacidades de Claude a traves del protocolo MCP estandar.

```bash
# Iniciar Claude Code como servidor MCP en stdio
claude mcp serve
```

Otras aplicaciones pueden entonces conectarse a este server como lo harian con cualquier servidor MCP basado en stdio. Por ejemplo, para agregar Claude Code como servidor MCP en otra instancia de Claude Code:

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

Esto es util para construir workflows multiagente donde una instancia de Claude orquesta a otra.

## Configuracion MCP administrada (Enterprise)

Para despliegues empresariales, los administradores de IT pueden aplicar politicas de servidor MCP a traves del archivo de configuracion `managed-mcp.json`. Este archivo proporciona control exclusivo sobre que servidores MCP estan permitidos o bloqueados a nivel de toda la organizacion.

**Ubicacion:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `~/.config/ClaudeCode/managed-mcp.json`
- Windows: `%APPDATA%\ClaudeCode\managed-mcp.json`

**Caracteristicas:**
- `allowedMcpServers` -- lista blanca de servidores permitidos
- `deniedMcpServers` -- lista negra de servidores prohibidos
- Soporta coincidencia por nombre de server, comando y patrones de URL
- Politicas MCP a nivel de organizacion aplicadas antes que la configuracion del usuario
- Previene conexiones a servidores no autorizados

**Configuracion de ejemplo:**

```json
{
  "allowedMcpServers": [
    {
      "serverName": "github",
      "serverUrl": "https://api.github.com/mcp"
    },
    {
      "serverName": "company-internal",
      "serverCommand": "company-mcp-server"
    }
  ],
  "deniedMcpServers": [
    {
      "serverName": "untrusted-*"
    },
    {
      "serverUrl": "http://*"
    }
  ]
}
```

> **Nota:** Cuando tanto `allowedMcpServers` como `deniedMcpServers` coinciden con un server, la regla de denegacion tiene precedencia.

## Servidores MCP provistos por plugins

Los plugins pueden incluir sus propios servidores MCP, haciendolos disponibles automaticamente cuando el plugin esta instalado. Los servidores MCP provistos por plugins pueden definirse de dos formas:

1. **`.mcp.json` independiente** -- Coloca un archivo `.mcp.json` en el directorio raiz del plugin
2. **Inline en `plugin.json`** -- Define servidores MCP directamente dentro del manifiesto del plugin

Usa la variable `${CLAUDE_PLUGIN_ROOT}` para referenciar rutas relativas al directorio de instalacion del plugin:

```json
{
  "mcpServers": {
    "plugin-tools": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/dist/mcp-server.js"],
      "env": {
        "CONFIG_PATH": "${CLAUDE_PLUGIN_ROOT}/config.json"
      }
    }
  }
}
```

## MCP con ambito de subagente

Los servidores MCP pueden definirse inline dentro del frontmatter de un agente usando la clave `mcpServers:`, limitando su alcance a un subagente especifico en lugar de todo el proyecto. Esto es util cuando un agente necesita acceso a un servidor MCP particular que otros agentes del workflow no requieren.

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

Los servidores MCP con ambito de subagente solo estan disponibles dentro del contexto de ejecucion de ese agente y no se comparten con los agentes padre o hermanos.

## Limites de salida MCP

Claude Code aplica limites en la salida de herramientas MCP para prevenir el desbordamiento del contexto:

| Limite | Umbral | Comportamiento |
|-------|-----------|----------|
| **Advertencia** | 10.000 tokens | Se muestra una advertencia de que la salida es grande |
| **Maximo por defecto** | 25.000 tokens | La salida se trunca mas alla de este limite |
| **Persistencia en disco** | 50.000 caracteres | Los resultados de herramientas que superan 50K caracteres se guardan en disco |

El limite maximo de salida es configurable mediante la variable de entorno `MAX_MCP_OUTPUT_TOKENS`:

```bash
# Aumentar el maximo de salida a 50.000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

## Resolviendo el problema del contexto saturado con ejecucion de codigo

A medida que la adopcion de MCP escala, conectarse a docenas de servidores con cientos o miles de herramientas crea un desafio significativo: **saturacion del contexto**. Este es posiblemente el mayor problema con MCP a escala, y el equipo de ingenieria de Anthropic ha propuesto una solucion elegante: usar ejecucion de codigo en lugar de llamadas directas a herramientas.

> **Fuente**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — Blog de Ingenieria de Anthropic

### El problema: dos fuentes de desperdicio de tokens

**1. Las definiciones de herramientas sobrecargan la ventana de contexto**

La mayoria de los clientes MCP cargan todas las definiciones de herramientas al inicio. Al conectarse a miles de herramientas, el modelo debe procesar cientos de miles de tokens antes siquiera de leer la solicitud del usuario.

**2. Los resultados intermedios consumen tokens adicionales**

Cada resultado intermedio de herramienta pasa por el contexto del modelo. Considera transferir una transcripcion de reunion de Google Drive a Salesforce: la transcripcion completa fluye por el contexto **dos veces**: una al leerla, y otra al escribirla en el destino. Una transcripcion de 2 horas puede significar mas de 50.000 tokens adicionales.

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### La solucion: herramientas MCP como APIs de codigo

En lugar de pasar definiciones de herramientas y resultados por la ventana de contexto, el agente **escribe codigo** que llama a herramientas MCP como APIs. El codigo se ejecuta en un entorno sandboxed, y solo el resultado final regresa al modelo.

```mermaid
graph LR
    A["Model"] -->|"Writes code"| B["Code Execution<br/>Environment"]
    B -->|"Calls tools directly"| C["MCP Servers"]
    C -->|"Data stays in<br/>execution env"| B
    B -->|"Only final result<br/>(minimal tokens)"| A

    style A fill:#c8e6c9,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
```

#### Como funciona

Las herramientas MCP se presentan como un arbol de archivos de funciones tipadas:

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
└── ...
```

Cada archivo de herramienta contiene un wrapper tipado:

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

export async function getDocument(
  input: GetDocumentInput
): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>(
    'google_drive__get_document', input
  );
}
```

El agente entonces escribe codigo para orquestar las herramientas:

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// Data flows directly between tools — never through the model
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**Resultado: el uso de tokens cae de ~150.000 a ~2.000, una reduccion del 98,7%.**

### Beneficios clave

| Beneficio | Descripcion |
|---------|-------------|
| **Divulgacion progresiva** | El agente navega el sistema de archivos para cargar solo las definiciones de herramientas que necesita, en lugar de todas al inicio |
| **Resultados eficientes en contexto** | Los datos se filtran/transforman en el entorno de ejecucion antes de volver al modelo |
| **Control de flujo potente** | Bucles, condicionales y manejo de errores se ejecutan en codigo sin viajes de ida y vuelta al modelo |
| **Preservacion de privacidad** | Los datos intermedios (PII, registros sensibles) permanecen en el entorno de ejecucion; nunca entran al contexto del modelo |
| **Persistencia de estado** | Los agentes pueden guardar resultados intermedios en archivos y construir funciones de skill reutilizables |

#### Ejemplo: filtrar conjuntos de datos grandes

```typescript
// Without code execution — all 10,000 rows flow through context
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> returns 10,000 rows in context

// With code execution — filter in the execution environment
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Only 5 rows reach the model
```

#### Ejemplo: bucle sin viajes de ida y vuelta

```typescript
// Poll for a deployment notification — runs entirely in code
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({
    channel: 'C123456'
  });
  found = messages.some(
    m => m.text.includes('deployment complete')
  );
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

### Compensaciones a considerar

La ejecucion de codigo introduce su propia complejidad. Ejecutar codigo generado por un agente requiere:

- Un **entorno de ejecucion sandboxed seguro** con limites de recursos apropiados
- **Monitoreo y registro** del codigo ejecutado
- **Infraestructura adicional** en comparacion con las llamadas directas a herramientas

Los beneficios (reduccion de costos en tokens, menor latencia, mejor composicion de herramientas) deben evaluarse frente a estos costos de implementacion. Para agentes con solo unos pocos servidores MCP, las llamadas directas a herramientas pueden ser mas simples. Para agentes a escala (docenas de servidores, cientos de herramientas), la ejecucion de codigo es una mejora significativa.

### MCPorter: un runtime para composicion de herramientas MCP

[MCPorter](https://github.com/steipete/mcporter) es un runtime TypeScript y un kit de herramientas CLI que hace practico llamar a servidores MCP sin boilerplate, y ayuda a reducir la saturacion del contexto mediante exposicion selectiva de herramientas y wrappers tipados.

**Que resuelve:** En lugar de cargar todas las definiciones de herramientas de todos los servidores MCP al inicio, MCPorter te permite descubrir, inspeccionar y llamar herramientas especificas bajo demanda, manteniendo tu contexto liviano.

**Caracteristicas clave:**

| Caracteristica | Descripcion |
|---------|-------------|
| **Descubrimiento sin configuracion** | Descubre automaticamente servidores MCP desde Cursor, Claude, Codex o configuraciones locales |
| **Clientes de herramientas tipados** | `mcporter emit-ts` genera interfaces `.d.ts` y wrappers listos para usar |
| **API composable** | `createServerProxy()` expone herramientas como metodos camelCase con helpers `.text()`, `.json()`, `.markdown()` |
| **Generacion de CLI** | `mcporter generate-cli` convierte cualquier servidor MCP en un CLI standalone con filtrado `--include-tools` / `--exclude-tools` |
| **Ocultamiento de parametros** | Los parametros opcionales permanecen ocultos por defecto, reduciendo la verbosidad del schema |

**Instalacion:**

```bash
npx mcporter list          # No install required — discover servers instantly
pnpm add mcporter          # Add to a project
brew install steipete/tap/mcporter  # macOS via Homebrew
```

**Ejemplo: composicion de herramientas en TypeScript:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// Data flows between tools without passing through the model context
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**Ejemplo: llamada a herramienta via CLI:**

```bash
# Call a specific tool directly
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# List available servers and tools
npx mcporter list
```

MCPorter complementa el enfoque de ejecucion de codigo descrito arriba proporcionando la infraestructura de runtime para llamar a herramientas MCP como APIs tipadas, haciendo sencillo mantener los datos intermedios fuera del contexto del modelo.

## Buenas practicas

### Consideraciones de seguridad

#### Hacer ✅
- Usar variables de entorno para todas las credenciales
- Rotar tokens y API keys regularmente (se recomienda mensualmente)
- Usar tokens de solo lectura cuando sea posible
- Limitar el alcance de acceso del servidor MCP al minimo necesario
- Monitorear el uso y los logs de acceso del servidor MCP
- Usar OAuth para servicios externos cuando este disponible
- Implementar limitacion de velocidad en las solicitudes MCP
- Probar las conexiones MCP antes de usarlas en produccion
- Documentar todas las conexiones MCP activas
- Mantener actualizados los paquetes del servidor MCP

#### No hacer ❌
- No incluir credenciales hardcodeadas en los archivos de configuracion
- No hacer commit de tokens o secretos en git
- No compartir tokens en chats de equipo o emails
- No usar tokens personales para proyectos de equipo
- No otorgar permisos innecesarios
- No ignorar errores de autenticacion
- No exponer endpoints MCP publicamente
- No ejecutar servidores MCP con privilegios root/admin
- No almacenar datos sensibles en logs
- No deshabilitar mecanismos de autenticacion

### Buenas practicas de configuracion

1. **Control de versiones**: Manten `.mcp.json` en git pero usa variables de entorno para los secretos
2. **Minimo privilegio**: Otorga los permisos minimos necesarios para cada servidor MCP
3. **Aislamiento**: Ejecuta diferentes servidores MCP en procesos separados cuando sea posible
4. **Monitoreo**: Registra todas las solicitudes y errores MCP para auditorias
5. **Pruebas**: Prueba todas las configuraciones MCP antes de desplegar a produccion

### Consejos de rendimiento

- Cachea los datos de acceso frecuente a nivel de la aplicacion
- Usa consultas MCP especificas para reducir la transferencia de datos
- Monitorea los tiempos de respuesta de las operaciones MCP
- Considera la limitacion de velocidad para APIs externas
- Usa operaciones en lote cuando se realizan multiples operaciones

## Instrucciones de instalacion

### Prerequisitos
- Node.js y npm instalados
- Claude Code CLI instalado
- Tokens/credenciales de API para servicios externos

### Configuracion paso a paso

1. **Agrega tu primer servidor MCP** usando el CLI (ejemplo: GitHub):
```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

   O crea un archivo `.mcp.json` en la raiz de tu proyecto:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

2. **Establece las variables de entorno:**
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

3. **Prueba la conexion:**
```bash
claude /mcp
```

4. **Usa las herramientas MCP:**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### Instalacion para servicios especificos

**GitHub MCP:**
```bash
npm install -g @modelcontextprotocol/server-github
```

**Database MCP:**
```bash
npm install -g @modelcontextprotocol/server-database
```

**Filesystem MCP:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP:**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## Solucion de problemas

### Servidor MCP no encontrado
```bash
# Verificar que el servidor MCP este instalado
npm list -g @modelcontextprotocol/server-github

# Instalar si falta
npm install -g @modelcontextprotocol/server-github
```

### Fallo de autenticacion
```bash
# Verificar que la variable de entorno este definida
echo $GITHUB_TOKEN

# Re-exportar si es necesario
export GITHUB_TOKEN="your_token"

# Verificar que el token tenga los permisos correctos
# Revisar los scopes del token en GitHub: https://github.com/settings/tokens
```

### Timeout de conexion
- Verificar la conectividad de red: `ping api.github.com`
- Verificar que el endpoint de la API sea accesible
- Comprobar los limites de velocidad de la API
- Intentar aumentar el timeout en la configuracion
- Comprobar si hay problemas de firewall o proxy

### Caidas del servidor MCP
- Revisar los logs del servidor MCP: `~/.claude/logs/`
- Verificar que todas las variables de entorno esten definidas
- Asegurarse de que los permisos de archivos sean correctos
- Intentar reinstalar el paquete del servidor MCP
- Comprobar si hay procesos en conflicto en el mismo puerto

## Conceptos relacionados

### Memory vs MCP
- **Memory**: Almacena datos persistentes que no cambian (preferencias, contexto, historial)
- **MCP**: Accede a datos en vivo que cambian (APIs, bases de datos, servicios en tiempo real)

### Cuando usar cada uno
- **Usa Memory** para: Preferencias del usuario, historial de conversaciones, contexto aprendido
- **Usa MCP** para: Issues actuales de GitHub, consultas en vivo a bases de datos, datos en tiempo real

### Integracion con otras funciones de Claude
- Combina MCP con Memory para un contexto enriquecido
- Usa herramientas MCP en prompts para mejor razonamiento
- Aprovecha multiples MCPs para workflows complejos

## Recursos adicionales

- [Documentacion oficial de MCP](https://code.claude.com/docs/en/mcp)
- [Especificacion del protocolo MCP](https://modelcontextprotocol.io/specification)
- [Repositorio MCP en GitHub](https://github.com/modelcontextprotocol/servers)
- [Servidores MCP disponibles](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — Runtime TypeScript y CLI para llamar servidores MCP sin boilerplate
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Blog de ingenieria de Anthropic sobre como resolver la saturacion del contexto
- [Referencia del CLI de Claude Code](https://code.claude.com/docs/en/cli-reference)
- [Documentacion de la API de Claude](https://docs.anthropic.com)

---
**Ultima Actualizacion**: Abril 2026
**Version de Claude Code**: 2.1+
**Modelos compatibles**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
