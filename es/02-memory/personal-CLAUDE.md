# Mis Preferencias de Desarrollo

## Sobre Mi

- **Nivel de Experiencia**: 8 anios de desarrollo full-stack
- **Lenguajes Preferidos**: TypeScript, Python
- **Estilo de Comunicacion**: Directo, con ejemplos
- **Estilo de Aprendizaje**: Diagramas visuales con codigo

## Preferencias de Codigo

### Manejo de Errores

Prefiero manejo explicito de errores con bloques try-catch y mensajes de error significativos.
Evitar errores genericos. Siempre logear errores para debugging.

### Comentarios

Usar comentarios para el POR QUE, no el QUE. El codigo debe ser auto-documentado.
Los comentarios deben explicar logica de negocio o decisiones no obvias.

### Testing

Prefiero TDD (test-driven development).
Escribir tests primero, luego la implementacion.
Enfocar en comportamiento, no en detalles de implementacion.

### Arquitectura

Prefiero diseno modular y desacoplado.
Usar inyeccion de dependencias para testabilidad.
Separar responsabilidades (Controllers, Services, Repositories).

## Preferencias de Debugging

- Usar console.log con prefijo: `[DEBUG]`
- Incluir contexto: nombre de funcion, variables relevantes
- Usar stack traces cuando esten disponibles
- Siempre incluir timestamps en los logs

## Comunicacion

- Explicar conceptos complejos con diagramas
- Mostrar ejemplos concretos antes de explicar teoria
- Incluir snippets de codigo antes/despues
- Resumir puntos clave al final

## Organizacion de Proyectos

Organizo mis proyectos asi:

```text
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

## Herramientas

- **IDE**: VS Code con keybindings de vim
- **Terminal**: Zsh con Oh-My-Zsh
- **Formateo**: Prettier (100 caracteres por linea)
- **Linter**: ESLint con config airbnb
- **Framework de Test**: Jest con React Testing Library

---

**Ultima Actualizacion**: Abril 2026
