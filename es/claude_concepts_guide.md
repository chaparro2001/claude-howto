<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Guia Completa de Conceptos de Claude

Una guia de referencia exhaustiva que cubre Slash Commands, Subagents, Memory, MCP Protocol y Agent Skills con tablas, diagramas y ejemplos practicos.

---

## Tabla de Contenidos

1. [Slash Commands](#slash-commands)
2. [Subagents](#subagents)
3. [Memory](#memory)
4. [MCP Protocol](#mcp-protocol)
5. [Agent Skills](#agent-skills)
6. [Plugins](#claude-code-plugins)
7. [Hooks](#hooks)
8. [Checkpoints and Rewind](#checkpoints-and-rewind)
9. [Advanced Features](#advanced-features)
10. [Comparison & Integration](#comparison--integration)

---

## Slash Commands

### Descripcion General

Los slash commands son atajos invocados por el usuario almacenados como archivos Markdown que Claude Code puede ejecutar. Permiten a los equipos estandarizar prompts y workflows de uso frecuente.

### Arquitectura

```mermaid
graph TD
    A["User Input: /command-name"] -->|Triggers| B["Search .claude/commands/"]
    B -->|Finds| C["command-name.md"]
    C -->|Loads| D["Markdown Content"]
    D -->|Executes| E["Claude Processes Prompt"]
    E -->|Returns| F["Result in Context"]
```

### Estructura de Archivos

```mermaid
graph LR
    A["Project Root"] -->|contains| B[".claude/commands/"]
    B -->|contains| C["optimize.md"]
    B -->|contains| D["test.md"]
    B -->|contains| E["docs/"]
    E -->|contains| F["generate-api-docs.md"]
    E -->|contains| G["generate-readme.md"]
```

### Tabla de Organizacion de Comandos

| Ubicacion | Alcance | Disponibilidad | Caso de Uso | Rastreado por Git |
|----------|-------|--------------|----------|-------------|
| `.claude/commands/` | Especifico del proyecto | Miembros del equipo | Workflows de equipo, estandares compartidos | ✅ Si |
| `~/.claude/commands/` | Personal | Usuario individual | Atajos personales entre proyectos | ❌ No |
| Subdirectorios | Con espacio de nombres | Segun el padre | Organizar por categoria | ✅ Si |

### Funcionalidades y Capacidades

| Funcionalidad | Ejemplo | Soportado |
|---------|---------|-----------|
| Ejecucion de shell scripts | `bash scripts/deploy.sh` | ✅ Si |
| Referencias de archivos | `@path/to/file.js` | ✅ Si |
| Integracion con Bash | `$(git log --oneline)` | ✅ Si |
| Argumentos | `/pr --verbose` | ✅ Si |
| Comandos MCP | `/mcp__github__list_prs` | ✅ Si |

### Ejemplos Practicos

#### Ejemplo 1: Comando de Optimizacion de Codigo

**Archivo:** `.claude/commands/optimize.md`

```markdown
---
name: Code Optimization
description: Analyze code for performance issues and suggest optimizations
tags: performance, analysis
---

# Code Optimization

Review the provided code for the following issues in order of priority:

1. **Performance bottlenecks** - identify O(n²) operations, inefficient loops
2. **Memory leaks** - find unreleased resources, circular references
3. **Algorithm improvements** - suggest better algorithms or data structures
4. **Caching opportunities** - identify repeated computations
5. **Concurrency issues** - find race conditions or threading problems

Format your response with:
- Issue severity (Critical/High/Medium/Low)
- Location in code
- Explanation
- Recommended fix with code example
```

**Uso:**
```bash
# El usuario escribe en Claude Code
/optimize

# Claude carga el prompt y espera la entrada de codigo
```

#### Ejemplo 2: Comando de Ayuda para Pull Request

**Archivo:** `.claude/commands/pr.md`

```markdown
---
name: Prepare Pull Request
description: Clean up code, stage changes, and prepare a pull request
tags: git, workflow
---

# Pull Request Preparation Checklist

Before creating a PR, execute these steps:

1. Run linting: `prettier --write .`
2. Run tests: `npm test`
3. Review git diff: `git diff HEAD`
4. Stage changes: `git add .`
5. Create commit message following conventional commits:
   - `fix:` for bug fixes
   - `feat:` for new features
   - `docs:` for documentation
   - `refactor:` for code restructuring
   - `test:` for test additions
   - `chore:` for maintenance

6. Generate PR summary including:
   - What changed
   - Why it changed
   - Testing performed
   - Potential impacts
```

**Uso:**
```bash
/pr

# Claude sigue el checklist y prepara el PR
```

#### Ejemplo 3: Generador de Documentacion Jerarquico

**Archivo:** `.claude/commands/docs/generate-api-docs.md`

```markdown
---
name: Generate API Documentation
description: Create comprehensive API documentation from source code
tags: documentation, api
---

# API Documentation Generator

Generate API documentation by:

1. Scanning all files in `/src/api/`
2. Extracting function signatures and JSDoc comments
3. Organizing by endpoint/module
4. Creating markdown with examples
5. Including request/response schemas
6. Adding error documentation

Output format:
- Markdown file in `/docs/api.md`
- Include curl examples for all endpoints
- Add TypeScript types
```

### Diagrama del Ciclo de Vida de un Comando

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant FS as File System
    participant CLI as Shell/Bash

    User->>Claude: Types /optimize
    Claude->>FS: Searches .claude/commands/
    FS-->>Claude: Returns optimize.md
    Claude->>Claude: Loads Markdown content
    Claude->>User: Displays prompt context
    User->>Claude: Provides code to analyze
    Claude->>CLI: (May execute scripts)
    CLI-->>Claude: Results
    Claude->>User: Returns analysis
```

### Buenas Practicas

| ✅ Hacer | ❌ No Hacer |
|------|---------|
| Usar nombres claros y orientados a la accion | Crear comandos para tareas de una sola vez |
| Documentar palabras clave en la descripcion | Construir logica compleja en los comandos |
| Mantener los comandos enfocados en una sola tarea | Crear comandos redundantes |
| Versionar los comandos del proyecto en git | Hardcodear informacion sensible |
| Organizar en subdirectorios | Crear listas largas de comandos |
| Usar prompts simples y legibles | Usar redaccion abreviada o críptica |

---

## Subagents

### Descripcion General

Los subagents son asistentes de IA especializados con context windows aislados y system prompts personalizados. Permiten la ejecucion delegada de tareas manteniendo una separacion clara de responsabilidades.

### Diagrama de Arquitectura

```mermaid
graph TB
    User["👤 User"]
    Main["🎯 Main Agent<br/>(Coordinator)"]
    Reviewer["🔍 Code Reviewer<br/>Subagent"]
    Tester["✅ Test Engineer<br/>Subagent"]
    Docs["📝 Documentation<br/>Subagent"]

    User -->|asks| Main
    Main -->|delegates| Reviewer
    Main -->|delegates| Tester
    Main -->|delegates| Docs
    Reviewer -->|returns result| Main
    Tester -->|returns result| Main
    Docs -->|returns result| Main
    Main -->|synthesizes| User
```

### Ciclo de Vida de un Subagent

```mermaid
sequenceDiagram
    participant User
    participant MainAgent as Main Agent
    participant CodeReviewer as Code Reviewer<br/>Subagent
    participant Context as Separate<br/>Context Window

    User->>MainAgent: "Build new auth feature"
    MainAgent->>MainAgent: Analyze task
    MainAgent->>CodeReviewer: "Review this code"
    CodeReviewer->>Context: Initialize clean context
    Context->>CodeReviewer: Load reviewer instructions
    CodeReviewer->>CodeReviewer: Perform review
    CodeReviewer-->>MainAgent: Return findings
    MainAgent->>MainAgent: Incorporate results
    MainAgent-->>User: Provide synthesis
```

### Tabla de Configuracion de Subagents

| Configuracion | Tipo | Proposito | Ejemplo |
|---------------|------|---------|---------|
| `name` | String | Identificador del agente | `code-reviewer` |
| `description` | String | Proposito y terminos de activacion | `Comprehensive code quality analysis` |
| `tools` | List/String | Capacidades permitidas | `read, grep, diff, lint_runner` |
| `system_prompt` | Markdown | Instrucciones de comportamiento | Guias personalizadas |

### Jerarquia de Acceso a Herramientas

```mermaid
graph TD
    A["Subagent Configuration"] -->|Option 1| B["Inherit All Tools<br/>from Main Thread"]
    A -->|Option 2| C["Specify Individual Tools"]
    B -->|Includes| B1["File Operations"]
    B -->|Includes| B2["Shell Commands"]
    B -->|Includes| B3["MCP Tools"]
    C -->|Explicit List| C1["read, grep, diff"]
    C -->|Explicit List| C2["Bash(npm:*), Bash(test:*)"]
```

### Ejemplos Practicos

#### Ejemplo 1: Configuracion Completa de Subagent

**Archivo:** `.claude/agents/code-reviewer.md`

```yaml
---
name: code-reviewer
description: Comprehensive code quality and maintainability analysis
tools: read, grep, diff, lint_runner
---

# Code Reviewer Agent

You are an expert code reviewer specializing in:
- Performance optimization
- Security vulnerabilities
- Code maintainability
- Testing coverage
- Design patterns

## Review Priorities (in order)

1. **Security Issues** - Authentication, authorization, data exposure
2. **Performance Problems** - O(n²) operations, memory leaks, inefficient queries
3. **Code Quality** - Readability, naming, documentation
4. **Test Coverage** - Missing tests, edge cases
5. **Design Patterns** - SOLID principles, architecture

## Review Output Format

For each issue:
- **Severity**: Critical / High / Medium / Low
- **Category**: Security / Performance / Quality / Testing / Design
- **Location**: File path and line number
- **Issue Description**: What's wrong and why
- **Suggested Fix**: Code example
- **Impact**: How this affects the system

## Example Review

### Issue: N+1 Query Problem
- **Severity**: High
- **Category**: Performance
- **Location**: src/user-service.ts:45
- **Issue**: Loop executes database query in each iteration
- **Fix**: Use JOIN or batch query
```

**Archivo:** `.claude/agents/test-engineer.md`

```yaml
---
name: test-engineer
description: Test strategy, coverage analysis, and automated testing
tools: read, write, bash, grep
---

# Test Engineer Agent

You are expert at:
- Writing comprehensive test suites
- Ensuring high code coverage (>80%)
- Testing edge cases and error scenarios
- Performance benchmarking
- Integration testing

## Testing Strategy

1. **Unit Tests** - Individual functions/methods
2. **Integration Tests** - Component interactions
3. **End-to-End Tests** - Complete workflows
4. **Edge Cases** - Boundary conditions
5. **Error Scenarios** - Failure handling

## Test Output Requirements

- Use Jest for JavaScript/TypeScript
- Include setup/teardown for each test
- Mock external dependencies
- Document test purpose
- Include performance assertions when relevant

## Coverage Requirements

- Minimum 80% code coverage
- 100% for critical paths
- Report missing coverage areas
```

**Archivo:** `.claude/agents/documentation-writer.md`

```yaml
---
name: documentation-writer
description: Technical documentation, API docs, and user guides
tools: read, write, grep
---

# Documentation Writer Agent

You create:
- API documentation with examples
- User guides and tutorials
- Architecture documentation
- Changelog entries
- Code comment improvements

## Documentation Standards

1. **Clarity** - Use simple, clear language
2. **Examples** - Include practical code examples
3. **Completeness** - Cover all parameters and returns
4. **Structure** - Use consistent formatting
5. **Accuracy** - Verify against actual code

## Documentation Sections

### For APIs
- Description
- Parameters (with types)
- Returns (with types)
- Throws (possible errors)
- Examples (curl, JavaScript, Python)
- Related endpoints

### For Features
- Overview
- Prerequisites
- Step-by-step instructions
- Expected outcomes
- Troubleshooting
- Related topics
```

#### Ejemplo 2: Delegacion de Subagent en Accion

```markdown
# Escenario: Construir una Funcionalidad de Pagos

## Solicitud del Usuario
"Build a secure payment processing feature that integrates with Stripe"

## Flujo del Agente Principal

1. **Fase de Planificacion**
   - Comprende los requisitos
   - Determina las tareas necesarias
   - Planifica la arquitectura

2. **Delega al Subagent Code Reviewer**
   - Tarea: "Review the payment processing implementation for security"
   - Contexto: Auth, API keys, manejo de tokens
   - Revisa: inyeccion SQL, exposicion de claves, aplicacion de HTTPS

3. **Delega al Subagent Test Engineer**
   - Tarea: "Create comprehensive tests for payment flows"
   - Contexto: Escenarios exitosos, fallos, casos borde
   - Crea tests para: pagos validos, tarjetas rechazadas, fallos de red, webhooks

4. **Delega al Subagent Documentation Writer**
   - Tarea: "Document the payment API endpoints"
   - Contexto: Esquemas de request/response
   - Produce: documentacion de API con ejemplos curl, codigos de error

5. **Sintesis**
   - El agente principal recolecta todos los resultados
   - Integra los hallazgos
   - Devuelve la solucion completa al usuario
```

#### Ejemplo 3: Alcance de Permisos de Herramientas

**Configuracion Restrictiva - Limitada a Comandos Especificos**

```yaml
---
name: secure-reviewer
description: Security-focused code review with minimal permissions
tools: read, grep
---

# Secure Code Reviewer

Reviews code for security vulnerabilities only.

This agent:
- ✅ Reads files to analyze
- ✅ Searches for patterns
- ❌ Cannot execute code
- ❌ Cannot modify files
- ❌ Cannot run tests

This ensures the reviewer doesn't accidentally break anything.
```

**Configuracion Extendida - Todas las Herramientas para Implementacion**

```yaml
---
name: implementation-agent
description: Full implementation capabilities for feature development
tools: read, write, bash, grep, edit, glob
---

# Implementation Agent

Builds features from specifications.

This agent:
- ✅ Reads specifications
- ✅ Writes new code files
- ✅ Runs build commands
- ✅ Searches codebase
- ✅ Edits existing files
- ✅ Finds files matching patterns

Full capabilities for independent feature development.
```

### Gestion de Contexto en Subagents

```mermaid
graph TB
    A["Main Agent Context<br/>50,000 tokens"]
    B["Subagent 1 Context<br/>20,000 tokens"]
    C["Subagent 2 Context<br/>20,000 tokens"]
    D["Subagent 3 Context<br/>20,000 tokens"]

    A -->|Clean slate| B
    A -->|Clean slate| C
    A -->|Clean slate| D

    B -->|Results only| A
    C -->|Results only| A
    D -->|Results only| A

    style A fill:#e1f5ff
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

### Cuando Usar Subagents

| Escenario | Usar Subagent | Por que |
|----------|--------------|-----|
| Funcionalidad compleja con muchos pasos | ✅ Si | Separar responsabilidades, evitar contaminacion de contexto |
| Code review rapido | ❌ No | Sobrecarga innecesaria |
| Ejecucion de tareas en paralelo | ✅ Si | Cada subagent tiene su propio contexto |
| Se necesita experiencia especializada | ✅ Si | System prompts personalizados |
| Analisis de larga duracion | ✅ Si | Evita el agotamiento del contexto principal |
| Tarea unica | ❌ No | Agrega latencia innecesaria |

### Agent Teams

Los Agent Teams coordinan multiples agents trabajando en tareas relacionadas. En lugar de delegar a un subagent a la vez, los Agent Teams permiten al agente principal orquestar un grupo de agents que colaboran, comparten resultados intermedios y trabajan hacia un objetivo comun. Esto es util para tareas a gran escala como el desarrollo de funcionalidades full-stack donde un agente de frontend, uno de backend y uno de testing trabajan en paralelo.

---

## Memory

### Descripcion General

La Memory permite que Claude retenga contexto entre sesiones y conversaciones. Existe en dos formas: sintesis automatica en claude.ai, y CLAUDE.md basado en el sistema de archivos en Claude Code.

### Arquitectura de Memory

```mermaid
graph TB
    A["Claude Session"]
    B["User Input"]
    C["Memory System"]
    D["Memory Storage"]

    B -->|User provides info| C
    C -->|Synthesizes every 24h| D
    D -->|Loads automatically| A
    A -->|Uses context| C
```

### Jerarquia de Memory en Claude Code (7 Niveles)

Claude Code carga memory desde 7 niveles, listados de mayor a menor prioridad:

```mermaid
graph TD
    A["1. Managed Policy<br/>Enterprise admin policies"] --> B["2. Project Memory<br/>./CLAUDE.md"]
    B --> C["3. Project Rules<br/>.claude/rules/*.md"]
    C --> D["4. User Memory<br/>~/.claude/CLAUDE.md"]
    D --> E["5. User Rules<br/>~/.claude/rules/*.md"]
    E --> F["6. Local Memory<br/>.claude/local/CLAUDE.md"]
    F --> G["7. Auto Memory<br/>Automatically captured preferences"]

    style A fill:#fce4ec,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e1f5fe,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
    style G fill:#fff3e0,stroke:#333,color:#333
```

### Tabla de Ubicaciones de Memory

| Nivel | Ubicacion | Alcance | Prioridad | Compartido | Ideal Para |
|------|----------|-------|----------|--------|----------|
| 1. Managed Policy | Admin enterprise | Organizacion | Maxima | Todos los usuarios de la org | Politicas de cumplimiento y seguridad |
| 2. Project | `./CLAUDE.md` | Proyecto | Alta | Equipo (Git) | Estandares del equipo, arquitectura |
| 3. Project Rules | `.claude/rules/*.md` | Proyecto | Alta | Equipo (Git) | Convenciones modulares del proyecto |
| 4. User | `~/.claude/CLAUDE.md` | Personal | Media | Individual | Preferencias personales |
| 5. User Rules | `~/.claude/rules/*.md` | Personal | Media | Individual | Modulos de reglas personales |
| 6. Local | `.claude/local/CLAUDE.md` | Local | Baja | No compartido | Configuraciones especificas de la maquina |
| 7. Auto Memory | Automatica | Sesion | Minima | Individual | Preferencias y patrones aprendidos |

### Auto Memory

La Auto Memory captura automaticamente las preferencias y patrones del usuario observados durante las sesiones. Claude aprende de tus interacciones y recuerda:

- Preferencias de estilo de codigo
- Correcciones frecuentes que realizas
- Elecciones de frameworks y herramientas
- Preferencias de estilo de comunicacion

La Auto Memory funciona en segundo plano y no requiere configuracion manual.

### Ciclo de Vida de Actualizacion de Memory

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Editor as File System
    participant Memory as CLAUDE.md

    User->>Claude: "Remember: use async/await"
    Claude->>User: "Which memory file?"
    User->>Claude: "Project memory"
    Claude->>Editor: Open ~/.claude/settings.json
    Claude->>Memory: Write to ./CLAUDE.md
    Memory-->>Claude: File saved
    Claude->>Claude: Load updated memory
    Claude-->>User: "Memory saved!"
```

### Ejemplos Practicos

#### Ejemplo 1: Estructura de Memory del Proyecto

**Archivo:** `./CLAUDE.md`

```markdown
# Project Configuration

## Project Overview
- **Name**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Team Size**: 5 developers
- **Deadline**: Q4 2025

## Architecture
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## Development Standards

### Code Style
- Use Prettier for formatting
- Use ESLint with airbnb config
- Maximum line length: 100 characters
- Use 2-space indentation

### Naming Conventions
- **Files**: kebab-case (user-controller.js)
- **Classes**: PascalCase (UserService)
- **Functions/Variables**: camelCase (getUserById)
- **Constants**: UPPER_SNAKE_CASE (API_BASE_URL)
- **Database Tables**: snake_case (user_accounts)

### Git Workflow
- Branch names: `feature/description` or `fix/description`
- Commit messages: Follow conventional commits
- PR required before merge
- All CI/CD checks must pass
- Minimum 1 approval required

### Testing Requirements
- Minimum 80% code coverage
- All critical paths must have tests
- Use Jest for unit tests
- Use Cypress for E2E tests
- Test filenames: `*.test.ts` or `*.spec.ts`

### API Standards
- RESTful endpoints only
- JSON request/response
- Use HTTP status codes correctly
- Version API endpoints: `/api/v1/`
- Document all endpoints with examples

### Database
- Use migrations for schema changes
- Never hardcode credentials
- Use connection pooling
- Enable query logging in development
- Regular backups required

### Deployment
- Docker-based deployment
- Kubernetes orchestration
- Blue-green deployment strategy
- Automatic rollback on failure
- Database migrations run before deploy

## Common Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start development server |
| `npm test` | Run test suite |
| `npm run lint` | Check code style |
| `npm run build` | Build for production |
| `npm run migrate` | Run database migrations |

## Team Contacts
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## Known Issues & Workarounds
- PostgreSQL connection pooling limited to 20 during peak hours
- Workaround: Implement query queuing
- Safari 14 compatibility issues with async generators
- Workaround: Use Babel transpiler

## Related Projects
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`
```

#### Ejemplo 2: Memory Especifica de Directorio

**Archivo:** `./src/api/CLAUDE.md`

~~~~markdown
# API Module Standards

This file overrides root CLAUDE.md for everything in /src/api/

## API-Specific Standards

### Request Validation
- Use Zod for schema validation
- Always validate input
- Return 400 with validation errors
- Include field-level error details

### Authentication
- All endpoints require JWT token
- Token in Authorization header
- Token expires after 24 hours
- Implement refresh token mechanism

### Response Format

All responses must follow this structure:

```json
{
  "success": true,
  "data": { /* actual data */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

### Error responses:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* field errors */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Pagination
- Use cursor-based pagination (not offset)
- Include `hasMore` boolean
- Limit max page size to 100
- Default page size: 20

### Rate Limiting
- 1000 requests per hour for authenticated users
- 100 requests per hour for public endpoints
- Return 429 when exceeded
- Include retry-after header

### Caching
- Use Redis for session caching
- Cache duration: 5 minutes default
- Invalidate on write operations
- Tag cache keys with resource type
~~~~

#### Ejemplo 3: Memory Personal

**Archivo:** `~/.claude/CLAUDE.md`

~~~~markdown
# My Development Preferences

## About Me
- **Experience Level**: 8 years full-stack development
- **Preferred Languages**: TypeScript, Python
- **Communication Style**: Direct, with examples
- **Learning Style**: Visual diagrams with code

## Code Preferences

### Error Handling
I prefer explicit error handling with try-catch blocks and meaningful error messages.
Avoid generic errors. Always log errors for debugging.

### Comments
Use comments for WHY, not WHAT. Code should be self-documenting.
Comments should explain business logic or non-obvious decisions.

### Testing
I prefer TDD (test-driven development).
Write tests first, then implementation.
Focus on behavior, not implementation details.

### Architecture
I prefer modular, loosely-coupled design.
Use dependency injection for testability.
Separate concerns (Controllers, Services, Repositories).

## Debugging Preferences
- Use console.log with prefix: `[DEBUG]`
- Include context: function name, relevant variables
- Use stack traces when available
- Always include timestamps in logs

## Communication
- Explain complex concepts with diagrams
- Show concrete examples before explaining theory
- Include before/after code snippets
- Summarize key points at the end

## Project Organization
I organize my projects as:
```
project/
  ├── src/
  │   ├── api/
  │   ├── services/
  │   ├── models/
  │   └── utils/
  ├── tests/
  ├── docs/
  └── docker/
```

## Tooling
- **IDE**: VS Code with vim keybindings
- **Terminal**: Zsh with Oh-My-Zsh
- **Format**: Prettier (100 char line length)
- **Linter**: ESLint with airbnb config
- **Test Framework**: Jest with React Testing Library
~~~~

#### Ejemplo 4: Actualizacion de Memory Durante una Sesion

**Interaccion de Sesion:**

```markdown
User: Remember that I prefer using React hooks instead of class components
     for all new components.

Claude: I'm adding that to your memory. Which memory file should this go in?
        1. Project memory (./CLAUDE.md)
        2. Personal memory (~/.claude/CLAUDE.md)

User: Project memory

Claude: ✅ Memory saved!

Added to ./CLAUDE.md:
---

### Component Development
- Use functional components with React Hooks
- Prefer hooks over class components
- Custom hooks for reusable logic
- Use useCallback for event handlers
- Use useMemo for expensive computations
```

### Memory en Claude Web/Desktop

#### Linea de Tiempo de Sintesis de Memory

```mermaid
graph LR
    A["Day 1: User<br/>Conversations"] -->|24 hours| B["Day 2: Memory<br/>Synthesis"]
    B -->|Automatic| C["Memory Updated<br/>Summarized"]
    C -->|Loaded in| D["Day 2-N:<br/>New Conversations"]
    D -->|Add to| E["Memory"]
    E -->|24 hours later| F["Memory Refreshed"]
```

**Ejemplo de Resumen de Memory:**

```markdown
## Claude's Memory of User

### Professional Background
- Senior full-stack developer with 8 years experience
- Focus on TypeScript/Node.js backends and React frontends
- Active open source contributor
- Interested in AI and machine learning

### Project Context
- Currently building e-commerce platform
- Tech stack: Node.js, PostgreSQL, React 18, Docker
- Working with team of 5 developers
- Using CI/CD and blue-green deployments

### Communication Preferences
- Prefers direct, concise explanations
- Likes visual diagrams and examples
- Appreciates code snippets
- Explains business logic in comments

### Current Goals
- Improve API performance
- Increase test coverage to 90%
- Implement caching strategy
- Document architecture
```

### Comparacion de Funcionalidades de Memory

| Funcionalidad | Claude Web/Desktop | Claude Code (CLAUDE.md) |
|---------|-------------------|------------------------|
| Auto-sintesis | ✅ Cada 24h | ❌ Manual |
| Multi-proyecto | ✅ Compartida | ❌ Especifica del proyecto |
| Acceso del equipo | ✅ Proyectos compartidos | ✅ Rastreado por Git |
| Buscable | ✅ Integrado | ✅ A traves de `/memory` |
| Editable | ✅ En el chat | ✅ Edicion directa del archivo |
| Importar/Exportar | ✅ Si | ✅ Copiar/pegar |
| Persistente | ✅ 24h+ | ✅ Indefinido |

---

## MCP Protocol

### Descripcion General

MCP (Model Context Protocol) es una forma estandarizada para que Claude acceda a herramientas externas, APIs y fuentes de datos en tiempo real. A diferencia de Memory, MCP proporciona acceso en vivo a datos que cambian.

### Arquitectura MCP

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
```

### Ecosistema MCP

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
```

### Proceso de Configuracion MCP

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

### Tabla de Servidores MCP Disponibles

| Servidor MCP | Proposito | Herramientas Comunes | Auth | Tiempo Real |
|------------|---------|--------------|------|-----------|
| **Filesystem** | Operaciones de archivos | read, write, delete | Permisos del SO | ✅ Si |
| **GitHub** | Gestion de repositorios | list_prs, create_issue, push | OAuth | ✅ Si |
| **Slack** | Comunicacion de equipo | send_message, list_channels | Token | ✅ Si |
| **Database** | Consultas SQL | query, insert, update | Credenciales | ✅ Si |
| **Google Docs** | Acceso a documentos | read, write, share | OAuth | ✅ Si |
| **Asana** | Gestion de proyectos | create_task, update_status | API Key | ✅ Si |
| **Stripe** | Datos de pagos | list_charges, create_invoice | API Key | ✅ Si |
| **Memory** | Memoria persistente | store, retrieve, delete | Local | ❌ No |

### Ejemplos Practicos

#### Ejemplo 1: Configuracion de GitHub MCP

**Archivo:** `.mcp.json` (alcance de proyecto) o `~/.claude.json` (alcance de usuario)

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

**Herramientas GitHub MCP Disponibles:**

~~~~markdown
# GitHub MCP Tools

## Pull Request Management
- `list_prs` - List all PRs in repository
- `get_pr` - Get PR details including diff
- `create_pr` - Create new PR
- `update_pr` - Update PR description/title
- `merge_pr` - Merge PR to main branch
- `review_pr` - Add review comments

Example request:
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

## Issue Management
- `list_issues` - List all issues
- `get_issue` - Get issue details
- `create_issue` - Create new issue
- `close_issue` - Close issue
- `add_comment` - Add comment to issue

## Repository Information
- `get_repo_info` - Repository details
- `list_files` - File tree structure
- `get_file_content` - Read file contents
- `search_code` - Search across codebase

## Commit Operations
- `list_commits` - Commit history
- `get_commit` - Specific commit details
- `create_commit` - Create new commit
~~~~

#### Ejemplo 2: Configuracion de Database MCP

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

**Ejemplo de Uso:**

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

#### Ejemplo 3: Workflow Multi-MCP

**Escenario: Generacion de Reporte Diario**

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

#### Ejemplo 4: Operaciones con Filesystem MCP

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

**Operaciones Disponibles:**

| Operacion | Comando | Proposito |
|-----------|---------|---------|
| Listar archivos | `ls ~/projects` | Mostrar contenido del directorio |
| Leer archivo | `cat src/main.ts` | Leer contenido del archivo |
| Escribir archivo | `create docs/api.md` | Crear nuevo archivo |
| Editar archivo | `edit src/app.ts` | Modificar archivo |
| Buscar | `grep "async function"` | Buscar en archivos |
| Eliminar | `rm old-file.js` | Eliminar archivo |

### MCP vs Memory: Matriz de Decision

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]

    style B fill:#e1f5ff
    style D fill:#fff9c4
```

### Patron de Request/Response

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

---

## Agent Skills

### Descripcion General

Los Agent Skills son capacidades reutilizables invocadas por el modelo, empaquetadas como carpetas que contienen instrucciones, scripts y recursos. Claude detecta y usa automaticamente los skills relevantes.

### Arquitectura de Skill

```mermaid
graph TB
    A["Skill Directory"]
    B["SKILL.md"]
    C["YAML Metadata"]
    D["Instructions"]
    E["Scripts"]
    F["Templates"]

    A --> B
    B --> C
    B --> D
    E --> A
    F --> A
```

### Proceso de Carga de Skill

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude
    participant System as System
    participant Skill as Skill

    User->>Claude: "Create Excel report"
    Claude->>System: Scan available skills
    System->>System: Load skill metadata
    Claude->>Claude: Match user request to skills
    Claude->>Skill: Load xlsx skill SKILL.md
    Skill-->>Claude: Return instructions + tools
    Claude->>Claude: Execute skill
    Claude->>User: Generate Excel file
```

### Tabla de Tipos y Ubicaciones de Skills

| Tipo | Ubicacion | Alcance | Compartido | Sync | Ideal Para |
|------|----------|-------|--------|------|----------|
| Pre-construido | Integrado | Global | Todos los usuarios | Auto | Creacion de documentos |
| Personal | `~/.claude/skills/` | Individual | No | Manual | Automatizacion personal |
| Proyecto | `.claude/skills/` | Equipo | Si | Git | Estandares del equipo |
| Plugin | Via instalacion de plugin | Variable | Depende | Auto | Funcionalidades integradas |

### Skills Pre-construidos

```mermaid
graph TB
    A["Pre-built Skills"]
    B["PowerPoint (pptx)"]
    C["Excel (xlsx)"]
    D["Word (docx)"]
    E["PDF"]

    A --> B
    A --> C
    A --> D
    A --> E

    B --> B1["Create presentations"]
    B --> B2["Edit slides"]
    C --> C1["Create spreadsheets"]
    C --> C2["Analyze data"]
    D --> D1["Create documents"]
    D --> D2["Format text"]
    E --> E1["Generate PDFs"]
    E --> E2["Fill forms"]
```

### Bundled Skills

Claude Code ahora incluye 5 bundled skills disponibles de serie:

| Skill | Comando | Proposito |
|-------|---------|---------|
| **Simplify** | `/simplify` | Simplificar codigo o explicaciones complejas |
| **Batch** | `/batch` | Ejecutar operaciones en multiples archivos o elementos |
| **Debug** | `/debug` | Debugging sistematico de problemas con analisis de causa raiz |
| **Loop** | `/loop` | Programar tareas recurrentes con un temporizador |
| **Claude API** | `/claude-api` | Interactuar directamente con la API de Anthropic |

Estos bundled skills estan siempre disponibles y no requieren instalacion ni configuracion.

### Ejemplos Practicos

#### Ejemplo 1: Skill Personalizado de Code Review

**Estructura de Directorio:**

```
~/.claude/skills/code-review/
├── SKILL.md
├── templates/
│   ├── review-checklist.md
│   └── finding-template.md
└── scripts/
    ├── analyze-metrics.py
    └── compare-complexity.py
```

**Archivo:** `~/.claude/skills/code-review/SKILL.md`

```yaml
---
name: Code Review Specialist
description: Comprehensive code review with security, performance, and quality analysis
version: "1.0.0"
tags:
  - code-review
  - quality
  - security
when_to_use: When users ask to review code, analyze code quality, or evaluate pull requests
effort: high
shell: bash
---

# Code Review Skill

This skill provides comprehensive code review capabilities focusing on:

1. **Security Analysis**
   - Authentication/authorization issues
   - Data exposure risks
   - Injection vulnerabilities
   - Cryptographic weaknesses
   - Sensitive data logging

2. **Performance Review**
   - Algorithm efficiency (Big O analysis)
   - Memory optimization
   - Database query optimization
   - Caching opportunities
   - Concurrency issues

3. **Code Quality**
   - SOLID principles
   - Design patterns
   - Naming conventions
   - Documentation
   - Test coverage

4. **Maintainability**
   - Code readability
   - Function size (should be < 50 lines)
   - Cyclomatic complexity
   - Dependency management
   - Type safety

## Review Template

For each piece of code reviewed, provide:

### Summary
- Overall quality assessment (1-5)
- Key findings count
- Recommended priority areas

### Critical Issues (if any)
- **Issue**: Clear description
- **Location**: File and line number
- **Impact**: Why this matters
- **Severity**: Critical/High/Medium
- **Fix**: Code example

### Findings by Category

#### Security (if issues found)
List security vulnerabilities with examples

#### Performance (if issues found)
List performance problems with complexity analysis

#### Quality (if issues found)
List code quality issues with refactoring suggestions

#### Maintainability (if issues found)
List maintainability problems with improvements
```
## Python Script: analyze-metrics.py

```python
#!/usr/bin/env python3
import re
import sys

def analyze_code_metrics(code):
    """Analyze code for common metrics."""

    # Count functions
    functions = len(re.findall(r'^def\s+\w+', code, re.MULTILINE))

    # Count classes
    classes = len(re.findall(r'^class\s+\w+', code, re.MULTILINE))

    # Average line length
    lines = code.split('\n')
    avg_length = sum(len(l) for l in lines) / len(lines) if lines else 0

    # Estimate complexity
    complexity = len(re.findall(r'\b(if|elif|else|for|while|and|or)\b', code))

    return {
        'functions': functions,
        'classes': classes,
        'avg_line_length': avg_length,
        'complexity_score': complexity
    }

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        code = f.read()
    metrics = analyze_code_metrics(code)
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")
```

## Python Script: compare-complexity.py

```python
#!/usr/bin/env python3
"""
Compare cyclomatic complexity of code before and after changes.
Helps identify if refactoring actually simplifies code structure.
"""

import re
import sys
from typing import Dict, Tuple

class ComplexityAnalyzer:
    """Analyze code complexity metrics."""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split('\n')

    def calculate_cyclomatic_complexity(self) -> int:
        """
        Calculate cyclomatic complexity using McCabe's method.
        Count decision points: if, elif, else, for, while, except, and, or
        """
        complexity = 1  # Base complexity

        # Count decision points
        decision_patterns = [
            r'\bif\b',
            r'\belif\b',
            r'\bfor\b',
            r'\bwhile\b',
            r'\bexcept\b',
            r'\band\b(?!$)',
            r'\bor\b(?!$)'
        ]

        for pattern in decision_patterns:
            matches = re.findall(pattern, self.code)
            complexity += len(matches)

        return complexity

    def calculate_cognitive_complexity(self) -> int:
        """
        Calculate cognitive complexity - how hard is it to understand?
        Based on nesting depth and control flow.
        """
        cognitive = 0
        nesting_depth = 0

        for line in self.lines:
            # Track nesting depth
            if re.search(r'^\s*(if|for|while|def|class|try)\b', line):
                nesting_depth += 1
                cognitive += nesting_depth
            elif re.search(r'^\s*(elif|else|except|finally)\b', line):
                cognitive += nesting_depth

            # Reduce nesting when unindenting
            if line and not line[0].isspace():
                nesting_depth = 0

        return cognitive

    def calculate_maintainability_index(self) -> float:
        """
        Maintainability Index ranges from 0-100.
        > 85: Excellent
        > 65: Good
        > 50: Fair
        < 50: Poor
        """
        lines = len(self.lines)
        cyclomatic = self.calculate_cyclomatic_complexity()
        cognitive = self.calculate_cognitive_complexity()

        # Simplified MI calculation
        mi = 171 - 5.2 * (cyclomatic / lines) - 0.23 * (cognitive) - 16.2 * (lines / 1000)

        return max(0, min(100, mi))

    def get_complexity_report(self) -> Dict:
        """Generate comprehensive complexity report."""
        return {
            'cyclomatic_complexity': self.calculate_cyclomatic_complexity(),
            'cognitive_complexity': self.calculate_cognitive_complexity(),
            'maintainability_index': round(self.calculate_maintainability_index(), 2),
            'lines_of_code': len(self.lines),
            'avg_line_length': round(sum(len(l) for l in self.lines) / len(self.lines), 2) if self.lines else 0
        }


def compare_files(before_file: str, after_file: str) -> None:
    """Compare complexity metrics between two code versions."""

    with open(before_file, 'r') as f:
        before_code = f.read()

    with open(after_file, 'r') as f:
        after_code = f.read()

    before_analyzer = ComplexityAnalyzer(before_code)
    after_analyzer = ComplexityAnalyzer(after_code)

    before_metrics = before_analyzer.get_complexity_report()
    after_metrics = after_analyzer.get_complexity_report()

    print("=" * 60)
    print("CODE COMPLEXITY COMPARISON")
    print("=" * 60)

    print("\nBEFORE:")
    print(f"  Cyclomatic Complexity:    {before_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {before_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {before_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {before_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {before_metrics['avg_line_length']}")

    print("\nAFTER:")
    print(f"  Cyclomatic Complexity:    {after_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {after_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {after_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {after_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {after_metrics['avg_line_length']}")

    print("\nCHANGES:")
    cyclomatic_change = after_metrics['cyclomatic_complexity'] - before_metrics['cyclomatic_complexity']
    cognitive_change = after_metrics['cognitive_complexity'] - before_metrics['cognitive_complexity']
    mi_change = after_metrics['maintainability_index'] - before_metrics['maintainability_index']
    loc_change = after_metrics['lines_of_code'] - before_metrics['lines_of_code']

    print(f"  Cyclomatic Complexity:    {cyclomatic_change:+d}")
    print(f"  Cognitive Complexity:     {cognitive_change:+d}")
    print(f"  Maintainability Index:    {mi_change:+.2f}")
    print(f"  Lines of Code:            {loc_change:+d}")

    print("\nASSESSMENT:")
    if mi_change > 0:
        print("  ✅ Code is MORE maintainable")
    elif mi_change < 0:
        print("  ⚠️  Code is LESS maintainable")
    else:
        print("  ➡️  Maintainability unchanged")

    if cyclomatic_change < 0:
        print("  ✅ Complexity DECREASED")
    elif cyclomatic_change > 0:
        print("  ⚠️  Complexity INCREASED")
    else:
        print("  ➡️  Complexity unchanged")

    print("=" * 60)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python compare-complexity.py <before_file> <after_file>")
        sys.exit(1)

    compare_files(sys.argv[1], sys.argv[2])
```

## Template: review-checklist.md

```markdown
# Code Review Checklist

## Security Checklist
- [ ] No hardcoded credentials or secrets
- [ ] Input validation on all user inputs
- [ ] SQL injection prevention (parameterized queries)
- [ ] CSRF protection on state-changing operations
- [ ] XSS prevention with proper escaping
- [ ] Authentication checks on protected endpoints
- [ ] Authorization checks on resources
- [ ] Secure password hashing (bcrypt, argon2)
- [ ] No sensitive data in logs
- [ ] HTTPS enforced

## Performance Checklist
- [ ] No N+1 queries
- [ ] Appropriate use of indexes
- [ ] Caching implemented where beneficial
- [ ] No blocking operations on main thread
- [ ] Async/await used correctly
- [ ] Large datasets paginated
- [ ] Database connections pooled
- [ ] Regular expressions optimized
- [ ] No unnecessary object creation
- [ ] Memory leaks prevented

## Quality Checklist
- [ ] Functions < 50 lines
- [ ] Clear variable naming
- [ ] No duplicate code
- [ ] Proper error handling
- [ ] Comments explain WHY, not WHAT
- [ ] No console.logs in production
- [ ] Type checking (TypeScript/JSDoc)
- [ ] SOLID principles followed
- [ ] Design patterns applied correctly
- [ ] Self-documenting code

## Testing Checklist
- [ ] Unit tests written
- [ ] Edge cases covered
- [ ] Error scenarios tested
- [ ] Integration tests present
- [ ] Coverage > 80%
- [ ] No flaky tests
- [ ] Mock external dependencies
- [ ] Clear test names
```

## Template: finding-template.md

~~~~markdown
# Code Review Finding Template

Use this template when documenting each issue found during code review.

---

## Issue: [TITLE]

### Severity
- [ ] Critical (blocks deployment)
- [ ] High (should fix before merge)
- [ ] Medium (should fix soon)
- [ ] Low (nice to have)

### Category
- [ ] Security
- [ ] Performance
- [ ] Code Quality
- [ ] Maintainability
- [ ] Testing
- [ ] Design Pattern
- [ ] Documentation

### Location
**File:** `src/components/UserCard.tsx`

**Lines:** 45-52

**Function/Method:** `renderUserDetails()`

### Issue Description

**What:** Describe what the issue is.

**Why it matters:** Explain the impact and why this needs to be fixed.

**Current behavior:** Show the problematic code or behavior.

**Expected behavior:** Describe what should happen instead.

### Code Example

#### Current (Problematic)

```typescript
// Shows the N+1 query problem
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // Query per user!
  renderUserPosts(posts);
});
```

#### Suggested Fix

```typescript
// Optimized with JOIN query
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### Impact Analysis

| Aspect | Impact | Severity |
|--------|--------|----------|
| Performance | 100+ queries for 20 users | High |
| User Experience | Slow page load | High |
| Scalability | Breaks at scale | Critical |
| Maintainability | Hard to debug | Medium |

### Related Issues

- Similar issue in `AdminUserList.tsx` line 120
- Related PR: #456
- Related issue: #789

### Additional Resources

- [N+1 Query Problem](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Database Join Documentation](https://docs.example.com/joins)

### Reviewer Notes

- This is a common pattern in this codebase
- Consider adding this to the code style guide
- Might be worth creating a helper function

### Author Response (for feedback)

*To be filled by the code author:*

- [ ] Fix implemented in commit: `abc123`
- [ ] Fix status: Complete / In Progress / Needs Discussion
- [ ] Questions or concerns: (describe)

---

## Finding Statistics (for Reviewer)

When reviewing multiple findings, track:

- **Total Issues Found:** X
- **Critical:** X
- **High:** X
- **Medium:** X
- **Low:** X

**Recommendation:** ✅ Approve / ⚠️ Request Changes / 🔄 Needs Discussion

**Overall Code Quality:** 1-5 stars
~~~~

## Ejemplo de Uso

~~~~markdown
User: Review this React component code

Claude: I'll conduct a comprehensive code review using my Code Review Skill.

[Loads SKILL.md]
[Analyzes code against checklist]
[Runs Python metrics script]
[Applies templates]

## Code Review Results

### Summary
Quality Score: 3.5/5
Key Findings: 7 items
Priority Areas: Performance optimization, error handling

### Critical Issues: 1

**Issue**: N+1 Query Problem
**Location**: UserComponent.tsx, lines 45-52
**Impact**: Renders 100+ database queries for list of 20 users
**Severity**: High
**Fix**:
```javascript
// Before: N+1 queries
const users = fetchUsers();
users.forEach(user => fetchUserPosts(user.id)); // 20+ queries

// After: Single query with JOIN
const users = fetchUsersWithPosts(); // 1 query
```

### Performance Findings
- Missing pagination on large lists
- Recommendation: Use React.memo() for items
- Database query: Could be optimized with index

### Quality Findings
- Function in line 20 is 127 lines (max: 50)
- Missing error boundary
- Props should have TypeScript types
~~~~

#### Ejemplo 2: Skill de Voz de Marca

**Estructura de Directorio:**

```
.claude/skills/brand-voice/
├── SKILL.md
├── brand-guidelines.md
├── tone-examples.md
└── templates/
    ├── email-template.txt
    ├── social-post-template.txt
    └── blog-post-template.md
```

**Archivo:** `.claude/skills/brand-voice/SKILL.md`

```yaml
---
name: Brand Voice Consistency
description: Ensure all communication matches brand voice and tone guidelines
tags:
  - brand
  - writing
  - consistency
when_to_use: When creating marketing copy, customer communications, or public-facing content
---

# Brand Voice Skill

## Overview
This skill ensures all communications maintain consistent brand voice, tone, and messaging.

## Brand Identity

### Mission
Help teams automate their development workflows with AI

### Values
- **Simplicity**: Make complex things simple
- **Reliability**: Rock-solid execution
- **Empowerment**: Enable human creativity

### Tone of Voice
- **Friendly but professional** - approachable without being casual
- **Clear and concise** - avoid jargon, explain technical concepts simply
- **Confident** - we know what we're doing
- **Empathetic** - understand user needs and pain points

## Writing Guidelines

### Do's ✅
- Use "you" when addressing readers
- Use active voice: "Claude generates reports" not "Reports are generated by Claude"
- Start with value proposition
- Use concrete examples
- Keep sentences under 20 words
- Use lists for clarity
- Include calls-to-action

### Don'ts ❌
- Don't use corporate jargon
- Don't patronize or oversimplify
- Don't use "we believe" or "we think"
- Don't use ALL CAPS except for emphasis
- Don't create walls of text
- Don't assume technical knowledge

## Vocabulary

### ✅ Preferred Terms
- Claude (not "the Claude AI")
- Code generation (not "auto-coding")
- Agent (not "bot")
- Streamline (not "revolutionize")
- Integrate (not "synergize")

### ❌ Avoid Terms
- "Cutting-edge" (overused)
- "Game-changer" (vague)
- "Leverage" (corporate-speak)
- "Utilize" (use "use")
- "Paradigm shift" (unclear)
```
## Examples

### ✅ Good Example
"Claude automates your code review process. Instead of manually checking each PR, Claude reviews security, performance, and quality—saving your team hours every week."

Why it works: Clear value, specific benefits, action-oriented

### ❌ Bad Example
"Claude leverages cutting-edge AI to provide comprehensive software development solutions."

Why it doesn't work: Vague, corporate jargon, no specific value

## Template: Email

```
Subject: [Clear, benefit-driven subject]

Hi [Name],

[Opening: What's the value for them]

[Body: How it works / What they'll get]

[Specific example or benefit]

[Call to action: Clear next step]

Best regards,
[Name]
```

## Template: Social Media

```
[Hook: Grab attention in first line]
[2-3 lines: Value or interesting fact]
[Call to action: Link, question, or engagement]
[Emoji: 1-2 max for visual interest]
```

## File: tone-examples.md
```
Exciting announcement:
"Save 8 hours per week on code reviews. Claude reviews your PRs automatically."

Empathetic support:
"We know deployments can be stressful. Claude handles testing so you don't have to worry."

Confident product feature:
"Claude doesn't just suggest code. It understands your architecture and maintains consistency."

Educational blog post:
"Let's explore how agents improve code review workflows. Here's what we learned..."
```

#### Ejemplo 3: Skill Generador de Documentacion

**Archivo:** `.claude/skills/doc-generator/SKILL.md`

~~~~yaml
---
name: API Documentation Generator
description: Generate comprehensive, accurate API documentation from source code
version: "1.0.0"
tags:
  - documentation
  - api
  - automation
when_to_use: When creating or updating API documentation
---

# API Documentation Generator Skill

## Generates

- OpenAPI/Swagger specifications
- API endpoint documentation
- SDK usage examples
- Integration guides
- Error code references
- Authentication guides

## Documentation Structure

### For Each Endpoint

```markdown
## GET /api/v1/users/:id

### Description
Brief explanation of what this endpoint does

### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

### Response

**200 Success**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 Not Found**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "User does not exist"
}
```

### Examples

**cURL**
```bash
curl -X GET "https://api.example.com/api/v1/users/usr_123" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**JavaScript**
```javascript
const user = await fetch('/api/v1/users/usr_123', {
  headers: { 'Authorization': 'Bearer token' }
}).then(r => r.json());
```

**Python**
```python
response = requests.get(
    'https://api.example.com/api/v1/users/usr_123',
    headers={'Authorization': 'Bearer token'}
)
user = response.json()
```

## Python Script: generate-docs.py

```python
#!/usr/bin/env python3
import ast
import json
from typing import Dict, List

class APIDocExtractor(ast.NodeVisitor):
    """Extract API documentation from Python source code."""

    def __init__(self):
        self.endpoints = []

    def visit_FunctionDef(self, node):
        """Extract function documentation."""
        if node.name.startswith('get_') or node.name.startswith('post_'):
            doc = ast.get_docstring(node)
            endpoint = {
                'name': node.name,
                'docstring': doc,
                'params': [arg.arg for arg in node.args.args],
                'returns': self._extract_return_type(node)
            }
            self.endpoints.append(endpoint)
        self.generic_visit(node)

    def _extract_return_type(self, node):
        """Extract return type from function annotation."""
        if node.returns:
            return ast.unparse(node.returns)
        return "Any"

def generate_markdown_docs(endpoints: List[Dict]) -> str:
    """Generate markdown documentation from endpoints."""
    docs = "# API Documentation\n\n"

    for endpoint in endpoints:
        docs += f"## {endpoint['name']}\n\n"
        docs += f"{endpoint['docstring']}\n\n"
        docs += f"**Parameters**: {', '.join(endpoint['params'])}\n\n"
        docs += f"**Returns**: {endpoint['returns']}\n\n"
        docs += "---\n\n"

    return docs

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        tree = ast.parse(f.read())

    extractor = APIDocExtractor()
    extractor.visit(tree)

    markdown = generate_markdown_docs(extractor.endpoints)
    print(markdown)
~~~~
### Descubrimiento e Invocacion de Skills

```mermaid
graph TD
    A["User Request"] --> B["Claude Analyzes"]
    B -->|Scans| C["Available Skills"]
    C -->|Metadata check| D["Skill Description Match?"]
    D -->|Yes| E["Load SKILL.md"]
    D -->|No| F["Try next skill"]
    F -->|More skills?| D
    F -->|No more| G["Use general knowledge"]
    E --> H["Extract Instructions"]
    H --> I["Execute Skill"]
    I --> J["Return Results"]
```

### Skills vs Otras Funcionalidades

```mermaid
graph TB
    A["Extending Claude"]
    B["Slash Commands"]
    C["Subagents"]
    D["Memory"]
    E["MCP"]
    F["Skills"]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F

    B -->|User-invoked| G["Quick shortcuts"]
    C -->|Auto-delegated| H["Isolated contexts"]
    D -->|Persistent| I["Cross-session context"]
    E -->|Real-time| J["External data access"]
    F -->|Auto-invoked| K["Autonomous execution"]
```

---

## Claude Code Plugins

### Descripcion General

Los Claude Code Plugins son colecciones agrupadas de personalizaciones (slash commands, subagents, servidores MCP y hooks) que se instalan con un solo comando. Representan el mecanismo de extension de mas alto nivel — combinando multiples funcionalidades en paquetes cohesivos y compartibles.

### Arquitectura

```mermaid
graph TB
    A["Plugin"]
    B["Slash Commands"]
    C["Subagents"]
    D["MCP Servers"]
    E["Hooks"]
    F["Configuration"]

    A -->|bundles| B
    A -->|bundles| C
    A -->|bundles| D
    A -->|bundles| E
    A -->|bundles| F
```

### Proceso de Carga de Plugin

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Plugin as Plugin Marketplace
    participant Install as Installation
    participant SlashCmds as Slash Commands
    participant Subagents
    participant MCPServers as MCP Servers
    participant Hooks
    participant Tools as Configured Tools

    User->>Claude: /plugin install pr-review
    Claude->>Plugin: Download plugin manifest
    Plugin-->>Claude: Return plugin definition
    Claude->>Install: Extract components
    Install->>SlashCmds: Configure
    Install->>Subagents: Configure
    Install->>MCPServers: Configure
    Install->>Hooks: Configure
    SlashCmds-->>Tools: Ready to use
    Subagents-->>Tools: Ready to use
    MCPServers-->>Tools: Ready to use
    Hooks-->>Tools: Ready to use
    Tools-->>Claude: Plugin installed ✅
```

### Tipos y Distribucion de Plugins

| Tipo | Alcance | Compartido | Autoridad | Ejemplos |
|------|-------|--------|-----------|----------|
| Oficial | Global | Todos los usuarios | Anthropic | PR Review, Security Guidance |
| Comunidad | Publico | Todos los usuarios | Comunidad | DevOps, Data Science |
| Organizacion | Interno | Miembros del equipo | Empresa | Estandares internos, herramientas |
| Personal | Individual | Usuario unico | Desarrollador | Workflows personalizados |

### Estructura de Definicion de Plugin

```yaml
---
name: plugin-name
version: "1.0.0"
description: "What this plugin does"
author: "Your Name"
license: MIT

# Plugin metadata
tags:
  - category
  - use-case

# Requirements
requires:
  - claude-code: ">=1.0.0"

# Components bundled
components:
  - type: commands
    path: commands/
  - type: agents
    path: agents/
  - type: mcp
    path: mcp/
  - type: hooks
    path: hooks/

# Configuration
config:
  auto_load: true
  enabled_by_default: true
---
```

### Estructura de Plugin

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── task-1.md
│   ├── task-2.md
│   └── workflows/
├── agents/
│   ├── specialist-1.md
│   ├── specialist-2.md
│   └── configs/
├── skills/
│   ├── skill-1.md
│   └── skill-2.md
├── hooks/
│   └── hooks.json
├── .mcp.json
├── .lsp.json
├── settings.json
├── templates/
│   └── issue-template.md
├── scripts/
│   ├── helper-1.sh
│   └── helper-2.py
├── docs/
│   ├── README.md
│   └── USAGE.md
└── tests/
    └── plugin.test.js
```

### Ejemplos Practicos

#### Ejemplo 1: Plugin PR Review

**Archivo:** `.claude-plugin/plugin.json`

```json
{
  "name": "pr-review",
  "version": "1.0.0",
  "description": "Complete PR review workflow with security, testing, and docs",
  "author": {
    "name": "Anthropic"
  },
  "license": "MIT"
}
```

**Archivo:** `commands/review-pr.md`

```markdown
---
name: Review PR
description: Start comprehensive PR review with security and testing checks
---

# PR Review

This command initiates a complete pull request review including:

1. Security analysis
2. Test coverage verification
3. Documentation updates
4. Code quality checks
5. Performance impact assessment
```

**Archivo:** `agents/security-reviewer.md`

```yaml
---
name: security-reviewer
description: Security-focused code review
tools: read, grep, diff
---

# Security Reviewer

Specializes in finding security vulnerabilities:
- Authentication/authorization issues
- Data exposure
- Injection attacks
- Secure configuration
```

**Instalacion:**

```bash
/plugin install pr-review

# Resultado:
# ✅ 3 slash commands installed
# ✅ 3 subagents configured
# ✅ 2 MCP servers connected
# ✅ 4 hooks registered
# ✅ Ready to use!
```

#### Ejemplo 2: Plugin DevOps

**Componentes:**

```
devops-automation/
├── commands/
│   ├── deploy.md
│   ├── rollback.md
│   ├── status.md
│   └── incident.md
├── agents/
│   ├── deployment-specialist.md
│   ├── incident-commander.md
│   └── alert-analyzer.md
├── mcp/
│   ├── github-config.json
│   ├── kubernetes-config.json
│   └── prometheus-config.json
├── hooks/
│   ├── pre-deploy.js
│   ├── post-deploy.js
│   └── on-error.js
└── scripts/
    ├── deploy.sh
    ├── rollback.sh
    └── health-check.sh
```

#### Ejemplo 3: Plugin de Documentacion

**Componentes Agrupados:**

```
documentation/
├── commands/
│   ├── generate-api-docs.md
│   ├── generate-readme.md
│   ├── sync-docs.md
│   └── validate-docs.md
├── agents/
│   ├── api-documenter.md
│   ├── code-commentator.md
│   └── example-generator.md
├── mcp/
│   ├── github-docs-config.json
│   └── slack-announce-config.json
└── templates/
    ├── api-endpoint.md
    ├── function-docs.md
    └── adr-template.md
```

### Marketplace de Plugins

```mermaid
graph TB
    A["Plugin Marketplace"]
    B["Official<br/>Anthropic"]
    C["Community<br/>Marketplace"]
    D["Enterprise<br/>Registry"]

    A --> B
    A --> C
    A --> D

    B -->|Categories| B1["Development"]
    B -->|Categories| B2["DevOps"]
    B -->|Categories| B3["Documentation"]

    C -->|Search| C1["DevOps Automation"]
    C -->|Search| C2["Mobile Dev"]
    C -->|Search| C3["Data Science"]

    D -->|Internal| D1["Company Standards"]
    D -->|Internal| D2["Legacy Systems"]
    D -->|Internal| D3["Compliance"]
```

### Instalacion y Ciclo de Vida de un Plugin

```mermaid
graph LR
    A["Discover"] -->|Browse| B["Marketplace"]
    B -->|Select| C["Plugin Page"]
    C -->|View| D["Components"]
    D -->|Install| E["/plugin install"]
    E -->|Extract| F["Configure"]
    F -->|Activate| G["Use"]
    G -->|Check| H["Update"]
    H -->|Available| G
    G -->|Done| I["Disable"]
    I -->|Later| J["Enable"]
    J -->|Back| G
```

### Comparacion de Funcionalidades de Plugins

| Funcionalidad | Slash Command | Skill | Subagent | Plugin |
|---------|---------------|-------|----------|--------|
| **Instalacion** | Copia manual | Copia manual | Config manual | Un comando |
| **Tiempo de Configuracion** | 5 minutos | 10 minutos | 15 minutos | 2 minutos |
| **Agrupacion** | Archivo unico | Archivo unico | Archivo unico | Multiples |
| **Versionado** | Manual | Manual | Manual | Automatico |
| **Compartir con Equipo** | Copiar archivo | Copiar archivo | Copiar archivo | ID de instalacion |
| **Actualizaciones** | Manual | Manual | Manual | Disponible automaticamente |
| **Dependencias** | Ninguna | Ninguna | Ninguna | Puede incluir |
| **Marketplace** | No | No | No | Si |
| **Distribucion** | Repositorio | Repositorio | Repositorio | Marketplace |

### Casos de Uso de Plugins

| Caso de Uso | Recomendacion | Por que |
|----------|-----------------|-----|
| **Incorporacion de Equipo** | ✅ Usar Plugin | Configuracion instantanea, todas las configuraciones |
| **Configuracion de Framework** | ✅ Usar Plugin | Agrupa comandos especificos del framework |
| **Estandares Enterprise** | ✅ Usar Plugin | Distribucion central, control de versiones |
| **Automatizacion Rapida de Tareas** | ❌ Usar Command | Complejidad excesiva |
| **Experiencia de Dominio Unico** | ❌ Usar Skill | Demasiado pesado, usar skill en su lugar |
| **Analisis Especializado** | ❌ Usar Subagent | Crear manualmente o usar skill |
| **Acceso a Datos en Vivo** | ❌ Usar MCP | Independiente, no agrupar |

### Cuando Crear un Plugin

```mermaid
graph TD
    A["Should I create a plugin?"]
    A -->|Need multiple components| B{"Multiple commands<br/>or subagents<br/>or MCPs?"}
    B -->|Yes| C["✅ Create Plugin"]
    B -->|No| D["Use Individual Feature"]
    A -->|Team workflow| E{"Share with<br/>team?"}
    E -->|Yes| C
    E -->|No| F["Keep as Local Setup"]
    A -->|Complex setup| G{"Needs auto<br/>configuration?"}
    G -->|Yes| C
    G -->|No| D
```

### Publicar un Plugin

**Pasos para publicar:**

1. Crear la estructura del plugin con todos los componentes
2. Escribir el manifiesto `.claude-plugin/plugin.json`
3. Crear `README.md` con documentacion
4. Probar localmente con `/plugin install ./my-plugin`
5. Enviar al marketplace de plugins
6. Ser revisado y aprobado
7. Publicado en el marketplace
8. Los usuarios pueden instalar con un solo comando

**Ejemplo de envio:**

~~~~markdown
# PR Review Plugin

## Description
Complete PR review workflow with security, testing, and documentation checks.

## What's Included
- 3 slash commands for different review types
- 3 specialized subagents
- GitHub and CodeQL MCP integration
- Automated security scanning hooks

## Installation
```bash
/plugin install pr-review
```

## Features
✅ Security analysis
✅ Test coverage checking
✅ Documentation verification
✅ Code quality assessment
✅ Performance impact analysis

## Usage
```bash
/review-pr
/check-security
/check-tests
```

## Requirements
- Claude Code 1.0+
- GitHub access
- CodeQL (optional)
~~~~

### Plugin vs Configuracion Manual

**Configuracion Manual (2+ horas):**
- Instalar slash commands uno por uno
- Crear subagents individualmente
- Configurar MCPs por separado
- Configurar hooks manualmente
- Documentar todo
- Compartir con el equipo (esperando que lo configuren correctamente)

**Con Plugin (2 minutos):**
```bash
/plugin install pr-review
# ✅ Everything installed and configured
# ✅ Ready to use immediately
# ✅ Team can reproduce exact setup
```

---

## Comparison & Integration

### Matriz de Comparacion de Funcionalidades

| Funcionalidad | Invocacion | Persistencia | Alcance | Caso de Uso |
|---------|-----------|------------|-------|----------|
| **Slash Commands** | Manual (`/cmd`) | Solo sesion | Comando unico | Atajos rapidos |
| **Subagents** | Delegacion automatica | Contexto aislado | Tarea especializada | Distribucion de tareas |
| **Memory** | Carga automatica | Multi-sesion | Contexto usuario/equipo | Aprendizaje a largo plazo |
| **MCP Protocol** | Consulta automatica | Externo en tiempo real | Acceso a datos en vivo | Informacion dinamica |
| **Skills** | Invocacion automatica | Basado en filesystem | Experiencia reutilizable | Workflows automatizados |

### Linea de Tiempo de Interaccion

```mermaid
graph LR
    A["Session Start"] -->|Load| B["Memory (CLAUDE.md)"]
    B -->|Discover| C["Available Skills"]
    C -->|Register| D["Slash Commands"]
    D -->|Connect| E["MCP Servers"]
    E -->|Ready| F["User Interaction"]

    F -->|Type /cmd| G["Slash Command"]
    F -->|Request| H["Skill Auto-Invoke"]
    F -->|Query| I["MCP Data"]
    F -->|Complex task| J["Delegate to Subagent"]

    G -->|Uses| B
    H -->|Uses| B
    I -->|Uses| B
    J -->|Uses| B
```

### Ejemplo de Integracion Practica: Automatizacion de Soporte al Cliente

#### Arquitectura

```mermaid
graph TB
    User["Customer Email"] -->|Receives| Router["Support Router"]

    Router -->|Analyze| Memory["Memory<br/>Customer history"]
    Router -->|Lookup| MCP1["MCP: Customer DB<br/>Previous tickets"]
    Router -->|Check| MCP2["MCP: Slack<br/>Team status"]

    Router -->|Route Complex| Sub1["Subagent: Tech Support<br/>Context: Technical issues"]
    Router -->|Route Simple| Sub2["Subagent: Billing<br/>Context: Payment issues"]
    Router -->|Route Urgent| Sub3["Subagent: Escalation<br/>Context: Priority handling"]

    Sub1 -->|Format| Skill1["Skill: Response Generator<br/>Brand voice maintained"]
    Sub2 -->|Format| Skill2["Skill: Response Generator"]
    Sub3 -->|Format| Skill3["Skill: Response Generator"]

    Skill1 -->|Generate| Output["Formatted Response"]
    Skill2 -->|Generate| Output
    Skill3 -->|Generate| Output

    Output -->|Post| MCP3["MCP: Slack<br/>Notify team"]
    Output -->|Send| Reply["Customer Reply"]
```

#### Flujo de Solicitudes

```markdown
## Customer Support Request Flow

### 1. Incoming Email
"I'm getting error 500 when trying to upload files. This is blocking my workflow!"

### 2. Memory Lookup
- Loads CLAUDE.md with support standards
- Checks customer history: VIP customer, 3rd incident this month

### 3. MCP Queries
- GitHub MCP: List open issues (finds related bug report)
- Database MCP: Check system status (no outages reported)
- Slack MCP: Check if engineering is aware

### 4. Skill Detection & Loading
- Request matches "Technical Support" skill
- Loads support response template from Skill

### 5. Subagent Delegation
- Routes to Tech Support Subagent
- Provides context: customer history, error details, known issues
- Subagent has full access to: read, bash, grep tools

### 6. Subagent Processing
Tech Support Subagent:
- Searches codebase for 500 error in file upload
- Finds recent change in commit 8f4a2c
- Creates workaround documentation

### 7. Skill Execution
Response Generator Skill:
- Uses Brand Voice guidelines
- Formats response with empathy
- Includes workaround steps
- Links to related documentation

### 8. MCP Output
- Posts update to #support Slack channel
- Tags engineering team
- Updates ticket in Jira MCP

### 9. Response
Customer receives:
- Empathetic acknowledgment
- Explanation of cause
- Immediate workaround
- Timeline for permanent fix
- Link to related issues
```

### Orquestacion Completa de Funcionalidades

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Memory as Memory<br/>CLAUDE.md
    participant MCP as MCP Servers
    participant Skills as Skills
    participant SubAgent as Subagents

    User->>Claude: Request: "Build auth system"
    Claude->>Memory: Load project standards
    Memory-->>Claude: Auth standards, team practices
    Claude->>MCP: Query GitHub for similar implementations
    MCP-->>Claude: Code examples, best practices
    Claude->>Skills: Detect matching Skills
    Skills-->>Claude: Security Review Skill + Testing Skill
    Claude->>SubAgent: Delegate implementation
    SubAgent->>SubAgent: Build feature
    Claude->>Skills: Apply Security Review Skill
    Skills-->>Claude: Security checklist results
    Claude->>SubAgent: Delegate testing
    SubAgent-->>Claude: Test results
    Claude->>User: Complete system delivered
```

### Cuando Usar Cada Funcionalidad

```mermaid
graph TD
    A["New Task"] --> B{Type of Task?}

    B -->|Repeated workflow| C["Slash Command"]
    B -->|Need real-time data| D["MCP Protocol"]
    B -->|Remember for next time| E["Memory"]
    B -->|Specialized subtask| F["Subagent"]
    B -->|Domain-specific work| G["Skill"]

    C --> C1["✅ Team shortcut"]
    D --> D1["✅ Live API access"]
    E --> E1["✅ Persistent context"]
    F --> F1["✅ Parallel execution"]
    G --> G1["✅ Auto-invoked expertise"]
```

### Arbol de Decision de Seleccion

```mermaid
graph TD
    Start["Need to extend Claude?"]

    Start -->|Quick repeated task| A{"Manual or Auto?"}
    A -->|Manual| B["Slash Command"]
    A -->|Auto| C["Skill"]

    Start -->|Need external data| D{"Real-time?"}
    D -->|Yes| E["MCP Protocol"]
    D -->|No/Cross-session| F["Memory"]

    Start -->|Complex project| G{"Multiple roles?"}
    G -->|Yes| H["Subagents"]
    G -->|No| I["Skills + Memory"]

    Start -->|Long-term context| J["Memory"]
    Start -->|Team workflow| K["Slash Command +<br/>Memory"]
    Start -->|Full automation| L["Skills +<br/>Subagents +<br/>MCP"]
```

---

## Tabla de Resumen

| Aspecto | Slash Commands | Subagents | Memory | MCP | Skills | Plugins |
|--------|---|---|---|---|---|---|
| **Dificultad de Configuracion** | Facil | Media | Facil | Media | Media | Facil |
| **Curva de Aprendizaje** | Baja | Media | Baja | Media | Media | Baja |
| **Beneficio para el Equipo** | Alto | Alto | Medio | Alto | Alto | Muy Alto |
| **Nivel de Automatizacion** | Bajo | Alto | Medio | Alto | Alto | Muy Alto |
| **Gestion del Contexto** | Una sesion | Aislado | Persistente | Tiempo real | Persistente | Todas las funcionalidades |
| **Carga de Mantenimiento** | Baja | Media | Baja | Media | Media | Baja |
| **Escalabilidad** | Buena | Excelente | Buena | Excelente | Excelente | Excelente |
| **Facilidad de Compartir** | Regular | Regular | Buena | Buena | Buena | Excelente |
| **Versionado** | Manual | Manual | Manual | Manual | Manual | Automatico |
| **Instalacion** | Copia manual | Config manual | N/A | Config manual | Copia manual | Un comando |

---

## Guia de Inicio Rapido

### Semana 1: Comenzar Simple
- Crear 2-3 slash commands para tareas frecuentes
- Habilitar Memory en Configuracion
- Documentar estandares del equipo en CLAUDE.md

### Semana 2: Agregar Acceso en Tiempo Real
- Configurar 1 MCP (GitHub o Database)
- Usar `/mcp` para configurar
- Consultar datos en vivo en tus workflows

### Semana 3: Distribuir el Trabajo
- Crear primer Subagent para un rol especifico
- Usar el comando `/agents`
- Probar la delegacion con una tarea simple

### Semana 4: Automatizar Todo
- Crear primer Skill para automatizacion repetida
- Usar el marketplace de Skills o construir uno personalizado
- Combinar todas las funcionalidades para un workflow completo

### En Adelante
- Revisar y actualizar Memory mensualmente
- Agregar nuevos Skills a medida que surjan patrones
- Optimizar consultas MCP
- Refinar prompts de Subagents

---

## Hooks

### Descripcion General

Los Hooks son comandos de shell disparados por eventos que se ejecutan automaticamente en respuesta a eventos de Claude Code. Permiten automatizacion, validacion y workflows personalizados sin intervencion manual.

### Eventos de Hook

Claude Code soporta **25 eventos de hook** en cuatro tipos de hooks (command, http, prompt, agent):

| Evento de Hook | Disparador | Casos de Uso |
|------------|---------|-----------|
| **SessionStart** | La sesion comienza/se reanuda/se limpia/se compacta | Configuracion del entorno, inicializacion |
| **InstructionsLoaded** | Se carga CLAUDE.md o un archivo de reglas | Validacion, transformacion, aumentacion |
| **UserPromptSubmit** | El usuario envia un prompt | Validacion de entrada, filtrado de prompts |
| **PreToolUse** | Antes de que se ejecute cualquier herramienta | Validacion, puertas de aprobacion, logging |
| **PermissionRequest** | Se muestra el dialogo de permisos | Flujos de auto-aprobacion/denegacion |
| **PostToolUse** | Despues de que la herramienta tiene exito | Auto-formateo, notificaciones, limpieza |
| **PostToolUseFailure** | La ejecucion de la herramienta falla | Manejo de errores, logging |
| **Notification** | Se envia una notificacion | Alertas, integraciones externas |
| **SubagentStart** | Se lanza un subagent | Inyeccion de contexto, inicializacion |
| **SubagentStop** | El subagent termina | Validacion de resultados, logging |
| **Stop** | Claude termina de responder | Generacion de resumen, tareas de limpieza |
| **StopFailure** | Un error de API termina el turno | Recuperacion de errores, logging |
| **TeammateIdle** | Un agente del equipo esta inactivo | Distribucion de trabajo, coordinacion |
| **TaskCompleted** | La tarea se marca como completa | Procesamiento post-tarea |
| **TaskCreated** | La tarea se crea via TaskCreate | Seguimiento de tareas, logging |
| **ConfigChange** | Los archivos de configuracion cambian | Validacion, propagacion |
| **CwdChanged** | El directorio de trabajo cambia | Configuracion especifica del directorio |
| **FileChanged** | Un archivo vigilado cambia | Monitoreo de archivos, disparadores de reconstruccion |
| **PreCompact** | Antes de la compactacion del contexto | Preservacion del estado |
| **PostCompact** | Despues de que la compactacion se completa | Acciones post-compactacion |
| **WorktreeCreate** | Se esta creando un worktree | Configuracion del entorno, instalacion de dependencias |
| **WorktreeRemove** | Se esta eliminando un worktree | Limpieza, desasignacion de recursos |
| **Elicitation** | El servidor MCP solicita entrada del usuario | Validacion de entrada |
| **ElicitationResult** | El usuario responde a una elicitacion | Procesamiento de la respuesta |
| **SessionEnd** | La sesion termina | Limpieza, logging final |

### Hooks Comunes

Los hooks se configuran en `~/.claude/settings.json` (nivel de usuario) o `.claude/settings.json` (nivel de proyecto):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write $CLAUDE_FILE_PATH"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "eslint $CLAUDE_FILE_PATH"
          }
        ]
      }
    ]
  }
}
```

### Variables de Entorno de Hooks

- `$CLAUDE_FILE_PATH` - Ruta al archivo que se esta editando/escribiendo
- `$CLAUDE_TOOL_NAME` - Nombre de la herramienta que se esta usando
- `$CLAUDE_SESSION_ID` - Identificador de la sesion actual
- `$CLAUDE_PROJECT_DIR` - Ruta del directorio del proyecto

### Buenas Practicas

✅ **Hacer:**
- Mantener los hooks rapidos (< 1 segundo)
- Usar hooks para validacion y automatizacion
- Manejar errores con gracia
- Usar rutas absolutas

❌ **No Hacer:**
- Hacer los hooks interactivos
- Usar hooks para tareas de larga duracion
- Hardcodear credenciales

**Ver**: [06-hooks/](06-hooks/) para ejemplos detallados

---

## Checkpoints and Rewind

### Descripcion General

Los Checkpoints te permiten guardar el estado de la conversacion y volver a puntos anteriores, habilitando la experimentacion segura y la exploracion de multiples enfoques.

### Conceptos Clave

| Concepto | Descripcion |
|---------|-------------|
| **Checkpoint** | Instantanea del estado de la conversacion incluyendo mensajes, archivos y contexto |
| **Rewind** | Volver a un checkpoint anterior, descartando los cambios posteriores |
| **Branch Point** | Checkpoint desde el cual se exploran multiples enfoques |

### Acceder a los Checkpoints

Los checkpoints se crean automaticamente con cada prompt del usuario. Para volver atras:

```bash
# Presionar Esc dos veces para abrir el navegador de checkpoints
Esc + Esc

# O usar el comando /rewind
/rewind
```

Cuando seleccionas un checkpoint, puedes elegir entre cinco opciones:
1. **Restore code and conversation** -- Revertir ambos a ese punto
2. **Restore conversation** -- Rebobinar mensajes, mantener el codigo actual
3. **Restore code** -- Revertir archivos, mantener la conversacion
4. **Summarize from here** -- Comprimir la conversacion en un resumen
5. **Never mind** -- Cancelar

### Casos de Uso

| Escenario | Workflow |
|----------|----------|
| **Explorar Enfoques** | Guardar → Probar A → Guardar → Rewind → Probar B → Comparar |
| **Refactorizacion Segura** | Guardar → Refactorizar → Probar → Si falla: Rewind |
| **Pruebas A/B** | Guardar → Diseno A → Guardar → Rewind → Diseno B → Comparar |
| **Recuperacion de Errores** | Detectar problema → Rewind al ultimo estado bueno |

### Configuracion

```json
{
  "autoCheckpoint": true
}
```

**Ver**: [08-checkpoints/](08-checkpoints/) para ejemplos detallados

---

## Advanced Features

### Planning Mode

Crea planes de implementacion detallados antes de codificar.

**Activacion:**
```bash
/plan Implement user authentication system
```

**Beneficios:**
- Hoja de ruta clara con estimaciones de tiempo
- Evaluacion de riesgos
- Desglose sistematico de tareas
- Oportunidad de revision y modificacion

### Extended Thinking

Razonamiento profundo para problemas complejos.

**Activacion:**
- Alternar con `Alt+T` (o `Option+T` en macOS) durante una sesion
- Establecer la variable de entorno `MAX_THINKING_TOKENS` para control programatico

```bash
# Enable extended thinking via environment variable
export MAX_THINKING_TOKENS=50000
claude -p "Should we use microservices or monolith?"
```

**Beneficios:**
- Analisis exhaustivo de compensaciones
- Mejores decisiones arquitectonicas
- Consideracion de casos borde
- Evaluacion sistematica

### Background Tasks

Ejecutar operaciones largas sin bloquear la conversacion.

**Uso:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Show all tasks
/task status bg-1234 # Check progress
/task show bg-1234   # View output
/task cancel bg-1234 # Cancel task
```

### Permission Modes

Controlar lo que Claude puede hacer.

| Modo | Descripcion | Caso de Uso |
|------|-------------|----------|
| **default** | Permisos estandar con prompts para acciones sensibles | Desarrollo general |
| **acceptEdits** | Aceptar automaticamente ediciones de archivos sin confirmacion | Workflows de edicion de confianza |
| **plan** | Solo analisis y planificacion, sin modificacion de archivos | Revision de codigo, planificacion de arquitectura |
| **auto** | Aprobar automaticamente acciones seguras, pedir solo para las riesgosas | Autonomia equilibrada con seguridad |
| **dontAsk** | Ejecutar todas las acciones sin prompts de confirmacion | Usuarios experimentados, automatizacion |
| **bypassPermissions** | Acceso completo sin restricciones, sin verificaciones de seguridad | Pipelines CI/CD, scripts de confianza |

**Uso:**
```bash
claude --permission-mode plan          # Read-only analysis
claude --permission-mode acceptEdits   # Auto-accept edits
claude --permission-mode auto          # Auto-approve safe actions
claude --permission-mode dontAsk       # No confirmation prompts
```

### Headless Mode (Print Mode)

Ejecutar Claude Code sin entrada interactiva para automatizacion y CI/CD usando el flag `-p` (print).

**Uso:**
```bash
# Run specific task
claude -p "Run all tests"

# Pipe input for analysis
cat error.log | claude -p "explain this error"

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR changes and report issues"

# JSON output for scripting
claude -p --output-format json "list all functions in src/"
```

### Scheduled Tasks

Ejecutar tareas en un horario repetido usando el comando `/loop`.

**Uso:**
```bash
/loop every 30m "Run tests and report failures"
/loop every 2h "Check for dependency updates"
/loop every 1d "Generate daily summary of code changes"
```

Las tareas programadas se ejecutan en segundo plano y reportan los resultados al completarse. Son utiles para monitoreo continuo, verificaciones periodicas y workflows de mantenimiento automatizado.

### Chrome Integration

Claude Code puede integrarse con el navegador Chrome para tareas de automatizacion web. Esto habilita capacidades como navegar paginas web, completar formularios, tomar capturas de pantalla y extraer datos de sitios web directamente dentro de tu workflow de desarrollo.

### Session Management

Gestionar multiples sesiones de trabajo.

**Comandos:**
```bash
/resume                # Resume a previous conversation
/rename "Feature"      # Name the current session
/fork                  # Fork into a new session
claude -c              # Continue most recent conversation
claude -r "Feature"    # Resume session by name/ID
```

### Interactive Features

**Atajos de Teclado:**
- `Ctrl + R` - Buscar en el historial de comandos
- `Tab` - Autocompletar
- `↑ / ↓` - Historial de comandos
- `Ctrl + L` - Limpiar pantalla

**Entrada Multi-linea:**
```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

### Configuracion

Ejemplo de configuracion completa:

```json
{
  "planning": {
    "autoEnter": true,
    "requireApproval": true
  },
  "extendedThinking": {
    "enabled": true,
    "showThinkingProcess": true
  },
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5
  },
  "permissions": {
    "mode": "default"
  }
}
```

**Ver**: [09-advanced-features/](09-advanced-features/) para guia completa

---

## Resources

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [Anthropic Documentation](https://docs.anthropic.com)
- [MCP GitHub Servers](https://github.com/modelcontextprotocol/servers)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

---

*Ultima Actualizacion: Abril 2026*
*Para Claude Haiku 4.5, Sonnet 4.6 y Opus 4.6*
*Incluye ahora: Hooks, Checkpoints, Planning Mode, Extended Thinking, Background Tasks, Permission Modes (6 modos), Headless Mode, Session Management, Auto Memory, Agent Teams, Scheduled Tasks, Chrome Integration, Channels, Voice Dictation y Bundled Skills*

---
**Ultima Actualizacion**: Abril 2026
**Claude Code Version**: 2.1+
