<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Cómo contribuir a Claude How To

Gracias por tu interés en contribuir a este proyecto. Esta guía te ayudará a entender cómo hacerlo de manera efectiva.

## Acerca de este proyecto

Claude How To es una guía visual y orientada a ejemplos para Claude Code. Ofrecemos:
- **Diagramas Mermaid** que explican cómo funcionan las funcionalidades
- **Templates listos para producción** que puedes usar de inmediato
- **Ejemplos del mundo real** con contexto y buenas prácticas
- **Rutas de aprendizaje progresivas** desde principiante hasta avanzado

## Tipos de contribuciones

### 1. Nuevos ejemplos o templates
Agrega ejemplos para funcionalidades existentes (slash commands, skills, hooks, etc.):
- Código listo para copiar y pegar
- Explicaciones claras de cómo funciona
- Casos de uso y beneficios
- Consejos para solución de problemas

### 2. Mejoras a la documentación
- Aclarar secciones confusas
- Corregir errores tipográficos y gramaticales
- Agregar información faltante
- Mejorar ejemplos de código

### 3. Guías de funcionalidades
Crear guías para nuevas funcionalidades de Claude Code:
- Tutoriales paso a paso
- Diagramas de arquitectura
- Patrones comunes y anti-patrones
- Workflows del mundo real

### 4. Reportes de errores
Reportar problemas que encuentres:
- Describir qué esperabas
- Describir qué ocurrió realmente
- Incluir pasos para reproducirlo
- Agregar versión de Claude Code y sistema operativo

### 5. Comentarios y sugerencias
Ayudá a mejorar la guía:
- Sugerir mejores explicaciones
- Señalar vacíos en la cobertura
- Recomendar nuevas secciones o reorganización

## Cómo empezar

### 1. Fork y clonación
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2. Crear un branch
Usa un nombre descriptivo para el branch:
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3. Configurar tu entorno

Los pre-commit hooks ejecutan las mismas verificaciones que el CI de manera local antes de cada commit. Las cuatro verificaciones deben pasar antes de que se acepte un PR.

**Dependencias requeridas:**

```bash
# Herramientas Python (uv es el gestor de paquetes de este proyecto)
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Linter de Markdown (Node.js)
npm install -g markdownlint-cli

# Validador de diagramas Mermaid (Node.js)
npm install -g @mermaid-js/mermaid-cli

# Instalar pre-commit y activar los hooks
uv pip install pre-commit
pre-commit install
```

**Verificar tu configuración:**

```bash
pre-commit run --all-files
```

Los hooks que se ejecutan en cada commit son:

| Hook | Qué verifica |
|------|---------------|
| `markdown-lint` | Formato y estructura del Markdown |
| `cross-references` | Links relativos, anclas, bloques de código |
| `mermaid-syntax` | Que todos los bloques ` ```mermaid ` se parseen correctamente |
| `link-check` | Que las URLs externas sean accesibles |
| `build-epub` | Que el EPUB se genere sin errores (en cambios a `.md`) |

## Estructura de directorios

```
├── 01-slash-commands/      # Atajos invocados por el usuario
├── 02-memory/              # Ejemplos de contexto persistente
├── 03-skills/              # Capacidades reutilizables
├── 04-subagents/           # Asistentes de IA especializados
├── 05-mcp/                 # Ejemplos de Model Context Protocol
├── 06-hooks/               # Automatización basada en eventos
├── 07-plugins/             # Funcionalidades empaquetadas
├── 08-checkpoints/         # Snapshots de sesión
├── 09-advanced-features/   # Planificación, pensamiento, backgrounds
├── 10-cli/                 # Referencia del CLI
├── scripts/                # Scripts de construcción y utilidades
└── README.md               # Guía principal
```

## Cómo contribuir con ejemplos

### Agregar un slash command
1. Crear un archivo `.md` en `01-slash-commands/`
2. Incluir:
   - Descripción clara de qué hace
   - Casos de uso
   - Instrucciones de instalación
   - Ejemplos de uso
   - Consejos de personalización
3. Actualizar `01-slash-commands/README.md`

### Agregar una skill
1. Crear un directorio en `03-skills/`
2. Incluir:
   - `SKILL.md` - Documentación principal
   - `scripts/` - Scripts auxiliares si son necesarios
   - `templates/` - Templates de prompt
   - Ejemplo de uso en el README
3. Actualizar `03-skills/README.md`

### Agregar un subagente
1. Crear un archivo `.md` en `04-subagents/`
2. Incluir:
   - Propósito y capacidades del agente
   - Estructura del system prompt
   - Casos de uso de ejemplo
   - Ejemplos de integración
3. Actualizar `04-subagents/README.md`

### Agregar una configuración MCP
1. Crear un archivo `.json` en `05-mcp/`
2. Incluir:
   - Explicación de la configuración
   - Variables de entorno requeridas
   - Instrucciones de configuración
   - Ejemplos de uso
3. Actualizar `05-mcp/README.md`

### Agregar un hook
1. Crear un archivo `.sh` en `06-hooks/`
2. Incluir:
   - Shebang y descripción
   - Comentarios claros que expliquen la lógica
   - Manejo de errores
   - Consideraciones de seguridad
3. Actualizar `06-hooks/README.md`

## Pautas de escritura

### Estilo Markdown
- Usar encabezados claros (H2 para secciones, H3 para subsecciones)
- Mantener párrafos cortos y enfocados
- Usar listas con viñetas para enumeraciones
- Incluir bloques de código con especificación de lenguaje
- Agregar líneas en blanco entre secciones

### Ejemplos de código
- Hacer que los ejemplos sean listos para copiar y pegar
- Comentar la lógica no obvia
- Incluir versiones simples y avanzadas
- Mostrar casos de uso del mundo real
- Destacar posibles problemas

### Documentación
- Explicar el "por qué" y no solo el "qué"
- Incluir prerequisitos
- Agregar secciones de solución de problemas
- Enlazar a temas relacionados
- Mantenerlo accesible para principiantes

### JSON/YAML
- Usar indentación apropiada (2 o 4 espacios de manera consistente)
- Agregar comentarios que expliquen la configuración
- Incluir ejemplos de validación

### Diagramas
- Usar Mermaid cuando sea posible
- Mantener los diagramas simples y legibles
- Incluir descripciones debajo de los diagramas
- Enlazar a secciones relevantes

## Pautas para commits

Seguir el formato de conventional commits:
```
type(scope): description

[optional body]
```

Tipos:
- `feat`: Nueva funcionalidad o ejemplo
- `fix`: Corrección de error
- `docs`: Cambios en la documentación
- `refactor`: Reestructuración del código
- `style`: Cambios de formato
- `test`: Adiciones o cambios en pruebas
- `chore`: Build, dependencias, etc.

Ejemplos:
```
feat(slash-commands): Add API documentation generator
docs(memory): Improve personal preferences example
fix(README): Correct table of contents link
docs(skills): Add comprehensive code review skill
```

## Antes de enviar

### Lista de verificación
- [ ] El código sigue el estilo y las convenciones del proyecto
- [ ] Los nuevos ejemplos incluyen documentación clara
- [ ] Los archivos README están actualizados (tanto el local como el raíz)
- [ ] Sin información sensible (claves de API, credenciales)
- [ ] Los ejemplos están probados y funcionan
- [ ] Los links están verificados y son correctos
- [ ] Los archivos tienen los permisos adecuados (los scripts son ejecutables)
- [ ] El mensaje del commit es claro y descriptivo

### Pruebas locales
```bash
# Ejecutar todas las verificaciones de pre-commit (las mismas que el CI)
pre-commit run --all-files

# Revisar tus cambios
git diff
```

## Proceso de Pull Request

1. **Crear PR con descripción clara**:
   - ¿Qué agrega o corrige?
   - ¿Por qué es necesario?
   - Issues relacionados (si los hay)

2. **Incluir detalles relevantes**:
   - ¿Nueva funcionalidad? Incluir casos de uso
   - ¿Documentación? Explicar las mejoras
   - ¿Ejemplos? Mostrar antes/después

3. **Enlazar a issues**:
   - Usar `Closes #123` para cerrar automáticamente issues relacionados

4. **Tener paciencia con las revisiones**:
   - Los mantenedores pueden sugerir mejoras
   - Iterar en base a los comentarios
   - La decisión final corresponde a los mantenedores

## Proceso de revisión de código

Los revisores verificarán:
- **Exactitud**: ¿Funciona como se describe?
- **Calidad**: ¿Está listo para producción?
- **Consistencia**: ¿Sigue los patrones del proyecto?
- **Documentación**: ¿Es claro y completo?
- **Seguridad**: ¿Hay alguna vulnerabilidad?

## Reportar issues

### Reportes de errores
Incluir:
- Versión de Claude Code
- Sistema operativo
- Pasos para reproducir
- Comportamiento esperado
- Comportamiento real
- Capturas de pantalla si corresponde

### Solicitudes de funcionalidades
Incluir:
- Caso de uso o problema que se resuelve
- Solución propuesta
- Alternativas consideradas
- Contexto adicional

### Issues de documentación
Incluir:
- Qué es confuso o está faltando
- Mejoras sugeridas
- Ejemplos o referencias

## Políticas del proyecto

### Información sensible
- Nunca hacer commit de claves de API, tokens o credenciales
- Usar valores de marcador de posición en los ejemplos
- Incluir `.env.example` para archivos de configuración
- Documentar las variables de entorno requeridas

### Calidad del código
- Mantener los ejemplos enfocados y legibles
- Evitar soluciones sobrediseñadas
- Incluir comentarios para la lógica no obvia
- Probar exhaustivamente antes de enviar

### Propiedad intelectual
- El contenido original pertenece al autor
- El proyecto usa licencia educativa
- Respetar los derechos de autor existentes
- Dar atribución cuando corresponda

## Obtener ayuda

- **Preguntas**: Abrir una discusión en GitHub Issues
- **Ayuda general**: Revisar la documentación existente
- **Ayuda con el desarrollo**: Revisar ejemplos similares
- **Revisión de código**: Etiquetar a los mantenedores en los PRs

## Reconocimiento

Los colaboradores son reconocidos en:
- Sección de colaboradores del README.md
- Página de contributors de GitHub
- Historial de commits

## Seguridad

Al contribuir con ejemplos y documentación, seguir las prácticas de codificación segura:

- **Nunca dejar secretos o claves de API en el código** - Usar variables de entorno
- **Advertir sobre implicaciones de seguridad** - Destacar riesgos potenciales
- **Usar valores seguros por defecto** - Activar funciones de seguridad por defecto
- **Validar las entradas** - Mostrar validación y sanitización adecuadas
- **Incluir notas de seguridad** - Documentar consideraciones de seguridad

Para issues de seguridad, ver [SECURITY.md](SECURITY.md) para nuestro proceso de reporte de vulnerabilidades.

## Código de conducta

Estamos comprometidos a brindar una comunidad acogedora e inclusiva. Por favor lee [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) para nuestros estándares completos de comunidad.

En resumen:
- Ser respetuoso e inclusivo
- Recibir los comentarios con buena disposición
- Ayudar a otros a aprender y crecer
- Evitar el acoso o la discriminación
- Reportar problemas a los mantenedores

Se espera que todos los colaboradores respeten este código y se traten mutuamente con amabilidad y respeto.

## Licencia

Al contribuir a este proyecto, aceptas que tus contribuciones estarán licenciadas bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## ¿Preguntas?

- Consultar el [README](README.md)
- Revisar [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)
- Ver los ejemplos existentes
- Abrir un issue para discutir

Gracias por contribuir! 🙏

---
**Ultima Actualizacion**: Abril 2026
