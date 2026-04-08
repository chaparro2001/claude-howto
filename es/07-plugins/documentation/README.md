<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Plugin de documentacion

Generacion y mantenimiento integral de documentacion para tu proyecto.

## Funcionalidades

✅ Generacion de documentacion de API
✅ Creacion y actualizacion de README
✅ Sincronizacion de documentacion
✅ Mejoras en comentarios de codigo
✅ Generacion de ejemplos

## Instalacion

```bash
/plugin install documentation
```

## Que incluye

### Slash Commands
- `/generate-api-docs` - Generar documentacion de API
- `/generate-readme` - Crear o actualizar README
- `/sync-docs` - Sincronizar docs con cambios de codigo
- `/validate-docs` - Validar documentacion

### Subagentes
- `api-documenter` - Especialista en documentacion de API
- `code-commentator` - Mejoras de comentarios en codigo
- `example-generator` - Creacion de ejemplos de codigo

### Templates
- `api-endpoint.md` - Template de documentacion de endpoint de API
- `function-docs.md` - Template de documentacion de funciones
- `adr-template.md` - Template de Architecture Decision Record

### Servidores MCP
- Integracion con GitHub para sincronizacion de documentacion

## Uso

### Generar documentacion de API
```
/generate-api-docs
```

### Crear README
```
/generate-readme
```

### Sincronizar documentacion
```
/sync-docs
```

### Validar documentacion
```
/validate-docs
```

## Requisitos

- Claude Code 1.0+
- Acceso a GitHub (opcional)

## Ejemplo de workflow

```
User: /generate-api-docs

Claude:
1. Scans all API endpoints in /src/api/
2. Delegates to api-documenter subagent
3. Extracts function signatures and JSDoc
4. Organizes by module/endpoint
5. Uses api-endpoint.md template
6. Generates comprehensive markdown docs
7. Includes curl, JavaScript, and Python examples

Result:
✅ API documentation generated
📄 Files created:
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 Coverage: 23/23 endpoints documented
```

## Uso de templates

### Template de endpoint de API
Usar para documentar endpoints de API REST con ejemplos completos.

### Template de documentacion de funciones
Usar para documentar funciones o metodos individuales.

### Template ADR
Usar para documentar decisiones de arquitectura.

## Configuracion

Configurar el token de GitHub para sincronizacion de documentacion:
```bash
export GITHUB_TOKEN="your_github_token"
```

## Buenas practicas

- Mantener la documentacion cerca del codigo
- Actualizar los docs con los cambios de codigo
- Incluir ejemplos practicos
- Validar regularmente
- Usar templates para consistencia
