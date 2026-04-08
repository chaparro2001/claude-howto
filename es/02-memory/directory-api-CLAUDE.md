# Estandares del Modulo API

Este archivo sobrescribe el CLAUDE.md raiz para todo en /src/api/

## Estandares Especificos de la API

### Validacion de Requests

- Usar Zod para validacion de schemas
- Siempre validar input
- Retornar 400 con errores de validacion
- Incluir detalles de error a nivel de campo

### Autenticacion

- Todos los endpoints requieren token JWT
- Token en header Authorization
- El token expira despues de 24 horas
- Implementar mecanismo de refresh token

### Formato de Respuesta

Todas las respuestas deben seguir esta estructura:

```json
{
  "success": true,
  "data": { /* datos reales */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

Respuestas de error:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Mensaje para el usuario",
    "details": { /* errores por campo */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Paginacion

- Usar paginacion basada en cursor (no offset)
- Incluir boolean `hasMore`
- Limitar tamano maximo de pagina a 100
- Tamano de pagina por defecto: 20

### Rate Limiting

- 1000 requests por hora para usuarios autenticados
- 100 requests por hora para endpoints publicos
- Retornar 429 cuando se exceda
- Incluir header retry-after

### Caching

- Usar Redis para caching de sesiones
- Duracion de cache: 5 minutos por defecto
- Invalidar en operaciones de escritura
- Etiquetar claves de cache con tipo de recurso

---

**Ultima Actualizacion**: Abril 2026
